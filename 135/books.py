from collections import namedtuple
from datetime import datetime
from operator import attrgetter

Book = namedtuple("Book", "title authors pages published")

books = [
    Book(
        title="Python Interviews",
        authors="Michael Driscoll",
        pages=366,
        published="2018-02-28",
    ),
    Book(
        title="Python Cookbook",
        authors="David Beazley, Brian K. Jones",
        pages=706,
        published="2013-05-10",
    ),
    Book(
        title="The Quick Python Book",
        authors="Naomi Ceder",
        pages=362,
        published="2010-01-15",
    ),
    Book(
        title="Fluent Python",
        authors="Luciano Ramalho",
        pages=792,
        published="2015-07-30",
    ),
    Book(
        title="Automate the Boring Stuff with Python",
        authors="Al Sweigart",
        pages=504,
        published="2015-04-14",
    ),
]


# all functions return books sorted in ascending order.


def sort_books_by_len_of_title(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    return sorted(books, key=lambda book: len(book.title))


# split several authors and get last name of first
def _first_authors_last_name(book):
    return book.authors.split(",")[0].split()[-1]


def sort_books_by_first_authors_last_name(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    # don't need to use lambda if using auxiliary functions
    return sorted(books, key=_first_authors_last_name)


def sort_books_by_number_of_page(books=books):
    """
    Expected last book in list:
    Fluent Python
    """
    # if using a named tuple use getattr to call a variable
    # in this case called pages attribute
    return sorted(books, key=attrgetter("pages"))


# Returns datetime object from str date
def _published_date(book):
    return datetime.strptime(book.published, "%Y-%m-%d")


def sort_books_by_published_date(books=books):
    """
    Expected last book in list:
    Python Interviews
    """
    # don't need to use lambda if using auxilirary functions
    return sorted(books, key=_published_date)
