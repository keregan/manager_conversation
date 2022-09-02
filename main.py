import csv

with open('test_data.csv', 'r', encoding='utf-8', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        text_message = "".join(row)
        text_message = text_message.lower()
        greetings = True if 'здравствуйте' in text_message else False
        self_presentation = 'меня зовут' if 'меня зовут' in text_message else False
        manager_name = text_message.partition('меня зовут')[2].split()[0] if 'меня зовут' in text_message else False
        company_name = text_message.partition('компании')[2].split()[0] if 'компании' in text_message else False
        said_goodbye = text_message.partition('досвидания')[2].split()[0] if 'досвидания' in text_message else False
        farewell = True if 'досвидания' in text_message else False
        print('text_message = ', text_message, '\n greetings = ', greetings, '\n self_presentation = ',
                               self_presentation, '\n manager_name = ', manager_name, '\n company_name = ',
                               company_name, '\n said_goodbye = ', said_goodbye, '\n farewell = ', farewell)
        # print(text_message, text_message.count(' ') + 1)
        # print(text_message[text_message.find(a)+1:])
        # print(text_message.partition('меня зовут')[2].split()[0])



