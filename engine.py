def trigger_event(personajes, event):
    for personaje in personajes.values():
        for regla in personaje.rules:
            if regla.event == event:
                personaje.mood = regla.new_mood
                print(f"{personaje.name} se siente {personaje.mood} al escuchar música.")


def process_event(world, event, logger):

    logger.separator()
    logger.log(f"EVENTO OCURRIDO: {event}")

    world.add_event(event)
    
    for personaje in world.personajes.values():
        
        logger.log(f"\nEvaluando reglas de {personaje.name} (mood={personaje.mood})")

        for regla in personaje.rules:
            
            logger.log(
                f"  Regla: IF hears '{regla.event}'"
                + (f" AND mood IS {regla.required_mood}" if regla.required_mood else "")
                + f" THEN mood = {regla.new_mood}"
            )

            if regla.event != event:
                continue

            if regla.required_mood is not None:
                if personaje.mood != regla.required_mood:
                    continue

            old_mood = personaje.mood
            personaje.mood = regla.new_mood
            print(f"{personaje.name} cambia de {old_mood} a {personaje.mood}")