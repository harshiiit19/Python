import random

player_choice = input("Enter the Choice (sanke, water, gun): ")  

possible_choice = ["snake", "water", "gun"]
computer_choice = random.choice(possible_choice)

print(f"\n Your Choice {player_choice}.\n Computer Choice {computer_choice}. \n")

if player_choice == computer_choice :
    print(f"Both are selecetd same option {player_choice}. Match is TIE!")
    
if player_choice == "snake":
    if computer_choice == "water":
        print("Snake drinks the water hence wins. Player WIN!")
    else:
        print("Gun will kill the snake and win. Computer WIN!")
if player_choice == "water":
    if computer_choice == "gun":
        print("The gun will drown in water, hence a point for water. Player WIN!")
    else:
        print("Snake drinks the water hence wins. Computer WIN!")
if player_choice == "gun":
    if computer_choice == "sanke":
        print("Gun will kill the snake and win. Player WIN!")
    else:
        print("The gun will drown in water, hence a point for water. Computer WIN!")


