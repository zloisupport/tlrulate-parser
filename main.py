import argparse
import os
import sys

from parser2.command import Receiver, BookCommand, Invoker


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument("--book_url", type=str, help="URL of the book")
    parser.add_argument(
        "--file_format",
        type=str,
        help="Desired file format for the output.\n1 for EPUB, 2 for TXT.Example: main.py(Main.exe) --file_format=2 ",
        default=2,
    )
    return parser


def execute_command(book_url: str, file_format: int = 2):
    receiver = Receiver()
    cmd = BookCommand(receiver=receiver, book_url=book_url, file_format=file_format)
    invoker = Invoker()
    invoker.command(cmd=cmd)
    invoker.execute()


def main():
    # init
    parser = init_argparse()
    args = parser.parse_args()

    if len(sys.argv) > 1:
        execute_command(args.book_url, args.file_format)
    else:
        try:
            print("Press Enter to continue or Ctrl+C to exit")
            while True:
                print("Please Enter Url:")
                url = str(input("URL:"))
                print("Please Enter File Format:1 -Epub ,2 -TXT(default)")
                file_format = int(input("File Format:"))
                if url != "" and len(url) > 25 and (file_format != "" and len(str(file_format))==1):

                    execute_command(url, file_format)
                else:
                    print("Invalid input. Please try again.")
        except KeyboardInterrupt:
            print("\nStopped")


if __name__ == "__main__":
    main()
