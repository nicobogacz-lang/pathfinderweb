#!/usr/bin/env python3
"""
PathFinder — scraper semanal de eventos universitarios (v2).

Vectores de descubrimiento usados:
  1. Google News RSS: captura noticias de CUALQUIER uni argentina
     con keywords vocacionales ("charla vocacional", "feria de carreras",
     "jornada puertas abiertas", etc.).
  2. WordPress REST API: muchas unis (UNLP, UP y otras) corren WordPress.
     Les pegamos a /wp-json/wp/v2/posts?search=... para traer posts.
  3. HTML scraping: para unis con páginas estáticas (UBA, UNC).
  4. Sitemap XML: scanea /sitemap.xml de unis target y filtra URLs
     con keywords vocacionales.
  5. Eventbrite público: fallback para eventos cargados ahí por terceros.

Preserva eventos manuales (los que NO tienen "fuente_scraper").
"""

import json
import re
import sys
import time
import html
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import date
from urllib.parse import urljoin, quote

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Faltan deps. Corré: pip install requests beautifulsoup4", file=sys.stderr)
    sys.exit(1)

# ────────────────────────────────────────────────────────────────
# CONFIG
# ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
EVENTOS_PATH = ROOT / "guia" / "charlas" / "eventos.json"
UA = "Mozilla/5.0 (compatible; PathFinderBot/2.0; +https://pathfinder.net.ar)"
TIMEOUT = 25
HOY = date.today().isoformat()

# Keywords amplios para detectar eventos vocacionales / de ingreso
KEYWORDS_FUERTES = [
    "orientación vocacional", "orientacion vocacional",
    "charla vocacional", "charla informativa",
    "puertas abiertas", "open day", "open house",
    "feria de carreras", "muestra de carreras",
    "expo carreras", "expo universidad", "expo educativa",
    "jornada vocacional", "jornada de ingresantes",
    "información para ingresantes", "informacion para ingresantes",
    "yoquieroestudiar", "yo quiero estudiar",
    "future day", "mundo universitario",
    "visita al campus", "visitas guiadas",
    "talleres vocacionales",
]
# Keywords de contexto (sumadas a "universidad" o nombre de uni)
KEYWORDS_CONTEXTO = ["ingreso", "ingresantes", "aspirantes", "carreras", "admisión", "admision"]

# Mapeo sigla → datos de la universidad (para enriquecer)
UNIVERSIDADES = {
    "UBA":     ("Universidad de Buenos Aires", "pública"),
    "UNC":     ("Universidad Nacional de Córdoba", "pública"),
    "UNLP":    ("Universidad Nacional de La Plata", "pública"),
    "UNR":     ("Universidad Nacional de Rosario", "pública"),
    "UNL":     ("Universidad Nacional del Litoral", "pública"),
    "UNCUYO":  ("Universidad Nacional de Cuyo", "pública"),
    "UNT":     ("Universidad Nacional de Tucumán", "pública"),
    "UTN":     ("Universidad Tecnológica Nacional", "pública"),
    "UNS":     ("Universidad Nacional del Sur", "pública"),
    "UNSAM":   ("Universidad Nacional de San Martín", "pública"),
    "UNQ":     ("Universidad Nacional de Quilmes", "pública"),
    "UNNE":    ("Universidad Nacional del Nordeste", "pública"),
    "UCA":     ("Universidad Católica Argentina", "privada"),
    "UCES":    ("Universidad de Ciencias Empresariales y Sociales", "privada"),
    "UADE":    ("Universidad Argentina de la Empresa", "privada"),
    "UP":      ("Universidad de Palermo", "privada"),
    "UB":      ("Universidad de Belgrano", "privada"),
    "UTDT":    ("Universidad Torcuato Di Tella", "privada"),
    "UdeSA":   ("Universidad de San Andrés", "privada"),
    "ITBA":    ("Instituto Tecnológico de Buenos Aires", "privada"),
    "USAL":    ("Universidad del Salvador", "privada"),
    "UAI":     ("Universidad Abierta Interamericana", "privada"),
    "UCEMA":   ("Universidad del CEMA", "privada"),
    "ORT":     ("Universidad ORT Argentina", "privada"),
    "Austral": ("Universidad Austral", "privada"),
    "UCCUYO":  ("Universidad Católica de Cuyo", "privada"),
    "Siglo 21":("Universidad Siglo 21", "privada"),
    "UADER":   ("Universidad Autónoma de Entre Ríos", "pública"),
    "UNER":    ("Universidad Nacional de Entre Ríos", "pública"),
    "UNaM":    ("Universidad Nacional de Misiones", "pública"),
    "UNCo":    ("Universidad Nacional del Comahue", "pública"),
    "UNRC":    ("Universidad Nacional de Río Cuarto", "pública"),
    "UNSa":    ("Universidad Nacional de Salta", "pública"),
    "UNJu":    ("Universidad Nacional de Jujuy", "pública"),
    "UNSE":    ("Universidad Nacional de Santiago del Estero", "pública"),
    "UNLaM":   ("Universidad Nacional de La Matanza", "pública"),
    "UNLa":    ("Universidad Nacional de Lanús", "pública"),
    "UNSJ":    ("Universidad Nacional de San Juan", "pública"),
    "UNLZ":    ("Universidad Nacional de Lomas de Zamora", "pública"),
    "UNICEN":  ("Universidad Nacional del Centro de la Pcia de Bs As", "pública"),
    "UNM":     ("Universidad Nacional de Moreno", "pública"),
    "UBP":     ("Universidad Blas Pascal", "privada"),
    "UMET":    ("Universidad Metropolitana para la Educación y el Trabajo", "privada"),
    "UFLO":    ("Universidad de Flores", "privada"),
    "UMSA":    ("Universidad del Museo Social Argentino", "privada"),
    "UNA":     ("Universidad Nacional de las Artes", "pública"),
}

# Patrones de nombres completos → sigla
NAME_TO_SIGLA = {
    "universidad de buenos aires": "UBA", "uba": "UBA",
    "universidad nacional de córdoba": "UNC", "unc": "UNC",
    "universidad nacional de la plata": "UNLP", "unlp": "UNLP",
    "universidad nacional de rosario": "UNR", "unr": "UNR",
    "universidad nacional del litoral": "UNL", "unl": "UNL",
    "universidad nacional de cuyo": "UNCUYO",
    "universidad nacional de tucumán": "UNT", "universidad nacional de tucuman": "UNT",
    "universidad tecnológica nacional": "UTN", "universidad tecnologica nacional": "UTN", "utn": "UTN",
    "universidad nacional del sur": "UNS",
    "universidad nacional de san martín": "UNSAM", "universidad nacional de san martin": "UNSAM",
    "universidad nacional de quilmes": "UNQ",
    "universidad nacional del nordeste": "UNNE",
    "universidad católica argentina": "UCA", "universidad catolica argentina": "UCA",
    "uca": "UCA",
    "universidad argentina de la empresa": "UADE", "uade": "UADE",
    "universidad de palermo": "UP",
    "universidad de belgrano": "UB",
    "universidad torcuato di tella": "UTDT", "di tella": "UTDT",
    "universidad de san andrés": "UdeSA", "universidad de san andres": "UdeSA",
    "san andrés": "UdeSA", "udesa": "UdeSA",
    "instituto tecnológico de buenos aires": "ITBA", "itba": "ITBA",
    "universidad del salvador": "USAL",
    "universidad abierta interamericana": "UAI",
    "universidad del cema": "UCEMA", "ucema": "UCEMA",
    "universidad ort": "ORT", "ort argentina": "ORT",
    "universidad austral": "Austral",
    "universidad católica de cuyo": "UCCUYO", "uccuyo": "UCCUYO",
    "universidad siglo 21": "Siglo 21", "siglo 21": "Siglo 21", "siglo21": "Siglo 21",
    "universidad autónoma de entre ríos": "UADER", "universidad autonoma de entre rios": "UADER", "uader": "UADER",
    "universidad nacional de entre ríos": "UNER", "universidad nacional de entre rios": "UNER",
    "universidad nacional de misiones": "UNaM",
    "universidad nacional del comahue": "UNCo",
    "universidad nacional de río cuarto": "UNRC", "universidad nacional de rio cuarto": "UNRC",
    "universidad nacional de salta": "UNSa",
    "universidad nacional de jujuy": "UNJu",
    "universidad nacional de santiago del estero": "UNSE",
    "universidad nacional de la matanza": "UNLaM",
    "universidad nacional de lanús": "UNLa", "universidad nacional de lanus": "UNLa",
    "universidad nacional de san juan": "UNSJ",
    "universidad nacional de lomas de zamora": "UNLZ",
    "universidad nacional del centro": "UNICEN", "unicen": "UNICEN",
    "universidad nacional de moreno": "UNM",
    "universidad blas pascal": "UBP",
    "universidad metropolitana para la educación": "UMET",
    "universidad de flores": "UFLO",
    "universidad del museo social argentino": "UMSA",
    "universidad nacional de las artes": "UNA",
}

MESES = {"ene":1,"enero":1,"feb":2,"febrero":2,"mar":3,"marzo":3,"abr":4,"abril":4,
         "may":5,"mayo":5,"jun":6,"junio":6,"jul":7,"julio":7,"ago":8,"agosto":8,
         "sep":9,"sept":9,"septiembre":9,"oct":10,"octubre":10,"nov":11,"noviembre":11,
         "dic":12,"diciembre":12}

# ────────────────────────────────────────────────────────────────
# HELPERS
# ────────────────────────────────────────────────────────────────

def fetch(url, **kwargs):
    headers = kwargs.pop("headers", {})
    headers.setdefault("User-Agent", UA)
    headers.setdefault("Accept-Language", "es-AR,es;q=0.9,en;q=0.5")
    for i in range(3):
        try:
            r = requests.get(url, timeout=TIMEOUT, headers=headers, **kwargs)
            if r.status_code == 200:
                return r
            print(f"  ⚠️  HTTP {r.status_code} en {url[:80]}", file=sys.stderr)
            return None
        except requests.RequestException as e:
            print(f"  ⚠️  Intento {i+1}/3 falló {url[:80]}: {type(e).__name__}", file=sys.stderr)
            time.sleep(2)
    return None

def normalize_text(s):
    if not s: return ""
    s = html.unescape(s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def contains_fuerte(text):
    t = text.lower()
    return any(kw in t for kw in KEYWORDS_FUERTES)

def contains_contexto_universidad(text):
    """True si menciona universidad + contexto vocacional/ingreso."""
    t = text.lower()
    has_uni = "universidad" in t or any(sl.lower() in t for sl in UNIVERSIDADES.keys())
    has_ctx = any(kw in t for kw in KEYWORDS_CONTEXTO)
    return has_uni and has_ctx

def detect_universidad(text):
    """Intenta detectar sigla de universidad en el texto.
       Ordena matches por longitud descendente (así UADER no es confundido con UADE)
       y usa word-boundary para siglas cortas (evita UBA en 'subaltierno')."""
    t = text.lower()
    # Primero intentar matches de nombre completo (más confiable)
    full_names = [(n, s) for n, s in NAME_TO_SIGLA.items() if " " in n]
    full_names.sort(key=lambda x: -len(x[0]))
    for name, sigla in full_names:
        if name in t:
            return sigla
    # Después siglas sueltas, con word boundary. Más largas primero.
    siglas = sorted([(n, s) for n, s in NAME_TO_SIGLA.items() if " " not in n],
                    key=lambda x: -len(x[0]))
    for name, sigla in siglas:
        if re.search(r"\b" + re.escape(name) + r"\b", t):
            return sigla
    return None

def mentions_past_year(text):
    """Descartar eventos de años anteriores a este."""
    year_now = date.today().year
    for y in range(2015, year_now):
        if re.search(r"\b" + str(y) + r"\b", text):
            return True
    return False

def extract_date(text):
    """Intenta extraer una fecha ISO (YYYY-MM-DD) del texto. Devuelve None si no."""
    t = text.lower()
    year_now = date.today().year
    # Formato: "20 de octubre de 2026" o "20 de octubre"
    m = re.search(r"(\d{1,2})\s+de\s+([a-zñ]+)(?:\s+de\s+(\d{4}))?", t)
    if m:
        d, mes, y = m.group(1), m.group(2)[:4], m.group(3)
        mes_n = next((v for k,v in MESES.items() if k.startswith(mes)), None)
        if mes_n:
            y = int(y) if y else year_now
            try:
                return date(y, mes_n, int(d)).isoformat()
            except ValueError:
                pass
    # Formato: "20/10/2026" o "20-10-2026"
    m = re.search(r"\b(\d{1,2})[/\-](\d{1,2})[/\-](\d{2,4})\b", t)
    if m:
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if y < 100: y += 2000
        try:
            return date(y, mo, d).isoformat()
        except ValueError:
            pass
    return None

def detect_tipo(text):
    t = text.lower()
    if any(k in t for k in ["expo", "feria", "muestra", "mundo universitario"]): return "feria"
    if "open day" in t or "puertas abiertas" in t: return "open-day"
    if "jornada" in t: return "jornada"
    if "workshop" in t or "taller" in t: return "workshop"
    return "charla"

def detect_modalidad(text):
    t = text.lower()
    if "virtual" in t or "online" in t or "zoom" in t or "youtube live" in t: return "virtual"
    if "híbrido" in t or "hibrido" in t: return "hibrido"
    return "presencial"

def mk_id(prefix, title, fecha):
    base = f"{prefix}-{title[:60]}-{fecha}".lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return base[:80]

def normalize_event(**kwargs):
    """Toma un evento parcial y lo completa con defaults."""
    titulo = kwargs.get("titulo", "")
    link = kwargs.get("link", "")
    fecha_explicita = kwargs.get("fecha_inicio")
    fecha_inicio = fecha_explicita or HOY
    fecha_estimada = not bool(fecha_explicita)
    universidad = kwargs.get("universidad") or "???"
    sigla = universidad
    if universidad in UNIVERSIDADES:
        nombre, sistema = UNIVERSIDADES[universidad]
    else:
        nombre = kwargs.get("universidad_nombre", universidad)
        sistema = kwargs.get("sistema", "privada")
    tipo = kwargs.get("tipo") or detect_tipo(titulo + " " + kwargs.get("descripcion",""))
    modalidad = kwargs.get("modalidad") or detect_modalidad(titulo + " " + kwargs.get("descripcion",""))
    fuente_scraper = kwargs.get("fuente_scraper", "generico")
    ev_id = kwargs.get("id") or mk_id(fuente_scraper + "-" + sigla, titulo, fecha_inicio)
    return {
        "id": ev_id,
        "titulo": titulo,
        "universidad": sigla,
        "universidad_nombre": nombre,
        "sistema": sistema,
        "tipo": tipo,
        "modalidad": modalidad,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": kwargs.get("fecha_fin"),
        "fecha_estimada": fecha_estimada,
        "hora": kwargs.get("hora", ""),
        "ubicacion": kwargs.get("ubicacion", ""),
        "descripcion": kwargs.get("descripcion", "Evento detectado automáticamente. Ver el link para fecha y detalles."),
        "link": link,
        "fuente_scraper": fuente_scraper,
        "actualizado": HOY,
        "nota": kwargs.get("nota", "Detectado automáticamente — confirmar fecha y detalles en el link oficial.")
    }

# ────────────────────────────────────────────────────────────────
# SCRAPERS
# ────────────────────────────────────────────────────────────────

def scrape_google_news():
    """Google News RSS por queries vocacionales. Captura cualquier uni."""
    out = []
    queries = [
        '"charla vocacional" universidad site:*.edu.ar OR site:*.edu',
        '"feria de carreras" universidad argentina 2026',
        '"puertas abiertas" universidad argentina',
        '"open day" universidad argentina',
        '"orientación vocacional" universidad 2026',
        '"muestra de carreras" universidad',
        '"expo carreras" argentina universidad',
    ]
    for q in queries:
        url = f"https://news.google.com/rss/search?q={quote(q)}&hl=es-419&gl=AR&ceid=AR:es-419"
        r = fetch(url)
        if not r: continue
        try:
            root = ET.fromstring(r.content)
        except ET.ParseError:
            continue
        for item in root.iter("item"):
            title = normalize_text((item.findtext("title") or ""))
            link = (item.findtext("link") or "").strip()
            desc = normalize_text((item.findtext("description") or ""))
            pub = (item.findtext("pubDate") or "").strip()
            full = title + " " + desc
            if not (contains_fuerte(full) or contains_contexto_universidad(full)):
                continue
            # Filtrar menciones a años anteriores
            if mentions_past_year(full):
                continue
            sigla = detect_universidad(full) or "???"
            if sigla == "???": continue
            fecha = extract_date(full)
            # Fallback: usar pubDate del feed si no hay fecha en el texto
            if not fecha and pub:
                try:
                    from email.utils import parsedate_to_datetime
                    fecha_pub = parsedate_to_datetime(pub).date().isoformat()
                    fecha = fecha_pub
                except Exception:
                    pass
            out.append(normalize_event(
                titulo=title[:140],
                link=link,
                fecha_inicio=fecha,  # None => fecha_estimada=True
                universidad=sigla,
                descripcion=desc[:280] or title,
                fuente_scraper="google-news",
                nota="Detectado vía Google News — confirmar fecha y detalles en el link."
            ))
    return out

def scrape_wordpress(sigla, base_url, keyword="charla"):
    """Hits WordPress REST API genérico."""
    out = []
    url = f"{base_url}/wp-json/wp/v2/posts?search={quote(keyword)}&per_page=20&_fields=id,title,link,excerpt,date"
    r = fetch(url)
    if not r:
        return out
    try:
        posts = r.json()
    except ValueError:
        return out
    for p in posts if isinstance(posts, list) else []:
        title = normalize_text(p.get("title",{}).get("rendered",""))
        excerpt = normalize_text(p.get("excerpt",{}).get("rendered",""))
        link = p.get("link","")
        full = title + " " + excerpt
        if not (contains_fuerte(full) or contains_contexto_universidad(full)):
            continue
        if mentions_past_year(full):
            continue
        fecha = extract_date(full) or (p.get("date","")[:10] if p.get("date") else None)
        out.append(normalize_event(
            titulo=title[:140],
            link=link,
            fecha_inicio=fecha,
            universidad=sigla,
            descripcion=excerpt[:280] or title,
            fuente_scraper=f"wp-{sigla.lower()}"
        ))
    return out

def scrape_uba_noticias():
    """HTML scraping de UBA noticias."""
    out = []
    r = fetch("https://www.uba.ar/ubanoticias/")
    if not r: return out
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.select("a[href*='/ubanoticias/noticias/']"):
        title = a.get_text(strip=True)
        if not title: continue
        if not (contains_fuerte(title) or contains_contexto_universidad(title)): continue
        if mentions_past_year(title): continue
        href = urljoin("https://www.uba.ar/", a.get("href",""))
        fecha = extract_date(title)
        out.append(normalize_event(
            titulo=title[:140],
            link=href,
            fecha_inicio=fecha,
            universidad="UBA",
            descripcion=title,
            fuente_scraper="uba-noticias"
        ))
    return out

def scrape_unc_noticias():
    """UNC - scraping de prensa UNC."""
    out = []
    for url in ["https://www.unc.edu.ar/", "https://www.unc.edu.ar/pr-general/"]:
        r = fetch(url)
        if not r: continue
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.find_all("a", href=True):
            title = a.get_text(strip=True)
            if not title or len(title) < 20: continue
            if not (contains_fuerte(title) or ("muestra" in title.lower() and "carrera" in title.lower())): continue
            if mentions_past_year(title): continue
            href = urljoin(url, a["href"])
            fecha = extract_date(title)
            out.append(normalize_event(
                titulo=title[:140],
                link=href,
                fecha_inicio=fecha,
                universidad="UNC",
                descripcion=title,
                fuente_scraper="unc-noticias"
            ))
    return out

def scrape_sitemap(sigla, sitemap_url):
    """Scanea un sitemap buscando URLs que mencionen keywords vocacionales."""
    out = []
    r = fetch(sitemap_url)
    if not r: return out
    # Soportar sitemap index o sitemap simple
    text = r.text
    urls = re.findall(r"<loc>([^<]+)</loc>", text)
    for u in urls:
        slug_part = u.lower().split("/")[-2] if u.endswith("/") else u.lower().split("/")[-1]
        if not any(kw in slug_part for kw in ["charla","vocacional","puertas-abiertas","open-day","feria-carreras","muestra-carreras","expo-carreras","yoquieroestudiar","futureday","mundo-universitario","ingresantes"]):
            continue
        out.append(normalize_event(
            titulo=slug_part.replace("-"," ").title()[:140],
            link=u,
            fecha_inicio=HOY,
            universidad=sigla,
            descripcion=f"URL detectada en sitemap de {sigla}",
            fuente_scraper=f"sitemap-{sigla.lower()}",
            nota="Detectado en sitemap — confirmar que esté vigente."
        ))
    return out[:5]  # máximo 5 por sitemap para no inundar

def scrape_eventbrite_search():
    """Eventbrite público."""
    out = []
    url = "https://www.eventbrite.com.ar/d/argentina/university/"
    r = fetch(url)
    if not r: return out
    soup = BeautifulSoup(r.text, "html.parser")
    for card in soup.find_all("article"):
        title_el = card.find(["h2","h3","h4"])
        if not title_el: continue
        title = title_el.get_text(strip=True)
        if not title: continue
        if not (contains_fuerte(title) or contains_contexto_universidad(title)): continue
        link_el = card.find("a", href=True)
        href = link_el["href"] if link_el else url
        sigla = detect_universidad(title) or "???"
        out.append(normalize_event(
            titulo=title[:140],
            link=href,
            fecha_inicio=HOY,
            universidad=sigla if sigla != "???" else "UBA",
            descripcion=title,
            fuente_scraper="eventbrite",
            nota="Detectado vía Eventbrite — confirmar en el link."
        ))
    return out

# ────────────────────────────────────────────────────────────────
# ORQUESTACIÓN
# ────────────────────────────────────────────────────────────────

SCRAPERS = [
    ("Google News (todas las unis)", scrape_google_news),
    ("UBA noticias",                   scrape_uba_noticias),
    ("UNC noticias",                   scrape_unc_noticias),
    ("WP · UNLP",                      lambda: scrape_wordpress("UNLP","https://unlp.edu.ar")),
    ("WP · UP",                        lambda: scrape_wordpress("UP",  "https://www.palermo.edu")),
    ("WP · UNSAM",                     lambda: scrape_wordpress("UNSAM","https://www.unsam.edu.ar")),
    ("WP · UCES",                      lambda: scrape_wordpress("UCES","https://www.uces.edu.ar")),
    ("Sitemap · UBA",                  lambda: scrape_sitemap("UBA","https://www.uba.ar/sitemap.xml")),
    ("Sitemap · UNC",                  lambda: scrape_sitemap("UNC","https://www.unc.edu.ar/sitemap_index.xml")),
    ("Sitemap · UCA",                  lambda: scrape_sitemap("UCA","https://uca.edu.ar/sitemap.xml")),
    ("Eventbrite",                     scrape_eventbrite_search),
]

def main():
    print(f"🔎 PathFinder scraper v2 — {HOY}\n")

    if EVENTOS_PATH.exists():
        with EVENTOS_PATH.open(encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"actualizado": HOY, "eventos": []}

    eventos_actuales = data.get("eventos", [])
    manuales = [e for e in eventos_actuales if "fuente_scraper" not in e]
    print(f"📌 {len(manuales)} eventos manuales preservados\n")

    nuevos = []
    for nombre, fn in SCRAPERS:
        print(f"  🔍 {nombre}…", end=" ", flush=True)
        try:
            found = fn()
            print(f"OK ({len(found)})")
            nuevos.extend(found)
        except Exception as e:
            print(f"❌ {type(e).__name__}: {e}")

    # Dedupe por id
    ids_manuales = {e["id"] for e in manuales}
    seen = set(ids_manuales)
    deduped = []
    for e in nuevos:
        if e["id"] in seen: continue
        seen.add(e["id"])
        deduped.append(e)

    # Dedupe fuzzy por título normalizado (evitar duplicados cross-fuente)
    seen_titles = set()
    final_scraped = []
    for e in deduped:
        key = re.sub(r"[^a-z0-9]+", "", e["titulo"].lower())[:60]
        if key in seen_titles: continue
        seen_titles.add(key)
        final_scraped.append(e)

    todos = manuales + final_scraped
    data["eventos"] = todos
    data["actualizado"] = HOY

    # Chequeo de cambio para el workflow
    changed = True
    if EVENTOS_PATH.exists():
        prev_text = EVENTOS_PATH.read_text(encoding="utf-8")
        new_text = json.dumps(data, ensure_ascii=False, indent=2)
        prev_norm = re.sub(r'"actualizado":\s*"[^"]*"', '', prev_text)
        new_norm = re.sub(r'"actualizado":\s*"[^"]*"', '', new_text)
        changed = prev_norm.strip() != new_norm.strip()

    EVENTOS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with EVENTOS_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Total: {len(todos)} ({len(manuales)} manuales + {len(final_scraped)} scrapeados)")
    print(f"   Cambios: {'SÍ' if changed else 'no'}")
    print(f"   Guardado: {EVENTOS_PATH}")

if __name__ == "__main__":
    main()
