name = input("Enter your name: ")
print("welcome to adventure game", name)
game = input("Do you want to play fun adventure game (yes/no)? ").lower()
if game == "yes":
    print("Lets Start")
    answer = input("Do you want to play horror game or funny game (horror/funny)? ").lower()
    if answer =="horror":
        horror = input("You came across to the jungle and there are two paths: left and right. Where you want to go (left/right)? ").lower()
        if horror == "left":
            left = input("Oh no! there a big wolf standing there! you want to fight or run away? (fight/run)? ").lower()
            if left == "fight":
                print("You fight well. YOU WIN! ;) ")

            elif left == "run":
                print("You run too many miles and dies out of thirst. YOU LOSE! ")
            else:
                print("You typed wrong. YOU LOSE!")
        elif horror == "right":
            right = input("You heard something unusual. Do you want to explore who is there or just ignore it (explore/ignore)? ").lower()
            if right == "explore":
                explore = input("You saw someone standing there and comming towards you. There is a sword and a rock there. what you want to pick (sword/rock)? ").lower()
                if explore == "sword":
                    print("You killed that thing. YOU WON! ")
                elif explore == "rock":
                    print("You are being killed by that thing. YOU LOSE! ")
                else:
                    print("You typed wrong. YOU LOSE!")
            elif right == "ignore":
                print("You didn't see the swamp . and you got stucked. YOU LOSE! ")
            else:
                print("You typed wrong. YOU LOSE!")
        else:
            print("You typed wrong. YOU LOSE!")

    elif answer == "funny":
        funny = input("There is a road having two sides. south and east where you want to go (south/east)? ").lower()
        if funny == "south":
            south = input("A man is standing there and giving a task to do a funny dance you want to do (yes/no)? ")
            if south == "yes":
                print("You do a funny dance hahahahaa. and won a prize. Congrats you win! ")
            elif south == "no":
                print("You ignore the funny part. YOU LOSE! ")
            else:
                print("you typed wrong. YOU LOSE! ")
        elif funny == "east":
            east = input("A function is helding there and need someone who can make audience laugh. Do you want to participate? (yes/no) ").lower()
            if east == "yes":
                print("You cracked a funny joke. Everyone laughed YOU WON! ")
            elif east == "no":
                print("you missed the chance to win the game. YOU LOSE! ")
            else:
                print("You typed wrong. YOU LOSE! ")
    else:
        print("You typed wrong. YOU LOSE! ")
else:
    print("You quit the game. Goodbye! ")
    quit()

