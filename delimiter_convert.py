import csv
with open('E:\dataset\Book Crossing\BX-Book-Ratings1.csv', "r+", encoding="utf-8") as csv_file:
    content = csv_file.read()

with open('E:\dataset\Book Crossing\BX-Book-Ratings1.csv', "w+", encoding="utf-8") as csv_file:
    csv_file.write(content.replace('your delimiter','target delimiter'))
