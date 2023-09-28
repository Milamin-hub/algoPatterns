def replace_world(text: str, world: str, new_world: str) -> str:
    while True:
        index = text.find(world)

        if index != -1:
            text = text[:index] + new_world + text[index+len(world):]
        else:
            break

    return text
    