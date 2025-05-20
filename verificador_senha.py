import string

def verifica_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("Senha muito curta")
    if not any(c.isupper() for c in senha):
        erros.append("Falta letra maiúscula")
    if not any(c.islower() for c in senha):
        erros.append("Falta letra minúscula")
    if not any(c.isdigit() for c in senha):
        erros.append("Falta número")
    if not any(c in string.punctuation for c in senha):
        erros.append("Falta caractere especial")
    if any(c.isspace() for c in senha):
        erros.append("Contém espaços")
    return erros