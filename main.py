import sys

def next():
    input("Нажмите ENTER, чтобы продолжить...")

def openFile():
    fileName = str(input("Введите имя файла >>> "))
    try:
        file = open(fileName, "r", encoding = 'utf-8')
    except:
        print("Не получается открыть файл."
              "\nПрограмма завершает свою работу.")
        next()
        sys.exit()
    else:
        return file

def welcom():
    print("\t\t\tДобро пожаловать в игру викторину!")


def block(file):



def main():
    welcom()
    file = openFile()



main()
