from stats import characters, count_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    content = get_book_text("books/frankenstein.txt")
    print(count_words(content))
    print(characters(content))

    print(
        "============ BOOKBOT ============"
        "Analyzing book found at books/frankenstein.txt..."
        "----------- Word Count ----------"
        f"Found {count_words(content)} total words"
        "--------- Character Count -------"
    )


main()
