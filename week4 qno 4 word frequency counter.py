def word_frequency(text):
    text = text.lower()


    for ch in ".,!?":
        text = text.replace(ch, "")
    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    sorted_words = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )


    print("Top 3 words:")

    for word, count in sorted_words[:3]:
        print(f"{word} — {count} times")



