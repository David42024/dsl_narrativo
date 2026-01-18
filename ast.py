#Clases para definir Nodos
#Son estructuras

class CharacterNode:
    def __init__(self, name):
        self.name = name
        self.mood = "neutral"
        self.rules = []

class RuleNode:
    def __init__(self, event, new_mood, required_mood):
        self.event = event
        self.new_mood = new_mood
        self.required_mood = required_mood