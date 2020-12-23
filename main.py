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

def readNextLine(file):
    line = file.readline()
    line = line.replace('/', '\n')
    return line

def block(file):
    category = readNextLine(file)
    question = readNextLine(file)
    answers = []
    for i in range(4):
        answers.append(readNextLine(file))
    correct = readNextLine(file)
    if correct:
        correct = correct[0]
    explanation = readNextLine(file)
    return category, question, answers, correct, explanation




def main():
    welcom()
    score = 0
    file = openFile()
    category, question, answers, correct, explanation = block(file)

    while category:
        print(category)
        print(question)
        for i in range(len(answers)):
            print("\t" + str(i + 1) + ". - " + answers[i])
        userAns = input("Ваш ответ >>> ")
        if str(userAns) == str(correct):
            print("Да!")
            score += 1
        else:
            print("Нет!")
        print(explanation)
        print("Ваш счет " + str(score))
        category, question, answers, correct, explanation = block(file)
    file.close()
    print("Игра окончена! Вы набрали " + str(score))
    next()


main()
