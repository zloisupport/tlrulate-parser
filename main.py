
import argparse
from parser2.book import Book, FileFormat


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument("--book_url",type=str,help="URL of the book")
    parser.add_argument("--file_format",type=str,help="Desired file format for the output.\n1 for EPUB, 2 for TXT.Example: main.py(Main.exe) --file_format=2 ",default=2)
    return parser


def main():
    # init
    parser = init_argparse()
    args = parser.parse_args()

    # main
    file_format = args.file_format
    book = Book(args.book_url,file_format)

    book.parse()
    book.parse_chapters()
    book.print_content()
    book.save()


    input("Enter to continue...")


if __name__ == "__main__":
    main()
