# Quick Quiz Game

import sys
import os
import time

class QuizGame:

    def __init__(self,fileName,questionList):
        self.__fileName = fileName
        self.__questionList = questionList
        print('instance of quiz created successfully')

    def openFile(self):
        # Open quiz game file
        try:
            self.__infile = open(self.__fileName, 'r')
            print(self.__fileName, ' opened successfully.')
        except:
            print(self.__fileName, 'failed to open. Closing program.')
            sys.exit()

    def closeFile(self):
        self.__infile.close()
        print('Quiz file closed.')

    def makeQuestionList(self):
        self.__numQues = 0
        for line in self.__infile:
            if line[0] == '#':
                self.__numQues += 1
                newLine = (line.rstrip()).lstrip()
                lineList = newLine.split('#')
                self.__questionList.append(lineList)

    def addQuestion(self):
        qid = input('Enter ID of question. Should not be a duplicate of an already existing ID: ')
        question = input('What is the question? ')
        answer = input('What is the answer? ')
        newQuestion = '#' + qid + '#' + question + '#' + answer
        self.__questionList.append(newQuestion.split('#'))
        self.__numQues += 1

    def deleteQuestion(self):
        found = False
        qid = input('Enter ID of question to be deleted.')
        for i in range(self.__numQues):
            qidComparison = self.__questionList[i][1]
            if qid == qidComparison:
                found = True
                self.__questionList.pop(i)
                self.__numQues -= 1
                print('Question was deleted.')
                break
        if found == False:
            print('Question ID wasn\'t found.')

    def saveFile(self):
        newFile = input('Enter new filename without extension: ')
        newFile = newFile + '.txt'
        outfile = open(newFile, 'w')
        print('Enter comment lines starting with \'!\': ')
        print('Press enter to stop adding comments.')
        while True:
            line = input('Comment: ')
            if len(line) == 0:
                break
            else:
                print('! ' + line, file=outfile)
        for i in range(self.__numQues):
            printString = '#'.join(self.__questionList[i])
            print(printString, file=outfile)

        outfile.close()
        print(newFile, 'has been written to and closed.')
        
    def listQuestionsArray(self):
        
        print('Questions Array listing:')
        print(self.__questionList)

    def playGame(self):
        self.__numCorrect = 0
        for i in range(self.__numQues):
            question = self.__questionList[i][2]
            time.sleep(2)
            print('Here is the question:')
            time.sleep(2)
            print(question)
            answer = input('What is your answer?: ')
            if answer == self.__questionList[i][3]:
                time.sleep(2)
                print('Congratulations! You got the correct answer!')
                time.sleep(2)
                print('Time for the next question.\n\n')
                self.__numCorrect += 1
            else:
                time.sleep(2)
                print('Sorry, the correct answer was:', self.__questionList[i][3], '\nMaybe next time!\n\n')
        print('The game is now over. \nHere is your score: ')
        time.sleep(2)
        print('You got',self.__numCorrect, 'questions correct out of', self.__numQues, 'questions.')
        print('That\'s {0}%.'.format(round(self.__numCorrect/self.__numQues*100, 2)))

    def menuOptions(self):
        if self.__option == 1:
            print('Now Starting Game!')
            self.playGame()
        elif self.__option == 2:
            print('Add a question.')
            self.addQuestion()
        elif self.__option == 3:
            print('Delete a question.')
            self.deleteQuestion()
        elif self.__option == 4:
            print('Save changes to a file.')
            self.saveFile()
        elif self.__option == 5:
            self.listQuestionsArray()
        elif self.__option == 6:
            print('Exiting game.')
        else:
            print('Invalid option selected. Closing program.')
            sys.exit()

    def printMenu(self):
        print('\nPick an option: ')
        print('  1  play the game')
        print('  2  add a question')
        print('  3  delete a question')
        print('  4  save changes to file')
        print('  5  print question list')
        print('  6  exit program')
        self.__option = eval(input('Enter option: '))
        return self.__option

def inputFileName(): 
    default = int(input('For Questions.txt, please enter 1; for another file, enter 0:'))

    if default == 1:
        fileName = 'Questions.txt'
    else:
        fileExt = '.txt'
        allFiles = os.listdir()      
        print('\nPick a file from the following list: ')
        for aFile in allFiles:            
            if fileExt in aFile:
                print(aFile)
        fileName = input('Type filename:')

    return fileName

def main():
    print('Quiz Game - v1.0')
    fileName = inputFileName()
    createQuiz = QuizGame(fileName,[])
    createQuiz.openFile()
    createQuiz.makeQuestionList()
    while True:
        option = createQuiz.printMenu()
        if option == 6:
            print('Exiting program.')
            break
        else:
            createQuiz.menuOptions()
    createQuiz.closeFile()

main()
        
    
