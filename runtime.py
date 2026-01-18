from lexer import tokenizador
from parser import parser
from engine import process_event
from world import World
from log import Logger


with open("examples/historia.dsl", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    tokens = tokenizador(contenido)
    personajes = parser(tokens)

world = World(personajes)
logger = Logger()

print("ESTADO INICIAL: ")
for personaje in world.personajes.values(): #values para las clases
    print(f"{personaje.name}: mood={personaje.mood}")

process_event(world, "music", logger)

print("\nESTADO FINAL: ")
for personaje in world.personajes.values(): #values para las clases
    print(f"{personaje.name}: mood={personaje.mood}")

print("\nHISTORIAL DE EVENTOS:")
print(world.get_events())

