import random
import os
import time


print(r""" 
___________                                 ._.
╲_   _____╱ ______ ____ _____  ______   ____│ │
 │    __)_ ╱  ___╱╱ ___╲╲__  ╲ ╲____ ╲_╱ __ ╲ │
 │        ╲╲___ ╲╲  ╲___ ╱ __ ╲│  │_> >  ___╱╲│
╱_______  ╱____  >╲___  >____  ╱   __╱ ╲___  >_
        ╲╱     ╲╱     ╲╱     ╲╱│__│        ╲╱╲╱
""")
time.sleep(2)

print("""

The Robots have caught you, taken your weapons and locked you up.
Suddenly you remember you still have your sonar wristwatch, which can be
tuned to produce sounds ofany frequency. If you can only find the resonant
frequency of your Robot guards, they should vibrate so much they fall apart.
You must be careful not to use frequencies that are too low or the building
wll vibrate and cllapse on top ofyou. If you go too high, you will get such a
terrible headache you will have to give up.

Can you escape the horrors of the Robot prison? (Look carefuUy at the
program for a clue to the range offrequencies to try.)""")

time.sleep(6)

robot_frequency = random.randint(100, 1000) #the resonant frequency of the robot guards is randomly generated between 100 and 1000 Hz
print(robot_frequency) #for testing purposes, you can comment this line out to hide the frequency from the player

chances = 10
won = False

while chances > 0:
    if chances == 1:
        print("Be careful! You only have one chance left!")
    else:
        print(f"\nYou have {chances} chances left.")
    try:
        player_guess = int(input("Enter a frequency to try (100 - 1000 Hz): "))
    except ValueError:
        print("Invalid input! Please enter a number between 100 and 1000.")
        continue
    
    #win condition
    if abs(robot_frequency - player_guess) <= 5: #if the player's guess is within 5 Hz of the robot's frequency, they win
        print("Congratulations! You found the resonant frequency and escaped the prison!")
        won = True
        break
    
    elif player_guess < robot_frequency:
        print("Too Low! The building is starting to vibrate. You lose a chance.")
    elif player_guess > robot_frequency:
        print("Too High! You get a terrible headache. You lose a chance.")
           
    chances -= 1
    
    

if __name__ == "__main__":
    if not won:
        print(f"Game over! The frequency was {robot_frequency} Hz. You failed to escape the prison.")
    