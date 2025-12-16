import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV Swann Accajou", page_icon="📊", layout="wide")

# --- STYLE CSS ---
st.markdown("""
    <style>
    /* Réduction de l'espace global dans la sidebar */
    [data-testid="stSidebarUserContent"] {
        padding-top: 20px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1E3A8A;
        color: white !important;
    }
    .company-header { font-size: 24px; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .job-title { font-size: 19px; font-weight: bold; color: #374151; margin-top: 0px; }
    .date-text { color: #6B7280; font-style: italic; font-weight: 600; }
    
    /* Style pour des lignes de séparation plus fines */
    hr {
        margin-top: 5px;
        margin-bottom: 10px;
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
    st.write("- Esprit Responsable & Solidaire")

    # --- SECTION : REMERCIEMENTS (Espace réduit) ---
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
    * **Master Data Management (MDM) :** Pilotage de la stratégie de gestion des données de référence.
    * **Data Gouvernance :** Définition des standards de qualité et des politiques de sécurité des données.
    * **Coordination :** Liaison entre les équipes IT et les métiers.
    """)
    st.divider()

    # FINLIVE
    st.markdown('<p class="company-header">FINLIVE</p>', unsafe_allow_html=True)
    st.markdown('<p class="job-title">Traitement de Produits Structurés Financiers</p>', unsafe_allow_html=True)
    st.markdown('<p class="date-text">Juin - Août 2025 | Paris</p>', unsafe_allow_html=True)
    st.markdown("""
    * **Web Scraping :** Extraction automatisée de données financières.
    * **NoSQL :** Intégration et structuration de données sur MongoDB.
    """)
    st.divider()

    # QUALISTAT
    st.markdown('<p class="company-header">QUALISTAT</p>', unsafe_allow_html=True)
    st.markdown('<p class="job-title">Développeur Data & Full-Stack</p>', unsafe_allow_html=True)
    st.markdown('<p class="date-text">Mai - Juillet 2024 | Guadeloupe</p>', unsafe_allow_html=True)
    st.write("* **SQL & PHP :** Création d'une plateforme de gestion de données pour le relogement social.")

# --- ONGLET 2 : FORMATION ---
with tab_form:
    st.header("Cursus Académique")
    st.subheader("EFREI Paris")
    st.markdown('<p class="date-text">2023 - Présent</p>', unsafe_allow_html=True)
    st.write("**Ingénierie Informatique, Data & Marketing**")
    
    st.subheader("Asia Pacific University (APU)")
    st.markdown('<p class="date-text">2025 | Malaisie</p>', unsafe_allow_html=True)
    st.write("**Échange : AI & Business Intelligence**")

    st.subheader("Polytechnique Montréal")
    st.markdown('<p class="date-text">2018 - 2022 | Canada</p>', unsafe_allow_html=True)
    st.write("**Ingénierie Mécanique**")

# --- ONGLET 3 : LANGUES & INTÉRÊTS ---
with tab_comp:
    col1, col2 = st.columns(2)
    with col1:
        st.header("🌍 Langues")
        st.write("🇬🇧 **Anglais :** C1")
        st.write("🇪🇸 **Espagnol :** B2")
    
    with col2:
        st.header("⚽ Centres d'intérêt")
        st.write("- **Golf :** Pratique et enseignement.")
        st.write("- **Investissement :** Gestion active (PEA, Crypto, NFT).")

st.write("---")
st.caption("Application Portfolio - Swann Accajou")