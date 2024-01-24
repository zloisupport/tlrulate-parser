
import argparse
from parser2.book import Book


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument("book_url")

    return parser


def main():
    # init
    parser = init_argparse()
    args = parser.parse_args()

    # main
    book = Book(args.book_url)

    book.parse()
    book.parse_chapters()
    book.print_content()
    book.save_as_epub(f"{book.title}.epub")
    # book.save_as_text(f"{book.title}.txt")
    input("Enter to continue...")


if __name__ == "__main__":
    main()
