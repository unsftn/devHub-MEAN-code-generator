def inputType(type):
    if type == "String":
        return "text"
    elif type == 'Boolean':
        return 'checkbox'
    elif type.__class__.__name__ == 'Reference':
        return 'Reference'
    #moglo bi se dodati i za ostale tipove html input polja (uz prosirenje gramatike)
    #tipa date, password itd.
    return "text"