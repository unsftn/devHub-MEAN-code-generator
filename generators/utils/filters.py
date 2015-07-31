def inputType(type):
    if type == "String":
        return "text"
    elif type == 'Boolean':
        return 'checkbox'
    elif type.__class__.__name__ == 'Reference':
        return 'Reference'
    return "text"
