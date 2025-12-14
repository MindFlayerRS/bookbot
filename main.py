from stats import characters, count_words, create_and_sort


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    content = get_book_text("books/frankenstein.txt")
    chars = characters(content)
    sorted_list = create_and_sort(chars)

    print(
        "============ BOOKBOT ============\n"
        "Analyzing book found at books/frankenstein.txt...\n"
        "----------- Word Count ----------\n"
        f"Found {count_words(content)} total words\n"
        "--------- Character Count -------"
    )

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
