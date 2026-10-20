# -*- coding: utf-8 -*-
"""
Contenido editorial para las 187 carreras.
Cada entrada: descripcion, duracion, campo_laboral, extra_unis.
extra_unis se agrega a las ya existentes (solo si estaba vacía).
"""

CONTENIDO = {
# ============== CIENCIAS DE LA SALUD (22) ==============
"medicina": {
    "descripcion": "Formación integral del médico generalista para diagnosticar, tratar y prevenir enfermedades. Combina ciencias básicas (anatomía, fisiología, bioquímica) con clínica hospitalaria desde los primeros años.",
    "duracion": "6 años + residencia",
    "campo_laboral": "Hospitales públicos y privados, consultorios, obras sociales, prepagas, salud pública, investigación biomédica, docencia universitaria, medicina legal, cooperación internacional.",
},
"odontologia": {
    "descripcion": "Prevención, diagnóstico y tratamiento de patologías bucodentales. Formación clínica desde segundo año con prácticas en pacientes reales y especialidades como ortodoncia, endodoncia o cirugía.",
    "duracion": "5 años",
    "campo_laboral": "Consultorio propio, clínicas odontológicas, obras sociales, hospitales, odontología estética, implantología, docencia e investigación.",
},
"farmacia-y-bioquimica": {
    "descripcion": "Dos carreras hermanadas: Farmacia prepara para el diseño, control y dispensa de medicamentos; Bioquímica analiza muestras biológicas para diagnóstico clínico. Base química, biológica y clínica.",
    "duracion": "5 años",
    "campo_laboral": "Farmacias de oficina y hospitalarias, laboratorios de análisis clínicos, industria farmacéutica, bromatología, control de calidad, investigación.",
},
"enfermeria": {
    "descripcion": "Cuidado integral del paciente en todas las etapas de la vida y niveles de atención. Combina conocimiento científico, procedimientos clínicos y vínculo humano con el paciente.",
    "duracion": "3 años (tecnicatura) o 5 años (licenciatura)",
    "campo_laboral": "Hospitales, clínicas, salas de guardia, cuidados intensivos, atención domiciliaria, geriátricos, obras sociales, instituciones educativas, salud comunitaria.",
},
"kinesiologia-y-fisiatria": {
    "descripcion": "Rehabilitación del movimiento humano: recuperación de lesiones traumatológicas, neurológicas, deportivas y respiratorias. Combina anatomía funcional, biomecánica y técnicas manuales.",
    "duracion": "5 años",
    "campo_laboral": "Consultorios, hospitales, clubes deportivos, centros de rehabilitación, cuidados intensivos (kinesiología respiratoria), geriátricos, atención domiciliaria.",
},
"fonoaudiologia": {
    "descripcion": "Diagnóstico y tratamiento de trastornos de la voz, el habla, el lenguaje, la audición y la deglución. Trabaja desde la lactancia hasta la vejez, en lo educativo y lo clínico.",
    "duracion": "5 años",
    "campo_laboral": "Hospitales, consultorios, escuelas, centros de rehabilitación auditiva, clínicas de voz, geriátricos, equipos interdisciplinarios de desarrollo infantil.",
},
"nutricion": {
    "descripcion": "Planificación de la alimentación como herramienta de salud, prevención y tratamiento. Abarca desde la nutrición clínica hospitalaria hasta la seguridad alimentaria y la nutrición deportiva.",
    "duracion": "5 años",
    "campo_laboral": "Hospitales, consultorios, servicios de alimentación institucional, clubes deportivos, industria alimentaria, salud pública, educación.",
},
"optometria": {
    "descripcion": "Evaluación de la función visual, prescripción de lentes y detección temprana de patologías oculares. Puente clínico entre el oftalmólogo y el paciente.",
    "duracion": "3-4 años (tecnicatura/licenciatura)",
    "campo_laboral": "Ópticas, clínicas oftalmológicas, laboratorios de lentes de contacto, hospitales, salud ocupacional.",
    "extra_unis": ["UNLP","UNNE","UB","UCA"],
},
"terapia-ocupacional": {
    "descripcion": "Acompañamiento de personas con discapacidad, trastornos del desarrollo o enfermedades que afectan sus actividades cotidianas, para recuperar o construir autonomía.",
    "duracion": "5 años",
    "campo_laboral": "Hospitales, centros de día, escuelas de educación especial, geriátricos, consultorios, equipos de rehabilitación neurológica y psiquiátrica.",
},
"psicologia": {
    "descripcion": "Estudio científico del comportamiento, los procesos mentales y la subjetividad humana. Formación amplia con orientaciones clínica, educacional, laboral, jurídica y social.",
    "duracion": "5-6 años",
    "campo_laboral": "Consultorio privado, hospitales, obras sociales, escuelas, empresas (RRHH, selección), peritaje judicial, investigación, docencia.",
},
"psicopedagogia": {
    "descripcion": "Diagnóstico y tratamiento de dificultades de aprendizaje. Trabaja en la intersección entre lo educativo y lo clínico, desde la primera infancia hasta la adolescencia.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas, gabinetes psicopedagógicos, consultorios, equipos interdisciplinarios, obras sociales, hospitales de día.",
},
"instrumentacion-quirurgica": {
    "descripcion": "Formación técnica en el manejo del instrumental y la logística del quirófano. Rol clave en el equipo quirúrgico junto al cirujano.",
    "duracion": "3 años (tecnicatura)",
    "campo_laboral": "Quirófanos de hospitales y clínicas, cirugía ambulatoria, salas de parto, industria de insumos médicos.",
    "extra_unis": ["UBA","UNC","UNR","UNNE","UCA"],
},
"biotecnologia-salud": {
    "descripcion": "Aplicación de organismos vivos o sus componentes a problemas sanitarios: vacunas, terapias génicas, diagnóstico molecular, biofármacos. Carrera de perfil científico-tecnológico.",
    "duracion": "5 años",
    "campo_laboral": "Laboratorios de investigación (CONICET, universidades), industria farmacéutica y biotecnológica, startups biotech, agencias regulatorias.",
},
"salud-publica": {
    "descripcion": "Mirada poblacional de la salud: diseño de políticas, programas de prevención, epidemiología y gestión de sistemas sanitarios. Generalmente como licenciatura o posgrado.",
    "duracion": "4-5 años",
    "campo_laboral": "Ministerios, hospitales (gestión), ONGs sanitarias, OPS/OMS, obras sociales, consultoría en políticas de salud.",
},
"bioquimica": {
    "descripcion": "Análisis clínicos de muestras biológicas para diagnóstico y seguimiento de pacientes. Formación química, biológica y clínica profunda, con amplio campo en investigación.",
    "duracion": "5 años",
    "campo_laboral": "Laboratorios de análisis clínicos, hospitales, bromatología, industria farmacéutica, investigación en biomedicina, control de calidad.",
    "extra_unis": ["UBA","UNLP","UNR","UNC","UNT"],
},
"licenciatura-en-bioimagenes": {
    "descripcion": "Operación e interpretación técnica de equipos de diagnóstico por imágenes: radiología, tomografía, resonancia, ecografía. Perfil técnico-sanitario de alta demanda.",
    "duracion": "4 años",
    "campo_laboral": "Centros de diagnóstico por imágenes, hospitales, clínicas, servicios de emergencia, radiología intervencionista.",
    "extra_unis": ["UNSAM","UNLaM","UCA","UB"],
},
"podologia": {
    "descripcion": "Prevención y tratamiento de patologías del pie. Rol central en pie diabético, geriatría y deporte. Formación técnica con fuerte componente clínico.",
    "duracion": "3 años (tecnicatura)",
    "campo_laboral": "Consultorio propio, centros de pie diabético, geriátricos, clubes deportivos, obras sociales.",
    "extra_unis": ["UB","UAI","UCES","USAL"],
},
"toxicologia": {
    "descripcion": "Estudio de los efectos adversos de sustancias químicas sobre el organismo. En Argentina se accede principalmente como orientación o posgrado desde Bioquímica, Farmacia o Medicina.",
    "duracion": "5 años (base) + especialización",
    "campo_laboral": "Hospitales (toxicología clínica), peritaje forense, control bromatológico, salud ocupacional, industria química y farmacéutica.",
    "extra_unis": ["UBA","UNC","UNLP","UNR"],
},
"epidemiologia": {
    "descripcion": "Estudio de la distribución y los determinantes de enfermedades en poblaciones. En Argentina se cursa típicamente como posgrado tras una carrera de ciencias de la salud.",
    "duracion": "Posgrado (2-3 años)",
    "campo_laboral": "Ministerios de Salud, hospitales, OPS/OMS, investigación biomédica, docencia universitaria, consultoría sanitaria.",
    "extra_unis": ["UBA","UNC","UNLP","FLACSO"],
},
"hemoterapia-e-inmunohematologia": {
    "descripcion": "Técnicas de obtención, procesamiento y transfusión de sangre y hemocomponentes. Rol técnico-sanitario crítico en bancos de sangre y servicios transfusionales.",
    "duracion": "3 años (tecnicatura)",
    "campo_laboral": "Bancos de sangre, servicios de hemoterapia hospitalaria, centros de donación, laboratorios de inmunohematología.",
    "extra_unis": ["UBA","UNR","UNC","UCA"],
},
"musicoterapia": {
    "descripcion": "Uso terapéutico del sonido y la música en procesos de salud mental, rehabilitación neurológica, estimulación temprana y acompañamiento en cuidados paliativos.",
    "duracion": "5 años",
    "campo_laboral": "Hospitales, centros de día, escuelas especiales, geriátricos, consultorios, equipos interdisciplinarios de salud mental.",
},
"gerontologia": {
    "descripcion": "Abordaje integral del envejecimiento desde lo biológico, lo psicológico y lo social. Dado el envejecimiento poblacional argentino, es un campo con fuerte proyección.",
    "duracion": "4-5 años (licenciatura/posgrado)",
    "campo_laboral": "Geriátricos, hospitales, programas comunitarios, PAMI, consultoría en políticas de envejecimiento activo, educación.",
},

# ============== CIENCIAS SOCIALES Y HUMANAS (30) ==============
"derecho": {
    "descripcion": "Formación en el ordenamiento jurídico: derecho civil, penal, comercial, laboral, constitucional, internacional. Prepara para el ejercicio profesional y la carrera judicial.",
    "duracion": "5-6 años",
    "campo_laboral": "Ejercicio liberal, estudios jurídicos, poder judicial, empresas (compliance, legales), administración pública, docencia e investigación.",
},
"sociologia": {
    "descripcion": "Análisis científico de la vida social: estructuras, instituciones, desigualdades, movimientos colectivos. Herramientas cuantitativas y cualitativas para investigar lo social.",
    "duracion": "5 años",
    "campo_laboral": "Investigación social, consultoría, políticas públicas, ONGs, think tanks, docencia, estudios de opinión y mercado.",
},
"ciencia-politica": {
    "descripcion": "Estudio del poder, los sistemas políticos, el Estado y las políticas públicas. Combina teoría política, análisis institucional y métodos de investigación empírica.",
    "duracion": "4-5 años",
    "campo_laboral": "Administración pública, partidos políticos, parlamento, ONGs, think tanks, comunicación política, cooperación internacional, docencia.",
},
"relaciones-internacionales": {
    "descripcion": "Formación en política mundial, derecho internacional, comercio exterior y organismos multilaterales. Perfil diplomático, de cooperación o de negocios internacionales.",
    "duracion": "4-5 años",
    "campo_laboral": "Cancillería, embajadas, organismos internacionales (ONU, OEA, OMC), empresas multinacionales, cooperación internacional, ONGs globales.",
},
"trabajo-social": {
    "descripcion": "Intervención profesional en problemáticas sociales desde una mirada de derechos. Trabajo territorial con familias, comunidades e instituciones.",
    "duracion": "5 años",
    "campo_laboral": "Hospitales, escuelas, municipios, ONGs, servicios de niñez, programas sociales, salud mental comunitaria, poder judicial (equipos interdisciplinarios).",
},
"filosofia": {
    "descripcion": "Reflexión rigurosa sobre los grandes problemas del pensamiento: conocimiento, ética, política, lenguaje. Herramienta transversal para la investigación y la docencia.",
    "duracion": "5 años",
    "campo_laboral": "Docencia secundaria y universitaria, investigación (CONICET), edición académica, consultoría ética, periodismo cultural.",
},
"historia": {
    "descripcion": "Investigación y enseñanza de los procesos históricos. Formación amplia en metodología, archivos y debates historiográficos sobre Argentina, América Latina y el mundo.",
    "duracion": "5 años",
    "campo_laboral": "Docencia secundaria y universitaria, investigación (CONICET), museos, archivos, patrimonio cultural, divulgación histórica, editorial.",
},
"geografia": {
    "descripcion": "Estudio de los procesos naturales y humanos que organizan el espacio terrestre. Herramientas GIS, planificación territorial y análisis ambiental.",
    "duracion": "5 años",
    "campo_laboral": "Ordenamiento territorial, planificación urbana, estudios ambientales, docencia, cartografía digital, consultoría en catastro y GIS.",
},
"letras-literaturas": {
    "descripcion": "Estudio crítico de la literatura y el lenguaje en todas sus variantes: literatura argentina, hispanoamericana, clásica, teoría literaria y lingüística.",
    "duracion": "5 años",
    "campo_laboral": "Docencia, investigación literaria, edición, corrección, periodismo cultural, guionismo, traducción, gestión cultural.",
},
"linguistica": {
    "descripcion": "Estudio científico del lenguaje humano: fonología, sintaxis, semántica, sociolingüística. Puente entre humanidades y ciencias cognitivas.",
    "duracion": "5 años",
    "campo_laboral": "Investigación (CONICET), docencia, procesamiento del lenguaje natural (IA), lexicografía, planificación lingüística, consultoría editorial.",
    "extra_unis": ["UBA","UNC","UNLP","UNT","UNR"],
},
"antropologia": {
    "descripcion": "Estudio de la diversidad cultural y biológica de la humanidad. Orientaciones social, arqueológica y biológica. Trabajo de campo y análisis simbólico.",
    "duracion": "5-6 años",
    "campo_laboral": "Investigación, museos, patrimonio cultural, consultoría intercultural, políticas públicas, ONGs de pueblos originarios, docencia.",
},
"arqueologia": {
    "descripcion": "Estudio de culturas pasadas a través de sus restos materiales. Combina trabajo de campo (excavación), laboratorio y análisis histórico-cultural.",
    "duracion": "5 años",
    "campo_laboral": "Investigación (CONICET), museos, patrimonio cultural, consultoría en obras públicas (impacto arqueológico), docencia.",
    "extra_unis": ["UBA","UNLP","UNC","UNT","UNCO"],
},
"comunicacion-social": {
    "descripcion": "Estudio de los procesos de comunicación mediática, cultural e institucional. Combina teoría, análisis de discurso y producción en distintos formatos.",
    "duracion": "4-5 años",
    "campo_laboral": "Medios, agencias de publicidad y PR, comunicación institucional en empresas y gobierno, docencia, producción audiovisual, redes sociales.",
},
"periodismo": {
    "descripcion": "Formación específica para la cobertura informativa, la investigación periodística y la narración en medios gráficos, radiales, televisivos y digitales.",
    "duracion": "4 años",
    "campo_laboral": "Medios de comunicación, redacciones digitales, agencias de noticias, podcasts, documentales, comunicación corporativa, freelance.",
},
"publicidad": {
    "descripcion": "Diseño estratégico y creativo de campañas publicitarias. Combina investigación de mercado, redacción creativa, dirección de arte y planificación de medios.",
    "duracion": "4 años",
    "campo_laboral": "Agencias de publicidad, departamentos de marketing, consultoras de branding, productoras audiovisuales, freelance creativo.",
},
"relaciones-publicas": {
    "descripcion": "Gestión de la reputación y los vínculos de una organización con sus públicos. Comunicación institucional, prensa, eventos y gestión de crisis.",
    "duracion": "4 años",
    "campo_laboral": "Consultoras de PR, áreas de comunicación de empresas y gobierno, agencias de prensa, organización de eventos, lobby.",
},
"psicologia-social": {
    "descripcion": "Mirada específica sobre los procesos psíquicos en lo colectivo: grupos, instituciones, vínculos. En Argentina es carrera independiente (Pichon-Rivière) o especialización.",
    "duracion": "3-4 años",
    "campo_laboral": "Grupos de reflexión, trabajo comunitario, RRHH, intervención en instituciones, acompañamiento terapéutico, consultoría organizacional.",
    "extra_unis": ["UCES","UB","UP","UAI"],
},
"turismo": {
    "descripcion": "Gestión integral de la actividad turística: diseño de productos, operaciones, marketing de destinos y sustentabilidad. Puente entre lo cultural y lo económico.",
    "duracion": "4-5 años",
    "campo_laboral": "Agencias de viajes, hoteles, organismos de promoción turística, consultoría en destinos, cruceros, turismo rural y de aventura.",
},
"hoteleria": {
    "descripcion": "Gestión de establecimientos de alojamiento y servicios asociados: operaciones, revenue management, F&B, calidad de servicio y recursos humanos.",
    "duracion": "4 años",
    "campo_laboral": "Hoteles de cadenas internacionales y boutique, cruceros, resorts, consultoría hotelera, emprendimientos propios.",
},
"gestion-cultural": {
    "descripcion": "Formación en el diseño y producción de proyectos culturales: festivales, programación de espacios, políticas culturales y gestión de patrimonio.",
    "duracion": "4-5 años",
    "campo_laboral": "Centros culturales, teatros, museos, festivales, gobiernos locales, fundaciones, producción independiente.",
},
"bibliotecologia": {
    "descripcion": "Organización, preservación y acceso a la información documental: desde bibliotecas tradicionales hasta repositorios digitales y bibliotecas especializadas.",
    "duracion": "4 años",
    "campo_laboral": "Bibliotecas universitarias, escolares, públicas, archivos, centros de documentación, repositorios digitales, consultoría en información.",
    "extra_unis": ["UBA","UNC","UNLP","UNMDP","UNNE"],
},
"archivistica": {
    "descripcion": "Gestión documental de archivos históricos y administrativos: clasificación, conservación, digitalización y acceso. Clave para patrimonio y transparencia.",
    "duracion": "3-4 años",
    "campo_laboral": "Archivos nacionales, provinciales y municipales, archivos de empresas, universidades, poder judicial, patrimonio documental.",
    "extra_unis": ["UNC","UNLP","UBA","UNNE"],
},
"criminologia": {
    "descripcion": "Estudio del delito, sus causas y los sistemas de control social. Enfoque interdisciplinario entre derecho, sociología, psicología y ciencia política.",
    "duracion": "4-5 años",
    "campo_laboral": "Instituciones penales, consultoría en seguridad, poder judicial, investigación, medios especializados, políticas públicas de seguridad.",
},
"seguridad": {
    "descripcion": "Licenciaturas en Seguridad orientadas a la gestión de la seguridad pública y privada, prevención del delito y análisis criminal.",
    "duracion": "4 años",
    "campo_laboral": "Fuerzas de seguridad, consultoría en seguridad privada, análisis criminal, políticas públicas, inteligencia estratégica.",
    "extra_unis": ["IUPFA","UCES","UNLa","UB"],
},
"tecnicatura-en-diseno-y-comunicacion": {
    "descripcion": "Formación corta y aplicada en diseño gráfico, digital y comunicación visual. Base para insertarse rápido en estudios y agencias.",
    "duracion": "2-3 años (tecnicatura)",
    "campo_laboral": "Estudios de diseño, agencias de publicidad, equipos de comunicación en empresas, freelance, producción editorial.",
    "extra_unis": ["UP","UADE","UB","ORT"],
},
"notariado-escribania": {
    "descripcion": "Carrera específica para el ejercicio del notariado: fe pública, redacción de escrituras, derecho inmobiliario y societario. Suele cursarse como orientación de Derecho.",
    "duracion": "5-6 años",
    "campo_laboral": "Escribanía propia, colegios de escribanos, departamentos legales inmobiliarios, poder judicial, docencia.",
},
"traductorado-traduccion": {
    "descripcion": "Formación técnica y lingüística para la traducción pública y literaria en idiomas como inglés, francés, portugués o alemán. Incluye traducción jurídica y especializada.",
    "duracion": "4-5 años",
    "campo_laboral": "Traductorado público (matriculado), editoriales, agencias de traducción, organismos internacionales, freelance, interpretación.",
},
"criminalistica": {
    "descripcion": "Ciencia aplicada al esclarecimiento de hechos delictivos: pericias, balística, documentoscopía, dactiloscopía y análisis de escena del crimen.",
    "duracion": "4 años",
    "campo_laboral": "Poder judicial, policía científica, peritaje forense, consultoría privada, docencia e investigación.",
},
"ciencias-del-comportamiento": {
    "descripcion": "Mirada interdisciplinaria entre psicología, economía y neurociencias sobre cómo tomamos decisiones. Carrera reciente en Argentina, con fuerte proyección aplicada.",
    "duracion": "4 años",
    "campo_laboral": "Consultoría en behavioral economics, UX research, políticas públicas, marketing, investigación aplicada, startups.",
},
"comunicacion-digital": {
    "descripcion": "Comunicación específicamente en entornos digitales: contenidos, SEO, redes sociales, analítica, estrategia multiplataforma y narrativa transmedia.",
    "duracion": "4 años",
    "campo_laboral": "Agencias digitales, áreas de marketing digital en empresas, medios nativos digitales, content studios, consultoría, freelance.",
},

# ============== CIENCIAS EXACTAS Y NATURALES (19) ==============
"matematica": {
    "descripcion": "Estudio profundo de estructuras abstractas, análisis, álgebra, probabilidad y modelos matemáticos. Base de la ciencia moderna y de muchas tecnologías.",
    "duracion": "5 años",
    "campo_laboral": "Investigación (CONICET), docencia universitaria, data science, finanzas cuantitativas, criptografía, consultoría científica.",
},
"fisica": {
    "descripcion": "Estudio de las leyes fundamentales que rigen la materia y la energía. Investigación teórica y experimental con fuerte base matemática y de laboratorio.",
    "duracion": "5-6 años",
    "campo_laboral": "Investigación (CONICET, Balseiro, CNEA), tecnología nuclear, energías, instrumentación, consultoría científica, docencia.",
},
"quimica": {
    "descripcion": "Estudio de la composición, estructura y transformaciones de la materia. Formación general con salidas hacia química orgánica, inorgánica, analítica y de materiales.",
    "duracion": "5 años",
    "campo_laboral": "Industria química, farmacéutica, petroquímica, laboratorios de control de calidad, investigación, docencia.",
},
"biologia": {
    "descripcion": "Estudio de la vida en todos sus niveles, desde lo molecular hasta los ecosistemas. Orientaciones diversas: molecular, ecológica, genética, zoológica, botánica.",
    "duracion": "5 años",
    "campo_laboral": "Investigación (CONICET), biotecnología, consultoría ambiental, museos de ciencias, docencia, divulgación científica.",
},
"geologia": {
    "descripcion": "Estudio de la Tierra sólida: minerales, rocas, procesos geológicos, recursos naturales. Fuerte trabajo de campo y laboratorio.",
    "duracion": "5 años",
    "campo_laboral": "Minería, petróleo y gas, hidrogeología, estudios ambientales, investigación (CONICET), docencia.",
    "extra_unis": ["UBA","UNC","UNLP","UNT","UNS"],
},
"astronomia": {
    "descripcion": "Estudio del universo, los cuerpos celestes y los procesos cósmicos. Formación matemática y física intensa, con uso de observatorios y modelado computacional.",
    "duracion": "5 años",
    "campo_laboral": "Investigación (CONICET), observatorios (OAC, CASLEO), docencia universitaria, divulgación científica, planetarios.",
    "extra_unis": ["UNLP","UNC","UNR"],
},
"meteorologia": {
    "descripcion": "Estudio de la atmósfera, el clima y los fenómenos meteorológicos. Combina física, matemática y simulación numérica de gran escala.",
    "duracion": "5 años",
    "campo_laboral": "Servicio Meteorológico Nacional, aeronáutica, agro, consultoría climática, investigación, medios.",
    "extra_unis": ["UBA"],
},
"oceanografia": {
    "descripcion": "Estudio físico, químico y biológico de los océanos. Carrera con fuerte componente de campo (campañas oceanográficas) y laboratorio.",
    "duracion": "5 años",
    "campo_laboral": "Investigación (CONICET, INIDEP), pesca, estudios ambientales marinos, consultoría costera, docencia.",
    "extra_unis": ["UNS","UBA","UNMDP"],
},
"paleontologia": {
    "descripcion": "Estudio de los seres vivos del pasado a través del registro fósil. En Argentina se accede principalmente desde Biología o Geología con orientación o posgrado.",
    "duracion": "5 años + especialización",
    "campo_laboral": "Investigación (CONICET), museos de ciencias naturales, parques y reservas, docencia, divulgación científica.",
    "extra_unis": ["UNLP","UNC","UBA","UNT"],
},
"estadistica": {
    "descripcion": "Diseño de experimentos y análisis de datos para extraer conclusiones confiables en ciencia, industria y políticas públicas. Base matemática y computacional sólida.",
    "duracion": "5 años",
    "campo_laboral": "INDEC, consultoría, finanzas, data science, laboratorios, salud pública, docencia e investigación.",
},
"ciencias-de-la-atmosfera": {
    "descripcion": "Estudio profundo de los procesos atmosféricos y climáticos a distintas escalas. Más amplia que la meteorología clásica, con fuerte énfasis en cambio climático.",
    "duracion": "5 años",
    "campo_laboral": "Investigación en cambio climático, SMN, agro, consultoría ambiental, modelado climático, políticas públicas.",
    "extra_unis": ["UBA"],
},
"ecologia": {
    "descripcion": "Estudio de las relaciones entre organismos y su ambiente. Herramienta central para la conservación, el manejo de recursos y el estudio del cambio climático.",
    "duracion": "5 años (orientación en Biología)",
    "campo_laboral": "Áreas protegidas, APN, consultoría ambiental, investigación, ONGs ambientalistas, políticas públicas.",
    "extra_unis": ["UNC","UNS","UNLP","UBA","UNCO"],
},
"genetica": {
    "descripcion": "Estudio de la herencia y la variación genética. Carrera clave en biotecnología, mejoramiento vegetal/animal y diagnóstico molecular.",
    "duracion": "5 años",
    "campo_laboral": "Laboratorios de diagnóstico molecular, biotecnología agrícola, investigación biomédica, forense genética, docencia.",
    "extra_unis": ["UNNE","UBA","UNLP","UNR"],
},
"microbiologia": {
    "descripcion": "Estudio de microorganismos: bacterias, virus, hongos y parásitos. Clave en salud, industria alimentaria y biotecnología.",
    "duracion": "5 años",
    "campo_laboral": "Laboratorios clínicos, bromatología, industria alimentaria y farmacéutica, investigación biomédica, control de calidad.",
    "extra_unis": ["UBA","UNC","UNLP","UNR","UNT"],
},
"bioinformatica": {
    "descripcion": "Cruce entre biología molecular, estadística y computación: análisis de genomas, proteómica, modelado de redes biológicas y biología de sistemas.",
    "duracion": "5 años",
    "campo_laboral": "Investigación biomédica, startups biotech, farmacéutica, agro-biotecnología, data science aplicada a biología.",
},
"ciencias-del-suelo-exactas": {
    "descripcion": "Estudio físico-químico-biológico del suelo como recurso natural. Base para agricultura, ingeniería ambiental y planificación territorial.",
    "duracion": "5 años (orientación)",
    "campo_laboral": "INTA, consultoría agropecuaria, estudios ambientales, investigación, políticas públicas de suelos.",
    "extra_unis": ["UBA","UNS","UNLP","UNR"],
},
"geofisica": {
    "descripcion": "Estudio de los procesos físicos del interior terrestre: sismología, prospección, geomagnetismo. Herramienta clave para exploración de recursos y riesgo sísmico.",
    "duracion": "5 años",
    "campo_laboral": "Industria petrolera, minería, investigación (CONICET), INPRES, consultoría geofísica.",
    "extra_unis": ["UNLP","UNS","UNR"],
},
"mineralogia": {
    "descripcion": "Estudio de los minerales: identificación, génesis y aplicaciones. Se cursa como orientación o especialización de Geología.",
    "duracion": "5 años (como orientación)",
    "campo_laboral": "Minería, museos de ciencias, investigación, consultoría geológica, gemología.",
    "extra_unis": ["UBA","UNC","UNLP","UNT","UNS"],
},
"quimica-industrial": {
    "descripcion": "Formación aplicada en procesos químicos industriales: diseño, operación, control de calidad y seguridad. Puente entre química pura e ingeniería química.",
    "duracion": "5 años",
    "campo_laboral": "Industria química, petroquímica, farmacéutica, alimentos, cosméticos, control de calidad, I+D industrial.",
    "extra_unis": ["UTN","UBA","UNL","UNS"],
},

# ============== INGENIERÍA Y TECNOLOGÍA (33) ==============
"ingenieria-civil": {
    "descripcion": "Diseño, cálculo y construcción de obras civiles: edificios, puentes, caminos, obras hidráulicas y sanitarias. Fuerte base matemática y de materiales.",
    "duracion": "5-6 años",
    "campo_laboral": "Empresas constructoras, estudios de ingeniería, obras públicas (Vialidad, AySA), consultoría, dirección de obra, docencia.",
},
"ingenieria-mecanica": {
    "descripcion": "Diseño y mantenimiento de máquinas, mecanismos y sistemas térmicos. Base amplia para industria metalmecánica, automotriz y energética.",
    "duracion": "5-6 años",
    "campo_laboral": "Industria automotriz, metalmecánica, agroindustria, energías, mantenimiento industrial, consultoría, diseño mecánico.",
},
"ingenieria-electrica": {
    "descripcion": "Diseño, operación y mantenimiento de sistemas eléctricos de potencia: generación, transmisión y distribución de energía eléctrica.",
    "duracion": "5-6 años",
    "campo_laboral": "Distribuidoras eléctricas, generadoras, industria, consultoría energética, obras electromecánicas, energías renovables.",
},
"ingenieria-electronica": {
    "descripcion": "Diseño de circuitos y sistemas electrónicos: desde microelectrónica hasta sistemas embebidos, telecomunicaciones y control automático.",
    "duracion": "5-6 años",
    "campo_laboral": "Industria electrónica, telecomunicaciones, automatización, aeroespacial (INVAP, CONAE), startups de hardware, I+D.",
},
"ingenieria-industrial": {
    "descripcion": "Gestión integral de sistemas productivos: optimización de procesos, calidad, logística, recursos humanos y proyectos. Perfil técnico-gerencial.",
    "duracion": "5-6 años",
    "campo_laboral": "Industria manufacturera, consultoría, logística, operaciones en empresas de servicios, management, emprendimientos propios.",
},
"ingenieria-en-sistemas-informatica": {
    "descripcion": "Análisis, diseño y desarrollo de sistemas de software y bases de datos. Carrera eje del sector IT argentino, con enorme demanda y variedad de salidas.",
    "duracion": "5 años",
    "campo_laboral": "Empresas de software y servicios IT, bancos, startups, consultoría, product management, desarrollo full-stack, DevOps.",
},
"ingenieria-quimica": {
    "descripcion": "Diseño y operación de procesos químicos a escala industrial. Combina química, termodinámica, operaciones unitarias y economía de plantas.",
    "duracion": "5-6 años",
    "campo_laboral": "Petroquímica, farmacéutica, alimentos, papelera, celulosa, minería, cosméticos, I+D industrial.",
},
"ingenieria-en-alimentos": {
    "descripcion": "Diseño de procesos para elaborar alimentos seguros, nutritivos y escalables. Combina química, microbiología y operaciones unitarias.",
    "duracion": "5 años",
    "campo_laboral": "Industria alimentaria, bromatología, control de calidad, I+D de productos, consultoría, exportación.",
},
"ingenieria-agronomica": {
    "descripcion": "Formación integral para la producción agrícola, ganadera y agroindustrial. Combina agronomía, economía rural y gestión tecnológica.",
    "duracion": "5 años",
    "campo_laboral": "Empresas agropecuarias, INTA, acopiadoras, agroexportadoras, consultoría, insumos agrícolas, emprendimientos propios.",
},
"ingenieria-ambiental": {
    "descripcion": "Diseño de soluciones para problemas ambientales: tratamiento de efluentes, residuos, aire, remediación de suelos y evaluación de impacto.",
    "duracion": "5 años",
    "campo_laboral": "Consultoría ambiental, industria, gobiernos (impacto), ONGs, saneamiento, sector energético.",
},
"ingenieria-aeronautica": {
    "descripcion": "Diseño, construcción y mantenimiento de aeronaves y sus sistemas. Especialización técnica muy requerida y con proyección aeroespacial.",
    "duracion": "5-6 años",
    "campo_laboral": "Industria aeronáutica, FAdeA, CONAE, INVAP, aerolíneas (mantenimiento), consultoría, defensa.",
},
"ingenieria-naval-y-mecanica": {
    "descripcion": "Diseño y construcción de buques, embarcaciones y estructuras navales. Formación con base en ingeniería mecánica aplicada al medio acuático.",
    "duracion": "5-6 años",
    "campo_laboral": "Astilleros, armada, flota pesquera, consultoría naval, offshore, inspección y certificación naval.",
},
"ingenieria-metalurgica": {
    "descripcion": "Procesos de obtención y transformación de metales. Clave en siderurgia, industria del aluminio y manufactura metalmecánica.",
    "duracion": "5 años",
    "campo_laboral": "Siderurgia (Techint, Aluar), metalmecánica, I+D de materiales, minería, consultoría metalúrgica.",
    "extra_unis": ["UNSAM","UTN","UBA","UNS"],
},
"ingenieria-de-minas": {
    "descripcion": "Exploración, extracción y procesamiento de recursos minerales. Combina geología aplicada, operaciones mineras y gestión ambiental.",
    "duracion": "5 años",
    "campo_laboral": "Empresas mineras, consultoría, SEGEMAR, estudios de prefactibilidad, auditoría ambiental minera.",
    "extra_unis": ["UNSJ","UNT"],
},
"ingenieria-en-petroleo": {
    "descripcion": "Exploración, extracción, producción y transporte de hidrocarburos. Carrera estratégica para el sector energético argentino, con fuerte presencia en Vaca Muerta.",
    "duracion": "5 años",
    "campo_laboral": "YPF, operadoras internacionales, servicios petroleros, consultoría energética, I+D en Vaca Muerta.",
},
"ingenieria-biomedica": {
    "descripcion": "Aplicación de la ingeniería al diseño de equipamiento médico, prótesis, bioinstrumentación y software clínico. Puente entre tecnología y salud.",
    "duracion": "5-6 años",
    "campo_laboral": "Industria de equipamiento médico, hospitales (ingeniería clínica), startups healthtech, I+D, regulatoria sanitaria.",
},
"ingenieria-en-telecomunicaciones": {
    "descripcion": "Diseño de redes y sistemas de comunicación: fibra óptica, redes móviles 5G, satélites, infraestructura de datos. Rama especializada de la electrónica.",
    "duracion": "5-6 años",
    "campo_laboral": "Operadoras de telecomunicaciones, ENACOM, fabricantes de equipamiento, ARSAT, consultoría en redes.",
},
"ingenieria-en-materiales": {
    "descripcion": "Diseño y caracterización de nuevos materiales: polímeros, cerámicos, metales, composites y nanomateriales. Clave en innovación industrial y aeroespacial.",
    "duracion": "5 años",
    "campo_laboral": "I+D en industria, CNEA, INVAP, consultoría, nanotecnología, aeroespacial, startups de materiales avanzados.",
    "extra_unis": ["UNSAM","ITBA","UBA"],
},
"ingenieria-en-energias-renovables": {
    "descripcion": "Diseño y gestión de sistemas de generación renovable: solar, eólica, biomasa, hidrógeno. Área con enorme proyección en la matriz energética.",
    "duracion": "5 años",
    "campo_laboral": "Parques eólicos y solares, consultoras energéticas, gobierno (energía), startups cleantech, cooperativas eléctricas.",
    "extra_unis": ["UNSAM","UNLa","UTN","UNS"],
},
"licenciatura-en-ciencias-de-la-computacion": {
    "descripcion": "Enfoque teórico-científico de la computación: algoritmos, complejidad, inteligencia artificial, lenguajes de programación. Más rigurosa que las ingenierías aplicadas en IT.",
    "duracion": "5 años",
    "campo_laboral": "Investigación en IA, startups de alto componente técnico, big tech, academia, criptografía, data science avanzada.",
},
"licenciatura-en-analisis-de-sistemas": {
    "descripcion": "Formación aplicada en desarrollo de software y análisis de sistemas de información. Más corta que la ingeniería, con rápida inserción laboral.",
    "duracion": "4 años",
    "campo_laboral": "Empresas de software, consultoría IT, bancos, startups, desarrollo full-stack, análisis funcional.",
    "extra_unis": ["UBA","UCA","UP","UAI"],
},
"tecnicatura-en-programacion": {
    "descripcion": "Formación corta y aplicada en programación: desarrollo web, mobile y de sistemas. Puerta rápida al mercado IT, con posibilidad de continuar a licenciatura.",
    "duracion": "2-3 años",
    "campo_laboral": "Desarrollo de software, soporte técnico avanzado, QA, startups, freelance.",
    "extra_unis": ["UTN","UNQ","UNSAM","UP"],
},
"tecnicatura-en-redes": {
    "descripcion": "Formación aplicada en diseño, implementación y administración de redes informáticas. Base técnica para roles en infraestructura IT.",
    "duracion": "2-3 años",
    "campo_laboral": "Administración de redes, data centers, telecomunicaciones, ciberseguridad operativa, soporte avanzado.",
    "extra_unis": ["UTN","UNLaM","UNQ","UAI"],
},
"tecnicatura-en-electronica": {
    "descripcion": "Formación técnica aplicada en electrónica analógica y digital, microcontroladores y sistemas embebidos. Base rápida para industria y automatización.",
    "duracion": "2-3 años",
    "campo_laboral": "Industria electrónica, automatización, mantenimiento, Internet of Things, emprendimientos hardware.",
    "extra_unis": ["UTN","UNQ","UNSAM"],
},
"tecnicatura-en-mecatronica": {
    "descripcion": "Integración de mecánica, electrónica, control y software en sistemas automatizados. Perfil técnico muy demandado en industria 4.0.",
    "duracion": "2-3 años",
    "campo_laboral": "Automatización industrial, robótica, mantenimiento mecatrónico, manufactura avanzada, emprendimientos técnicos.",
    "extra_unis": ["UNQ","UNSAM","UTN"],
},
"inteligencia-artificial": {
    "descripcion": "Diseño de sistemas que aprenden de datos: machine learning, deep learning, procesamiento de lenguaje natural y visión por computadora. Base matemática fuerte.",
    "duracion": "5 años",
    "campo_laboral": "Startups de IA, consultoría avanzada, big tech, bancos, investigación aplicada, productos basados en modelos.",
},
"ciencia-de-datos": {
    "descripcion": "Extracción de valor a partir de datos: estadística, programación, machine learning y visualización. Carrera transversal con enorme demanda intersectorial.",
    "duracion": "4-5 años",
    "campo_laboral": "Bancos, telcos, retail, consultoría, startups, salud, agro, gobierno (data-driven decisions).",
},
"ciberseguridad": {
    "descripcion": "Protección de sistemas, redes y datos frente a amenazas. Combina programación, redes, criptografía, análisis forense y gestión de riesgos.",
    "duracion": "4-5 años",
    "campo_laboral": "Bancos, telcos, consultoría de seguridad, SOCs, pentesting, respuesta a incidentes, gobierno.",
},
"robotica": {
    "descripcion": "Diseño e implementación de robots y sistemas autónomos. Convergencia de mecánica, electrónica, control y software con IA aplicada.",
    "duracion": "5 años",
    "campo_laboral": "Automatización industrial, startups de robótica, I+D, logística automatizada, agro-robótica, educación.",
    "extra_unis": ["UNQ","UNSAM","UTN","ITBA"],
},
"ingenieria-en-videojuegos": {
    "descripcion": "Formación específica para el desarrollo de videojuegos: motores (Unity, Unreal), gráficos, física, IA de juegos y producción. Industria creativa y técnica en crecimiento.",
    "duracion": "4-5 años",
    "campo_laboral": "Estudios de videojuegos, outsourcing para gaming internacional, serious games, VR/AR, estudios indie, docencia.",
},
"arquitectura-ingenieria": {
    "descripcion": "Diseño, proyecto y construcción de edificios y espacios urbanos. Combina arte, técnica constructiva, urbanismo, sustentabilidad y gestión de obra.",
    "duracion": "5-6 años",
    "campo_laboral": "Estudios de arquitectura, dirección de obra, obra pública, desarrollo inmobiliario, urbanismo, docencia, emprendimientos.",
},
"ingenieria-en-automatizacion-y-control": {
    "descripcion": "Diseño de sistemas automáticos de control industrial: PLCs, SCADA, control de procesos. Clave en industria 4.0 y manufactura avanzada.",
    "duracion": "5 años",
    "campo_laboral": "Automatización industrial, manufactura, petroquímica, agro-tech, consultoría de ingeniería, mantenimiento.",
},
"ingenieria-textil": {
    "descripcion": "Diseño y gestión de procesos de la industria textil: fibras, hilados, tejidos, tintorería y confección. Carrera específica con fuerte componente industrial.",
    "duracion": "5 años",
    "campo_laboral": "Industria textil, confección, I+D en materiales textiles, consultoría de calidad, importadoras.",
},

# ============== CIENCIAS ECONÓMICAS Y ADMINISTRACIÓN (20) ==============
"contador-publico": {
    "descripcion": "Formación contable, impositiva, auditoría y de gestión económica. Habilita a firmar balances y actuar como auditor, perito y asesor fiscal.",
    "duracion": "5 años",
    "campo_laboral": "Estudios contables, Big Four, empresas (controller), AFIP, auditoría interna, consultoría tributaria, emprendimientos propios.",
},
"administracion-de-empresas": {
    "descripcion": "Formación integral en gestión organizacional: estrategia, finanzas, marketing, operaciones y recursos humanos. Puente al management y la consultoría.",
    "duracion": "4-5 años",
    "campo_laboral": "Grandes empresas (trainee), consultoría, banca, startups, operaciones, management, emprendimientos propios.",
},
"economia": {
    "descripcion": "Análisis riguroso de los fenómenos económicos: microeconomía, macroeconomía, econometría, finanzas y economía aplicada. Fuerte base matemática.",
    "duracion": "5 años",
    "campo_laboral": "Bancos, consultoría económica, gobierno (BCRA, Hacienda), think tanks, investigación, docencia, finanzas.",
},
"actuaria": {
    "descripcion": "Aplicación de matemática y estadística al cálculo de riesgos: seguros, pensiones, finanzas. Carrera con fuerte base cuantitativa y gran empleabilidad.",
    "duracion": "5 años",
    "campo_laboral": "Compañías de seguros, bancos, AFJP, consultoría actuarial, finanzas cuantitativas, superintendencia.",
    "extra_unis": ["UBA","UCA","UADE","UCEMA"],
},
"comercio-internacional": {
    "descripcion": "Gestión de operaciones de importación y exportación: aduanas, logística internacional, financiamiento del comercio exterior, mercados globales.",
    "duracion": "4 años",
    "campo_laboral": "Empresas exportadoras/importadoras, despachantes de aduana, consultoría en comex, cámaras bilaterales, logística internacional.",
},
"comercializacion-marketing": {
    "descripcion": "Estrategia de marketing, investigación de mercado, branding, marketing digital y comunicación comercial. Puente entre comercial y creativo.",
    "duracion": "4-5 años",
    "campo_laboral": "Empresas de consumo masivo, agencias de marketing, consultoría, e-commerce, product management, retail.",
},
"recursos-humanos": {
    "descripcion": "Gestión del talento en las organizaciones: selección, desarrollo, compensaciones, clima, relaciones laborales. Carrera clave en empresas medianas y grandes.",
    "duracion": "4 años",
    "campo_laboral": "Áreas de RRHH en empresas, consultoría de talento, headhunting, formación corporativa, HR tech.",
},
"finanzas": {
    "descripcion": "Formación específica en finanzas corporativas, mercados de capitales, inversiones y análisis de riesgo. Perfil cuantitativo y estratégico.",
    "duracion": "4-5 años",
    "campo_laboral": "Bancos, mercado de capitales (ByMA), fondos de inversión, consultoría financiera, tesorerías corporativas, fintech.",
},
"logistica-y-transporte": {
    "descripcion": "Gestión de cadenas de suministro: planificación, operaciones, transporte, almacenamiento y distribución. Carrera clave en comercio y manufactura.",
    "duracion": "4 años",
    "campo_laboral": "Operadores logísticos, retail, e-commerce (Mercado Libre), industria, consultoría SCM, exportadoras.",
},
"gestion-de-empresas-agropecuarias": {
    "descripcion": "Formación específica para administrar empresas del sector agro: planificación, finanzas rurales, insumos, comercialización de granos y hacienda.",
    "duracion": "4-5 años",
    "campo_laboral": "Empresas agropecuarias, cooperativas, acopiadoras, agroexportadoras, consultoría agro, bancos (sector agro).",
    "extra_unis": ["UCA","UCEMA","UB","Austral"],
},
"administracion-de-empresas-turisticas": {
    "descripcion": "Gestión específica de negocios turísticos: hoteles, operadores, destinos. Combina administración, marketing y operaciones hoteleras.",
    "duracion": "4 años",
    "campo_laboral": "Cadenas hoteleras, agencias de viajes mayoristas, operadores receptivos, consultoría turística, destinos locales.",
    "extra_unis": ["UP","UCEMA","UCA","UB"],
},
"gestion-de-pymes": {
    "descripcion": "Formación orientada específicamente a la gestión de pequeñas y medianas empresas: finanzas, operaciones y comercialización en contexto de recursos acotados.",
    "duracion": "3-4 años",
    "campo_laboral": "PyMEs familiares, emprendimientos propios, consultoría para PyMEs, cámaras empresariales, instituciones de apoyo (CAME, SEPYME).",
    "extra_unis": ["UP","UTN","UCES","UAI"],
},
"negocios-internacionales": {
    "descripcion": "Formación en gestión de negocios globales: estrategia internacional, marketing global, finanzas internacionales y entorno regulatorio multinacional.",
    "duracion": "4-5 años",
    "campo_laboral": "Multinacionales, consultoría internacional, trading, bancos globales, startups con proyección internacional.",
    "extra_unis": ["UP","UADE","Siglo 21","UCES"],
},
"economia-agraria": {
    "descripcion": "Aplicación de la economía al sector agropecuario: mercados de commodities, políticas rurales, análisis financiero agro. Carrera o especialización.",
    "duracion": "5 años (orientación)",
    "campo_laboral": "Bolsas de cereales, bancos (sector agro), consultoría agro, Ministerio de Agricultura, think tanks, fondos de inversión agropecuarios.",
    "extra_unis": ["UBA","UNR","UNC","UCA"],
},
"administracion-publica": {
    "descripcion": "Formación para la gestión en el sector público: políticas públicas, derecho administrativo, finanzas públicas y planificación estratégica estatal.",
    "duracion": "4 años",
    "campo_laboral": "Administración nacional, provincial y municipal, legislativo, organismos descentralizados, consultoría pública, ONGs.",
},
"gestion-de-organizaciones-sin-fines-de-lucro": {
    "descripcion": "Formación específica para gestionar ONGs, fundaciones y cooperativas: financiamiento, impacto, gobernanza y relaciones con donantes y Estado.",
    "duracion": "3-4 años (muchas veces como posgrado)",
    "campo_laboral": "ONGs, fundaciones, cooperación internacional, consultoría de impacto, RSE corporativa, filantropía.",
    "extra_unis": ["FLACSO","UBA","Siglo 21","UCES"],
},
"tecnicatura-en-gestion-y-administracion": {
    "descripcion": "Formación técnica corta en gestión y administración de organizaciones. Rápida inserción laboral en empresas y organismos.",
    "duracion": "2-3 años",
    "campo_laboral": "Administración de empresas, gestión operativa, PyMEs, administración pública, emprendimientos.",
    "extra_unis": ["UTN","UP","UCES","UAI"],
},
"gastronomia": {
    "descripcion": "Formación profesional en artes culinarias, gestión gastronómica, pastelería y bebidas. Combina técnica, creatividad y gestión de salón.",
    "duracion": "3-4 años",
    "campo_laboral": "Restaurantes, hoteles, catering, consultoría gastronómica, emprendimientos propios, docencia en escuelas.",
},
"negocios-digitales": {
    "descripcion": "Modelos de negocio digitales: e-commerce, marketplaces, SaaS, plataformas, growth y product management. Carrera moderna cruzada entre tecnología y comercial.",
    "duracion": "4 años",
    "campo_laboral": "Startups, e-commerce, product management, growth, consultoría digital, big tech, emprendimientos propios.",
},
"organizacion-de-eventos": {
    "descripcion": "Diseño, planificación y producción de eventos corporativos, culturales y sociales. Perfil con mix de creatividad, logística y comunicación.",
    "duracion": "3-4 años",
    "campo_laboral": "Agencias de eventos, hoteles, convenciones, bodas, lanzamientos de marca, freelance, departamentos corporativos.",
},

# ============== ARTE, DISEÑO Y ARQUITECTURA (25) ==============
"arquitectura-arte": {
    "descripcion": "Diseño del hábitat humano: edificios, espacios interiores y urbanos. Combina arte, técnica constructiva y pensamiento sobre la ciudad.",
    "duracion": "5-6 años",
    "campo_laboral": "Estudios de arquitectura, dirección de obra, desarrollo inmobiliario, urbanismo, interiorismo, docencia.",
},
"diseno-grafico": {
    "descripcion": "Comunicación visual aplicada: identidad visual, tipografía, editorial, packaging, diseño web. Rama central del diseño en Argentina.",
    "duracion": "4-5 años",
    "campo_laboral": "Estudios de diseño, agencias, editoriales, departamentos in-house de marcas, freelance, startups.",
},
"diseno-industrial": {
    "descripcion": "Diseño de productos y objetos industriales: desde el electrodoméstico hasta mobiliario y transporte. Combina ergonomía, materiales y procesos productivos.",
    "duracion": "5 años",
    "campo_laboral": "Industria manufacturera, estudios de diseño, consultoría de productos, I+D industrial, emprendimientos propios.",
},
"diseno-de-indumentaria-y-textil": {
    "descripcion": "Diseño de prendas, colecciones y textiles. Combina proyecto, moldería, materiales y gestión de la cadena de valor fashion.",
    "duracion": "4-5 años",
    "campo_laboral": "Marcas de moda, industria textil, retail, diseño independiente, consultoría, estilismo, docencia.",
},
"diseno-de-interiores": {
    "descripcion": "Diseño integral de espacios interiores: residenciales, comerciales, hoteleros. Formación en proyecto, mobiliario, iluminación y materialidad.",
    "duracion": "3-4 años",
    "campo_laboral": "Estudios de interiorismo, retail (visual merchandising), hotelería, estudios de arquitectura, freelance.",
},
"diseno-de-imagen-y-sonido": {
    "descripcion": "Diseño en lenguajes audiovisuales: cine, TV, publicidad, nuevos medios. Formación amplia en narrativa, imagen, sonido y producción.",
    "duracion": "4-5 años",
    "campo_laboral": "Producción audiovisual, publicidad, cine, series, videoclips, animación, nuevos medios, docencia.",
},
"diseno-uxui": {
    "descripcion": "Diseño de la experiencia e interfaz de productos digitales: investigación de usuarios, prototipado, interacción y accesibilidad.",
    "duracion": "3-4 años",
    "campo_laboral": "Startups, product teams en empresas, agencias digitales, consultoría UX, freelance, big tech.",
},
"artes-visuales": {
    "descripcion": "Formación amplia en pintura, escultura, grabado y nuevos medios. Carrera orientada tanto a la práctica artística como a la enseñanza.",
    "duracion": "4-5 años",
    "campo_laboral": "Arte independiente, galerías, muestras, docencia, gestión cultural, ilustración, residencias artísticas.",
},
"artes-plasticas": {
    "descripcion": "Formación clásica en pintura, escultura, dibujo y grabado. Perfil centrado en la producción artística propia.",
    "duracion": "4-5 años",
    "campo_laboral": "Artista independiente, galerías, residencias, docencia en artes, ilustración, muralismo.",
    "extra_unis": ["UNA","UNLP","UNT","UNC"],
},
"bellas-artes": {
    "descripcion": "Formación integral en bellas artes: pintura, escultura, grabado, dibujo. Carrera de perfil clásico-contemporáneo.",
    "duracion": "4-5 años",
    "campo_laboral": "Artista plástico, docencia, galerías, museos, ilustración, consultoría en patrimonio artístico.",
    "extra_unis": ["UNLP","UNT","UNA","UNC"],
},
"musica": {
    "descripcion": "Formación integral en música: instrumento, teoría, composición e historia. Combina práctica performática y conocimiento musical.",
    "duracion": "5 años",
    "campo_laboral": "Interpretación, orquestas, docencia, producción musical, bandas, docencia en conservatorios, música para medios.",
},
"composicion-musical": {
    "descripcion": "Formación específica en composición: lenguaje musical, orquestación, música contemporánea. Carrera para quienes crean obra propia.",
    "duracion": "5 años",
    "campo_laboral": "Composición para orquestas, ensambles, cine y TV, música de concierto, docencia, producción propia.",
},
"direccion-orquestal": {
    "descripcion": "Formación específica en dirección de orquesta y ensambles. Carrera de alta especialización que combina interpretación, análisis y liderazgo musical.",
    "duracion": "5 años + especialización",
    "campo_laboral": "Dirección de orquestas sinfónicas, dirección coral, dirección en teatros líricos, docencia, dirección en ensambles de cámara.",
    "extra_unis": ["UNA","UCA","UNLP"],
},
"teatro": {
    "descripcion": "Formación integral en artes escénicas: actuación, dirección, dramaturgia, puesta en escena. Combina técnica actoral y pensamiento teatral.",
    "duracion": "4-5 años",
    "campo_laboral": "Teatro independiente y oficial, cine, TV, docencia teatral, dirección, gestión de salas.",
},
"actuacion": {
    "descripcion": "Formación específica en técnica actoral para teatro, cine y TV. Trabajo intensivo sobre cuerpo, voz y construcción de personaje.",
    "duracion": "3-4 años",
    "campo_laboral": "Teatro independiente y oficial, cine, series, publicidad, doblaje, docencia actoral.",
},
"direccion-teatral": {
    "descripcion": "Formación específica en dirección escénica: concepto, puesta, trabajo con actores y producción. Perfil autoral del teatro.",
    "duracion": "4-5 años",
    "campo_laboral": "Dirección de obras teatrales, teatro independiente y oficial, ópera, festivales, docencia.",
    "extra_unis": ["UNA","UBA","UNC"],
},
"danza": {
    "descripcion": "Formación integral en danza contemporánea, clásica o folclórica. Combina técnica corporal, análisis coreográfico y composición propia.",
    "duracion": "4-5 años",
    "campo_laboral": "Compañías de danza oficiales e independientes, teatros, docencia, performance, coreografía.",
    "extra_unis": ["UNA","UNC","UNT"],
},
"coreografia": {
    "descripcion": "Formación específica en creación coreográfica: composición escénica, dramaturgia del cuerpo, dirección de intérpretes.",
    "duracion": "4-5 años",
    "campo_laboral": "Coreografía para compañías, teatro musical, TV, videoclips, ópera, docencia superior.",
    "extra_unis": ["UNA"],
},
"cinematografia-realizacion-audiovisual": {
    "descripcion": "Dirección y realización audiovisual: cine, series y nuevos medios. Formación en narrativa, dirección, producción y lenguaje visual.",
    "duracion": "4-5 años",
    "campo_laboral": "Productoras de cine y TV, publicidad, documentales, plataformas de streaming, dirección independiente, docencia.",
},
"fotografia": {
    "descripcion": "Formación específica en fotografía como lenguaje visual: técnica, narrativa fotográfica, moda, documental, publicidad y edición.",
    "duracion": "3-4 años",
    "campo_laboral": "Fotografía editorial, publicitaria, de moda, bodas y eventos, documental, docencia, freelance.",
},
"animacion-digital": {
    "descripcion": "Formación en animación 2D y 3D: modelado, rigging, animación de personajes y efectos visuales. Industria creativa en crecimiento internacional.",
    "duracion": "4 años",
    "campo_laboral": "Estudios de animación, VFX para cine y publicidad, videojuegos, series animadas, outsourcing internacional.",
},
"produccion-musical": {
    "descripcion": "Formación técnica y artística en producción musical: grabación, mezcla, mastering, sonido en vivo y producción de proyectos propios y de terceros.",
    "duracion": "3-4 años",
    "campo_laboral": "Estudios de grabación, productoras musicales, sonido en vivo, bandas, sellos independientes, producción freelance.",
},
"diseno-de-videojuegos": {
    "descripcion": "Diseño conceptual y creativo de videojuegos: game design, narrativa, mecánicas, nivel y arte. Complementa la ingeniería con la mirada autoral.",
    "duracion": "4 años",
    "campo_laboral": "Estudios de videojuegos locales e internacionales, serious games, estudios indie, docencia, consultoría.",
},
"escritura-creativa": {
    "descripcion": "Formación en narrativa, poesía, guión y edición. Combina talleres prácticos con teoría literaria contemporánea.",
    "duracion": "4 años",
    "campo_laboral": "Escritura literaria propia, editorial, guionismo, periodismo cultural, docencia de escritura, redacción creativa publicitaria.",
},
"artes-del-espectaculo": {
    "descripcion": "Mirada integral de las artes escénicas y audiovisuales: teatro, danza, performance, dirección. Suele incluir orientación en gestión y producción.",
    "duracion": "4-5 años",
    "campo_laboral": "Producción de espectáculos, teatro, danza, festivales, gestión cultural, docencia, dirección artística.",
    "extra_unis": ["UNA","UBA","UNLP"],
},

# ============== CIENCIAS AGROPECUARIAS Y AMBIENTE (20) ==============
"agronomia": {
    "descripcion": "Formación integral para la producción agrícola y agroindustrial: cultivos, suelos, fitopatología, maquinaria, economía rural y manejo sustentable.",
    "duracion": "5 años",
    "campo_laboral": "Empresas agropecuarias, INTA, acopiadoras, insumos agrícolas, consultoría, cooperativas, gobierno rural.",
},
"veterinaria": {
    "descripcion": "Salud animal integral: medicina clínica de pequeños y grandes animales, producción pecuaria, salud pública veterinaria y bienestar animal.",
    "duracion": "5-6 años",
    "campo_laboral": "Clínica de mascotas, producción pecuaria, SENASA, laboratorios veterinarios, zoológicos, docencia, investigación.",
},
"ciencias-ambientales": {
    "descripcion": "Mirada científica e interdisciplinaria sobre los problemas ambientales. Combina ecología, química, planificación territorial y políticas públicas.",
    "duracion": "5 años",
    "campo_laboral": "Consultoría ambiental, APN, organismos de control, ONGs ambientalistas, investigación, educación ambiental.",
},
"ingenieria-forestal": {
    "descripcion": "Manejo sustentable de bosques y plantaciones forestales. Combina silvicultura, ecología, industria forestal y planificación territorial.",
    "duracion": "5 años",
    "campo_laboral": "Empresas forestales y papeleras, Parques Nacionales, INTA, consultoría, gobierno (bosques), ONGs ambientalistas.",
    "extra_unis": ["UNLP","UNNE","UNPSJB","UNLZ"],
},
"licenciatura-en-recursos-naturales": {
    "descripcion": "Manejo y conservación de recursos naturales: suelos, agua, fauna, flora. Perfil técnico-científico para el ordenamiento territorial.",
    "duracion": "5 años",
    "campo_laboral": "APN, consultoría ambiental, estudios de impacto, ONGs, Secretarías de Ambiente, investigación aplicada.",
    "extra_unis": ["UNLZ","UNNE","UNLPAM","UNCO"],
},
"ingenieria-en-produccion-agropecuaria": {
    "descripcion": "Gestión integral de empresas agropecuarias: producción, finanzas rurales, agronegocios. Perfil gerencial del campo.",
    "duracion": "4-5 años",
    "campo_laboral": "Empresas agropecuarias, cooperativas, agroexportadoras, consultoría agrotécnica, bancos (sector agro).",
    "extra_unis": ["UCA","UB","UCEMA","Austral"],
},
"biologia-con-orientacion-ecologia": {
    "descripcion": "Biología con énfasis en ecología: funcionamiento de ecosistemas, biodiversidad, conservación y cambio climático.",
    "duracion": "5 años",
    "campo_laboral": "APN, consultoría ambiental, estudios de impacto, investigación, ONGs ambientalistas, docencia.",
},
"gestion-ambiental": {
    "descripcion": "Formación aplicada en gestión ambiental: evaluación de impacto, sistemas de gestión (ISO 14001), licenciamiento, compliance ambiental.",
    "duracion": "4 años",
    "campo_laboral": "Consultoría ambiental, industria (sustainability), gobiernos locales, ONGs, certificación ambiental, auditoría.",
    "extra_unis": ["UCES","UBA","UNSAM","UB"],
},
"ingenieria-en-irrigacion": {
    "descripcion": "Diseño de sistemas de riego y manejo del agua para la producción agrícola. Crítica en provincias de Cuyo y NOA.",
    "duracion": "5 años",
    "campo_laboral": "Empresas agropecuarias (fruticultura, vitivinicultura), consultoría hídrica, gobiernos provinciales (irrigación), INTA.",
    "extra_unis": ["UNLPAM","UNNE","UNT"],
},
"tecnologia-de-los-alimentos": {
    "descripcion": "Formación técnica aplicada en procesos alimentarios: calidad, seguridad bromatológica, conservación y desarrollo de productos.",
    "duracion": "3-4 años",
    "campo_laboral": "Industria alimentaria, bromatología, control de calidad, I+D de productos, exportación, consultoría.",
    "extra_unis": ["UTN","UBA","UNQ","UNL"],
},
"enologia": {
    "descripcion": "Formación técnica y científica en elaboración de vinos: viticultura, procesos de vinificación, análisis sensorial y gestión de bodega.",
    "duracion": "4-5 años",
    "campo_laboral": "Bodegas, consultoría enológica, INV, exportación de vinos, enoturismo, I+D vitivinícola.",
    "extra_unis": ["UCA","UNNE","UNCO"],
},
"produccion-animal": {
    "descripcion": "Formación específica en producción pecuaria: ganadería bovina, porcina, aviar, lechería. Combina zootecnia, nutrición animal y gestión.",
    "duracion": "4-5 años",
    "campo_laboral": "Empresas pecuarias, cabañas, frigoríficos, lecherías, cooperativas, consultoría, INTA, insumos pecuarios.",
    "extra_unis": ["UNNE","UNLPAM","UCA","UB"],
},
"produccion-vegetal": {
    "descripcion": "Formación específica en producción vegetal intensiva y extensiva: cereales, oleaginosas, frutales, hortalizas y cultivos industriales.",
    "duracion": "4-5 años",
    "campo_laboral": "Empresas agrícolas, cooperativas, insumos (semillas, agroquímicos), INTA, consultoría agronómica, acopios.",
    "extra_unis": ["UNNE","UNLPAM","UCA","UB"],
},
"guardaparques": {
    "descripcion": "Formación específica para la gestión y protección de áreas naturales protegidas. Trabajo de campo intensivo y vocación conservacionista.",
    "duracion": "3-4 años (tecnicatura/licenciatura)",
    "campo_laboral": "Administración de Parques Nacionales, áreas protegidas provinciales, reservas privadas, ONGs conservacionistas.",
},
"paisajismo": {
    "descripcion": "Diseño y gestión del paisaje: jardines, parques, espacio público, paisajes productivos. Puente entre botánica, diseño y planificación territorial.",
    "duracion": "4 años",
    "campo_laboral": "Estudios de paisajismo, gobiernos locales (espacio público), desarrollos inmobiliarios, viveros, consultoría ambiental.",
},
"ciencias-del-suelo-agro": {
    "descripcion": "Carrera o especialización dedicada al estudio del suelo como recurso productivo. Clave para agro, agroforestería y manejo sustentable.",
    "duracion": "5 años (orientación/especialización)",
    "campo_laboral": "INTA, consultoría agronómica, empresas agropecuarias, cooperativas, gobierno (agricultura), I+D agrícola.",
    "extra_unis": ["UBA","UNS","UNLP","UNR"],
},
"acuicultura": {
    "descripcion": "Formación en producción controlada de organismos acuáticos: peces, moluscos, algas. Industria con proyección en Patagonia y litoral.",
    "duracion": "3-4 años",
    "campo_laboral": "Granjas acuícolas, pesquerías, I+D marina, consultoría de producción acuática, INIDEP, ONGs marinas.",
    "extra_unis": ["UNC","UNMDP","UNPSJB"],
},
"licenciatura-en-agroecologia": {
    "descripcion": "Carrera moderna orientada a la producción agrícola sustentable, basada en principios ecológicos y agricultura regenerativa.",
    "duracion": "5 años",
    "campo_laboral": "Producciones agroecológicas, consultoría en sustentabilidad agrícola, INTA (agroecología), ONGs, cooperativas.",
    "extra_unis": ["UNLP","UBA","UNR","UNL"],
},
"sanidad-animal": {
    "descripcion": "Formación específica en prevención y manejo sanitario del ganado y animales de producción. Alternativa a Veterinaria con foco productivo.",
    "duracion": "4 años",
    "campo_laboral": "SENASA, empresas pecuarias, laboratorios veterinarios, cooperativas, frigoríficos, control sanitario.",
    "extra_unis": ["UCA","UNNE","UNLPAM"],
},
"tecnicatura-en-produccion-agricola": {
    "descripcion": "Formación técnica corta y aplicada en producción agrícola. Rápida inserción en empresas y cooperativas del campo.",
    "duracion": "2-3 años",
    "campo_laboral": "Empresas agropecuarias, insumos, cooperativas, acopiadoras, servicios al productor.",
    "extra_unis": ["UNLZ","UNNE","UNLPAM"],
},

# ============== EDUCACIÓN Y CIENCIAS PEDAGÓGICAS (18) ==============
"ciencias-de-la-educacion": {
    "descripcion": "Mirada científica e interdisciplinaria sobre los procesos educativos: pedagogía, psicología educacional, políticas, didáctica y gestión.",
    "duracion": "5 años",
    "campo_laboral": "Gestión educativa, consultoría pedagógica, diseño curricular, docencia superior, investigación educativa, EdTech.",
},
"pedagogia": {
    "descripcion": "Reflexión teórica y práctica sobre la educación: didáctica, filosofía de la educación, políticas educativas. Base de la formación docente.",
    "duracion": "4-5 años",
    "campo_laboral": "Docencia superior, consultoría pedagógica, diseño de materiales, formación docente, investigación educativa.",
},
"licenciatura-en-educacion-inicial": {
    "descripcion": "Formación específica para la educación de niños de 45 días a 5 años. Combina didáctica específica, psicología del desarrollo y gestión de salas.",
    "duracion": "4 años",
    "campo_laboral": "Jardines maternales y de infantes, gestión educativa, formación docente, consultoría pedagógica, EdTech infantil.",
    "extra_unis": ["UBA","UNQ","UNLa","UNLP"],
},
"licenciatura-en-educacion-primaria": {
    "descripcion": "Formación específica para la educación primaria. Combina didácticas de las áreas curriculares con pedagogía y gestión de aula.",
    "duracion": "4 años",
    "campo_laboral": "Escuelas primarias, gestión educativa, formación docente, diseño curricular, EdTech, programas de apoyo escolar.",
    "extra_unis": ["UNQ","UNLa","UNLaM","UNDAV"],
},
"educacion-especial": {
    "descripcion": "Formación para la educación de personas con discapacidad intelectual, motora, sensorial o emocional. Combina didáctica específica y clínica educativa.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas especiales, integración en escuelas comunes, centros terapéuticos educativos, consultoría, obras sociales.",
},
"educacion-fisica": {
    "descripcion": "Formación integral para la enseñanza de la educación física: deporte escolar, entrenamiento, deportes individuales y colectivos, salud y cuerpo.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas, clubes, gimnasios, entrenamiento personal, direcciones deportivas, deporte federado, salud comunitaria.",
},
"profesorado-en-matematica": {
    "descripcion": "Formación en matemática y en didáctica específica para la enseñanza en nivel medio y superior. Combina formación disciplinar y pedagógica.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas secundarias, institutos de formación docente, apoyo escolar, EdTech, diseño curricular.",
},
"profesorado-en-fisica": {
    "descripcion": "Formación en física y en didáctica específica para la enseñanza en nivel medio y superior.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas secundarias, institutos de formación docente, divulgación científica, museos interactivos, EdTech.",
    "extra_unis": ["UBA","UNLP","UNC","UNR"],
},
"profesorado-en-quimica": {
    "descripcion": "Formación en química y en didáctica específica para la enseñanza en nivel medio y superior.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas secundarias, institutos de formación docente, laboratorios de didáctica, divulgación científica.",
    "extra_unis": ["UBA","UNLP","UNC","UNR"],
},
"profesorado-en-biologia": {
    "descripcion": "Formación en biología y en didáctica específica para la enseñanza en nivel medio y superior.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas secundarias, institutos de formación docente, divulgación científica, museos de ciencias.",
    "extra_unis": ["UBA","UNLP","UNC","UNR"],
},
"profesorado-en-historia": {
    "descripcion": "Formación en historia y en didáctica específica para la enseñanza en nivel medio y superior. Fuerte base en historia argentina y latinoamericana.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas secundarias, institutos de formación docente, museos, archivos, divulgación histórica.",
},
"profesorado-en-geografia": {
    "descripcion": "Formación en geografía y en didáctica específica para la enseñanza en nivel medio y superior. Base en geografía humana, física y GIS.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas secundarias, institutos de formación docente, consultoría en cartografía escolar, divulgación.",
    "extra_unis": ["UBA","UNLP","UNC","UNR"],
},
"profesorado-en-letras": {
    "descripcion": "Formación en literatura, lengua y didáctica específica. Clave para la enseñanza de literatura y prácticas del lenguaje en el nivel medio.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas secundarias, institutos de formación docente, apoyo escolar, edición didáctica, EdTech.",
    "extra_unis": ["UBA","UNLP","UNC","UNT"],
},
"profesorado-en-ingles": {
    "descripcion": "Formación lingüística y pedagógica avanzada en inglés. Alta demanda en escuelas, institutos y empresas (English for Business).",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas, institutos de idiomas, formación corporativa, docencia universitaria, traducción, examinadores internacionales.",
    "extra_unis": ["UBA","UNC","UNLP","UNT","UCA"],
},
"profesorado-en-artes": {
    "descripcion": "Formación específica en arte y didáctica del arte para la enseñanza en nivel inicial, primario, medio y superior.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas, institutos de arte, talleres propios, formación docente, centros culturales, EdTech cultural.",
    "extra_unis": ["UNA","UNLP","UNT","UNC"],
},
"profesorado-en-tecnologia": {
    "descripcion": "Formación en tecnología como asignatura escolar: lógica de proyecto, electrónica básica, programación, pensamiento computacional.",
    "duracion": "4-5 años",
    "campo_laboral": "Escuelas (área Tecnología/Educación Digital), formación docente, EdTech, programas de robótica escolar.",
    "extra_unis": ["UTN","UNQ","UNSAM","UNLa"],
},
"gestion-educativa": {
    "descripcion": "Formación para la dirección y gestión de instituciones educativas. Combina liderazgo, administración escolar, legislación y planificación.",
    "duracion": "4-5 años",
    "campo_laboral": "Dirección de escuelas, supervisión escolar, consultoría educativa, EdTech, gobierno educativo, formación docente.",
},
"educacion-y-tic": {
    "descripcion": "Formación en la intersección entre educación y tecnologías digitales: diseño instruccional, EdTech, educación a distancia, data en educación.",
    "duracion": "4 años",
    "campo_laboral": "EdTech, diseño instruccional en empresas y universidades, gobierno (programas digitales), consultoría, docencia universitaria.",
    "extra_unis": ["UNQ","FLACSO","UNICEN","UNL"],
},
}
