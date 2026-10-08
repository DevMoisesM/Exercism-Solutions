def is_isogram(phrase):
    phrase = phrase.upper()
    letter_phrase = []
    
    for letter in phrase:
        if letter not in letter_phrase:
            letter_phrase.append(letter)
        elif letter == "-":
            continue
        elif  letter == " ":
            continue
        else:
            return False
        
    return True