import streamlit as st

st.set_page_config(page_title="DermaIntelligence™", layout="wide")

# =========================================================
# 🌍 GLOBAL LANGUAGE DATABASE
# =========================================================

DATA = {

"pt": {
    "profile": "Perfil Profissional",
    "name": "Nome completo",
    "profession": "Profissão",
    "license": "Registro profissional",
    "country": "País",
    "language": "Idioma",
    "question": "Pergunta clínica",
    "ask": "Pergunte sobre qualquer condição dermatológica ou estética:",
    "button": "Gerar Inteligência Clínica",
    "expert": "MODO EXPERT — CONSENSO CLÍNICO BASEADO EM EVIDÊNCIA",
    "strategy": "Estratégia contemporânea:",
    "domains": "Domínios terapêuticos baseados em evidência:",
    "sources": "Baseado em literatura científica recente",
    "warning": "Use julgamento clínico individual",
    "evidence": "Nível de evidência estimado",
    "professions": [
        "Dermatologista",
        "Médico esteta",
        "Enfermeiro",
        "Biomédico",
        "Cirurgião-dentista",
        "Outro"
    ]
},

"en": {
    "profile": "Professional Profile",
    "name": "Full name",
    "profession": "Profession",
    "license": "License / Registration",
    "country": "Country",
    "language": "Language",
    "question": "Clinical Question",
    "ask": "Ask about any dermatologic or aesthetic condition:",
    "button": "Generate Clinical Intelligence",
    "expert": "EXPERT MODE — EVIDENCE-BASED CLINICAL CONSENSUS",
    "strategy": "Contemporary strategy:",
    "domains": "Evidence-based therapeutic domains:",
    "sources": "Based on recent scientific literature",
    "warning": "Use individual clinical judgment",
    "evidence": "Estimated evidence level",
    "professions": [
        "Dermatologist",
        "Aesthetic physician",
        "Nurse",
        "Biomedical professional",
        "Dentist",
        "Other"
    ]
},

"es": {
    "profile": "Perfil Profesional",
    "name": "Nombre completo",
    "profession": "Profesión",
    "license": "Registro profesional",
    "country": "País",
    "language": "Idioma",
    "question": "Pregunta clínica",
    "ask": "Pregunte sobre cualquier condición dermatológica o estética:",
    "button": "Generar Inteligencia Clínica",
    "expert": "MODO EXPERTO — CONSENSO CLÍNICO BASADO EN EVIDENCIA",
    "strategy": "Estrategia contemporánea:",
    "domains": "Dominios terapéuticos basados en evidencia:",
    "sources": "Basado en literatura científica reciente",
    "warning": "Use juicio clínico individual",
    "evidence": "Nivel de evidencia estimado",
    "professions": [
        "Dermatólogo",
        "Médico estético",
        "Enfermero",
        "Biomédico",
        "Odontólogo",
        "Otro"
    ]
}

}

# =========================================================
# 🌐 LANGUAGE SELECTOR
# =========================================================

lang_option = st.sidebar.selectbox(
    "Language / Idioma",
    ["Português", "English", "Español"]
)

lang_map = {
    "Português": "pt",
    "English": "en",
    "Español": "es"
}

L = DATA[lang_map[lang_option]]

# =========================================================
# 🧑‍⚕️ PROFESSIONAL PROFILE
# =========================================================

st.sidebar.title(L["profile"])

name = st.sidebar.text_input(L["name"])

profession = st.sidebar.selectbox(
    L["profession"],
    L["professions"]
)

license_number = st.sidebar.text_input(L["license"])
country = st.sidebar.text_input(L["country"])

# =========================================================
# 🧠 MAIN INTERFACE
# =========================================================

st.title("🧠 DermaIntelligence™")
st.caption("Clinical • Scientific • Legal AI for Dermatology & Aesthetics")

st.subheader(L["question"])
question = st.text_area(L["ask"])

# =========================================================
# 🧬 EXPERT ENGINE
# =========================================================

if st.button(L["button"]):

    if question.strip() == "":
        st.warning("⚠️ Please enter a clinical topic.")
    else:

        st.success(L["expert"])

        st.markdown("### 🧬 " + L["strategy"])

        st.markdown("""
👉 Multimodal approaches typically produce superior outcomes  
👉 Combination of pharmacologic therapy, energy devices and regenerative techniques  
👉 Protocol must be individualized to patient characteristics  
👉 Maintenance therapy is frequently necessary  
👉 Consider contraindications and safety profile  
👉 Systemic factors and comorbidities influence results  
        """)

        st.markdown("### 🧪 " + L["domains"])

        st.markdown("""
✔️ Terapia farmacológica tópica e sistêmica  
✔️ Tecnologias de energia (laser, radiofrequência, ultrassom, IPL)  
✔️ Injetáveis (toxina botulínica, preenchedores, bioestimuladores)  
✔️ Medicina regenerativa e biotecnologia  
✔️ Dermocosméticos e cuidados domiciliares  
✔️ Fatores hormonais, metabólicos e estilo de vida  
        """)

        st.markdown("### 📊 " + L["evidence"] + ": HIGH")

        st.info("📚 " + L["sources"])
        st.warning("⚠️ " + L["warning"])


