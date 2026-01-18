#entender los tokens
from ast import CharacterNode, RuleNode


def parser(tokens):

    personajes = {}
    current = None

    for line in tokens:
        if line.startswith("CHARACTER"):
            _, name = line.split(" ", 1)
            current = CharacterNode(name.strip())
            personajes[name.strip()] = current
        elif line.startswith("MOOD"):
            _, mood = line.split(" ", 1)
            current.mood = mood.strip()
        elif line.startswith("IF"):
            parts = line.split('"')
            event = parts[1]
            new_mood = parts[2].split()[-1]
            rule = RuleNode(event, new_mood)
            current.rules.append(rule)
    
    return personajes