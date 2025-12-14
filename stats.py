def count_words(text):
    words = text.split()
    return len(words)


def characters(text):
    text = text.lower()
    chars = {}

    for character in text:
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1

    return chars


def sort_on(d):
    return d["num"]


def create_and_sort(items):
    sorted_list = []

    for item in items:
        dictionary = {"char": item, "num": items[item]}
        sorted_list.append(dictionary)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
