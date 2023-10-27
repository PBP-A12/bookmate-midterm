import csv
from book_request.models import Book

def run():
    with open("pg-filtered-text-one-author.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            title = row[1]
            lang = row[2]
            first_name = row[3]
            last_name = row[4]
            year = row[5]
            subjects = row[6]
            if ";" in subject:
                subject = subjects.split(";")
            bookshelves = row[7]
            Book.objects.create(title=title, lang=lang, first_name=first_name, last_name=last_name, year=year, subject=subject, bookshelves=bookshelves)