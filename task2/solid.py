from utils.logger import logger
from abc import ABC, abstractmethod
from typing import List

# 1. SRP - Book 
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self) -> str:
        return "Title: %s, Author: %s, Year: %s" % (self.title, self.author, self.year)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return self.title == other.title


# 4. ISP - Interface lib
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass
    
    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass
    
    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# 3. LSP - can be replaced by any LibraryInterface
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []
    
    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)
            logger.info("Book '%s' added", book.title)
        else:
            logger.info("Book '%s' already exists", book.title)
    
    def remove_book(self, title: str) -> bool:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info("Book '%s' removed", title)
                return True
        logger.info("Book '%s' not found", title)
        return False
    
    def get_books(self) -> List[Book]:
        return self.books.copy()


# 5. DIP - LibraryManager
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library
    
    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
    
    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
    
    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            logger.info("Books in library:")
            for book in books:
                logger.info(str(book))
        else:
            logger.info("Library is empty")


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()