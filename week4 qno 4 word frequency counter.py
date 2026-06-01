def word_frequency(text):
    text = text.lower()


    for ch in ".,!?":
        text = text.replace(ch, "")
    words = text.split()

    freq = {}

    

