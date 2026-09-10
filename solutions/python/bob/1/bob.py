def response(hey_bob):
    if hey_bob.rstrip().endswith("?") and not hey_bob.isupper():
        return "Sure."
    if hey_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    if hey_bob.endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.isspace() or not hey_bob:
        return "Fine. Be that way!"
    return "Whatever."
