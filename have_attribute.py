def have_entities(message) -> str:
    if 'caption_entities' in str(message):
        return str(message.caption_entities)
    else:
        return 'None'
def have_entities_text(message) -> str:
    if 'entities' in str(message):
        return str(message.entities)
    else:
        return 'None'
