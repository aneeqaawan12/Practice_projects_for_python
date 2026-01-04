print("*****************************************")
print("   --------- QUIZ GAME --------------")

game = input("Do you want to play? ")
if game.lower() != 'yes':
    quit()

def questions():
    print("Let's Play! :) ")

    count = 0
    answer1 = input("What does CPU stand for? ")
    if answer1.lower()== "central processing unit":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer2 = input("What does GPU stand for? ")
    if answer2.lower()== "graphics processing unit":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer3 = input("What does RAM stand for? ")
    if answer3.lower()== "random access memory":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer4 = input("What does ROM stand for? ")
    if answer4.lower()== "read only memory":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer5 = input("What does PSU stand for? ")
    if answer5.lower()== "power supply":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer6 = input("What does OS stand for? ")
    if answer6.lower()== "operating system":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer7 = input("What is an error called? ")
    if answer7.lower()== "a bug":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")
    
    answer8 = input("which device is used to input data into computer? ")
    if answer8.lower()== "keyboard":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer9 = input("What does URL stand for? ")
    if answer9.lower()== "uniform resource locator":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    answer10 = input("What does HTTP stand for? ")
    if answer10.lower()== "hypertext transfer protocol":
        print("Correct!")
        count += 1
    else:
        print("Incorrect!")

    
    print("you got " + str(count) + " answers correct!")
    if count == 10:
        print("You topped the test!")

    elif count <10 and count >= 5:
        print("You passed the test!")
    
    else:
        print("You failed! work hard :)")


questions()
