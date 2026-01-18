from lexer import tokenizador
from parser import parser
from engine import trigger_event

with open("examples/historia.dsl", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    tokens = tokenizador(contenido)
    personajes = parser(tokens)


print("ESTADO INICIAL: ")
for personaje in personajes.values(): #values para las clases
    print(f"{personaje.name}: mood={personaje.mood}")

print("\nCAMBIOS DE ESTADO:")
trigger_event(personajes, "music")

print("\nESTADO FINAL: ")
for personaje in personajes.values(): #values para las clases
    print(f"{personaje.name}: mood={personaje.mood}")


