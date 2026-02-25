import streamlit as st
from openai import OpenAI

# 🔐 SUA CHAVE OPENAI DEVE ESTAR EM secrets.toml
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="DermaIntelligence™", layout="wide")

# =========================
# 🌍 SELEÇÃO DE IDIOMA
# =========================
idioma = st.selectbox(
    "Language / Idioma / Idioma",
    ["Português", "English", "Español"]
)

# =========================
# 👩‍⚕️ PERFIL PROFISSIONAL
# =========================
perfil = st.selectbox(
    "Perfil Profissional",
    [
        "Dermatologista",
        "Médico",
        "Enfermeiro",
        "Biomédico",
        "Dentista",
        "Esteticista",
        "Outro profissional de saúde"
    ]
)

# =========================
# 🧠 SYSTEM PROMPT GLOBAL
# =========================
SYSTEM_PROMPT = f"""
You are DermaIntelligence™, a global clinical intelligence system specialized in dermatology, skin health, and aesthetic medicine.

USER PROFILE: {perfil}
LANGUAGE SELECTED: {idioma}

MISSION:
Provide high-level, evidence-based clinical decision support for healthcare and aesthetic professionals worldwide.

LANGUAGE RULE:
Respond ONLY in {idioma}. Never mix languages.

TONE:
Professional, technical, precise.

DIVERSITY PRIORITY:
Give special attention to Fitzpatrick IV–VI skin types, mixed populations, and tropical dermatology.

STRUCTURE EVERY RESPONSE:

1. Clinical Assessment
2. Differential Diagnosis
3. Evidence-Based Management
4. Complementary Evaluation
5. Risks and Red Flags
6. Prognosis
7. Scientific Evidence Summary
8. References (academic standard preferred)

If information is insufficient, ask targeted clinical questions.

End every response with:
“Would you like to explore alternative treatments, combined protocols, prevention strategies, or another case?”
"""

st.title("🧠 DermaIntelligence™")
st.markdown("Global Clinical Intelligence for Dermatology & Aesthetic Medicine")

pergunta_usuario = st.text_area("Digite sua pergunta clínica:")

if st.button("Analisar Caso Clínico"):

    if pergunta_usuario.strip() == "":
        st.warning("Digite uma pergunta clínica.")
    else:
        with st.spinner("Analisando..."):

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": pergunta_usuario}
            ]

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.3
            )

            resposta = response.choices[0].message.content

        st.markdown("### 📋 Resposta Clínica")
        st.markdown(resposta)

st.markdown("---")
st.caption("DermaIntelligence™ provides decision support and does not replace clinical judgment.")           
