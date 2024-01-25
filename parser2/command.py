from abc import ABC

from parser2.book import Book, FileFormat


class Command(ABC):
    def __init__(self, receiver,book_url:str,file_format:int) -> None:
        self.receiver = receiver
        self.book_url = book_url
        self.file_format = file_format

    def process(self):
        pass


class BookCommand(Command):
    def __init__(self, receiver,book_url,file_format) -> None:
        self.receiver = receiver
        self.book_url = book_url
        self.file_format = file_format


    def process(self):
        self.receiver.save_action(self.book_url,self.file_format)


class Receiver:
    def save_action(self,book_url,file_format):

        if int(file_format) == 1:
            file_format = FileFormat.EPUB
        else:
            file_format = FileFormat.TXT

        book = Book(book_url,file_format)
        book.parse()
        book.parse_chapters()
        book.print_content()
        book.save()
        print('Success!')


class Invoker:
    def __init__(self):
        self.cmd = None

    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.process()