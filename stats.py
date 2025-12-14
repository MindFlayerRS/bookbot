def count_words(text):
    words = text.split()
    return f"Found {len(words)} total words"


def characters(text):
    text = text.lower()

    dict = {}

    for character in text:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1

    return dict
