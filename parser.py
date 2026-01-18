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
            required_mood = None

            if "mood IS" in line:
                parts = line.split()
                required_mood = parts[parts.index("IS") + 1]
            
            event = line.split('"')[1]
            new_mood = line.split()[-1]
            
            rule = RuleNode(event, new_mood, required_mood)
            current.rules.append(rule)
    
    return personajes