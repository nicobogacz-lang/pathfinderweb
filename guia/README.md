# PathFinder — Guía de Carreras

Páginas estáticas de la sección `/guia/` del sitio pathfinder.net.ar.

## 📁 Qué contiene

- **238 páginas HTML estáticas** listas para servir
- `index.html` — landing de la guía
- `areas/` — 8 páginas de áreas + index
- `carreras/` — 187 páginas de carreras + index con buscador/filtro
- `universidades/` — 38 páginas de universidades + index
- `data.json` — fuente única de datos (187 carreras + 8 áreas + 39 unis)
- `_generar.py` — script Python que re-genera todas las páginas desde `data.json`
- `_carreras_sin_universidades.csv` — CSV con las 78 carreras sin universidades para completar manualmente

## 🚀 Cómo subir a GitHub + desplegar en Vercel

### Opción A — Si querés mantener este repo como el del juego

Como el juego ya vive en el repo de GitHub `nicobogacz/pathfinder` (o similar) y se despliega vía Vercel, lo más limpio es:

1. **Cloná el repo del juego a tu computadora** (o abrí la carpeta local si ya la tenés).

2. **Dentro del repo, creá la carpeta `guia/`** y copiá todo el contenido de este paquete adentro. La estructura debe quedar así en tu repo:

   ```
   mi-repo/
   ├── index.html          ← landing del juego (ya existe)
   ├── admin.html          ← panel admin (ya existe)
   ├── guia/               ← ← ← NUEVO
   │   ├── index.html
   │   ├── data.json
   │   ├── _generar.py
   │   ├── _carreras_sin_universidades.csv
   │   ├── areas/
   │   │   ├── index.html
   │   │   ├── ciencias-de-la-salud.html
   │   │   └── ... (6 más)
   │   ├── carreras/
   │   │   ├── index.html
   │   │   └── ... (187 páginas)
   │   └── universidades/
   │       ├── index.html
   │       └── ... (39 páginas)
   ```

3. **Commit + Push desde la terminal:**

   ```bash
   cd mi-repo
   git add guia/
   git commit -m "Agregar sección Guía de Carreras (238 páginas)"
   git push
   ```

4. **Vercel detecta el push automáticamente** y despliega. En ~1-2 minutos tenés disponible:
   - `pathfinder.net.ar/guia/`
   - `pathfinder.net.ar/guia/carreras/`
   - `pathfinder.net.ar/guia/carreras/psicologia`
   - `pathfinder.net.ar/guia/universidades/uba`
   - etc.

### Opción B — Si usás GitHub Desktop (más visual)

1. Abrí GitHub Desktop → tu repo del juego.
2. En Finder (Mac) o Explorador (Windows), navegá a la carpeta del repo.
3. Copiá adentro la carpeta `guia/` completa.
4. Volvé a GitHub Desktop → vas a ver todos los archivos nuevos listados a la izquierda.
5. Abajo escribí un mensaje de commit: `"Agregar sección Guía de Carreras"`.
6. Click en **"Commit to main"**.
7. Click en **"Push origin"**.
8. Vercel detecta y despliega.

### Opción C — Subir vía GitHub web (si no tenés terminal)

1. Entrá a `github.com/nicobogacz/pathfinder` (o el nombre que tenga tu repo).
2. Click en **"Add file" → "Upload files"**.
3. **No podés subir carpetas enteras por web, pero sí podés arrastrar los archivos manteniendo la estructura**: creá la carpeta `guia/` en el repo primero clickeando "Create new file" y escribiendo `guia/placeholder.md` (eso te crea la carpeta); después seguís subiendo archivos de a tandas.
4. Esta opción es la más tediosa — recomiendo A o B.

## 🔗 Agregar link a la Guía desde la landing del juego

Para que los visitantes de `pathfinder.net.ar` descubran la guía, hay que agregar el link al menú principal.

Editá `index.html` del landing (el que vive en la raíz del repo) y en el `<nav>`, agregá:

```html
<a href="/guia/">Guía de carreras</a>
```

Lo mismo en el pie si lo creés oportuno.

## 🔄 Si editás `data.json` (ej. cargando las 78 carreras sin universidades)

```bash
cd guia/
python3 _generar.py
```

Eso regenera las 238 páginas HTML. Después hacés `git add . && git commit && git push` y Vercel re-despliega.

## 📝 Las 78 carreras sin universidades

Están en `_carreras_sin_universidades.csv`. Formato:

```
Carrera, Area, Universidades (siglas, coma)
Actuaría, Ciencias Económicas, "UBA,UNC,UADE"
...
```

Cuando completes las universidades, hay que:

1. Actualizar manualmente `data.json` con las nuevas universidades por carrera.
2. Correr `python3 _generar.py`.
3. Commit + push.

## ✅ Fase 2 completada (octubre 2026)

- **187 carreras** tienen descripción editorial (2-3 líneas), duración típica y campo laboral.
- **Las 78 carreras sin universidades** fueron completadas: hoy todas tienen al menos una universidad argentina.
- Catálogo de universidades expandido de 39 a **46** (se sumaron UNS, UNLaM, UNLa, UNSJ, UNLZ, UNICEN, UNRC).
- **sitemap.xml** generado con las 245 URLs del sitio.
- **robots.txt** incluido para permitir que Google indexe la guía.

## 📌 Deudas abiertas

- Testear performance con Lighthouse (ver sección más abajo).
- Afinar descripciones carrera por carrera cuando algún referente las revise.
- Imágenes OpenGraph por carrera para que los links se compartan lindos en WhatsApp/LinkedIn.

## 📈 Lighthouse (qué es)

Lighthouse es la **auditoría automática** que trae Chrome gratis para medir qué tan "bien hecho" está un sitio web. Te da una nota de 0 a 100 en 5 dimensiones:

1. **Performance**: cuánto tarda en cargar.
2. **Accessibility**: cuán usable es para personas con discapacidad (contraste, lectores de pantalla, teclado).
3. **Best practices**: si seguís convenciones modernas (HTTPS, APIs no obsoletas, etc).
4. **SEO**: si Google puede entender e indexar tu sitio correctamente.
5. **Progressive Web App**: si funciona como app instalable (no aplica a nuestro caso).

**Cómo correrlo** (toma 30 segundos):
1. Abrí la página en Chrome: `pathfinder.net.ar/guia/`
2. Click derecho → **Inspeccionar** (o F12).
3. En la barra de arriba del panel que se abre, buscá la pestaña **"Lighthouse"**.
4. Click en **"Analyze page load"**.
5. Después de ~30 seg te da las 5 notas y los puntos a mejorar.

Nuestro sitio es HTML puro y liviano, así que debería dar notas altas (90+). Si da algo bajo, en general es fácil de corregir.

## 🗺️ Sitemap.xml (qué es)

Es un archivo que **le dice a Google todas las URLs** de tu sitio, de un solo vistazo, para que no tenga que ir descubriéndolas una por una. Mejora significativamente la velocidad de indexación en Google y Bing.

Ya está generado en `sitemap.xml` con las 245 URLs del sitio (todas las carreras, áreas, universidades y los índices).

**Qué hacer con él** (una sola vez, 2 minutos):
1. Abrí [search.google.com/search-console](https://search.google.com/search-console) con tu cuenta de Google.
2. Agregá la propiedad `pathfinder.net.ar` (te pide verificar que sos el dueño — hay varias opciones, la más fácil es subir un archivo HTML a Vercel o agregar un registro DNS en tu panel).
3. Una vez verificado, en el menú lateral andá a **"Sitemaps"**.
4. Pegá la URL `https://pathfinder.net.ar/guia/sitemap.xml` y click en **"Enviar"**.
5. Google empieza a rastrear todas las URLs. En 24-72 horas aparecen indexadas.

También incluimos **robots.txt** en la raíz, que es otro archivo que Google busca automáticamente y que apunta a nuestro sitemap. No requiere nada de tu parte.

---

*Generado automáticamente a partir del motor de PathFinder. Octubre 2026.*
