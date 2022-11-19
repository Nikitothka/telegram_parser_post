def have_entities(message) -> str:
    if 'caption_entities' in str(message):
        return str(message.caption_entities)
    else:
        return 'None'
