def word_frequency(text):
    text = text.lower()


    for ch in ".,!?":
        text = text.replace(ch, "")
    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1
        

