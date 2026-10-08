def reverse(text):
    reverse_text = []
    for char in text:
        reverse_text.insert(0, char)
    
    return "".join(reverse_text)