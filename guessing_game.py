retry = None

bird = "\n               /´¯/) \n             ,/¯../ \n            /..../ \n      /´¯/'...'/´¯¯`·¸ \n   /'/.../..../......./¨¯\ \n  ('(...´...´.... ¯~/'...') \n  \.................'..../ \n   \...\.......... _.·´ \n     \..............( \n       \.............\\"

def bingo():
    print("Bingo! Hahahahahaha\n" + bird + "\n\nHey, ya know I love ya really.")

def wrong():
    print("Wrong! How do ya like them apples, doofus?!\n" + bird)

def how_many(retry):
    if retry == None:
        fingers = input("How many fingers am I holding up?\n")
        if fingers == "1":
            which_one()
        else:
            retry = input("Nope! Wanna guess again? (y/n)\n")
            how_many(retry)
    elif retry == "n":
        print("Suit yerself. Stupid game anyway...")
    elif retry == "y":
        fingers = input("Awright smart guy, how many?\n")
        if fingers == "1":
            which_one()
        else:
            print("Not the brightest bulb in the box, huh? Go back to sleep, buddy.")
    else:
        retry = input("Uh, you feelin' OK? You gotta type 'y' or 'n', dummy.\n")
        how_many(retry)

def which_one():
	finger = input("Correct! Guess which one! (one word or number)\n")
	if finger == "middle" or finger == "third" or finger == "3":
		bingo()
	else:
		wrong()
            
how_many(retry)