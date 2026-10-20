#!/usr/bin/env python3
"""
Generador de la Guía de Carreras de PathFinder.
Lee data.json y genera 237 páginas HTML estáticas.
Uso: python3 _generar.py
"""
import json, os, re, unicodedata, csv
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
with open(ROOT+'/data.json') as f: data = json.load(f)
os.makedirs(ROOT+'/carreras', exist_ok=True)
os.makedirs(ROOT+'/areas', exist_ok=True)
os.makedirs(ROOT+'/universidades', exist_ok=True)

def slugify(s):
    s = unicodedata.normalize('NFD', s).encode('ascii','ignore').decode()
    s = re.sub(r'[^\w\s-]','',s).strip().lower()
    s = re.sub(r'[\s_-]+','-',s)
    return s.rstrip('-')

CSS = "@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap');:root{--gold:#F5C040;--orange:#E87820;--cream:#FFF8EC;--muted:#A09070;--bg:#0A0610;--card:#160A24}*{margin:0;padding:0;box-sizing:border-box}html,body{background:var(--bg);color:var(--cream);font-family:'DM Sans',sans-serif;line-height:1.6}a{color:var(--gold);text-decoration:none}a:hover{color:var(--orange)}.wrap{max-width:1180px;margin:0 auto;padding:0 32px}nav{position:sticky;top:0;z-index:50;background:rgba(10,6,16,.92);backdrop-filter:blur(12px);border-bottom:1px solid rgba(245,192,64,.1);padding:16px 32px}.nav-inner{max-width:1180px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}nav .logo{font-family:'Cormorant Garamond',serif;font-size:22px;color:var(--gold);letter-spacing:1px}nav .menu{display:flex;gap:24px;font-size:14px}nav .menu a{color:rgba(255,248,236,.75)}nav .menu a:hover{color:var(--gold)}nav .cta{padding:10px 20px;border-radius:99px;background:var(--gold);color:#0a0510!important;font-weight:600;font-size:13px}.crumb{padding:30px 0 10px;color:rgba(255,248,236,.5);font-size:13px}.crumb a{color:rgba(255,248,236,.5)}.crumb a:hover{color:var(--gold)}.crumb .sep{margin:0 10px;color:rgba(255,248,236,.3)}footer{margin-top:80px;padding:40px 32px;background:#060310;color:rgba(255,248,236,.45);font-size:13px;text-align:center;border-top:1px solid rgba(245,192,64,.08)}footer a{color:var(--gold)}.btn-primary{display:inline-block;padding:16px 36px;border-radius:99px;background:var(--gold);color:#0a0510!important;font-weight:600;font-size:15px;transition:all .2s}.btn-primary:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(245,192,64,.3);color:#0a0510!important}"

NAV = '<nav><div class="nav-inner"><a href="/" class="logo">PathFinder</a><div class="menu"><a href="/#como">Cómo funciona</a><a href="/guia/">Guía</a><a href="/guia/carreras/">Carreras</a><a href="/guia/universidades/">Universidades</a><a href="/#contacto">Contacto</a></div><a href="https://pathfinder-rouge-iota.vercel.app/" class="cta">Probá el juego →</a></div></nav>'
FOOT = '<footer><div style="margin-bottom:12px;font-family:\'Cormorant Garamond\',serif;font-size:20px;color:var(--gold);">PathFinder</div><div>Guía de carreras · <a href="/">Volver al inicio</a> · <a href="/guia/">Guía</a> · <a href="/guia/carreras/">Carreras</a> · <a href="/guia/universidades/">Universidades</a></div><div style="margin-top:10px;opacity:.6;">© 2026 PathFinder · nicobogacz@gmail.com · pathfinder.net.ar</div></footer>'

DIM_DESC = {'D':('Dominancia','decisión y acción'),'I':('Influencia','persuasión y entusiasmo'),'S':('Estabilidad','paciencia y empatía'),'C':('Precisión','análisis y método'),'hR':('Realista','práctico, con las manos'),'hI':('Investigador','curioso, analítico'),'hA':('Artístico','creativo, expresivo'),'hS':('Social','orientado a personas'),'hE':('Emprendedor','liderazgo y gestión'),'hC':('Convencional','orden y sistemas'),'mTeo':('Teórico','busca el saber'),'mEco':('Pragmático','busca resultados tangibles'),'mEst':('Estético','busca forma y belleza'),'mSoc':('Social','busca servir'),'mAut':('Autonomía','busca independencia'),'mTra':('Tradicional','respeta normas'),'pdcP':('Personas','trabaja con y para personas'),'pdcD':('Datos','trabaja con información'),'pdcC':('Objetos','trabaja con cosas físicas')}

AREAS_DESC = {
    'Ciencias de la Salud': {'tagline':'Cuidar, curar, acompañar.','intro':'Las carreras de Ciencias de la Salud forman profesionales que trabajan directamente con y para las personas: diagnostican, tratan, previenen, acompañan procesos vitales. Es un área que exige dedicación de largo plazo, estudio continuo y una capacidad real de empatía.','perfil':'Perfiles con <b>orientación a personas</b> (pdcP), <b>sensibilidad social</b> (hS) y <b>paciencia</b> (S). Combinan rigor científico con vocación de servicio.','profesionales':'Médicos, psicólogos, enfermeros, kinesiólogos, nutricionistas, odontólogos, farmacéuticos, terapistas, instrumentistas quirúrgicos.'},
    'Ciencias Sociales y Humanas': {'tagline':'Entender a las personas y a la sociedad.','intro':'Las Ciencias Sociales y Humanas estudian cómo las personas se organizan, se comunican, deciden y construyen sentido en común. Son carreras que combinan reflexión teórica con intervención práctica.','perfil':'Perfiles con <b>orientación a personas</b> (pdcP), <b>influencia y comunicación</b> (I), <b>vocación de servicio</b> (mSoc) y <b>sensibilidad social</b> (hS).','profesionales':'Abogados, sociólogos, politólogos, comunicadores, psicopedagogos, trabajadores sociales, antropólogos, filósofos, periodistas, relaciones internacionales.'},
    'Ciencias Exactas y Naturales': {'tagline':'La curiosidad por entender cómo funciona el mundo.','intro':'Las Ciencias Exactas y Naturales buscan comprender la realidad desde sus leyes fundamentales. Son carreras para quienes se hacen preguntas profundas y disfrutan del rigor del método científico.','perfil':'Perfiles con <b>pensamiento investigador</b> (hI), <b>motivación teórica</b> (mTeo), <b>orden metódico</b> (hC) y <b>orientación a datos</b> (pdcD).','profesionales':'Matemáticos, físicos, químicos, biólogos, bioquímicos, geólogos, estadísticos, bioinformáticos.'},
    'Ingeniería y Tecnología': {'tagline':'Diseñar soluciones donde no las había.','intro':'Las Ingenierías aplican ciencia y método para resolver problemas concretos del mundo: construyen puentes, diseñan algoritmos, optimizan procesos, crean productos.','perfil':'Perfiles con <b>pensamiento analítico</b> (C), <b>curiosidad investigadora</b> (hI), <b>orientación a datos</b> (pdcD) y <b>método</b> (hC).','profesionales':'Ingenieros civiles, mecánicos, industriales, en sistemas, electrónicos, químicos, en inteligencia artificial, en ciencia de datos, biomédicos.'},
    'Ciencias Económicas y Administración': {'tagline':'El negocio, la decisión, el valor.','intro':'Las carreras del área económica forman profesionales que entienden cómo se crean y distribuyen los recursos: en empresas, mercados, políticas públicas.','perfil':'Perfiles con <b>espíritu emprendedor</b> (hE), <b>orientación a resultados económicos</b> (mEco), <b>dominancia</b> (D) y <b>análisis de datos</b> (pdcD).','profesionales':'Contadores, economistas, administradores, financistas, marketers, recursos humanos, actuarios, especialistas en negocios digitales.'},
    'Arte, Diseño y Arquitectura': {'tagline':'Crear forma, sentido y belleza.','intro':'Las carreras artísticas y de diseño transforman ideas en objetos, espacios, imágenes, sonidos y narrativas. Combinan la sensibilidad estética con la técnica.','perfil':'Perfiles con <b>sensibilidad artística</b> (hA), <b>motivación estética</b> (mEst), <b>autonomía creativa</b> (mAut) y <b>orientación a lo tangible</b> (pdcC).','profesionales':'Arquitectos, diseñadores gráficos, industriales, UX/UI, de indumentaria, cineastas, músicos, actores, artistas visuales, fotógrafos.'},
    'Ciencias Agropecuarias y Ambiente': {'tagline':'Vivir del campo, cuidar la tierra.','intro':'Las carreras agropecuarias y ambientales trabajan con los sistemas naturales que sostienen la vida y la producción. Van desde el manejo de cultivos y animales hasta la gestión de ecosistemas.','perfil':'Perfiles con <b>orientación realista y práctica</b> (hR), <b>trabajo con objetos físicos</b> (pdcC), <b>motivación teórica</b> (mTeo) y <b>respeto por los ciclos naturales</b> (mTra).','profesionales':'Agrónomos, veterinarios, ingenieros ambientales, en producción agropecuaria, en recursos naturales, guardaparques, paisajistas.'},
    'Educación y Ciencias Pedagógicas': {'tagline':'Formar a quienes vienen después.','intro':'Las carreras del área educativa preparan a quienes van a enseñar, acompañar y diseñar los procesos de aprendizaje de otros. Son profesiones de alto impacto social.','perfil':'Perfiles con <b>respeto por la tradición</b> (mTra), <b>sensibilidad social</b> (hS), <b>paciencia</b> (S) y <b>orientación a personas</b> (pdcP).','profesionales':'Docentes de nivel inicial, primario y secundario, profesores especializados, psicopedagogos, educadores especiales, gestores educativos.'},
}

uni_slugs = {sigla: slugify(sigla) for sigla in data['universidades']}
uni_to_careers = defaultdict(list)
for c in data['carreras']:
    for u in c['universidades']:
        uni_to_careers[u['sigla']].append(c)
areas_slug_map = {a['id']: a['slug'] for a in data['areas']}

def gen_carrera(c):
    sd = sorted(c['vector'].items(), key=lambda x:-x[1])[:5]
    dims=''
    for k,v in sd:
        lab,des = DIM_DESC[k]
        dims += '<div class="dim-row"><div class="dim-label"><b>'+lab+'</b> · '+des+'</div><div class="dim-bar"><div class="dim-fill" style="width:'+str(v)+'%"></div></div><div class="dim-val">'+str(v)+'</div></div>'
    if c['universidades']:
        unis=''
        for u in c['universidades']:
            sl = uni_slugs.get(u['sigla'], slugify(u['sigla']))
            unis += '<a href="/guia/universidades/'+sl+'" class="uni-item"><div class="uni-sigla">'+u['sigla']+'</div><div class="uni-nombre">'+u['nombre']+'</div><div class="uni-tipo">'+u['sistema'].capitalize()+'</div></a>'
        unisb = '<p>'+str(len(c['universidades']))+' universidades argentinas dictan '+c['nombre']+':</p><div class="unis-grid">'+unis+'</div>'
    else:
        unisb = '<div class="unis-pending"><div class="unis-pending-title">🧭 Universidades en relevamiento</div><p>Estamos completando el mapa de universidades argentinas que dictan <b>'+c['nombre']+'</b>. Si conocés esta carrera, escribinos a <a href="mailto:hola@pathfinder.net.ar">hola@pathfinder.net.ar</a>.</p></div>'
    asl = areas_slug_map[c['area']]
    desc_txt = c.get('descripcion','').strip()
    dur_txt  = c.get('duracion','').strip()
    campo_txt= c.get('campo_laboral','').strip()
    if desc_txt:
        df = "<p>"+desc_txt+"</p>"
    else:
        df = "<p>Esta página todavía no tiene una descripción detallada. Pronto compartiremos información sobre <b>"+c['nombre']+"</b>. Mientras tanto, podés ver el perfil comportamental que mejor encaja con esta carrera, o volver a <a href='/guia/areas/"+asl+"'>"+c['area_nombre']+"</a> para explorar otras opciones.</p>"
    campo_block = ('<div class="section-block"><h2>Campo laboral</h2><p>'+campo_txt+'</p></div>') if campo_txt else ''
    dur_fact = ('<div class="quick-fact"><b>Duración típica</b><span>'+dur_txt+'</span></div>') if dur_txt else ''
    ac = c['area_color']
    ec = ".c-hero{padding:60px 0 50px;border-bottom:1px solid rgba(245,192,64,.08);margin-bottom:50px}.c-hero .area-link{display:inline-block;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:"+ac+";font-weight:700;margin-bottom:16px;padding:6px 14px;border:1px solid "+ac+"66;border-radius:99px}.c-hero .area-link:hover{background:"+ac+"22}.c-hero h1{font-family:'Cormorant Garamond',serif;font-size:62px;font-weight:400;line-height:1.05}.c-grid{display:grid;grid-template-columns:2fr 1fr;gap:60px;padding-bottom:60px}.c-main h2{font-family:'Cormorant Garamond',serif;font-size:34px;font-weight:400;margin:0 0 20px}.c-main p{color:rgba(255,248,236,.82);font-size:16px;margin-bottom:20px}.section-block{margin-bottom:50px}.aside{background:var(--card);border-radius:16px;padding:28px;height:fit-content;position:sticky;top:100px}.aside h4{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:14px}.quick-fact{padding:14px 0;border-bottom:1px solid rgba(245,192,64,.08);font-size:14px}.quick-fact:last-child{border:none}.quick-fact b{color:var(--cream);display:block;margin-bottom:4px;font-size:13px;letter-spacing:.5px}.quick-fact span{color:rgba(255,248,236,.7)}.dim-row{display:grid;grid-template-columns:160px 1fr 44px;gap:16px;align-items:center;margin-bottom:14px}.dim-bar{background:rgba(245,192,64,.1);border-radius:99px;height:8px;overflow:hidden}.dim-fill{height:100%;background:linear-gradient(90deg,"+ac+",var(--gold));border-radius:99px}.dim-label{font-size:13px;color:rgba(255,248,236,.75)}.dim-label b{color:var(--cream)}.dim-val{text-align:right;font-size:13px;color:var(--gold);font-weight:600}.unis-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:20px}.uni-item{background:var(--card);border:1px solid rgba(245,192,64,.08);border-radius:12px;padding:16px 18px;color:inherit!important;transition:all .2s}.uni-item:hover{border-color:"+ac+";transform:translateY(-2px)}.uni-sigla{font-family:'Cormorant Garamond',serif;font-size:20px;color:var(--gold);font-weight:600;margin-bottom:3px}.uni-nombre{font-size:13px;color:rgba(255,248,236,.8);line-height:1.3;margin-bottom:6px}.uni-tipo{font-size:11px;color:rgba(255,248,236,.5);text-transform:uppercase;letter-spacing:.8px}.unis-pending{background:var(--card);border:1px dashed rgba(245,192,64,.3);border-radius:16px;padding:28px;margin-top:20px}.unis-pending-title{font-family:'Cormorant Garamond',serif;font-size:22px;color:var(--gold);margin-bottom:10px}.unis-pending p{color:rgba(255,248,236,.75);font-size:14px;margin:0}@media (max-width:720px){.c-hero h1{font-size:40px}.c-grid{grid-template-columns:1fr}.unis-grid{grid-template-columns:1fr}.dim-row{grid-template-columns:120px 1fr 40px}}"
    nunis = len(c['universidades'])
    quf_u = str(nunis)+(' identificadas' if nunis!=1 else ' identificada')+(' · en relevamiento' if not c['universidades'] else '')
    return '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>'+c['nombre']+' — Carrera · PathFinder</title><meta name="description" content="'+c['nombre']+' en Argentina: perfil ideal, universidades y campo laboral. Guía de PathFinder."><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+CSS+ec+'</style></head><body>'+NAV+'<div class="wrap"><div class="crumb"><a href="/">Inicio</a> <span class="sep">/</span> <a href="/guia/">Guía</a> <span class="sep">/</span> <a href="/guia/carreras/">Carreras</a> <span class="sep">/</span> '+c['nombre']+'</div><section class="c-hero"><a href="/guia/areas/'+asl+'" class="area-link">'+c['area_nombre']+'</a><h1>'+c['nombre']+'</h1></section><div class="c-grid"><div class="c-main"><div class="section-block"><h2>¿De qué se trata?</h2>'+df+'</div>'+campo_block+'<div class="section-block"><h2>El perfil que encaja</h2><p>Las 5 dimensiones más altas del perfil típico de la carrera, según el motor de PathFinder:</p><div style="margin-top:20px">'+dims+'</div></div><div class="section-block"><h2>Dónde estudiarla</h2>'+unisb+'</div></div><aside class="aside"><h4>Datos rápidos</h4><div class="quick-fact"><b>Área</b><span>'+c['area_nombre']+'</span></div>'+dur_fact+'<div class="quick-fact"><b>Universidades</b><span>'+quf_u+'</span></div><div style="margin-top:24px"><h4>¿Encaja con vos?</h4><p style="font-size:13px;color:rgba(255,248,236,.7);margin-bottom:16px">Jugá PathFinder y descubrí si tu perfil comportamental real se alinea con esta carrera.</p><a href="https://pathfinder-rouge-iota.vercel.app/" class="btn-primary" style="display:block;text-align:center">Jugá ahora →</a></div></aside></div></div>'+FOOT+'</body></html>'

def gen_area(aid):
    a = data['areas'][aid]
    desc = AREAS_DESC.get(a['nombre'], {})
    cars = sorted([c for c in data['carreras'] if c['area']==aid], key=lambda c:c['nombre'])
    rows=''
    for c in cars:
        if c['universidades']:
            ps=[]
            for u in c['universidades'][:5]:
                sl = uni_slugs.get(u['sigla'], slugify(u['sigla']))
                ps.append('<a href="/guia/universidades/'+sl+'" style="color:rgba(255,248,236,.6)">'+u['sigla']+'</a>')
            us = ' · '.join(ps)
            if len(c['universidades']) > 5: us += ' · +'+str(len(c['universidades'])-5)+' más'
        else:
            us='<span style="color:rgba(255,248,236,.3);font-style:italic">universidades en relevamiento</span>'
        rows += '<a href="/guia/carreras/'+c['slug']+'" class="career-row"><div class="career-name">'+c['nombre']+'</div><div class="career-unis">'+us+'</div></a>'
    ac=a['color']
    ec = ".area-hero{padding:60px 0 40px;border-bottom:1px solid rgba(245,192,64,.08);margin-bottom:50px}.area-hero .count{font-size:11px;letter-spacing:2px;text-transform:uppercase;color:"+ac+";font-weight:700;margin-bottom:16px}.area-hero h1{font-family:'Cormorant Garamond',serif;font-size:66px;font-weight:400;line-height:1.05;margin-bottom:12px}.area-hero .tagline{font-size:22px;color:rgba(255,248,236,.75);font-style:italic;font-family:'Cormorant Garamond',serif;margin-bottom:30px}.area-content{display:grid;grid-template-columns:2fr 1fr;gap:60px;padding-bottom:60px}.area-content .main p{margin-bottom:20px;font-size:16px;color:rgba(255,248,236,.85)}.area-content h3{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:400;margin:40px 0 16px;color:var(--gold)}.aside{background:var(--card);border-radius:16px;padding:28px;height:fit-content}.aside h4{font-size:12px;letter-spacing:1.5px;text-transform:uppercase;color:"+ac+";font-weight:700;margin-bottom:14px}.aside p{font-size:14px;color:rgba(255,248,236,.8);margin-bottom:16px}.careers-section{padding:40px 0 60px}.careers-section h2{font-family:'Cormorant Garamond',serif;font-size:40px;font-weight:400;margin-bottom:30px}.careers-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border-top:1px solid rgba(245,192,64,.1)}.career-row{padding:20px 0;border-bottom:1px solid rgba(245,192,64,.08);color:inherit!important;transition:all .2s;padding-left:12px;padding-right:12px}.career-row:hover{background:rgba(245,192,64,.03);padding-left:20px}.career-name{font-family:'Cormorant Garamond',serif;font-size:22px;color:var(--cream);margin-bottom:4px}.career-unis{font-size:12px;color:rgba(255,248,236,.5);letter-spacing:.3px}.career-unis a{color:rgba(255,248,236,.65)}.career-unis a:hover{color:var(--gold)}@media (max-width:720px){.area-hero h1{font-size:46px}.area-content{grid-template-columns:1fr}.careers-grid{grid-template-columns:1fr}}"
    return '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>'+a['nombre']+' — Guía de carreras · PathFinder</title><meta name="description" content="Las '+str(len(cars))+' carreras de '+a['nombre']+' en Argentina: perfil, universidades y campo laboral."><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+CSS+ec+'</style></head><body>'+NAV+'<div class="wrap"><div class="crumb"><a href="/">Inicio</a> <span class="sep">/</span> <a href="/guia/">Guía</a> <span class="sep">/</span> <a href="/guia/areas/">Áreas</a> <span class="sep">/</span> '+a['nombre']+'</div><section class="area-hero"><div class="count">'+str(len(cars))+' carreras · Área '+str(aid)+'</div><h1>'+a['nombre']+'</h1><p class="tagline">'+desc.get('tagline','')+'</p></section><div class="area-content"><div class="main"><p>'+desc.get('intro','')+'</p><h3>¿A qué perfil le encaja?</h3><p>'+desc.get('perfil','')+'</p><h3>Profesionales típicos</h3><p>'+desc.get('profesionales','')+'</p></div><aside class="aside"><h4>¿No sabés si es tu área?</h4><p>El juego de PathFinder analiza tu comportamiento real a través de 8 zonas de juego y te muestra cuál es tu área primaria con un porcentaje de afinidad.</p><a href="https://pathfinder-rouge-iota.vercel.app/" class="btn-primary" style="display:block;text-align:center">Jugá PathFinder →</a></aside></div><section class="careers-section"><h2>Las '+str(len(cars))+' carreras del área</h2><div class="careers-grid">'+rows+'</div></section></div>'+FOOT+'</body></html>'

def gen_universidad(sigla, info):
    cars = sorted(uni_to_careers.get(sigla, []), key=lambda c:c['nombre'])
    ba = defaultdict(list)
    for c in cars: ba[c['area']].append(c)
    sections=''
    for aid, aa in sorted(ba.items()):
        a=data['areas'][aid]
        rs = ''.join('<a href="/guia/carreras/'+c['slug']+'" class="car-link">'+c['nombre']+'</a>' for c in aa)
        sections += '<section class="uni-area-sec" style="--c:'+a['color']+'"><h3>'+a['nombre']+' <span class="count">('+str(len(aa))+')</span></h3><div class="cars-list">'+rs+'</div></section>'
    sc = '#4CAF50' if info['sistema']=='pública' else '#9C27B0'
    web = '<a href="https://'+info['web']+'" target="_blank" rel="noopener">'+info['web']+' ↗</a>' if info.get('web') else '—'
    ec = ".u-hero{padding:60px 0 50px;border-bottom:1px solid rgba(245,192,64,.08);margin-bottom:50px}.u-hero .sistema{display:inline-block;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:"+sc+";font-weight:700;margin-bottom:16px;padding:6px 14px;border:1px solid "+sc+"66;border-radius:99px}.u-hero h1{font-family:'Cormorant Garamond',serif;font-size:48px;font-weight:400;line-height:1.1;margin-bottom:10px}.u-hero .sigla{font-family:'Cormorant Garamond',serif;font-size:28px;color:var(--gold);font-style:italic;margin-bottom:20px}.u-hero .web{font-size:15px}.u-info{background:var(--card);border-radius:16px;padding:28px;margin-bottom:40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}.u-info-item h4{font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:6px}.u-info-item p{color:rgba(255,248,236,.85);font-size:15px}.u-cars h2{font-family:'Cormorant Garamond',serif;font-size:40px;font-weight:400;margin-bottom:12px}.u-cars > p{color:rgba(255,248,236,.65);margin-bottom:30px}.uni-area-sec{margin-bottom:36px}.uni-area-sec h3{font-family:'Cormorant Garamond',serif;font-size:24px;font-weight:400;color:var(--c);border-bottom:2px solid var(--c);padding-bottom:8px;margin-bottom:14px}.uni-area-sec .count{font-size:13px;color:rgba(255,248,236,.4);font-style:italic}.cars-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:4px}.car-link{padding:8px 14px;color:rgba(255,248,236,.85)!important;font-size:14px;border-radius:8px;transition:all .15s;line-height:1.3}.car-link:hover{background:rgba(245,192,64,.08);color:var(--gold)!important;padding-left:18px}.no-cars{background:var(--card);border:1px dashed rgba(245,192,64,.3);border-radius:16px;padding:28px;text-align:center;color:rgba(255,248,236,.75)}"
    content = sections if cars else '<div class="no-cars">Esta universidad todavía no tiene carreras mapeadas en PathFinder. Si estudiás ahí, escribinos a <a href="mailto:hola@pathfinder.net.ar">hola@pathfinder.net.ar</a>.</div>'
    return '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>'+info['nombre']+' — Universidad · PathFinder</title><meta name="description" content="'+info['nombre']+' ('+sigla+'): oferta de carreras y datos."><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+CSS+ec+'</style></head><body>'+NAV+'<div class="wrap"><div class="crumb"><a href="/">Inicio</a> <span class="sep">/</span> <a href="/guia/">Guía</a> <span class="sep">/</span> <a href="/guia/universidades/">Universidades</a> <span class="sep">/</span> '+sigla+'</div><section class="u-hero"><div class="sistema">Sistema '+info['sistema']+'</div><h1>'+info['nombre']+'</h1><div class="sigla">'+sigla+'</div><div class="web"><b style="color:var(--muted)">Sitio web oficial:</b> '+web+'</div></section><div class="u-info"><div class="u-info-item"><h4>Sigla</h4><p>'+sigla+'</p></div><div class="u-info-item"><h4>Sistema</h4><p>'+info['sistema'].capitalize()+'</p></div><div class="u-info-item"><h4>Carreras mapeadas</h4><p>'+str(len(cars))+'</p></div><div class="u-info-item"><h4>Áreas que cubre</h4><p>'+str(len(ba))+' de 8</p></div></div><section class="u-cars"><h2>Carreras disponibles</h2><p>Las '+str(len(cars))+' carreras que '+sigla+' dicta y están mapeadas en PathFinder, agrupadas por área:</p>'+content+'</section></div>'+FOOT+'</body></html>'

def gen_universidades_index():
    pubs = sorted([(s,i) for s,i in data['universidades'].items() if i['sistema']=='pública'], key=lambda x:x[0])
    privs = sorted([(s,i) for s,i in data['universidades'].items() if i['sistema']=='privada'], key=lambda x:x[0])
    def card(s, info):
        n = len(uni_to_careers.get(s, []))
        return '<a href="/guia/universidades/'+uni_slugs[s]+'" class="u-card"><div class="u-card-sigla">'+s+'</div><div class="u-card-nombre">'+info['nombre']+'</div><div class="u-card-stat">'+str(n)+' carrera'+('s' if n!=1 else '')+'</div></a>'
    ph = ''.join(card(s,i) for s,i in pubs)
    prh = ''.join(card(s,i) for s,i in privs)
    ec = ".header{padding:60px 0 30px}.header h1{font-family:'Cormorant Garamond',serif;font-size:60px;font-weight:400;margin-bottom:12px}.header .sub{font-size:17px;color:rgba(255,248,236,.7);max-width:720px}.unis-section{margin-bottom:60px}.unis-section h2{font-family:'Cormorant Garamond',serif;font-size:34px;font-weight:400;margin-bottom:20px;color:var(--gold)}.unis-section .sys-tag{display:inline-block;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;background:rgba(245,192,64,.15);color:var(--gold);padding:4px 12px;border-radius:99px;margin-left:12px;font-weight:600}.unis-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}.u-card{background:var(--card);border:1px solid rgba(245,192,64,.08);border-radius:14px;padding:22px;color:inherit!important;transition:all .2s;display:block}.u-card:hover{border-color:var(--gold);transform:translateY(-3px)}.u-card-sigla{font-family:'Cormorant Garamond',serif;font-size:28px;color:var(--gold);font-weight:600;margin-bottom:6px}.u-card-nombre{font-size:14px;color:rgba(255,248,236,.85);line-height:1.3;margin-bottom:10px;min-height:36px}.u-card-stat{font-size:12px;color:rgba(255,248,236,.5);letter-spacing:.5px;text-transform:uppercase}"
    total = len(pubs)+len(privs)
    return '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Las '+str(total)+' universidades argentinas — Guía · PathFinder</title><meta name="description" content="Las '+str(total)+' universidades argentinas mapeadas en PathFinder: públicas y privadas."><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+CSS+ec+'</style></head><body>'+NAV+'<div class="wrap"><div class="crumb"><a href="/">Inicio</a> <span class="sep">/</span> <a href="/guia/">Guía</a> <span class="sep">/</span> Universidades</div><section class="header"><h1>Las '+str(total)+' <span style="color:var(--gold);font-style:italic">universidades</span></h1><p class="sub">Las universidades argentinas mapeadas en PathFinder, agrupadas entre sistema público y privado. Cada una con el listado de carreras que dicta.</p></section><section class="unis-section"><h2>Sistema público <span class="sys-tag">'+str(len(pubs))+' universidades</span></h2><div class="unis-grid">'+ph+'</div></section><section class="unis-section"><h2>Sistema privado <span class="sys-tag">'+str(len(privs))+' universidades</span></h2><div class="unis-grid">'+prh+'</div></section></div>'+FOOT+'</body></html>'

# EJECUCIÓN
n=0
for c in data['carreras']:
    with open(ROOT+'/carreras/'+c['slug']+'.html','w',encoding='utf-8') as f: f.write(gen_carrera(c))
    n+=1
print(f'OK Carreras: {n}')

for a in data['areas']:
    with open(ROOT+'/areas/'+a['slug']+'.html','w',encoding='utf-8') as f: f.write(gen_area(a['id']))
print('OK Areas: 8')

with open(ROOT+'/universidades/index.html','w',encoding='utf-8') as f: f.write(gen_universidades_index())
print('OK Universidades index')

n=0
for sigla, info in data['universidades'].items():
    with open(ROOT+'/universidades/'+uni_slugs[sigla]+'.html','w',encoding='utf-8') as f: f.write(gen_universidad(sigla, info))
    n+=1
print(f'OK Universidades: {n}')

sin = [c for c in data['carreras'] if not c['universidades']]
with open(ROOT+'/_carreras_sin_universidades.csv','w',encoding='utf-8',newline='') as f:
    w = csv.writer(f)
    w.writerow(['Carrera','Area','Universidades (siglas, coma)'])
    for c in sorted(sin, key=lambda c:(c['area_nombre'],c['nombre'])):
        w.writerow([c['nombre'], c['area_nombre'], ''])
print(f'OK CSV: {len(sin)} carreras sin universidades')

import glob
tot = len(glob.glob(ROOT+'/**/*.html', recursive=True))
print(f'TOTAL HTML: {tot}')
