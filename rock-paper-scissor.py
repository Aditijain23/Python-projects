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

#Write your code below this line 👇
import random
choose=int(input("What do you choose. Type 0 for rock, 1 for paper and 2 for scissors."))
if choose==0:
  print(rock)
elif choose==1:
  print(paper)
else:
  print(scissors)
  
computer=random.randint(0, 2)

print(computer)
if computer==0:
  print(rock)
elif computer==1:
  print(paper)
else:
  print(scissors)

if choose==0 and computer==0:
  print("It's a tie")
elif choose==0 and computer==1:
  print("Computer win!")
elif choose==0 and computer==2:
  print("You win!")
elif choose==1 and computer==1:
  print("It's a tie")
elif choose==1 and computer== 0:
  print("You win!")
elif choose==1 and computer==2:
  print("Computer win!")
elif choose==2 and computer==2:
  print("It's a tie")
elif choose==2 and computer==0:
  print("Computer win!")
elif choose==2 and computer==1:
  print("You win!")