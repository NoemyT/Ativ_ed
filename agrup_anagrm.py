from collections import defaultdict

def anagramas(palavras):
    grupos = defaultdict(list)
    for palavra in palavras:
        sort = "".join(sorted(palavra))
        grupos[sort].append(palavra)
    return grupos
    
def mostrar_grps(grupos):
    for i, grupo in enumerate(grupos.values(), start=1):
        print(f"Grupo {i}: {' '.join(grupo)}")

palavras = ["alegria", "alergia", "regalia", "galeria", "muro", "rumo", "carro",
            "arroz", "rroca", "zorra", "macarrão", "racomarã"]
grupos = anagramas(palavras)
mostrar_grps(grupos)