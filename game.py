import random
MyLevel = input("Level: ")
MyLevelCheck = MyLevel.isdigit()

while True:
    if MyLevelCheck == True and int(MyLevel) > 0:
        MyLevel = int(MyLevel)
        break
    else:
        MyLevel = input("Level: ")
        MyLevelCheck = MyLevel.isdigit()

MyGuess = input("Guess: ")
MyCheck = MyGuess.isdigit()

while True:
    if MyCheck == True and int(MyGuess) > 0:
        MyGuess = int(MyGuess)
        break
    else:
        MyGuess = input("Guess: ")
        MyCheck = MyGuess.isdigit()        

CorrectNum = int(random.randrange(MyLevel))
    
while True:
    if int(MyGuess) == int(CorrectNum):
        print("Just right!")
        break
    elif int(MyGuess) < int(CorrectNum):
        print("Too small!")
        MyGuess = int(input("Guess: "))
    else:
        print("Too large!")
        MyGuess = int(input("Guess: "))
