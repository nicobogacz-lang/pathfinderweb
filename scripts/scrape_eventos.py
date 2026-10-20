#!/usr/bin/env python3
"""
PathFinder — scraper semanal de eventos universitarios.

Objetivo: encontrar charlas vocacionales, ferias y jornadas de
puertas abiertas en las webs de las universidades argentinas, y
mantener actualizado /guia/charlas/eventos.json.

Diseño:
- Se preservan los eventos manuales (los que no tienen tag "scraped").
- Cada scraper devuelve una lista de dicts normalizados.
- Si un scraper falla, se loguea y se sigue con los demás.
- Dedupe por id.
- Guarda el JSON solo si hubo cambios.

Agregar scrapers nuevos: ver sección SCRAPERS más abajo.
"""

import json
import re
import sys
import time
import hashlib
from pathlib import Path
from datetime import date, datetime
from urllib.parse import urljoin

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Faltan dependencias. Corré: pip install requests beautifulsoup4", file=sys.stderr)
    sys.exit(1)

# ────────────────────────────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
EVENTOS_PATH = ROOT / "guia" / "charlas" / "eventos.json"
UA = "Mozilla/5.0 (compatible; PathFinderBot/1.0; +https://pathfinder.net.ar)"
TIMEOUT = 20
HOY = date.today().isoformat()

# Keywords que indican que una noticia/evento es "charla vocacional"
KEYWORDS = [
    "charla vocacional", "orientación vocacional", "puertas abiertas",
    "open day", "feria de carreras", "muestra de carreras", "expo carreras",
    "jornada vocacional", "información para ingresantes", "charla informativa",
    "yoquieroestudiar", "future day", "expo universidad", "mundo universitario"
]

def fetch(url, **kwargs):
    """GET con retries y UA personalizado."""
    headers = kwargs.pop("headers", {})
    headers.setdefault("User-Agent", UA)
    for i in range(3):
        try:
            r = requests.get(url, timeout=TIMEOUT, headers=headers, **kwargs)
            if r.status_code == 200:
                return r
        except requests.RequestException as e:
            print(f"  ⚠️  Intento {i+1}/3 falló para {url}: {e}", file=sys.stderr)
            time.sleep(2)
    return None

def contains_kw(text):
    t = text.lower()
    return any(kw in t for kw in KEYWORDS)

def mk_id(prefix, title, fecha):
    """ID estable basado en universidad+titulo+fecha."""
    base = f"{prefix}-{title}-{fecha}".lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return base[:80]

# ────────────────────────────────────────────────────────────────
# SCRAPERS — uno por universidad
# Cada función devuelve lista de dicts con el schema estándar.
# Es OK devolver lista vacía o fallar silenciosamente.
# ────────────────────────────────────────────────────────────────

def scrape_uba():
    """Noticias UBA que mencionen charlas vocacionales / ferias."""
    out = []
    base = "https://www.uba.ar/ubanoticias/"
    r = fetch(base)
    if not r: return out
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.select("a[href*='ubanoticias/noticias/']")[:50]:
        title = a.get_text(strip=True)
        href = urljoin(base, a.get("href",""))
        if not title or not contains_kw(title): continue
        out.append({
            "id": mk_id("uba", title, HOY),
            "titulo": title,
            "universidad": "UBA",
            "universidad_nombre": "Universidad de Buenos Aires",
            "sistema": "pública",
            "tipo": "charla",
            "modalidad": "presencial",
            "fecha_inicio": HOY,
            "descripcion": "Evento detectado automáticamente en UBA. Ver link para fecha y detalles reales.",
            "link": href,
            "fuente_scraper": "uba",
            "actualizado": HOY,
            "nota": "Detectado automáticamente — confirmar fecha y detalles en el link oficial."
        })
    return out

def scrape_uade():
    """UADE: página de eventos."""
    out = []
    url = "https://www.uade.edu.ar/eventos/"
    r = fetch(url)
    if not r: return out
    soup = BeautifulSoup(r.text, "html.parser")
    for ev in soup.select("article, .evento, .event-item")[:30]:
        title_el = ev.find(["h2","h3","h4"])
        if not title_el: continue
        title = title_el.get_text(strip=True)
        if not title or not contains_kw(title): continue
        link_el = ev.find("a", href=True)
        href = urljoin(url, link_el["href"]) if link_el else url
        out.append({
            "id": mk_id("uade", title, HOY),
            "titulo": title,
            "universidad": "UADE",
            "universidad_nombre": "Universidad Argentina de la Empresa",
            "sistema": "privada",
            "tipo": "charla",
            "modalidad": "presencial",
            "fecha_inicio": HOY,
            "descripcion": "Evento detectado automáticamente en UADE. Ver link para fecha y detalles.",
            "link": href,
            "fuente_scraper": "uade",
            "actualizado": HOY,
            "nota": "Detectado automáticamente — confirmar fecha y detalles."
        })
    return out

def scrape_palermo():
    """UP: calendario académico."""
    out = []
    url = "https://www.palermo.edu/calendario-academico/"
    r = fetch(url)
    if not r: return out
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text(" ", strip=True)
    if contains_kw(text):
        out.append({
            "id": "up-agenda-" + HOY,
            "titulo": "Agenda de reuniones informativas UP",
            "universidad": "UP",
            "universidad_nombre": "Universidad de Palermo",
            "sistema": "privada",
            "tipo": "charla",
            "modalidad": "hibrido",
            "fecha_inicio": HOY,
            "descripcion": "Agenda rotativa de reuniones informativas de la UP, actualizada en calendario académico oficial.",
            "link": url,
            "fuente_scraper": "palermo",
            "actualizado": HOY,
            "nota": "Agenda rotativa — fechas vigentes en el link oficial."
        })
    return out

def scrape_eventbrite():
    """Eventbrite público: búsqueda por 'orientacion vocacional argentina'.
       Nota: Eventbrite tiene API pero requiere token. Esta es una
       búsqueda web pública como fallback liviano."""
    out = []
    url = "https://www.eventbrite.com.ar/d/argentina/universidad/"
    r = fetch(url)
    if not r: return out
    soup = BeautifulSoup(r.text, "html.parser")
    for card in soup.select("[data-testid='event-card']")[:20]:
        title_el = card.find(["h2","h3"])
        if not title_el: continue
        title = title_el.get_text(strip=True)
        if not title or not contains_kw(title): continue
        link_el = card.find("a", href=True)
        href = link_el["href"] if link_el else url
        out.append({
            "id": mk_id("evb", title, HOY),
            "titulo": title,
            "universidad": "VARIAS",
            "universidad_nombre": "Diversas (vía Eventbrite)",
            "sistema": "privada",
            "tipo": "charla",
            "modalidad": "presencial",
            "fecha_inicio": HOY,
            "descripcion": "Evento publicado en Eventbrite. Ver link para fecha y universidad organizadora.",
            "link": href,
            "fuente_scraper": "eventbrite",
            "actualizado": HOY,
            "nota": "Detectado automáticamente vía Eventbrite — confirmar en el link oficial."
        })
    return out

SCRAPERS = [
    ("UBA",        scrape_uba),
    ("UADE",       scrape_uade),
    ("Palermo",    scrape_palermo),
    ("Eventbrite", scrape_eventbrite),
]

# ────────────────────────────────────────────────────────────────
# ORQUESTACIÓN
# ────────────────────────────────────────────────────────────────

def main():
    print(f"🔎 PathFinder scraper — {HOY}")
    print(f"   Leyendo {EVENTOS_PATH}")

    if EVENTOS_PATH.exists():
        with EVENTOS_PATH.open(encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"actualizado": HOY, "eventos": []}

    # Preservar eventos manuales (los que NO tienen fuente_scraper)
    eventos_actuales = data.get("eventos", [])
    manuales = [e for e in eventos_actuales if "fuente_scraper" not in e]
    scraped_prev = [e for e in eventos_actuales if "fuente_scraper" in e]

    print(f"   📌 {len(manuales)} eventos manuales (se preservan)")
    print(f"   🔄 {len(scraped_prev)} eventos de scraping previo (serán reemplazados)")

    nuevos = []
    for nombre, fn in SCRAPERS:
        print(f"   • {nombre}…", end=" ")
        try:
            found = fn()
            print(f"OK ({len(found)} eventos)")
            nuevos.extend(found)
        except Exception as e:
            print(f"❌ falló: {e}")

    # Dedupe por id (manuales ganan ante colisión)
    ids_manuales = {e["id"] for e in manuales}
    nuevos = [e for e in nuevos if e["id"] not in ids_manuales]
    seen = set()
    deduped = []
    for e in nuevos:
        if e["id"] in seen: continue
        seen.add(e["id"])
        deduped.append(e)

    todos = manuales + deduped
    data["eventos"] = todos
    data["actualizado"] = HOY

    # Chequeo de cambio
    changed = True
    if EVENTOS_PATH.exists():
        prev_text = EVENTOS_PATH.read_text(encoding="utf-8")
        new_text = json.dumps(data, ensure_ascii=False, indent=2)
        # Comparar ignorando el campo "actualizado"
        prev_norm = re.sub(r'"actualizado":\s*"[^"]*"', '', prev_text)
        new_norm = re.sub(r'"actualizado":\s*"[^"]*"', '', new_text)
        changed = prev_norm.strip() != new_norm.strip()

    EVENTOS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with EVENTOS_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Total: {len(todos)} eventos ({len(manuales)} manuales + {len(deduped)} scrapeados)")
    print(f"   Cambios respecto a corrida anterior: {'SÍ' if changed else 'no'}")
    print(f"   Guardado en {EVENTOS_PATH}")
    # Exit code 0 = cambios, 10 = sin cambios (útil para el workflow)
    sys.exit(0 if changed else 10)

if __name__ == "__main__":
    main()
