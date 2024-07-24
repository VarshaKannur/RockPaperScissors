rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
picture = [rock,paper,scissors]
human = int(input("What do you want to choose?\n 0 for rock\n 1 for paper\n 2 for scissors\n"))
if human>=3 or human<0:
    print("Invalid choice")
else:
    print(picture[human])
    computer = random.randint(0,2) 
    print("Computer choose: \n")
    print(picture[computer])
    
    if human==computer:
        print("Draw")
    elif human==0 and computer==2:
        print("You win")
    elif human==1 and computer==0:
        print("You win")
    elif human==2 and computer==1:
        print("You win")
    else:
        print("You lose")
