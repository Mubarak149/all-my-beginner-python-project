

user = input("do you want to be rich(y/n): ")
if user == "y":
    user = input("you find your self in a small town where do you want to go(l/r) left or right: ")
    if user == "l":
        user = input("you come across army robbers where will you go(l/r) left or right: ")
        if user == "l":
            print("they think you are going to run away so they kill you")
            print("you loose")
            exit()

        elif user == "r":
            user = input("good you just move out of their way nobody see you now where do you go(l/r) left or right: ")
            if user == "l":
                print("go straight")
                print("finally you got the treasure")
            elif user == "r":
                user = input("you met with a friend call jef where do you want to go(l/r) left or right: ")
                if user == "l":
                    print("jef kill you in tha corner")
                    print("sorry you loose")
                    exit()
                elif user == "r":
                    print("jef run away and leave you to die in desert")
                    print("you loose")
                    exit()
    elif user == "r":
        user = input("you go into the small town(l/r) left or right: ")
        if user == "l":
            print("you go into the treasure hounters one of them kill you")
        elif user == "r":
            print("you come across a lake no road ")
            print("sorry you loose")
    else:
        print("invalid input")
        exit()
elif user == "n":
    print("some one get angry and kill you there")
    print("sorry you loose")

else:
    print("invalid input")
    exit()

