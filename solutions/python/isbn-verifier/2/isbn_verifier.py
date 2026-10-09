def isbn_formula(list_isbn):
    resultado = (list_isbn[0] * 10 + list_isbn[1] * 9 + list_isbn[2] * 8 + list_isbn[3] * 7 + list_isbn[4] * 6 + list_isbn[5] * 5 + list_isbn[6] * 4 + list_isbn[7] * 3 + list_isbn[8] * 2 + list_isbn[9] * 1) % 11

    return resultado

def is_valid_character(list_isbn):
    for char in list_isbn[:-1]:
        if not char.isdigit():
            return False

    if list_isbn[-1] != "X":
        if list_isbn[-1].isdigit():
            return True
        return False

    return True

def string_to_int(list_isbn):
    for index, char in enumerate(list_isbn):
        if char.isdigit():
            list_isbn[index] = int(char)
        elif char == "X":
            list_isbn[index] = 10

    return list_isbn

def is_valid(isbn):
    list_isbn = []
    
    for char in isbn:
        if char != "-":
            list_isbn.append(char)
        else:
            continue

    if len(list_isbn) == 10:
        if is_valid_character(list_isbn):
            list_isbn = string_to_int(list_isbn)
            return isbn_formula(list_isbn) == 0
            
        return False
    else:
        return False