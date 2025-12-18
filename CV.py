import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV Swann Accajou", page_icon="📊", layout="wide")

# --- STYLE CSS ADAPTATIF ---
st.markdown("""
    <style>
    /* Réduction de l'espace global dans la sidebar */
    [data-testid="stSidebarUserContent"] {
        padding-top: 20px;
    }
    
    /* Onglets adaptatifs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
        font-weight: bold;
        /* Utilisation d'une couleur de fond neutre qui s'adapte */
        background-color: rgba(151, 166, 195, 0.15); 
    }
    .stTabs [aria-selected="true"] {
        background-color: #1E3A8A; /* Bleu professionnel */
        color: white !important;
    }

    /* En-têtes d'entreprises - Utilisation d'un bleu plus clair pour le mode sombre */
    .company-header { 
        font-size: 24px; 
        font-weight: bold; 
        color: #3b82f6; /* Bleu plus vif (plus lisible en dark mode) */
        margin-bottom: 5px; 
    }
    
    /* Titres de postes - Couleur héritée du thème pour la lisibilité */
    .job-title { 
        font-size: 19px; 
        font-weight: bold; 
        margin-top: 0px; 
    }
    
    /* Texte de date - Utilisation d'un gris moyen universel */
    .date-text { 
        color: #9ca3af; 
        font-style: italic; 
        font-weight: 600; 
    }
    
    /* Séparateurs */
    hr {
        margin-top: 5px;
        margin-bottom: 10px;
        opacity: 0.3;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Swann Accajou")
    st.write("📍 Paris, France")
    st.write("📧 swann.accajou@gmail.com")
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Expertise Technique
    st.subheader("🛠 Expertise Technique")
    st.write("**Langages:** Python, SQL, PHP")
    st.write("**Data:** Pandas, NumPy, Scikit-learn")
    st.write("**Outils:** Power BI, MongoDB, Excel")
    st.write("**Domaines:** MDM, Data Gouvernance")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.subheader("Soft Skills")
    st.write("- Polyvalence & Autonomie")
    st.write("- Esprit Responsable & Solidair")

    # --- SECTION : REMERCIEMENTS ---
    st.markdown("<br>", unsafe_allow_html=True) 
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("🙏 Remerciements")
    st.write("Merci au **Dr Mano Joseph MATHEW** pour son expertise.")
    st.markdown("[🔗 Profil LinkedIn](https://www.linkedin.com/in/manomathew/)")

# --- TITRE PRINCIPAL ---
st.title("Swann Accajou")
st.subheader("Chargé de Projet MDM & Data Gouvernance | EFREI Paris")

# --- NAVIGATION PAR ONGLETS ---
tab_exp, tab_form, tab_comp = st.tabs(["💼 Expériences", "🎓 Formation", "🌍 Langues & Intérêts"])

# --- ONGLET 1 : EXPÉRIENCES ---
with tab_exp:
    st.header("Parcours Professionnel")

    # AGL
    st.markdown('<p class="company-header">AGL</p>', unsafe_allow_html=True)
    st.markdown('<p class="job-title">Chargé de Projet MDM et Data Gouvernance (Alternance)</p>', unsafe_allow_html=True)
    st.markdown('<p class="date-text">Novembre 2024 - Présent | Paris</p>', unsafe_allow_html=True)
    st.markdown("""
    * **Master Data Management (MDM) :** Pilotage opérationnel de la gestion des données de référence pour assurer une source de vérité unique et fiable au sein de l'organisation.
    * **Data Gouvernance :** Élaboration et mise en œuvre de cadres normatifs garantissant la qualité, la sécurité et la conformité des actifs data.
    * **Coordination transverse :** Animation des ateliers entre les directions IT et métiers pour aligner les architectures de données sur les besoins business.
    * *Cette alternance me permet de développer une vision stratégique du cycle de vie de la donnée en milieu industriel.*
    """)
    st.divider()

    # FINLIVE
    st.markdown('<p class="company-header">FINLIVE</p>', unsafe_allow_html=True)
    st.markdown('<p class="job-title">Traitement de Produits Structurés Financiers</p>', unsafe_allow_html=True)
    st.markdown('<p class="date-text">Juin - Août 2025 | Paris</p>', unsafe_allow_html=True)
    st.markdown("""
    * **Automatisation Data :** Conception de scripts Python pour le scraping et le parsing automatique de données complexes extraites de term-sheets financiers.
    * **Ingénierie de données :** Structuration et injection massive de flux de données hétérogènes vers une architecture MongoDB (NoSQL).
    * **Outil d'aide à la décision :** Développement d'une interface facilitant l'accès aux données pour optimiser l'analyse de risques des conseillers.
    * *Une mission axée sur la transformation de documents non structurés en bases de données exploitables.*
    """)
    st.divider()

    # QUALISTAT
    st.markdown('<p class="company-header">QUALISTAT</p>', unsafe_allow_html=True)
    st.markdown('<p class="job-title">Développeur Data & Full-Stack</p>', unsafe_allow_html=True)
    st.markdown('<p class="date-text">Mai - Juillet 2024 | Guadeloupe</p>', unsafe_allow_html=True)
    st.markdown("""
    * **Développement Application Web :** Création d'une plateforme de gestion et d'une base de données SQL dédiée au suivi du relogement social.
    * **Architecture SQL :** Modélisation de schémas de données pour traiter les informations liées à l'habitat insalubre et prioriser les interventions.
    * **Expérience Utilisateur (UX) :** Optimisation de l'interface en PHP pour faciliter la saisie terrain par les agents administratifs.
    * *Un projet à fort impact social utilisant la donnée pour améliorer les conditions de vie.*
    """)
    st.divider()

    # GSPOT
    st.markdown('<p class="company-header">GSPOT</p>', unsafe_allow_html=True)
    st.markdown('<p class="job-title">Responsable de Site et Professeur de Golf</p>', unsafe_allow_html=True)
    st.markdown('<p class="date-text">Juin - Juillet 2023</p>', unsafe_allow_html=True)
    st.markdown("""
    * **Stratégie Marketing :** Définition et exécution du plan de lancement pour l'ouverture du site, incluant la communication digitale.
    * **Paramétrage analytique :** Installation technique des simulateurs Trackman pour fournir des données précises sur les performances sportives.
    * **Gestion opérationnelle :** Management autonome de la relation client et de la logistique du site au quotidien.
    """)

# --- ONGLET 2 : FORMATION ---
with tab_form:
    st.header("Cursus Académique")
    
    st.subheader("EFREI Paris")
    st.markdown('<p class="date-text">2023 - Présent | Villejuif</p>', unsafe_allow_html=True)
    st.write("**Ingénierie Informatique, Data & Marketing**")
    st.markdown("""
    * Spécialisation hybride alliant ingénierie logicielle, data marketing et statistiques avancées.
    * Apprentissage approfondi de la visualisation de données (Power BI) et de la veille numérique stratégique.
    """)
    
    st.subheader("Asia Pacific University (APU)")
    st.markdown('<p class="date-text">2025 | Kuala Lumpur, Malaisie</p>', unsafe_allow_html=True)
    st.write("**Échange Universitaire : Digital Business & AI**")
    st.markdown("""
    * Immersion dans les écosystèmes business numériques et l'intelligence artificielle appliquée à la résolution de problèmes.
    * Pratique du Design Thinking pour la conception de solutions technologiques centrées sur l'utilisateur.
    """)

    st.subheader("Polytechnique Montréal")
    st.markdown('<p class="date-text">2018 - 2022 | Canada</p>', unsafe_allow_html=True)
    st.write("**Ingénierie Mécanique**")
    st.markdown("""
    * Cycle préparatoire intégré et cursus ingénieur axés sur les mathématiques appliquées et la physique.
    * Développement d'une forte rigueur d'analyse et d'une capacité à modéliser des systèmes complexes.
    """)

# --- ONGLET 3 : LANGUES & INTÉRÊTS ---
with tab_comp:
    col1, col2 = st.columns(2)
    with col1:
        st.header("🌍 Langues & Communication")
        st.write("🇬🇧 **Anglais :** Niveau C1 (Maîtrise professionnelle complète, usage quotidien possible).")
        st.write("🇪🇸 **Espagnol :** Niveau B2 (Bonne capacité de communication et de rédaction).")
        
    with col2:
        st.header("⚽ Centres d'intérêt & Engagement")
        st.write("- **Golf :** Compétition et enseignement (Transmet la discipline et la précision).")
        st.write("- **Investissement :** Gestion de portefeuille (PEA, Crypto) - Analyse des marchés financiers.")
        st.write("- **Esprit d'équipe :** Pratique régulière du basketball renforçant la solidarité et le leadership.")

st.write("---")
st.caption("CV Interactif généré par Swann Accajou - 2025")