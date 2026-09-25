import sys

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Portfolio y CV de Ana Colina Arismendi, Data Analyst / Junior Data Scientist.">
    <!-- Open Graph -->
    <meta property="og:title" content="Ana Colina Arismendi - Data Analyst">
    <meta property="og:description" content="Portfolio y CV de Ana Colina Arismendi, Data Analyst / Junior Data Scientist.">
    <meta property="og:type" content="website">
    <meta property="og:image" content="profile.jpg">
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Ana Colina Arismendi - Data Analyst">
    <meta name="twitter:description" content="Portfolio y CV de Ana Colina Arismendi, Data Analyst / Junior Data Scientist.">
    <meta name="twitter:image" content="profile.jpg">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📊</text></svg>">
    <title>Ana Colina Arismendi - Data Analyst</title>
    <style>
        :root {
            /* Colores principales (Azul corporativo claro) */
            --bg-body: #f0f4f8; /* Azul corporativo muy claro 1 */
            --bg-alt: #e2e8f0;  /* Azul corporativo claro 2 */
            --card-bg: #ffffff; /* Blanco para tarjetas */
            
            /* Bordes: Verde bosque claro */
            --card-border: #b2d8b2; /* Verde bosque claro */
            --timeline-border: #8fbc8f; /* Verde bosque más marcado para la línea */
            
            /* Azules corporativos */
            --navy-dark: #1a365d; /* Azul corporativo oscuro */
            --navy-light: #2c5282; /* Azul corporativo medio */
            --cobalt: #3182ce; 
            --cobalt-hover: #2b6cb0;
            
            /* Verdes para tags */
            --slate-light: #e6f2e6; 
            --slate-text: #2e8b57; 
            
            /* Vino Burdeos (Acento) */
            --btn-accent: #722f37; 
            --btn-accent-hover: #5a252b;
            
            /* Texto */
            --text-main: #2d3748;
            --text-muted: #4a5568;
            
            /* Accesibilidad */
            --focus-ring: #722f37;
        }

        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }

        .mono {
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        }

        body {
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.6;
            scroll-behavior: smooth;
        }

        a:focus-visible, button:focus-visible {
            outline: 3px solid var(--focus-ring);
            outline-offset: 2px;
        }
        
        a:focus, button:focus {
            outline: none;
        }

        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: var(--navy-dark);
            color: white;
            padding: 8px 16px;
            z-index: 2000;
            transition: top 0.2s;
            text-decoration: none;
            font-weight: bold;
        }
        .skip-link:focus-visible {
            top: 0;
            outline: 3px solid var(--btn-accent);
        }

        /* --- Navbar --- */
        nav {
            background-color: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(8px);
            position: sticky;
            top: 0;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 5%;
            border-bottom: 1px solid var(--card-border);
        }

        .menu-toggle {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--navy-dark);
            cursor: pointer;
        }

        .nav-links {
            display: flex;
            gap: 1.5rem;
        }
        
        .nav-links a {
            color: var(--navy-light);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: var(--btn-accent);
        }

        @media (max-width: 899px) {
            .menu-toggle {
                display: block;
            }
            .nav-links {
                display: none;
                flex-direction: column;
                position: absolute;
                top: 100%;
                left: 0;
                width: 100%;
                background-color: rgba(255, 255, 255, 0.98);
                padding: 1rem 5%;
                border-bottom: 1px solid var(--card-border);
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            }
            .nav-links.open {
                display: flex;
            }
        }

        .lang-selector {
            display: flex;
            gap: 0.25rem;
        }

        .lang-btn {
            background: none;
            border: 1px solid transparent;
            padding: 4px 8px;
            cursor: pointer;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--navy-light);
            transition: all 0.2s;
        }

        .lang-btn:hover {
            background-color: var(--bg-alt);
        }

        .lang-btn.active {
            background-color: var(--slate-light);
            color: var(--slate-text);
            border-color: var(--slate-text);
        }

        /* --- Hero Header --- */
        header {
            background: linear-gradient(135deg, var(--navy-dark), var(--navy-light));
            color: white;
            padding: 5rem 5%;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .avatar {
            width: 140px;
            height: 140px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid var(--bg-body);
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
            margin-bottom: 1.5rem;
        }

        header h1 {
            font-size: clamp(2rem, 5vw, 3.5rem);
            margin-bottom: 0.5rem;
            font-weight: 800;
            letter-spacing: -1px;
        }

        header p.hero-subtitle {
            font-size: clamp(1.1rem, 2.5vw, 1.4rem);
            font-weight: 400;
            color: var(--bg-alt);
            margin-bottom: 1.5rem;
            max-width: 700px;
        }

        .pills {
            display: flex;
            gap: 0.8rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 2rem;
        }

        .pill {
            background-color: rgba(255,255,255,0.15);
            backdrop-filter: blur(4px);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid rgba(255,255,255,0.2);
            letter-spacing: 0.5px;
        }

        .actions {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
        }

        .btn {
            padding: 10px 24px;
            border-radius: 8px;
            font-weight: 700;
            text-decoration: none;
            transition: transform 0.2s, box-shadow 0.2s;
            display: inline-block;
            cursor: pointer;
            border: none;
            font-size: 0.95rem;
        }

        .btn-accent {
            background-color: var(--btn-accent);
            color: #ffffff !important;
        }
        
        .btn-accent:hover {
            background-color: var(--btn-accent-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(114, 47, 55, 0.4);
        }

        .btn-secondary {
            background-color: transparent;
            color: white;
            border: 2px solid white;
        }

        .btn-secondary:hover {
            background-color: white;
            color: var(--navy-dark);
            transform: translateY(-2px);
        }

        /* --- Panel Métricas --- */
        .metrics-container {
            max-width: 1000px;
            margin: -3rem auto 2rem;
            padding: 0 5%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
            position: relative;
            z-index: 10;
        }

        .metric-card {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05);
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .metric-icon {
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--btn-accent);
        }

        .metric-text {
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--navy-dark);
            line-height: 1.4;
        }

        /* --- Main Content --- */
        main {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem 5%;
        }

        section {
            margin-bottom: 4rem;
        }

        .section-title {
            font-size: 1.8rem;
            color: var(--navy-dark);
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .section-title::after {
            content: '';
            height: 2px;
            flex-grow: 1;
            background-color: var(--card-border);
        }

        /* --- Perfil --- */
        .profile-card {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 2.5rem;
            border-radius: 16px;
            font-size: 1.05rem;
            color: var(--text-muted);
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        }

        /* --- Timeline (Exp & Edu) --- */
        .timeline {
            border-left: 3px solid var(--timeline-border);
            padding-left: 2rem;
            margin-left: 1rem;
        }

        .timeline-item {
            position: relative;
            margin-bottom: 3rem;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: -2.65rem;
            top: 0;
            width: 20px;
            height: 20px;
            background-color: var(--card-bg);
            border: 4px solid var(--btn-accent);
            border-radius: 50%;
        }

        .timeline-date {
            font-weight: 700;
            color: var(--btn-accent);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.3rem;
        }

        .timeline-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--navy-dark);
            margin-bottom: 0.2rem;
        }

        .timeline-subtitle {
            font-weight: 600;
            color: var(--text-muted);
            margin-bottom: 1rem;
            font-size: 1rem;
        }

        .timeline-content {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        }

        .timeline-content ul {
            margin-left: 1.2rem;
            color: var(--text-muted);
        }

        .timeline-content li {
            margin-bottom: 0.5rem;
        }

        /* --- Habilidades en Clusters --- */
        .skills-container {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
        }

        @media (min-width: 768px) {
            .skills-container {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        .skill-cluster {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        }

        .skill-cluster-title {
            font-size: 1.1rem;
            color: var(--navy-dark);
            margin-bottom: 1.2rem;
            font-weight: 700;
            border-bottom: 2px solid var(--bg-alt);
            padding-bottom: 0.5rem;
        }

        .skill-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
        }

        .skill-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-weight: 500;
            color: var(--text-muted);
        }

        .skill-item::before {
            content: '✓';
            color: var(--btn-accent);
            font-weight: bold;
        }

        /* --- Proyectos --- */
        .projects-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }

        @media (min-width: 768px) {
            .projects-grid {
                grid-template-columns: 1fr 1fr;
            }
        }

        .project-card {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 1.5rem;
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
        }

        .project-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.06);
            border-color: var(--btn-accent);
        }

        .project-title {
            font-size: 1.2rem;
            color: var(--navy-dark);
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .project-desc {
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
            flex-grow: 1;
        }

        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 1rem;
        }

        .tech-tag {
            background-color: var(--slate-light);
            color: var(--slate-text);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 700;
        }

        .project-link {
            color: var(--navy-light);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            padding: 6px 12px;
            background-color: var(--bg-body);
            border-radius: 6px;
            border: 1px solid var(--card-border);
            transition: all 0.2s;
        }
        
        .project-link:hover {
            background-color: var(--bg-alt);
            border-color: var(--btn-accent);
            color: var(--btn-accent);
        }

        /* --- Idiomas --- */
        .lang-cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }
        
        .lang-card {
            background-color: var(--card-bg);
            border: 1px solid var(--card-border);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
        }

        .lang-name {
            font-weight: 700;
            color: var(--navy-dark);
            font-size: 1.1rem;
            margin-bottom: 0.3rem;
        }

        .lang-level {
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        /* --- Footer & Contact --- */
        footer {
            background-color: var(--navy-dark);
            color: white;
            padding: 4rem 5% 2rem;
            text-align: center;
        }

        .contact-links {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-bottom: 3rem;
        }

        .contact-btn {
            background-color: rgba(255,255,255,0.1);
            color: white;
            padding: 12px 24px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: background-color 0.2s;
        }

        .contact-btn:hover {
            background-color: var(--btn-accent);
        }

        .copyright {
            color: rgba(255,255,255,0.6);
            font-size: 0.9rem;
            border-top: 1px solid rgba(255,255,255,0.1);
            padding-top: 2rem;
        }
    </style>
</head>
<body>
    <a href="#main-content" class="skip-link" data-i18n="skip_link">Saltar al contenido</a>

    <!-- Navegación -->
    <nav>
        <div class="logo" style="font-weight: 800; color: var(--navy-dark); letter-spacing: -0.5px;">A. Colina</div>
        
        <button class="menu-toggle" aria-expanded="false" aria-label="Abrir menú" onclick="toggleMenu()">☰</button>
        
        <div class="nav-links" id="nav-links">
            <a href="#profile" data-i18n="nav_profile" onclick="closeMenu()">Perfil</a>
            <a href="#experience" data-i18n="nav_exp" onclick="closeMenu()">Experiencia</a>
            <a href="#education" data-i18n="nav_edu" onclick="closeMenu()">Educación</a>
            <a href="#skills" data-i18n="nav_skills" onclick="closeMenu()">Habilidades</a>
            <a href="#projects" data-i18n="nav_projects" onclick="closeMenu()">Proyectos</a>
        </div>
        <div class="lang-selector">
            <button class="lang-btn active" aria-pressed="true" aria-label="Español" onclick="setLang('es', this)" id="btn-es">ES</button>
            <button class="lang-btn" aria-pressed="false" aria-label="English" onclick="setLang('en', this)" id="btn-en">EN</button>
            <button class="lang-btn" aria-pressed="false" aria-label="Deutsch" onclick="setLang('de', this)" id="btn-de">DE</button>
            <button class="lang-btn" aria-pressed="false" aria-label="Français" onclick="setLang('fr', this)" id="btn-fr">FR</button>
            <button class="lang-btn" aria-pressed="false" aria-label="Italiano" onclick="setLang('it', this)" id="btn-it">IT</button>
        </div>
    </nav>

    <!-- Cabecera Hero -->
    <header>
        <img src="profile.jpg" alt="Ana Colina Arismendi" class="avatar">
        <h1>Ana Colina Arismendi</h1>
        <p class="hero-subtitle" data-i18n="hero_title">Data Analyst / Junior Data Scientist</p>
        
        <div class="pills mono">
            <span class="pill">Python</span>
            <span class="pill">SQL</span>
            <span class="pill" data-i18n="pill_ml">Machine Learning</span>
            <span class="pill" data-i18n="pill_pharma">Farmacovigilancia</span>
        </div>

        <div class="actions">
            <a href="CV_AColina_ES.pdf" id="cv-link" target="_blank" class="btn btn-accent" data-i18n="btn_cv">Descargar CV (PDF)</a>
            <a href="#contact" class="btn btn-secondary" data-i18n="btn_contact">Contactar</a>
        </div>
    </header>

    <!-- Métricas / Data Highlights -->
    <div class="metrics-container">
        <div class="metric-card">
            <div class="metric-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            </div>
            <div class="metric-text" data-i18n="metric_1">Conocimiento del negocio (KAM) y datos regulatorios</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
            </div>
            <div class="metric-text" data-i18n="metric_2">Python & SQL para modelado, ETL y análisis predictivo</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8" y2="16"></line><line x1="16" y1="16" x2="16" y2="16"></line></svg>
            </div>
            <div class="metric-text" data-i18n="metric_3">Formación continua en IA y Machine Learning</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            </div>
            <div class="metric-text" data-i18n="metric_4">Español nativo · Inglés profesional · Alemán en formación</div>
        </div>
    </div>

    <main id="main-content">
        <!-- Perfil -->
        <section id="profile">
            <h2 class="section-title" data-i18n="section_profile">Perfil Profesional</h2>
            <div class="profile-card">
                <p data-i18n="profile_desc">
                    Data Analyst, especializada en Python y SQL para el análisis y modelado de datos. Actualmente cursando el grado de Ciencia de Datos Aplicada (UOC) y Bootcamp en Data & IA para profundizar en Machine Learning e Inteligencia Artificial. La trayectoria previa en el sector farmacéutico —centrada en gestión de cuentas clave, farmacovigilancia y CRM— aporta una sólida visión de negocio y rigor analítico en el manejo de datos regulatorios complejos y fuertes habilidades interpersonales. Orientada a transformar la información en soluciones estratégicas.
                </p>
            </div>
        </section>

        <!-- Experiencia -->
        <section id="experience">
            <h2 class="section-title" data-i18n="section_exp">Experiencia Laboral</h2>
            <div class="timeline">
                
                <!-- Puesto Actual -->
                <div class="timeline-item">
                    <div class="timeline-date" data-i18n="exp_date_new">[COMPLETAR: Fecha inicio — Presente]</div>
                    <div class="timeline-title" data-i18n="exp_title_new">Data Analyst / Proyectos Data Science</div>
                    <div class="timeline-subtitle" data-i18n="exp_subtitle_new">[COMPLETAR: Empresa o Freelance]</div>
                    <div class="timeline-content">
                        <ul>
                            <li data-i18n="exp_bullet1_new"><strong>[COMPLETAR: Acción]:</strong> empleando [COMPLETAR: Herramienta/Tecnología] logrando [COMPLETAR: Resultado/Cifra].</li>
                            <li data-i18n="exp_bullet2_new"><strong>[COMPLETAR: Acción]:</strong> empleando [COMPLETAR: Herramienta/Tecnología] logrando [COMPLETAR: Resultado/Cifra].</li>
                        </ul>
                    </div>
                </div>

                <!-- Puesto Anterior -->
                <div class="timeline-item">
                    <div class="timeline-date" data-i18n="exp_date">Ene 2015 — Oct 2017</div>
                    <div class="timeline-title" data-i18n="exp_title">Representante Comercial (KAM)</div>
                    <div class="timeline-subtitle">Laboratorios Pellier</div>
                    <div class="timeline-content">
                        <ul>
                            <li data-i18n="exp_bullet1"><strong>Gestión de Cuentas Clave:</strong> Lideré la planificación estratégica y prospección utilizando [COMPLETAR: Herramienta CRM/Software], incrementando la cartera en un [COMPLETAR: %/Cifra].</li>
                            <li data-i18n="exp_bullet2"><strong>Farmacovigilancia:</strong> Analicé y reporté datos de seguridad de medicamentos biológicos mediante [COMPLETAR: Herramienta/BBDD], asegurando un 100% de cumplimiento regulatorio.</li>
                            <li data-i18n="exp_bullet4"><strong>Optimización CRM:</strong> Integré y analicé datos transaccionales con [COMPLETAR: Herramienta, ej. Excel/SQL/CRM], mitigando riesgos comerciales en [COMPLETAR: Cifra] cuentas clave.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Habilidades (Clusters) -->
        <section id="skills">
            <h2 class="section-title" data-i18n="section_skills">Habilidades por Dominio</h2>
            <div class="skills-container">
                <!-- Cluster 1 -->
                <div class="skill-cluster">
                    <div class="skill-cluster-title" data-i18n="skill_group1">Ciencia de Datos & Análisis</div>
                    <ul class="skill-list">
                        <li class="skill-item">Python & SQL</li>
                        <li class="skill-item">Machine Learning</li>
                        <li class="skill-item">Pandas & NumPy</li>
                        <li class="skill-item">Streamlit</li>
                        <li class="skill-item" data-i18n="skill_api">Consumo de APIs</li>
                    </ul>
                </div>
                <!-- Cluster 2 -->
                <div class="skill-cluster">
                    <div class="skill-cluster-title" data-i18n="skill_group3">Estrategia & KAM</div>
                    <ul class="skill-list">
                        <li class="skill-item">Key Account Management</li>
                        <li class="skill-item" data-i18n="skill_crm">Sistemas CRM</li>
                        <li class="skill-item" data-i18n="skill_plan">Visión de Negocio</li>
                        <li class="skill-item" data-i18n="skill_risk">Gestión de Riesgos</li>
                    </ul>
                </div>
                <!-- Cluster 3 -->
                <div class="skill-cluster">
                    <div class="skill-cluster-title" data-i18n="skill_group2">Sector Farmacéutico</div>
                    <ul class="skill-list">
                        <li class="skill-item" data-i18n="skill_pharma">Farmacovigilancia</li>
                        <li class="skill-item" data-i18n="skill_bio">Fármacos Biológicos</li>
                        <li class="skill-item" data-i18n="skill_safety">Datos Regulatorios</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- Proyectos Data Science -->
        <section id="projects">
            <h2 class="section-title" data-i18n="section_projects">Proyectos Data Science</h2>
            <div class="projects-grid">
                
                <div class="project-card">
                    <div class="project-title" data-i18n="proj1_title">Predicción de Riesgo Cardiovascular</div>
                    <div class="project-tech mono">
                        <span class="tech-tag">Python</span>
                        <span class="tech-tag">Scikit-learn</span>
                        <span class="tech-tag">Streamlit</span>
                    </div>
                    <div class="project-desc" data-i18n="proj1_desc">
                        Modelo de Machine Learning interactivo implementado con Scikit-learn y Streamlit para la predicción de riesgos a partir de métricas de salud estandarizadas.
                    </div>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: auto;">
                        <a href="[COMPLETAR: URL del repo]" target="_blank" class="project-link">🔗 <span data-i18n="proj_link">Ver repositorio</span></a>
                        <a href="[COMPLETAR: URL de demo]" target="_blank" class="project-link">🌐 <span data-i18n="proj_demo">Ver demo</span></a>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-title" data-i18n="proj2_title">Consumo y Análisis de APIs con Python</div>
                    <div class="project-tech mono">
                        <span class="tech-tag">ETL</span>
                        <span class="tech-tag">Pandas</span>
                        <span class="tech-tag">GeoJSON</span>
                    </div>
                    <div class="project-desc" data-i18n="proj2_desc">
                        Pipeline ETL extrayendo datos de terremotos globales de USGS mediante APIs REST, procesamiento de datos estructurados con Pandas y mapeo GeoJSON.
                    </div>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: auto;">
                        <a href="[COMPLETAR: URL del repo]" target="_blank" class="project-link">🔗 <span data-i18n="proj_link">Ver repositorio</span></a>
                        <a href="[COMPLETAR: URL de demo]" target="_blank" class="project-link">🌐 <span data-i18n="proj_demo">Ver demo</span></a>
                    </div>
                </div>

            </div>
        </section>

        <!-- Educación -->
        <section id="education">
            <h2 class="section-title" data-i18n="section_edu">Educación y Formación</h2>
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-date" data-i18n="edu1_date">[COMPLETAR: Año] — En curso</div>
                    <div class="timeline-title" data-i18n="edu1_title">Ciencia de Datos Aplicada</div>
                    <div class="timeline-subtitle">Universitat Oberta de Catalunya (UOC)</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date" data-i18n="edu2_date">Mar 2017 — Nov 2017</div>
                    <div class="timeline-title" data-i18n="edu2_title">Gestión Comercial y Marketing Farmacéutico</div>
                    <div class="timeline-subtitle">Universidad Católica del Uruguay (UCU)</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date" data-i18n="edu3_date">2012 — 2017</div>
                    <div class="timeline-title" data-i18n="edu3_title">Estudios de Medicina en formación</div>
                    <div class="timeline-subtitle">Universidad de la República (UdelaR)</div>
                </div>
            </div>
        </section>
        
        <!-- Idiomas -->
        <section id="languages">
            <h2 class="section-title" data-i18n="section_lang">Idiomas</h2>
            <div class="lang-cards">
                <div class="lang-card">
                    <div class="lang-name" data-i18n="lang_es">Español</div>
                    <div class="lang-level" data-i18n="lang_es_lvl">Nativo</div>
                </div>
                <div class="lang-card">
                    <div class="lang-name" data-i18n="lang_en">Inglés</div>
                    <div class="lang-level" data-i18n="lang_en_lvl">Fluido / Profesional</div>
                </div>
                <div class="lang-card">
                    <div class="lang-name" data-i18n="lang_de">Alemán</div>
                    <div class="lang-level" data-i18n="lang_de_lvl">Básico (A1-A2) en formación</div>
                </div>
            </div>
        </section>
    </main>

    <footer id="contact">
        <h2 style="margin-bottom: 2rem;" data-i18n="footer_contact">Contacto y Enlaces</h2>
        <div class="contact-links">
            <a href="mailto:acolinaarismendi@gmail.com" class="contact-btn">
                ✉️ acolinaarismendi@gmail.com
            </a>
            <a href="https://www.linkedin.com/in/ana-colina-arismendi-24a27715a/" target="_blank" class="contact-btn">
                💼 LinkedIn
            </a>
            <a href="https://github.com/anacolinaarismendi" target="_blank" class="contact-btn">
                💻 GitHub
            </a>
            <div class="contact-btn" style="cursor: default;">
                📍 Frankfurt am Main, Germany
            </div>
        </div>
        <div class="copyright">
            © <span id="current-year"></span> Ana Colina Arismendi. <span data-i18n="footer_copy">Todos los derechos reservados.</span>
        </div>
    </footer>

    <!-- Script de Traducciones Dinámicas y Funcionalidad -->
    <script>
        document.getElementById('current-year').textContent = new Date().getFullYear();

        function toggleMenu() {
            const nav = document.getElementById('nav-links');
            const btn = document.querySelector('.menu-toggle');
            nav.classList.toggle('open');
            const isOpen = nav.classList.contains('open');
            btn.setAttribute('aria-expanded', isOpen);
        }
        
        function closeMenu() {
            const nav = document.getElementById('nav-links');
            const btn = document.querySelector('.menu-toggle');
            if(nav.classList.contains('open')) {
                nav.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
            }
        }

        const dict = {
            es: {
                doc_title: "Ana Colina Arismendi - Data Analyst",
                skip_link: "Saltar al contenido",
                nav_profile: "Perfil", nav_exp: "Experiencia", nav_edu: "Educación", nav_skills: "Habilidades", nav_projects: "Proyectos",
                hero_title: "Data Analyst / Junior Data Scientist",
                pill_ml: "Machine Learning", pill_pharma: "Farmacovigilancia",
                btn_cv: "Descargar CV (PDF)", btn_contact: "Contactar",
                metric_1: "Conocimiento del negocio (KAM) y datos regulatorios", 
                metric_2: "Python & SQL para modelado, ETL y análisis", 
                metric_3: "Formación continua en IA y Machine Learning", 
                metric_4: "Español nativo · Inglés profesional · Alemán en formación",
                section_profile: "Perfil Profesional",
                profile_desc: "Data Analyst, especializada en Python y SQL para el análisis y modelado de datos. Actualmente cursando el grado de Ciencia de Datos Aplicada (UOC) y Bootcamp en Data & IA para profundizar en Machine Learning e Inteligencia Artificial. La trayectoria previa en el sector farmacéutico —centrada en gestión de cuentas clave, farmacovigilancia y CRM— aporta una sólida visión de negocio y rigor analítico en el manejo de datos regulatorios complejos y fuertes habilidades interpersonales. Orientada a transformar la información en soluciones estratégicas.",
                section_exp: "Experiencia Laboral",
                exp_date_new: "[COMPLETAR: Fecha inicio — Presente]",
                exp_title_new: "Data Analyst / Proyectos Data Science",
                exp_subtitle_new: "[COMPLETAR: Empresa o Freelance]",
                exp_bullet1_new: "<strong>[COMPLETAR: Acción]:</strong> empleando [COMPLETAR: Herramienta/Tecnología] logrando [COMPLETAR: Resultado/Cifra].",
                exp_bullet2_new: "<strong>[COMPLETAR: Acción]:</strong> empleando [COMPLETAR: Herramienta/Tecnología] logrando [COMPLETAR: Resultado/Cifra].",
                exp_date: "Ene 2015 — Oct 2017", exp_title: "Representante Comercial (KAM)",
                exp_bullet1: "<strong>Gestión de Cuentas Clave:</strong> Lideré la planificación estratégica y prospección utilizando [COMPLETAR: Herramienta CRM/Software], incrementando la cartera en un [COMPLETAR: %/Cifra].",
                exp_bullet2: "<strong>Farmacovigilancia:</strong> Analicé y reporté datos de seguridad de medicamentos biológicos mediante [COMPLETAR: Herramienta/BBDD], asegurando un 100% de cumplimiento regulatorio.",
                exp_bullet4: "<strong>Optimización CRM:</strong> Integré y analicé datos transaccionales con [COMPLETAR: Herramienta, ej. Excel/SQL/CRM], mitigando riesgos comerciales en [COMPLETAR: Cifra] cuentas clave.",
                section_skills: "Habilidades por Dominio",
                skill_group1: "Ciencia de Datos & Análisis", skill_api: "Consumo de APIs",
                skill_group2: "Sector Farmacéutico", skill_pharma: "Farmacovigilancia", skill_bio: "Fármacos Biológicos", skill_safety: "Datos Regulatorios",
                skill_group3: "Estrategia & KAM", skill_crm: "Sistemas CRM", skill_plan: "Visión de Negocio", skill_risk: "Gestión de Riesgos",
                section_projects: "Proyectos Data Science",
                proj1_title: "Predicción de Riesgo Cardiovascular", proj1_desc: "Modelo de Machine Learning interactivo implementado con Scikit-learn y Streamlit para la predicción de riesgos a partir de métricas de salud estandarizadas.",
                proj2_title: "Consumo y Análisis de APIs con Python", proj2_desc: "Pipeline ETL extrayendo datos de terremotos globales de USGS mediante APIs REST, procesamiento de datos estructurados con Pandas y mapeo GeoJSON.",
                proj_link: "Ver repositorio", proj_demo: "Ver demo",
                section_edu: "Educación y Formación",
                edu1_date: "[COMPLETAR: Año] — En curso", edu1_title: "Ciencia de Datos Aplicada",
                edu2_date: "Mar 2017 — Nov 2017", edu2_title: "Gestión Comercial y Marketing Farmacéutico",
                edu3_date: "2012 — 2017", edu3_title: "Estudios de Medicina en formación", 
                section_lang: "Idiomas", lang_es: "Español", lang_es_lvl: "Nativo", lang_en: "Inglés", lang_en_lvl: "Fluido / Profesional", lang_de: "Alemán", lang_de_lvl: "Básico (A1-A2) en formación",
                footer_contact: "Contacto y Enlaces", footer_copy: "Todos los derechos reservados."
            },
            en: {
                doc_title: "Ana Colina Arismendi - Data Analyst",
                skip_link: "Skip to content",
                nav_profile: "Profile", nav_exp: "Experience", nav_edu: "Education", nav_skills: "Skills", nav_projects: "Projects",
                hero_title: "Data Analyst / Junior Data Scientist",
                pill_ml: "Machine Learning", pill_pharma: "Pharmacovigilance",
                btn_cv: "Download CV (PDF)", btn_contact: "Contact",
                metric_1: "Business acumen (KAM) and regulatory data", 
                metric_2: "Python & SQL for modeling, ETL and analysis", 
                metric_3: "Continuous training in AI and Machine Learning", 
                metric_4: "Native Spanish · Professional English · German in training",
                section_profile: "Professional Profile",
                profile_desc: "Data Analyst specializing in Python and SQL for data analysis and modeling. Currently pursuing a bachelor's degree in Applied Data Science (UOC) and a Data & AI Bootcamp to deepen knowledge in Machine Learning and Artificial Intelligence. Previous experience in the pharmaceutical sector—focused on key account management, pharmacovigilance, and CRM—provides strong business acumen, analytical rigor in handling complex regulatory data, and strong interpersonal skills. Driven to transform information into strategic solutions.",
                section_exp: "Work Experience",
                exp_date_new: "[COMPLETAR: Start Date — Present]",
                exp_title_new: "Data Analyst / Data Science Projects",
                exp_subtitle_new: "[COMPLETAR: Company or Freelance]",
                exp_bullet1_new: "<strong>[COMPLETAR: Action]:</strong> using [COMPLETAR: Tool/Tech] achieving [COMPLETAR: Result/Figure].",
                exp_bullet2_new: "<strong>[COMPLETAR: Action]:</strong> using [COMPLETAR: Tool/Tech] achieving [COMPLETAR: Result/Figure].",
                exp_date: "Jan 2015 — Oct 2017", exp_title: "Commercial Representative (KAM)",
                exp_bullet1: "<strong>Key Account Management:</strong> Led strategic planning and prospecting using [COMPLETAR: CRM Tool], increasing portfolio by [COMPLETAR: %/Figure].",
                exp_bullet2: "<strong>Pharmacovigilance:</strong> Analyzed and reported safety data for biological drugs using [COMPLETAR: Tool/DB], ensuring 100% regulatory compliance.",
                exp_bullet4: "<strong>CRM Optimisation:</strong> Integrated and analyzed transactional data with [COMPLETAR: Tool], mitigating commercial risks across [COMPLETAR: Figure] key accounts.",
                section_skills: "Domain Skills",
                skill_group1: "Data Science & Analysis", skill_api: "API Consumption",
                skill_group2: "Pharmaceutical Sector", skill_pharma: "Pharmacovigilance", skill_bio: "Biological Drugs", skill_safety: "Regulatory Data",
                skill_group3: "Strategy & KAM", skill_crm: "CRM Systems", skill_plan: "Business Acumen", skill_risk: "Risk Management",
                section_projects: "Data Science Projects",
                proj1_title: "Cardiovascular Risk Prediction", proj1_desc: "Interactive Machine Learning model implemented with Scikit-learn and Streamlit for risk prediction based on standardized health metrics.",
                proj2_title: "API Consumption & Analysis with Python", proj2_desc: "ETL pipeline extracting global earthquake data from USGS via REST APIs, structured data processing with Pandas and GeoJSON mapping.",
                proj_link: "View repository", proj_demo: "View demo",
                section_edu: "Education & Background",
                edu1_date: "[COMPLETAR: Year] — In progress", edu1_title: "Applied Data Science",
                edu2_date: "Mar 2017 — Nov 2017", edu2_title: "Commercial Management & Pharma Marketing",
                edu3_date: "2012 — 2017", edu3_title: "Medical Studies (In progress / Coursework)", 
                section_lang: "Languages", lang_es: "Spanish", lang_es_lvl: "Native", lang_en: "English", lang_en_lvl: "Fluent / Professional", lang_de: "German", lang_de_lvl: "Basic (A1-A2) in training",
                footer_contact: "Contact & Links", footer_copy: "All rights reserved."
            },
            de: {
                doc_title: "Ana Colina Arismendi - Data Analyst",
                skip_link: "Zum Hauptinhalt springen",
                nav_profile: "Profil", nav_exp: "Erfahrung", nav_edu: "Bildung", nav_skills: "Fähigkeiten", nav_projects: "Projekte",
                hero_title: "Data Analyst / Junior Data Scientist",
                pill_ml: "Machine Learning", pill_pharma: "Pharmakovigilanz",
                btn_cv: "Lebenslauf (PDF) laden", btn_contact: "Kontakt",
                metric_1: "Geschäftsverständnis (KAM) & regulatorische Daten", 
                metric_2: "Python & SQL für Modellierung, ETL und Analyse", 
                metric_3: "Kontinuierliche Weiterbildung in KI und ML", 
                metric_4: "Spanisch (Muttersprache) · Englisch (Fließend) · Deutsch (in Ausbildung)",
                section_profile: "Berufsprofil",
                profile_desc: "Data Analystin, spezialisiert auf Python und SQL für Datenanalyse und Modellierung. Derzeit im Bachelorstudiengang Applied Data Science (UOC) und einem Data & AI Bootcamp zur Vertiefung der Kenntnisse in Machine Learning und Künstlicher Intelligenz. Die bisherige Erfahrung im Pharmasektor – mit Fokus auf Key Account Management, Pharmakovigilanz und CRM – bietet ein starkes Geschäftsverständnis, analytische Strenge im Umgang mit komplexen regulatorischen Daten und ausgeprägte zwischenmenschliche Fähigkeiten. Darauf ausgerichtet, Informationen in strategische Lösungen zu transformieren.",
                section_exp: "Berufserfahrung",
                exp_date_new: "[COMPLETAR: Startdatum — Heute]",
                exp_title_new: "Data Analyst / Data Science Projekte",
                exp_subtitle_new: "[COMPLETAR: Unternehmen oder Freelance]",
                exp_bullet1_new: "<strong>[COMPLETAR: Aktion]:</strong> Verwendung von [COMPLETAR: Tool/Tech], um [COMPLETAR: Ergebnis/Zahl] zu erreichen.",
                exp_bullet2_new: "<strong>[COMPLETAR: Aktion]:</strong> Verwendung von [COMPLETAR: Tool/Tech], um [COMPLETAR: Ergebnis/Zahl] zu erreichen.",
                exp_date: "Jan 2015 — Okt 2017", exp_title: "Handelsvertreterin (KAM)",
                exp_bullet1: "<strong>Key Account Management:</strong> Strategische Planung und Akquise mit [COMPLETAR: CRM-Tool], Steigerung des Portfolios um [COMPLETAR: %/Zahl].",
                exp_bullet2: "<strong>Pharmakovigilanz:</strong> Analyse und Meldung von Sicherheitsdaten für biologische Arzneimittel mittels [COMPLETAR: Tool/DB] (100% regulatorische Compliance).",
                exp_bullet4: "<strong>CRM-Optimierung:</strong> Integration und Analyse von Transaktionsdaten mit [COMPLETAR: Tool] zur Minderung kommerzieller Risiken bei [COMPLETAR: Zahl] Schlüsselkunden.",
                section_skills: "Fähigkeiten",
                skill_group1: "Data Science & Analyse", skill_api: "API-Nutzung",
                skill_group2: "Pharmasektor", skill_pharma: "Pharmakovigilanz", skill_bio: "Biologische Arzneimittel", skill_safety: "Regulatorische Daten",
                skill_group3: "Strategie & KAM", skill_crm: "CRM-Systeme", skill_plan: "Geschäftsverständnis", skill_risk: "Risikomanagement",
                section_projects: "Data Science Projekte",
                proj1_title: "Vorhersage des kardiovaskulären Risikos", proj1_desc: "Interaktives Machine Learning Modell, implementiert mit Scikit-learn und Streamlit zur Risikovorhersage basierend auf standardisierten Gesundheitsmetriken.",
                proj2_title: "API-Nutzung und Analyse mit Python", proj2_desc: "ETL-Pipeline, die globale Erdbebendaten vom USGS über REST-APIs extrahiert und mit Pandas im GeoJSON-Format verarbeitet.",
                proj_link: "Repo ansehen", proj_demo: "Demo ansehen",
                section_edu: "Ausbildung",
                edu1_date: "[COMPLETAR: Jahr] — In Bearbeitung", edu1_title: "Applied Data Science",
                edu2_date: "Mär 2017 — Nov 2017", edu2_title: "Handelsmanagement und Pharma-Marketing",
                edu3_date: "2012 — 2017", edu3_title: "Medizinstudium (in Ausbildung)", 
                section_lang: "Sprachen", lang_es: "Spanisch", lang_es_lvl: "Muttersprache", lang_en: "Englisch", lang_en_lvl: "Fließend / Professionell", lang_de: "Deutsch", lang_de_lvl: "Grundkenntnisse (A1-A2)",
                footer_contact: "Kontakt & Links", footer_copy: "Alle Rechte vorbehalten."
            },
            fr: {
                doc_title: "Ana Colina Arismendi - Data Analyst",
                skip_link: "Aller au contenu principal",
                nav_profile: "Profil", nav_exp: "Expérience", nav_edu: "Éducation", nav_skills: "Compétences", nav_projects: "Projets",
                hero_title: "Data Analyst / Junior Data Scientist",
                pill_ml: "Machine Learning", pill_pharma: "Pharmacovigilance",
                btn_cv: "Télécharger le CV", btn_contact: "Contacter",
                metric_1: "Vision métier (KAM) et données réglementaires", 
                metric_2: "Python & SQL pour modélisation, ETL et analyse", 
                metric_3: "Formation continue en IA et Machine Learning", 
                metric_4: "Espagnol natif · Anglais professionnel · Allemand en formation",
                section_profile: "Profil Professionnel",
                profile_desc: "Data Analyst, spécialisée en Python et SQL pour l'analyse et la modélisation de données. Actuellement dans la licence de Data Science Appliquée (UOC) et un Bootcamp en Data & IA pour approfondir les connaissances en Machine Learning et Intelligence Artificielle. L'expérience préalable dans le secteur pharmaceutique — axée sur la gestion des comptes clés, la pharmacovigilance et le CRM — apporte une solide vision métier, une rigueur analytique dans le traitement de données réglementaires complexes et de fortes compétences interpersonnelles. Axée sur la transformation de l'information en solutions stratégiques.",
                section_exp: "Expérience Professionnelle",
                exp_date_new: "[COMPLETAR: Date de début — Présent]",
                exp_title_new: "Data Analyst / Projets Data Science",
                exp_subtitle_new: "[COMPLETAR: Entreprise ou Freelance]",
                exp_bullet1_new: "<strong>[COMPLETAR: Action] :</strong> utilisant [COMPLETAR: Outil/Tech] pour atteindre [COMPLETAR: Résultat/Chiffre].",
                exp_bullet2_new: "<strong>[COMPLETAR: Action] :</strong> utilisant [COMPLETAR: Outil/Tech] pour atteindre [COMPLETAR: Résultat/Chiffre].",
                exp_date: "Jan 2015 — Oct 2017", exp_title: "Représentante Commerciale (KAM)",
                exp_bullet1: "<strong>Gestion des Comptes Clés :</strong> Direction de la planification stratégique avec [COMPLETAR: Outil CRM], augmentant le portefeuille de [COMPLETAR: %/Chiffre].",
                exp_bullet2: "<strong>Pharmacovigilance :</strong> Analyse et signalement des données de sécurité des médicaments biologiques via [COMPLETAR: Outil/BD] (100% conformité).",
                exp_bullet4: "<strong>Optimisation CRM :</strong> Intégration et analyse des données transactionnelles avec [COMPLETAR: Outil] pour atténuer les risques de [COMPLETAR: Chiffre] comptes clés.",
                section_skills: "Compétences par Domaine",
                skill_group1: "Data Science & Analyse", skill_api: "Consommation d'APIs",
                skill_group2: "Secteur Pharmaceutique", skill_pharma: "Pharmacovigilance", skill_bio: "Médicaments Biologiques", skill_safety: "Données Réglementaires",
                skill_group3: "Stratégie & KAM", skill_crm: "Systèmes CRM", skill_plan: "Vision Métier", skill_risk: "Gestion des Risques",
                section_projects: "Projets Data Science",
                proj1_title: "Prédiction du Risque Cardiovasculaire", proj1_desc: "Modèle de Machine Learning interactif implémenté avec Scikit-learn et Streamlit pour la prédiction des risques.",
                proj2_title: "Analyse et Consommation d'API avec Python", proj2_desc: "Pipeline ETL extrayant des données sismiques mondiales de l'USGS via des API REST, traitement avec Pandas et GeoJSON.",
                proj_link: "Voir le dépôt", proj_demo: "Voir la démo",
                section_edu: "Éducation et Formation",
                edu1_date: "[COMPLETAR: Année] — En cours", edu1_title: "Applied Data Science",
                edu2_date: "Mar 2017 — Nov 2017", edu2_title: "Gestion Commerciale et Marketing Pharmaceutique",
                edu3_date: "2012 — 2017", edu3_title: "Études de médecine (en formation)", 
                section_lang: "Langues", lang_es: "Espagnol", lang_es_lvl: "Maternel", lang_en: "Anglais", lang_en_lvl: "Courant / Professionnel", lang_de: "Allemand", lang_de_lvl: "Basique (A1-A2)",
                footer_contact: "Contact & Liens", footer_copy: "Tous droits réservés."
            },
            it: {
                doc_title: "Ana Colina Arismendi - Data Analyst",
                skip_link: "Vai al contenuto principale",
                nav_profile: "Profilo", nav_exp: "Esperienza", nav_edu: "Formazione", nav_skills: "Competenze", nav_projects: "Progetti",
                hero_title: "Data Analyst / Junior Data Scientist",
                pill_ml: "Machine Learning", pill_pharma: "Farmacovigilanza",
                btn_cv: "Scarica CV (PDF)", btn_contact: "Contatto",
                metric_1: "Visione aziendale (KAM) e dati normativi", 
                metric_2: "Python & SQL per modellazione, ETL e analisi", 
                metric_3: "Formazione continua in IA e Machine Learning", 
                metric_4: "Spagnolo madrelingua · Inglese professionale · Tedesco in formazione",
                section_profile: "Profilo Professionale",
                profile_desc: "Data Analyst, specializzata in Python e SQL per l'analisi e la modellazione dei dati. Attualmente iscritta al corso di laurea in Data Science Applicata (UOC) e a un Bootcamp in Data & AI per approfondire le conoscenze in Machine Learning e Intelligenza Artificiale. L'esperienza pregressa nel settore farmaceutico — focalizzata sulla gestione dei clienti chiave, farmacovigilanza e CRM — fornisce una solida visione aziendale, rigore analitico nella gestione di complessi dati normativi e spiccate capacità interpersonali. Orientata a trasformare le informazioni in soluzioni strategiche.",
                section_exp: "Esperienza Lavorativa",
                exp_date_new: "[COMPLETAR: Data di inizio — Presente]",
                exp_title_new: "Data Analyst / Progetti Data Science",
                exp_subtitle_new: "[COMPLETAR: Azienda o Freelance]",
                exp_bullet1_new: "<strong>[COMPLETAR: Azione]:</strong> utilizzando [COMPLETAR: Strumento/Tech] per ottenere [COMPLETAR: Risultato/Cifra].",
                exp_bullet2_new: "<strong>[COMPLETAR: Azione]:</strong> utilizzando [COMPLETAR: Strumento/Tech] per ottenere [COMPLETAR: Risultato/Cifra].",
                exp_date: "Gen 2015 — Ott 2017", exp_title: "Rappresentante Commerciale (KAM)",
                exp_bullet1: "<strong>Key Account Management:</strong> Gestione della pianificazione strategica con [COMPLETAR: Strumento CRM], incrementando il portafoglio del [COMPLETAR: %/Cifra].",
                exp_bullet2: "<strong>Farmacovigilanza:</strong> Analisi e reportistica dei dati di sicurezza dei farmaci biologici tramite [COMPLETAR: Strumento/DB] (100% compliance).",
                exp_bullet4: "<strong>Ottimizzazione CRM:</strong> Integrazione e analisi dei dati transazionali con [COMPLETAR: Strumento] per mitigare i rischi di [COMPLETAR: Cifra] clienti chiave.",
                section_skills: "Competenze",
                skill_group1: "Data Science & Analisi", skill_api: "Consumo di API",
                skill_group2: "Settore Farmaceutico", skill_pharma: "Farmacovigilanza", skill_bio: "Farmaci Biologici", skill_safety: "Dati Normativi",
                skill_group3: "Strategia & KAM", skill_crm: "Sistemi CRM", skill_plan: "Visione Aziendale", skill_risk: "Gestione del Rischio",
                section_projects: "Progetti Data Science",
                proj1_title: "Previsione del Rischio Cardiovascolare", proj1_desc: "Modello di Machine Learning interattivo implementato con Scikit-learn e Streamlit per la previsione del rischio.",
                proj2_title: "Consumo di API e Analisi con Python", proj2_desc: "Pipeline ETL che estrae dati sismici globali dall'USGS tramite API REST, elaborazione con Pandas e mappatura GeoJSON.",
                proj_link: "Vedi repository", proj_demo: "Vedi demo",
                section_edu: "Formazione",
                edu1_date: "[COMPLETAR: Anno] — In corso", edu1_title: "Applied Data Science",
                edu2_date: "Mar 2017 — Nov 2017", edu2_title: "Gestione Commerciale e Marketing Farmaceutico",
                edu3_date: "2012 — 2017", edu3_title: "Studi di Medicina (in formazione)", 
                section_lang: "Lingue", lang_es: "Spagnolo", lang_es_lvl: "Madrelingua", lang_en: "Inglese", lang_en_lvl: "Fluente / Professionale", lang_de: "Tedesco", lang_de_lvl: "Base (A1-A2)",
                footer_contact: "Contatti e Link", footer_copy: "Tutti i diritti riservati."
            }
        };

        function setLang(lang, btnElement) {
            document.querySelectorAll('.lang-btn').forEach(btn => {
                btn.classList.remove('active');
                btn.setAttribute('aria-pressed', 'false');
            });
            
            const activeBtn = btnElement || document.getElementById('btn-' + lang);
            activeBtn.classList.add('active');
            activeBtn.setAttribute('aria-pressed', 'true');

            const translation = dict[lang];
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translation[key]) {
                    el.innerHTML = translation[key];
                }
            });

            document.documentElement.lang = lang;
            
            // Actualizar PDF enlace según idioma
            document.getElementById('cv-link').setAttribute('href', `CV_AColina_${lang.toUpperCase()}.pdf`);
            
            // Actualizar título del documento
            if(translation['doc_title']) {
                document.title = translation['doc_title'];
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            setLang('es', document.getElementById('btn-es'));
        });
    </script>
</body>
</html>
"""

with open('/Users/anaisabecolinaarismendi/Documents/GitHub/Ana Colina Ariemdni/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
