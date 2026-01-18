def trigger_event(personajes, event):
    for personaje in personajes.values():
        for regla in personaje.rules:
            if regla.event == event:
                personaje.mood = regla.new_mood
                print(f"{personaje.name} se siente {personaje.mood} al escuchar música.")