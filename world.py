class World:
    def __init__(self, personajes):
        self.personajes = personajes
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)
    
    def remove_event(self, event):
        self.events.remove(event)
    
    def get_events(self):
        return self.events

    def __repr__(self):
        return f"World(personajes={self.personajes}, events={self.events})"