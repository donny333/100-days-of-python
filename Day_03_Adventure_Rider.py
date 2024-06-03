motorcycle_art = """
            r==
        _  //
       |_)//(''''':
         //  \_____:_____.-----.P
        //   | ===  |   /        
    .:'//.   \ \=|   \ /  .:'':.
   :' // ':   \ \ ''..'--:'-.. ':
   '. '' .'    \:.....:--'.-'' .'
    ':..:'                ':..:'
"""
print(motorcycle_art)
print("motorcycle is taken from https://ascii.co.uk/art")
print("You are motorcycle rider. And you are going to a adventure.")
first_turn = input("You came to a crossroad. It is written: go to the left and there will be a highway. Go to the right and you will ride curvy forest road. Which way you will go? Type left or right.\n")
if first_turn.lower() == "left":
    print("There are no adventures on highways. Game over.")
else:
    second_choice = input("Good choice. Now you are riding a curvy road. After few days you came by the river. It looks very shallow, but there is a sign: wait for a ferry to come. Will you cross the river by your self? Write Y or N.\n")
    if second_choice.lower() == "n":
        print("You have been scammed. After waiting few minutes bandits came and took away your motorcycle. The adventure is over.")
    else:
        last_choice = input("You just have reached a camp. What is the first thing you do? Change bike oil? Go grab a drink with camp owner? Plan further journey? Type change, drink or plan.\n")
        if last_choice.lower() == 'drink':
            print("Congrats, you have finished your first part of adventure.")
        else:
            print("Camp owner feels offended. He confiscated your motorcycle and sold its parts. Game over.")