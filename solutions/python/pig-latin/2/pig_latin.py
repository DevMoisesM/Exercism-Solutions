def translate(text):
    text = text.split()
    list_text = []

    for word in text:
        pig_latin_word = word_of_text(word)
        list_text.append(pig_latin_word)

    pig_latin_text = " ".join(list_text)
    
    return pig_latin_text 

def word_of_text(word):
    vowels = ("a", "e", "i", "o", "u")

    if word[0] in vowels or word.startswith(("xr", "yt")):
        word += "ay"
        return word
    if word[0] not in vowels:
        word_consonant = ""
        idx = 0
        while idx < len(word):
            letter = word[idx]
            if letter not in vowels:
                if word[idx:idx+2] == "qu":
                    word_consonant += "qu"
                    idx += 2
                elif letter == "y" and not word.startswith("y"):
                    word = word[idx:]
                    word += word_consonant + "ay"
                    break
                else:
                    word_consonant += letter
                    idx += 1
            else:
                word = word[idx:]
                word += word_consonant + "ay"
                break
        return word
    return None