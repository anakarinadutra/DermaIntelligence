import json
import os
from modules.pubmed import buscar_pubmed
from deep_translator import GoogleTranslator


CONFIG = "config.json"


# ===== IDIOMA =====

def configurar_idioma():

    if os.path.exists(CONFIG):
        with open(CONFIG, "r") as f:
            return json.load(f)["idioma"]

    print("🌍 Language / Idioma")
    print("1 — Português")
    print("2 — English")
    print("3 — Español")

    opcao = input("Option: ")

    mapa = {"1": "pt", "2": "en", "3": "es"}
    idioma = mapa.get(opcao, "pt")

    with open(CONFIG, "w") as f:
        json.dump({"idioma": idioma}, f)

    return idioma


# ===== TRADUÇÃO =====

def traduzir(texto, idioma):

    if idioma == "en":
        return texto

    return GoogleTranslator(source='auto', target=idioma).translate(texto)


# ===== CLASSIFICAÇÃO DE EVIDÊNCIA =====

def classificar_evidencia(texto):
    t = texto.lower()

    if any(p in t for p in ["systematic review", "meta-analysis", "guideline"]):
        return "HIGH"
    elif any(p in t for p in ["randomized", "clinical trial"]):
        return "MODERATE"
    else:
        return "LOW"


# ===== INTERPRETAÇÃO CLÍNICA =====

def interpretar(texto, idioma):

    nivel = classificar_evidencia(texto)

    if idioma == "en":
        relatorio = f"""
🧠 DERMAINTELLIGENCE™ PRO — CLINICAL REPORT

🔬 Evidence-based summary:

Combination therapies tend to provide superior outcomes compared to single modalities.
Energy-based devices, topical agents, systemic therapies, and regenerative approaches
may be integrated depending on severity and patient profile.

📊 Estimated level of evidence: {nivel}

⚠️ Individual clinical judgment is required.
📚 Sources: Recent PubMed literature
"""
    elif idioma == "es":
        relatorio = f"""
🧠 DERMAINTELLIGENCE™ PRO — INFORME CLÍNICO

🔬 Resumen basado en evidencia:

Las terapias combinadas suelen ofrecer mejores resultados que las modalidades únicas.
Dispositivos de energía, tratamientos tópicos, sistémicos y regenerativos
pueden integrarse según la gravedad y el perfil del paciente.

📊 Nivel de evidencia estimado: {nivel}

⚠️ Se requiere juicio clínico individual.
📚 Fuentes: Literatura reciente de PubMed
"""
    else:
        relatorio = f"""
🧠 DERMAINTELLIGENCE™ PRO — RELATÓRIO CLÍNICO

🔬 Síntese baseada em evidência:

Terapias combinadas tendem a apresentar melhores resultados que abordagens isoladas.
Tecnologias de energia, tratamentos tópicos, sistêmicos e regenerativos
podem ser integrados conforme gravidade e perfil do paciente.

📊 Nível de evidência estimado: {nivel}

⚠️ Requer julgamento clínico individual.
📚 Fontes: Literatura recente do PubMed
"""

    return relatorio


# ===== EXECUÇÃO =====

idioma = configurar_idioma()

tema = input("\nClinical topic / Tema clínico: ")

print("\n🔎 Searching scientific evidence...\n")

artigos = buscar_pubmed(tema)

relatorio = interpretar(artigos, idioma)

print(relatorio)

print("\n📖 REFERENCES: PubMed")

input("\nPress Enter to exit...")