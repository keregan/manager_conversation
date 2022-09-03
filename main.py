import csv

greetings_all = ['здравствуйте', 'здраствуй', 'здрасте', 'приветствую']
farewell_all = ['досвидания', 'до встречи', 'всего доброго', 'всего хорошего']
self_presentation_all = ['меня зовут', 'моё имя']
company_name_all = ['представляю', 'компания', 'компанию', 'компании', 'организацию']


def main():
    with open('test_data.csv', 'r', encoding='utf-8', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            text_message = "".join(row)
            text_message = text_message.lower()

            for greet in greetings_all:
                if greet in text_message:
                    greetings = True
                    break
                greetings = False

            for far in farewell_all:
                if far in text_message:
                    farewell = True
                    break
                farewell = False

            for self in self_presentation_all:
                if self in text_message:
                    self_presentation = self
                    break
                self_presentation = False

            for name in self_presentation_all:
                if name in text_message:
                    manager_name = text_message.partition(name)[2].split()[0]
                    break
                manager_name = False

            for name in company_name_all:
                if name in text_message:
                    company_name = text_message.partition(name)[2].split()[0]
                    break
                company_name = False

            for far in farewell_all:
                if far in text_message:
                    said_goodbye = far
                    break
                said_goodbye = False

            print('text_message = ', text_message, '\n greetings = ', greetings, '\n self_presentation = ',
                  self_presentation, '\n manager_name = ', manager_name, '\n company_name = ',
                  company_name, '\n said_goodbye = ', said_goodbye, '\n farewell = ', farewell)


if __name__ == '__main__':
    main()