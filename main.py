import os
import csv
import random
import time

from playsound import playsound

class MultiplicationGame:
    playerName = ''
    initialLevel = 12
    def __init__(self, playerName):
        """
        Invoking constructor for initializing player name
             Parameters:
                playerName (str) : name of player who is playing
        """
        self.playerName = playerName

        with open('{}.csv'.format(self.playerName), mode='w') as playerRecord:
            playerWriter = csv.writer(playerRecord, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            playerWriter.writerow(['Question', 'Answer', 'Correct', 'Time Taken To Answer'])

        

    def nextQuestion(self):
        """
        This method will generate next question for the player.
        This will also start timer once question is shown to the user.
        """
        self.firstNumber = random.randint(1,self.initialLevel)
        self.secondNumber = random.randint(1,10)

        print("What is the answer of {} * {} ".format(self.firstNumber, self.secondNumber))
        self.startTime = time.time()

    def answerChecker(self):
        """
        This method will check user input answer.
        it will also log user's result for the given question and will also change the level.
        """
        try:
            if int(self.userInput) == (self.firstNumber*self.secondNumber):
                self.isCorrect = 'Yes' 
                print("Correct Answer")
                #playsound('assets/applause.mp3')
            else: 
                self.isCorrect = "No"
                print("Oops That's wrong.")
        except ValueError:
            self.isCorrect = 'No'
            print("Oops That's wrong.")
        self.responseLooger()
        self.changeLevel()

    def changeLevel(self):
        """
        This method will change the range of question to ask on the bases of previous answer.
        Logic:
            if the user have answered previous question then lets ask question from the higer table and visa versa.
        """
        if self.isCorrect:
            self.initialLevel = self.initialLevel + 1 if self.initialLevel < 12 else self.initialLevel
        else:
            self.initialLevel =  self.firstNumber if self.initialLevel > 1 else self.initialLevel

    def responseLooger(self):
        """
        This question will write result to cvs file.
        file will be created in the same directory where this script is have playerName as the name and extenstion as csv
        """
        with open('{}.csv'.format(self.playerName), mode='a') as playerRecord:
            playerWriter = csv.writer(playerRecord, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            playerWriter.writerow(['{} * {}'.format(self.firstNumber, self.secondNumber),
             self.userInput, self.isCorrect, self.endTime - self.startTime])

    def startGame(self):
        """
        This function is responsible to start the game
        """
        playMore = 'Y'
        while playMore == 'Y':

            self.nextQuestion()

            self.userInput = input("Enter Answer - ")
            self.endTime = time.time()
            self.answerChecker()

            playMore = input("What to play more?. Y/N - ")

        print("Good Bye {}".format(self.playerName))

if __name__ == '__main__':
    
    print("Hello Welcome to Math Practice Program")
    
    playerName = input("What's your name?. ")

    gameObj = MultiplicationGame(playerName=playerName)
    gameObj.startGame()