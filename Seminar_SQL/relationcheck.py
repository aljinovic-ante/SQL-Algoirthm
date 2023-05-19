def is_in(value, relation):
    for letter in value:
        if letter not in relation:
            return False
    return True

def is_combination_in(fr_main, lista):
    for fr in lista:
        if sorted(fr_main.lower()) == sorted(fr.lower()):
            return True
    return False