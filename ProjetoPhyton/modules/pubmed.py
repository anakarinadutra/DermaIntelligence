from Bio import Entrez

Entrez.email = "anakarinadutra@outlook.com"


def buscar_pubmed(termo):
    # 1️⃣ Buscar artigos
    handle = Entrez.esearch(
        db="pubmed",
        term=termo,
        retmax=5,
        sort="relevance"
    )
    record = Entrez.read(handle)
    ids = record["IdList"]

    if not ids:
        return "Nenhum artigo encontrado."

    # 2️⃣ Buscar detalhes (resumos)
    handle = Entrez.efetch(
        db="pubmed",
        id=",".join(ids),
        rettype="abstract",
        retmode="text"
    )

    textos = handle.read()

    # 3️⃣ Criar resposta clínica simples
    resposta = f"""
========================================
DERMAINTELLIGENCE™ — Análise Científica
========================================

Tema pesquisado:
{termo}

Principais evidências encontradas:

{textos}

⚠️ Baseado nos artigos mais relevantes do PubMed.
Use julgamento clínico individual.
"""

    return resposta