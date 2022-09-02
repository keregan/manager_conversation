import csv

with open('test_data.csv', 'r', encoding='utf-8', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        text_message = "".join(row)
        text_message = text_message.lower()
        greetings = True if 'здравствуйте' in text_message else False
        self_presentation = 'меня зовут' if 'меня зовут' in text_message else False
        manager_name = '?' if 'меня зовут' in text_message else False
        company_name = '?' if 'компании' in text_message else False
        said_goodbye = '?' if 'досвидания' in text_message else False
        farewell = True if 'досвидания' in text_message else False
        # print(text_message, greetings, self_presentation, manager_name, company_name, said_goodbye, farewell)
        print(text_message.count('меня зовут'))

