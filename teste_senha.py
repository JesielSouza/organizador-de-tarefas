import json

def salva_info(usuarios, arquivo="usuarios.json"):
    with open(arquivo, "w", encoding="utf-8") as s:
        json.dump(usuarios, s, indent=4, ensure_ascii=False)

def verifica_info(arquivo="usuarios.json"):
    try:
        with open(arquivo, "r", encoding="utf-8") as s:
            return json.load(s)
    except FileNotFoundError:
        return []