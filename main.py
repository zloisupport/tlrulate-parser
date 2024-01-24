
import argparse
from parser2.book import Book, FileFormat


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument("book_url")

    return parser


def main():
    # init
    parser = init_argparse()
    args = parser.parse_args()

    # main
    file_format = FileFormat.TXT
    book = Book(args.book_url,file_format)

    book.parse()
    book.parse_chapters()
    book.print_content()

    if file_format == FileFormat.EPUB:
        book.save_as_epub()
    else:
        book.save_as_text()

    input("Enter to continue...")


if __name__ == "__main__":
    main()
