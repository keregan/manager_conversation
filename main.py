import csv

with open('test_data.csv', 'r', encoding='utf-8', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        text_message = "".join(row)
        greetings = True if 'Здравствуйте' in text_message else False
        farewell = True if 'досвидания' in text_message else False
        print(text_message, greetings, farewell)

