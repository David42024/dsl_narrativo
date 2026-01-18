#Producción de tokens (por lineas)

def tokenizador(texto):
    return [line.strip() for line in texto.splitlines() if line.strip()]
