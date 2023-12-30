import random as rd

UserName = input("What is your Name: ")
rps = ["rock","paper","scissors"]
for ind, elm in enumerate(rps):
    print(ind+1,elm)

ComputerChoice = rd.choice(rps)
UserChoice = int(input("choose your weapon(1,2,3): "))
if ComputerChoice == rps[0] and rps[UserChoice-1] == rps[1]:
    print(f"computer choose {ComputerChoice}")
    print(UserName,"Well Done you win")
elif ComputerChoice == rps[0] and rps[UserChoice-1] == rps[2]:
    print("you loose sorry")
    print(f"computer choose {ComputerChoice}")
elif ComputerChoice == rps[1] and rps[UserChoice-1] == rps[0]:
    print("you loose sorry")
    print(f"computer choose {ComputerChoice}")
elif ComputerChoice == rps[2] and rps[UserChoice-1] == rps[0]:
    print(UserName,"Well Done you win")
    print(f"computer choose {ComputerChoice}")
elif ComputerChoice == rps[1] and rps[UserChoice-1] == rps[2]:
    print(UserName,"Well Done you win")
    print(f"computer choose {ComputerChoice}")
else:
    print(f"computer choose {ComputerChoice}")
    print("Tie")