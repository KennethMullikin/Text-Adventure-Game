# Hometown music is The Legend of Zelda: Ocarina of time - Game Title Theme
# Battle music is
# Final Fantasy VII - Boss Theme Original and or FFVII Battle Theme

# West battlefield music is Xenogears Soundtrack -June Mermaid
# West Battlefield boss music is Final Fantasy X - Zanarkand Ruins theme
# North forest music is Chrono Trigger - Myserty of the Forest
# South Mountain Village music is Dark Cloud - Main Theme
# East Cave music is Final Fantasy VIII - Blue Fields
# Abandoned House music is Xenogears - The Treasure Which Cannot be Stolen
# Game Over music is Final Fantasy VII Gameover /  Continue
# North forest music is Chrono Trigger - Myserty of the Forest
# Fake ending(Time Compression) is Final Fantasy VIII - Compression of Time
# The Future music is Final Fantasy VIII - The Castle
# The Future Final Battle Music is
# The Legend of Zelda: Twilight Princess - Hyrule Castle Tower

# Future Final Boss where you killed the Snake music is
# Xenogears - One who Bares Fangs at God

# Final Boss Battle music is Final Fantasy VII - Jenova
# The game has four different endings.


# A Knight's End

# Global Variables
import time
import random
gold = 0
health = 25
Diablos = 300

# To test how text would print
def test():
    print_pause("test")

# function that determines text speed
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

# function that is made for any decision about gold in the game
def grab_gold(goldamount):
    choice = input("Do you wish to grab the gold?\n").lower()
    if "yes" in choice:
        global gold
        gold += goldamount
        print_pause("You place the gold into your gold pouch.\n"
                    f"You now have {gold} gold! Use it wisely.\n")
    elif "no" in choice:
        print_pause("You leave it for someone else to grab.\n"
                    f"You have {gold} gold.\n")
    else:
        print_pause("Yes or No?")
        grab_gold(goldamount)

# function for final boss battle that changes message depending
# on health of final boss and what action he might take
def Diablos_health(damage, inventory):
    global Diablos
    Diablos += damage
    if int(Diablos) > 250:
        print_pause("Diablos has barely been weakened.\n"
                    f"He has {Diablos} health left.\n")
    elif int(Diablos) in range(150, 250):
        print_pause("He's starting to wear down and feel weaker!\n"
                    f"He has {Diablos} health!")
    elif int(Diablos) in range(50, 149):
        print_pause("He's getting angrier finish him fast!\n"
                    f"He has {Diablos} health!")
    elif int(Diablos) in range(-100, 49):
        print_pause("He's unleashing an ultimate attack as a last resort!\n"
                    f"He has {Diablos} health!")
        health_change(-20, inventory)
    else:
        print_pause("Diablos has been slain.")

# function for final boss battle that gives opportunity to do 
# extra damage at risk of losing health
def risk(inventory):
    global Diablos
    risk = input("Do you want to make a risky move to deal extra\n"
                 "damage to Diablos?\n").lower()
    if "yes" in risk:
        x = random.randint(0, 3)
        if x == 2:
            Diablos_health(-60, inventory)
            print_pause(f"Critical strike! Diablos has {Diablos} health left!")
        else:
            print_pause("You narrowly missed, better luck next time.\n"
                        "In the process you hurt yourself.")
            health_change(-2, inventory)
    else:
        print_pause("You block the attack perfectly with your\n"
                    "Shield of the Round Table.")

# function for change in hitpoints for the player with an option
# to use an item to heal
def health_change(hitpoints, inventory):
    global health
    health += hitpoints
    if int(health) > 21:
        print_pause(f"You're healthy as can be! You have {health} health!\n")
    elif int(health) in range(1, 20):
        print_pause(f"You're not looking so good. You have {health} health.\n")
        if "potion" in inventory:
            healchoice = input("Do you want to use a potion?\n").lower()
            if "yes" in healchoice:
                health += 20
                inventory.remove("potion")
                print_pause("You're feeling a lot better.\n"
                            f"You now have {health} health.")
            elif "no" in healchoice:
                print_pause("You may regret this decision later.\n"
                            f"You have {health} health.")
        else:
            print_pause("You have no potions in your inventory to heal.\n"
                        "You may want to visit a shop as soon as you can.\n"
                        f"You have {health} health.\n")

    elif int(health) <= 0:
        if "phoenix down" in inventory:
            print_pause(f"You have {health} health. As you draw your last\n"
                        "breath you realized you have a phoenix down in your\n"
                        "inventory.")
            phoenix = input("Do you want to use your Phoenix Down to heal?\n")
            if "yes" in phoenix:
                health += 25
                inventory.remove("phoenix down")
                print_pause("You have been revived from the brink of death.\n"
                            f"You now have {health} health.")
            else:
                print_pause("Oh dear you have died. Game Over.\n")
                play_again()

        else:
            print_pause("Oh dear you have died. Game Over.\n")
            play_again(inventory)

# function for intro of game
def intro(inventory):
    print_pause("Today starts like any other day.\n"
                "The world has been at peace\n"
                "for the last forty years after a hundred years of war.")
    print_pause("You don't know much about the war other than every knight\n"
                "fell, including your father that you've never met.\n")
    print_pause("You hear the windmills turning slowly as the wind sweeps\n"
                "across the country side.\n")
    print_pause("All of a sudden the earth shakes and you see a beam of\n"
                "light erupting in the North.")
    print_pause("You are the last son of any knight in the country.\n")
    print_pause("You look at your father's old sword a symbol of hope.")
    print_pause("A fire ignites inside you and start packing your\n"
                "belongings. It's your duty as a knight's son to investigate.")
    print_pause("You grab the rusted sword and frail wooden shield\n"
                "to start your new adventure.\n"
                "Before you leave you remember you had gold stashed away.\n")
    grab_gold(5)
    inventory.append("old sword")
    inventory.append("wooden shield")
    print_pause("You look around and notice four major areas to go to")
    print_pause("To the North is an old forest with a haunting beam of\n"
                "light beyond.")
    print_pause("To the East a giant cave that you've heard legends about a\n"
                "giant snake living there.")
    print_pause("To the West is an old battlefield with a neverending storm.")
    print_pause("To the South is a Mountain Village where you\n"
                "can buy some good to help you on your adventure.\n")

# function for final area of game that changes dialogue depending
# on what items you have acquired while playing
def The_End(inventory):
    global Diablos
    global health
    if "secret sword" in inventory:
        print_pause("Maybe with The Sword of the Round Table..\n"
                    "one the power of one soul allowed me to break free\n"
                    "of the time compression maybe all the knights' souls\n"
                    "that have held this sword could bring me back\n"
                    "to my time period?")
        print_pause("You hold the hilt of the sword\n"
                    "and point it above your head.")
        print_pause("This is your last hope,\n"
                    "if you're too late the world will be in ruin.\n")
        print_pause("A power explodes from the sword,\n"
                    "power from all the knights that have held onto this\n"
                    "blade across all time and space.")
        print_pause("Please, you plead, please send me back to my time.")
        print_pause("The sword sparks and is engulfed in flames,"
                    "it's painful to hold, but you bear it.")
        print_pause("The world flashes white and you end up right\n"
                    "past the North Forest.")
        print_pause("You look around and the world isn't in ruins yet.\n"
                    "You've made it. right before Diablos fully awakened.\n")
        print_pause("Relieved you take a look around\n"
                    "to gather your surroundings.")
        print_pause("Your other self was right,\n"
                    "you're already feeling the toll on your body.")
        print_pause("It's possible you might not have much time left.\n")
        print_pause("You walk towards the haunting light in the distance,\n"
                    "towards The End.")
        print_pause("You see a skeleton nearby")
        skeleton = input("Do you want to check out the skeleton?\n").lower()
        if "yes" in skeleton:
            print_pause("You carefully search the skeleton's satchel.")
            print_pause("He has two potions, well he won't be using those.")
            inventory.append("potion")
            inventory.append("potion")
        else:
            print_pause("I've been through a lot,\n"
                        "but I am not touching any skeleton.")
        print_pause("As you continue onward the whole earth\n"
                    "shakes and you hear a screech that isn't human.\n\n")
        print_pause("Diablos has awakened.\n")
        print_pause("Immediately tornados, lightning,\n"
                    "and thunder start striking every where.")
        print_pause("The earth starts to crack apart.")
        print_pause("You charge into the light barrier\n"
                    "that was holding Diablos all these years.")
        print_pause("As soon as he sees you he starts laughing\n"
                    "and rising up into the sky, hellfire\n"
                    "falling down as he rises.")
        print_pause("Everything around us freezes in time,\n"
                    "and the final battle begins.")
        health_change(0, inventory)
        print_pause("Diablos summons forth fireballs in his hands\n"
                    "and throws them towards you.")
        print_pause("You see parts of the earth flying up towards him\n"
                    "as gravity is unstable.")
        risk(inventory)
        print_pause("You feel a powerful energy build up within your sword.")
        print_pause("A holy power eminates from it,\n"
                    "you jump between all the floating rocks\n"
                    "above Diablos's head and stab down right\n"
                    "in between the eyes.")
        Diablos_health(-100, inventory)
        print_pause("Angry with you he grabs you from his head\n"
                    "and tosses you right to the ground.\n"
                    "You hit the ground hard and your sword slides away.")
        health_change(-5, inventory)
        print_pause("You're struggling to get up as\n"
                    "he attempts to grab your sword.")
        print_pause("You run to your sword and make it at the last minute.")
        risk(inventory)
        print_pause("He notices that you have the amulet that can seal him.")
        print_pause("Diablos starts getting desperate and tries to summon\n"
                    "a portal so he can escape.")
        print_pause("You run over as fast as you can\n"
                    "and slash down with all your might right on his hand\n"
                    "so he cannot use it anymore.")
        Diablos_health(-50, inventory)
        print_pause("You focus and gather all your strength\n"
                    "and the hopes of all of the spirits\n"
                    "held captive by Diablos.")
        print_pause("Noticing that you're guard is down he attacks you,\n"
                    "but you're perfectly protected\n"
                    "and now it's your time to strike.")
        print_pause("You slash Diablos for a total of nine times\n"
                    "and then go in for a final stab.")
        Diablos_health(-200, inventory)
        print_pause("Diablos falls. And with the amulet you seal his soul\n"
                    "forever so he can no longer do harm to our world.")
        print_pause("You fall to the ground and for the first time\n"
                    "in a while you smile and laugh.")
        print_pause("Congratulations you have won!\n"
                    "As you look into the sky you see all the spirits\n"
                    "held captive float away.")
        print_pause("You put all your energy into your last attack\n"
                    "so you're just trying to catch your breath.")
        print_pause("You smile knowing that you finally brought peace\n"
                    "to Earth for good.")
        print_pause("And so the last Knight's tale has ended.")
        print_pause("Congratulations and thank you for playing!")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
        print_pause("You have completed Ending 4 of 4, the perfect ending.")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
        play_again(inventory)
    elif "fixed sword" in inventory:
        print_pause("After what feels like forever you're free from\n"
                    "the time compression.")
        print_pause("You look down at your hands and you're the same age,\n"
                    "however the world around you is in ruins.")
        print_pause("Little do you know it's fifty years after you\n"
                    "originally went inside the North Forest.\n"
                    "The few left on Earth are on their last leg.")
        print_pause("But you can't focus on that, you need to foucs\n"
                    "on what's left of the future.")
        print_pause("All around you is ash falling from the sky,\n"
                    "the ground completely shattered storms everwhere.\n"
                    "Barely any sign of life.")
        print_pause("You feel a strong prescence flying towards you\n"
                    "and you know it's Diablos.")
        print_pause("He destroys earth from a mile away and the debris\n"
                    "are flying towards you.")
        print_pause("You try to block with your wooden shield,\n"
                    "and it breaks apart.")
        health_change(-3, inventory)
        print_pause("After getting hit and rolling several times\n"
                    "Diablos flys over you.")
        print_pause("You know this is for every thing so you go in\n"
                    "with a special attack.")
        risk(inventory)
        print_pause("After your attempt he starts shooting fire balls\n"
                    "from his mouth.")
        print_pause("You run back and forth to dodge and see an opening\n"
                    "for another attack.")
        risk(inventory)
        health_change(-1, inventory)
        print_pause("Diablos starts charging up an ultimate attack\n"
                    "so you go to slash him.")
        Diablos_health(-100, inventory)
        print_pause("As you attack him your sword splits in half\n"
                    "and he comes towards you full charge.")
        print_pause("All you have now is basically a dull dagger,\n"
                    "but you figure it's now or never.")
        print_pause("You use up your remaining energy to stab directly\n"
                    "into him with all your might.")
        health_change(-20, inventory)
        Diablos_health(-200, inventory)
        print_pause("You both fall at the same time.\n"
                    "You're barely holding on, but"
                    "he's done for good.")
        print_pause("With your last ounce of strength you lift up the amulet\n"
                    "and Diablos is sealed inside.")
        print_pause("Your vision fades as you smile.\n")
        print_pause("You did your best, and though you have fallen as well,\n"
                    "the Earth is safe.")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
        print_pause("Congratulations you have completed Ending 3 of 4.")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
    else:
        print_pause("After what feels like forever you're free\n"
                    "from the time compression.")
        print_pause("You look down at your hands and you're the same age,\n"
                    "however the world around you is in ruins.")
        print_pause("Little do you know it's fifty years after\n"
                    "you originally went inside the North Forest.\n"
                    "The few left on Earth are on their last leg.")
        print_pause("But you can't focus on that, you need to foucs\n"
                    "on what's left of the future.")
        print_pause("All around you is ash falling from the sky,\n"
                    "the ground completely shattered storms everwhere.\n"
                    "Barely any sign of life.")
        print_pause("You feel a strong prescence flying towards you\n"
                    "and you know it's Diablos.")
        print_pause("He destroys earth from a mile away\n"
                    "and the debris are flying towards you.")
        print_pause("You try to block with your wooden shield,\n"
                    "and it breaks apart.")
        health_change(-3, inventory)
        print_pause("After getting hit and rolling several times\n"
                    "Diablos flys over you.")
        print_pause("You're starting to feel that you're under prepared\n"
                    "with just your rusty sword.")
        print_pause("He towers over you and as he goes in to grab you,\n"
                    "you go to swing.")
        risk(inventory)
        print_pause("Your rusty sword shatters on impact.\n"
                    "It looks like all is lost.")
        print_pause("As though the Gods heard your prayers,\n"
                    "a bolt of lightning strikes Diablos.")
        Diablos_health(-100, inventory)
        print_pause("You run back and forth without\n"
                    "a weapon dodging each attack, but you feel that\n"
                    "he is just playing with you.")
        print_pause("You grow rapidly tired and his strength remains.")
        print_pause("He grabs you off the ground\n"
                    "and throws you against a cliff.")
        print_pause("The amulet shatters and along\n"
                    "with that the only hope for Earth.")
        print_pause("The last Knight falls this day,\n"
                    "but do not give up hope as,\n"
                    "in the future a knight may be reincarnated.")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
        print_pause("Congratulations you have completed Ending 2 of 4.")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
        play_again(inventory)

# function for a "bad" ending if player decided to rush straight
# to end of game without getting any items or exploring first
def fake_intro(inventory):
    if "amulet" in inventory:
        print_pause("Today starts like any other day\n"
                    "The world has been at peace forever.")
        print_pause("You spend your days with your mother and father\n"
                    "selling coal to neighboring towns.")
        print_pause("You hear the windmills turning slowly\n"
                    "as the wind sweeps across the country side.")
        print_pause("It's the perfect day, for your perfect life.")
        print_pause("But, something doesn't feel right.\n\n")
        print_pause("You feel extremely uneasy\n"
                    "like you're forgetting something.")
        print_pause("You look around your room\n"
                    "and see pictures of your whole family together.\n"
                    "That can't be right, can it?\n\n")
        print_pause("....le....t....am...u...\n\n")
        print_pause("There's something you need, you're forgetting something.")
        print_pause("You look in your inventory.")
        print_pause(inventory)
        print_pause("How do I have these items? It has to be something here.")
        print_pause("Everything around you is becoming distorted.\n"
                    "like the whole world is caving in.")
        look_at = input("What item is of importance?\n").lower()
        if "amulet" in look_at:
            print_pause("Yes the amulet I feel it. It's important, but why?")
            print_pause("Everything starts to shatter around you,\n"
                        "including the world itself")
            print_pause("You hear a voice call out your name")
            print_pause("You start falling through nothingness")
            print_pause(". . . . . . . . . . . . . . . . . . . . . . . .")
            print_pause(". . . . . . . . . . . . . . . . . . . . . . . .")
            print_pause("Again that voice, who are you?")
            print_pause(". . . . I'm you . . . . ")
            print_pause("You're me? How?")
            print_pause(". . . By the time we made it to the North Forest...")
            print_pause(". . The Master Demon, Diablos was already awake . .")
            print_pause(". . He began corrupting every soul on the planet . .")
            print_pause(". . . .He trapped us in this time compression. . . .")
            print_pause(" . . . . .We're not here or there or anywhere\n"
                        "in time and space. We just are now. . . . .")
            print_pause(". . . .You see long ago humans summoned Diablos\n"
                        "for their bidding. To fight against other humans. . ")
            print_pause("What can I do, I can't do anything!")
            print_pause(". .The amulet you hold is imbued\n"
                        "with a sealing magic. . ")
            print_pause(". . . You can use it to seal Diablos\n"
                        "once and for all once you weaken him. . . . \n"
                        "I'll give you the remainder of my energy. .")
            print_pause(". .This will allow you to break free\n"
                        "of the compression . .")
            print_pause(". . . However you'll be many years in the future\n"
                        ". . . .I'm sorry I can't do better. . .")
            print_pause(". . . This will affect your life force as well . . ")
            print_pause(". . .Goodbye . . .")
            inventory.remove("a lie")
            inventory.append("hope")
            walk_toward(inventory)
        else:
            print_pause("No it can't be that... what item can it be...")
            fake_intro(inventory)

    else:
        print_pause("Today starts like any other day.\n"
                    "The world has been at peace forever.")
        print_pause("You spend your days with your mother and\n"
                    "father selling coal to neighboring towns.")
        print_pause("You hear the windmills turning slowly\n"
                    "as the wind sweeps across the country side.")
        print_pause("It's the perfect day, for your perfect life.")
        print_pause("But, something doesn't feel right.\n\n")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
        print_pause("You have completed Ending 1 of 4.")
        print_pause(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
        play_again(inventory)

# function that asks players if they would like to play again.
# Also resets global variables.
def play_again(inventory):
    play_again = input("Do you wish to play again?\n").lower()
    if "yes" in play_again:
        global health
        global gold
        global Diablos
        print_pause("Restarting game . . . . .\n")
        Diablos = 300
        health = 25
        gold = 0
        play_game()
    elif "no" in play_again:
        print_pause("I hope you had fun and can't wait to see you next time!\n"
                    "Goodbye!")
        exit()
    else:
        print_pause("Sorry I do not understand, but we'll restart for you.")
        play_game(inventory)

# function for player to choose what direction to walk toward
# in the story, also has secret areas if player has a special item
def walk_toward(inventory):
    print_pause("What direction would you like to travel to?\n")
    if "knight's key" in inventory:
        direction = input("North Forest\n"
                          "East Snake Cave\n"
                          "West Battlefield\n"
                          "South Mountain Village\n"
                          "???\n").lower()
        if "north" in direction:
            north_forest(inventory)
        elif "east" in direction:
            snake_cave(inventory)
        elif "west" in direction:
            battlefield(inventory)
        elif "south" in direction:
            mountain_village(inventory)
        elif "???" in direction:
            northeast_house(inventory)
        else:
            print_pause("You stand there confused.\n")
            walk_toward(inventory)
    elif "a lie" in inventory:
        direction = input("Home\n"
                          "Home\n"
                          "Home\n"
                          "home\n")
        if "home" in direction:
            fake_intro(inventory)
        else:
            print_pause("You are not allowed to do that.")
            walk_toward(inventory)
    elif "hope" in inventory:
        direction = input("The End\n").lower()
        if "end" in direction:
            The_End(inventory)
        else:
            The_End(inventory)
    else:

        direction = input("North Forest\n"
                          "East Snake Cave\n"
                          "West Battlefield\n"
                          "South Mountain Village\n").lower()
        if "north" in direction:
            north_forest(inventory)
        elif "east" in direction:
            snake_cave(inventory)
        elif "west" in direction:
            battlefield(inventory)
        elif "south" in direction:
            mountain_village(inventory)
        else:
            print_pause("You stand there confused.\n")
            walk_toward(inventory)

# function for a shop at one of the places that the player can visit.
# Can tell how much gold player has and what they can buy
def shop(inventory):
    global gold
    shop = input("Do you wish to visit the village shop?\n").lower()
    if "yes" in shop:
        if "flute" in inventory:
            print_pause("Welcome to our shop!\n")
            print_pause("We're selling health potions for five gold\n"
                        "and a special for the day is a phoenix down which\n"
                        "revives you from the brink of death for 40 gold!\n")
            buy = input("Would you like to buy anything today?\n")
            if "yes" in buy:
                print_pause("What would you like to buy today?\n")
                purchase = input("A health potion for five gold\n"
                                 "or phoenix down for forty?\n")
                if "potion" in purchase:
                    if gold in range(5, 1000):
                        print_pause("You have enough gold to buy a potion!\n")
                        gold -= 5
                        print_pause(f"You now have {gold} gold.\n")
                        print_pause("You leave the shop with your\n"
                                    "purchase and head back home.\n")
                        inventory.append("potion")
                    else:
                        print_pause("Sorry you do not have enough gold.\n"
                                    f"You have {gold} gold.")
                        print_pause("Please come again soon!")
                        print_pause("You leave the shop empty handed,\n"
                                    "if only someone could pay you for work.\n"
                                    "You know your way around a forge.")

                elif "down" in purchase:
                    if gold in range(40, 1000):
                        print_pause("You have enough gold to"
                                    "buy a phoenix down!\n")
                        gold -= 40
                        print_pause(f"You now have {gold} gold.\n")
                        print_pause("You leave the shop with your purchase\n"
                                    "and head back home.\n")
                        inventory.append("phoenix down")
                    else:
                        print_pause("Sorry you do not have enough gold\n"
                                    "to make a purchase\n")
                        print_pause(f"You have {gold} gold.")
                        print_pause("Please come again soon!")
                        print_pause("You leave the shop empty handed,\n"
                                    "if only someone could pay you for work.\n"
                                    "You know your way around a forge.")
                else:
                    print_pause("Sorry I do not understand,\n"
                                "we only have these two items.")
                    print_pause("You head back home disappointed.")
            elif "no" in buy:
                print_pause("Please come again!\n")
                print_pause("You leave the shop and hike down\n"
                            "the mountain back home.\n")

            else:
                print_pause("Sorry I do not understand is that a yes\n"
                            "or a no? Maybe come back when\n"
                            "you're feeling a little better.")
                print_pause("He's right you're feeling a bit off.\n"
                            "You go back home to rest.")
        else:
            print_pause("Welcome to our shop!\n")
            print_pause("We're selling health potions for five gold\n"
                        "and a special for the day is a special flute which\n"
                        "is said to be able to change the weather\n"
                        "only for forty gold!\n")
            buy = input("Would you like to buy anything today?\n")
            if "yes" in buy:
                print_pause("What would you like to buy today?\n")
                purchase = input("A health potion for five gold\n"
                                 "or flute for forty?\n")
                if "potion" in purchase:
                    if gold in range(5, 1000):
                        print_pause("You have enough gold to buy a potion!\n")
                        gold -= 5
                        print_pause(f"You now have {gold} gold.\n")
                        print_pause("You leave the shop with your purchase\n"
                                    "and head back home.\n")
                        inventory.append("potion")
                    else:
                        print_pause("Sorry you do not have enough gold.\n"
                                    f"You have {gold} gold.")
                        print_pause("Please come again soon!")
                        print_pause("You leave the shop empty handed.\n"
                                    "If only someone\n"
                                    "could pay you for work.\n"
                                    "You know your way around a forge.")

                elif "flute" in purchase:
                    if gold in range(40, 1000):
                        print_pause("You have enough gold to buy a flute!\n")
                        gold -= 40
                        print_pause(f"You now have {gold} gold.\n")
                        print_pause("You leave the shop with your purchase\n"
                                    "and head back home.\n")
                        inventory.append("flute")
                    else:
                        print_pause("Sorry you do not have enough gold\n"
                                    "to make a purchase\n")
                        print_pause(f"You have {gold} gold.")
                        print_pause("Please come again soon!")
                        print_pause("You leave the shop empty handed.\n"
                                    "If only someone\n"
                                    "could pay you for work.\n"
                                    "You know your way around a forge.")
                else:
                    print_pause("Sorry I do not understand,\n"
                                "we only have these two items.")
                    print_pause("You head back home disappointed.")
            elif "no" in buy:
                print_pause("Please come again!\n")
                print_pause("You leave the shop and\n"
                            "hike down the mountain back home.\n")
                walk_toward(inventory)
            else:
                print_pause("Sorry I do not understand is that a yes\n"
                            "or a no? Maybe come back\n"
                            "when you're feeling a little better.")
                print_pause("He's right you're feeling a bit off.\n"
                            "You go back home to rest.")
    elif "no" in shop:
        print_pause("You decide to not stop by the shop\n"
                    "and instead continue dancing at the festival until\n"
                    "the sun goes down and then head home.\n")

    else:
        print_pause("You stand there confused,\n"
                    "your mind lost in the thought of a shop.\n")
        mountain_village(inventory)

# function for a secret boss that player needs an item to reach. 
# Dialogue changes depending on what weapon player has
def secret_boss(inventory):
    global health
    print_pause("The knight as a faint glow around him \n"
                "with the fog like substance flowing off of him.\n"
                "He starts to talk.")
    print_pause("His voice sounding like it's coming from all directions.")
    print_pause("He told me of the old war between knights and demons.")
    print_pause("The knights failed to fully seal the master demon,\n"
                "he was only temporarily sealed and\n"
                "could still terrorized the land.")
    print_pause("He uses the souls of those on the Planet\n"
                "as his strength and until\n"
                "he is sealed fully those souls captured cannot move on.\n")
    print_pause("He arms himself with sword in hand and\n"
                "gives me one last chance to\n"
                "heal before he strikes.\n")
    health_change(0, inventory)
    print_pause("He lunges right at you and completely stabs your\n"
                "wooden shield, destroying it.")
    inventory.remove("wooden shield")
    print_pause("You fall right back on the ground,\n"
                "gasping for air trying to keep calm.")
    if "fixed sword" in inventory:
        print_pause("You get right back up on your feet\n"
                    "and block each blow with your sword.")
        print_pause("The Snake smith did a perfect job in fixing\n"
                    "your sword and you keep your footing.")
        print_pause("He flips the sword in a surprise attack\n"
                    "and hits you with the bottom of the hilt.")
        health_change(-5, inventory)
        print_pause("You rub your new bruise and attack back with a flurry")
        print_pause("He parries one of your attacks and cuts your arm.")
        health_change(-5, inventory)
        print_pause("Luckily, not a serious scratch,\n"
                    "you attack him once more overhead\n"
                    "and then he yells to stop, you have passed the test.")
        print_pause("As he fades away he says that you and points northeast.")
        print_pause("A key falls from where he once stood.\n"
                    "Maybe I should investigate this\n"
                    "and find where this key goes to.")

        inventory.append("knight's key")
    else:
        print_pause("You get right back up on your feet\n"
                    "and struggle to block each blow with your sword.")
        print_pause("Your rusty sword is barely staying together,\n"
                    "chipping with each hit.")
        print_pause("He flips the sword in a surprise attack\n"
                    "and hits you with the bottom of the hilt.")
        health_change(-10, inventory)
        print_pause("You rub your new bruise and attack back with a flurry")
        print_pause("He parries one of your attacks and cuts your arm.")
        health_change(-10, inventory)
        print_pause("Not a fatal cut, but still you're on your last leg.\n"
                    "You attempt to strike again\n"
                    "and then he yells to stop, you have passed the test.")
        print_pause("As he fades away he says that you and points northeast.")
        print_pause("A key falls from where he once stood.\n"
                    "Maybe I should investigate this\n"
                    "and find where this key goes to.")
        print_pause("Feeling faint from the blood\n"
                    "loss you fall to the ground.")
        print_pause(".  .  .  .  .   .  .  .  .  .")
        print_pause("You wake up at home in your bed.")
        inventory.append("knight's key")

# function that was meant to be a riddle, but broke and was repurpose 
# to be a "jump scare" for the player during a "bad" ending
def riddle_game(inventory):
    s = "You're Stuck Here Forever."
    index = len(s)
    while index > 0:
        time.sleep(0)
        index -= 1
        print(s[:index])

# function for if the player walks north. Dialogue changes depending
# on what items the players had
def north_forest(inventory):
    global health
    print_pause("You step into the forest.\n"
                "You've always heard stories that spirits haunt this place.")
    print_pause("This forest seems very strange, but familiar in a way.")
    print_pause("Every step you take echoes,\n"
                "and it feels like you've been walking forever.\n"
                "You look back and you've gotten nowhere.")
    print_pause("What feels like seconds, turns into minutes,\n"
                "which turns into hours, then days.")
    print_pause("You've gone forward, back, left, right,\n"
                "it feels like the only thing you haven't\n"
                "tried is to move up or down.\n"
                "Everything is just starting to look the same.")
    while True:
        walk = input("Which direction do you want to go?\n"
                     "Right?\n"
                     "Left?\n"
                     "Forward?\n"
                     "Back?\n").lower()
        if walk == "up":
            print_pause("As soon as you look in that direction\n"
                        "the whole world shifts and\n"
                        "you fall towards the sky.")
            print_pause("You close your eyes in fear and open them and\n"
                        "you're back at the end of the North Forest.")
            print_pause("You move forward past the trees\n"
                        "to where there is a clearing.")
            break
        else:
            print_pause("You're not going anywhere.\n"
                        "You're stuck in the forest forever.\n"
                        "You hear a whisper to look towards the sky.")
    print_pause("You hear a ringing of bells and laughter of children,\n"
                "but there's no one here.")
    while True:
        game = input("Do you want to play a game?\n"
                     "yes\n"
                     "yes\n"
                     "yes\n"
                     "yes\n").lower()
        if game == "yes":
            print_pause("Ok let's play a game!")
            print_pause("Here's a riddle!")
            riddle_game(inventory)
            inventory.append("a lie")
            break
        else:
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("You have no choice.")
            print_pause("Ok let's play a game!")
            print_pause("Here's a riddle!")
            riddle_game(inventory)
            inventory.append("a lie")
            break
    walk_toward(inventory)

# function for if player goes east and dialogue changes depending on 
# how many visits and what they chose to do in the cave prior. 
# Can also unlock a job function if the player brings the snake food
def snake_cave(inventory):
    global gold
    global health
    print_pause("You've been warned many times to never enter this cave\n"
                "as a giant snake lives here.")
    print_pause("You can hear water droplets falling from the\n"
                "stalactites and a faint crackle from a fire glowing\n"
                "in the back of the cave.")
    if "amulet" in inventory:
        if "fixed sword" in inventory:
            if "turkey leg" in inventory:
                print_pause("Welcomessss back to my cave. Oh I sssseee\n"
                            "you've brought me a turkey leg to eat!\n")
                inventory.remove("turkey leg")
                inventory.append("turkey bone")
                print_pause("The snake eats the turkey leg nearly in one\n"
                            "gulp and then turns back to me")
                print_pause("You know I've been looking for someone\n"
                            "to help me sssssmith.")
                print_pause("If you help me I'll be ssssure to pay\n"
                            "you handsomely.")
                smith = input("Do you want to work at the forge, you'll\n"
                              "make ten gold and lost 10 health.\n").lower()

                if "yes" in smith:
                    print_pause("You try your hand smithing weapons\n"
                                "for the snake.")
                    print_pause("You're actually a lot better at this\n"
                                "than you thought.")
                    print_pause("The snake thanks you for your services\n"
                                "and pays you as promised.")
                    health_change(-10, inventory)
                    grab_gold(10)
                elif "no" in smith:
                    print_pause("That'sssss okay. I'll be here if\n"
                                "you want to work.")
                else:
                    print_pause("Ssssorry I don't understand.\n"
                                "Go take a resssst and come back.")
            elif "turkey bone" in inventory:
                print_pause("Welcome back to my home.\n"
                            "Would you likesss to work the forge?")
                health_change(0, inventory)
                smith = input("Do you want to work at the forge,\n"
                              "you'll make ten gold\n"
                              "and lost 10 health.\n").lower()
                if "yes" in smith:
                    print_pause("You try your hand smithing weapons\n"
                                "for the snake.")
                    print_pause("You're actually a lot better at this\n"
                                "than you thought.")
                    print_pause("The snake thanks you for your services\n"
                                "and pays you as promised.")
                    health_change(-10, inventory)
                    grab_gold(10)
                elif "no" in smith:
                    print_pause("That'sssss okay. I'll be here\n"
                                "if you want to work.")
                else:
                    print_pause("Ssssorry I don't understand.\n"
                                "Go take a resssst and come back.")
            else:
                print_pause("Ahhh you're back.\n"
                            "I'm notssss in the mood to talk")
                print_pause("Maybe... if you can bring me some food...")
                print_pause("You leave the cave wondering\n"
                            "where you can get some food.")
        else:
            print_pause("The snake's corpse is still here.")
            print_pause("Maybe I could've tried to see\n"
                        "if there was another way than killing him.")
            print_pause("Your footsteps echo throughout\n"
                        "the cave as you walk away.")
    else:
        print_pause("You walk towards the fire and no one is there.")
        print_pause("Confused you start walking away and\n"
                    "from the corner of your eye you see a giant\n"
                    "blur wrap around behind you.")
        print_pause("The colossal snake stood 30 feet tall and\n"
                    "on it's tail was a giant hammer.\n")
        print_pause("The snake slides it's face right up to you\n"
                    "it's tongue just centimeters away.\n"
                    "Is he friend or foe? You start to panic.")
        print_pause("Do you choose to protect yourself and attack the snake?")
        print_pause("Or stay calm and not do anything rash?")
        snake = input("Stay calm? or Attack?\n").lower()
        if "calm" in snake:
            print_pause("The snake's tongue hits your face and it rears back!")
            print_pause("It opens it's mouth wide and comes right at you!\n"
                        "You close your eyes ready for the end!")
            print_pause("Achooooo!!")
            print_pause("Confused you open your eyes\n"
                        "and the snake is just looking at you.")
            print_pause("What? You thought I wasssss going to eat you?\n"
                        "The snake laughs")
            print_pause("I don't have many visitorsssss since the war.")
            print_pause("I actually forge weaponssss here and for five gold\n"
                        "I'll fix your rusty ssssword\n"
                        "so it'll be like brand new.")
            print_pause("I'll even throw in this random amulet I found.\n"
                        "Maybe it'll be of some usssseee")
            if gold in range(5, 1000):
                print_pause("You have enough gold to fix your\n"
                            "sword and get that amulet\n")
                gold -= 5
                print_pause(f"You now have {gold} gold.\n")
                print_pause("You watch the snake use his tail\n"
                            "as a hammer to reforge your father's old sword.")
                print_pause("With each hit you see embers flying off\n"
                            "and the blade sharpening.")
                print("Sssseee brand new! And here's the amulet too.")
                inventory.remove("old sword")
                inventory.append("fixed sword")
                inventory.append("amulet")
                print_pause("The snake hands me both the amulet and sword.")
                print_pause("Ssseee you later alligator.\n"
                            "If you find food bring it to me too.")
            else:
                print_pause("Sssssorry you do not have enough gold.\n"
                            f"You have {gold} gold.")
                print_pause("Let'ssss work out a deal.\n"
                            "You work and I'll give you the items")
                print_pause("You agree to do so because that's a steal,\n"
                            "only at the cost of five health.")
                print_pause("You help around the forge \n"
                            "and when you're done the snake\n"
                            "gives you your fixed sword and amulet.")
                print_pause("Can't wait to sssseee you again,\n"
                            "bring some food next time!")
                inventory.remove("old sword")
                inventory.append("fixed sword")
                inventory.append("amulet")
                health_change(-5, inventory)

        elif "attack" in snake:
            print_pause("You unsheathe your sword as the snake rears back.")
            print_pause("You close your eyes and just stab forward and upward")
            print_pause("You hear a scream and you're in pain, you open your\n"
                        "eyes and the snake is on the ground dead\n"
                        "with your blade through it.")
            print_pause("Your arm has one of it's fangs through it.\n"
                        "You yelp in pain now that the adrenaline is wearing\n"
                        "off. You yank the fang out.")
            health_change(-15, inventory)
            print_pause("You search around the cave\n"
                        "and find one hundred gold and some old amulet.")
            grab_gold(100)
            inventory.append("amulet")
            print_pause("You wonder if this could have ended differently.")
            print_pause("You leave the cave.")
        else:
            print_pause("You're too stunned to think. You faint and pass out.")
            print_pause("You wake up in your home.")
    walk_toward(inventory)

# function for if player goes west, player either needs item flute to unlock
# or they could play a game of chance to dodge the lightning
def battlefield(inventory):
    global health
    print_pause("You walk along the charred path toward an old battlefield\n"
                "that was a part of the war.")
    print_pause("The sky is almost pitch black from the clouds and lightning\n"
                "is striking everywhere ahead.")
    print_pause("Fog covers the land and more and more you feel like\n"
                "you're beeing watched by an unknown force as the lightning\n"
                "strikes by your feet.")
    if "flute" in inventory:
        print_pause("You remember you bought a flute from the\n"
                    "mountain village that was said  to be able to change\n"
                    "the weather when played.")
        print_pause("You don't know if the story is real, but you take out\n"
                    "the flute and play an old tune\n"
                    "that your mom used to play.")
        print_pause("Lightning strikes around you rapidly as you play\n"
                    "and as the last note fades, so do the storm clouds.")
        print_pause("Though the atmostphere has not changed and the\n"
                    "fog thickens as you continue forward and the whispers\n"
                    "continue until you reach the battlefield.\n")
        print_pause("It goes dead silent.\n\n")
        print_pause("You feel like you hear people yelling from beyond.")
        print_pause("You see skeletons in armor every where you look,\n"
                    "however this battle does not look like it was a fight\n"
                    "among men.")
        print_pause("The land is still charred and scarred from the war\n"
                    "and you start hearing voices around you.")
        print_pause("What you thought was fog starts rapidly collecting\n"
                    "into one area.")
        print_pause("Stunned you fall back and drop your sword and\n"
                    "look up and see a spirit of a knight staring\n"
                    "right at you.\n")
        secret_boss(inventory)
    else:
        print_pause("As you move more forward the fog thickens and\n"
                    "lightning strikes are coming more often\n"
                    "and you feel like the lightning is targeting you.\n")
        lightning = input("Do you dare keep moving forward with the chance\n"
                          "of getting past or go back safely??\n").lower()
        if "yes" in lightning:
            print_pause("You decide to take your chances at\n"
                        "avoiding the lightning,hopefully a huge risk,\n"
                        "brings great reward.")
            x = random.randint(0, 15)
            if x == 7:
                print_pause("You narrowly dodge the lightning one by one\n"
                            "all the way to the battlefield.")
                print_pause("Past the lightning the atmostphere has not\n"
                            "changed and the fog thickens as you continue\n"
                            "forward. The whispers continue until you reach\n"
                            "the battlefield.\n")
                print_pause("It goes dead silent.\n\n")
                print_pause("You feel like you hear people yelling from\n"
                            "beyond.")
                print_pause("You see skeletons in armor everywhere you look,\n"
                            "however this battle does not look like it was\n"
                            "a fight among men.")
                print_pause("The land is still charred and scarred from\n"
                            "the war and you start hearing voices around you.")
                print_pause("What you thought was fog starts rapidly\n"
                            "collecting into one area.")
                print_pause("Stunned you fall back and drop your sword\n"
                            "and look up and see a spirit of a knight\n"
                            "staring right at you.\n")
                secret_boss(inventory)
            else:
                print_pause("You feel a zap of lightning\n"
                            "go straight through you!")
                print_pause("You lose two health,\n"
                            "but you get out safely so you can rest.")
                health_change(-2, inventory)
                print_pause("Do you dare go back? You feel as though there's\n"
                            "an item that can help you.\n")
                walk_toward(inventory)
        elif "no" in lightning:
            print_pause("You decide to not even risk it. You leave safely.")
            print_pause("You feel as though there's an item that can\n"
                        "help you.\n")
            walk_toward(inventory)
        else:
            print_pause("The weather is affecting your brain.\n"
                        "You head home.\n")
            walk_toward(inventory)
    walk_toward(inventory)

# function for if player goes south. Gives player special item upon visit
# player can also decide to shop for items while at the village
def mountain_village(inventory):
    if "candy apple" in inventory:
        print_pause("You hike up the mountain to the nearby village again\n"
                    "and see that the festival is still ongoing.\n")
        shop(inventory)
        walk_toward(inventory)
    else:
        print_pause("You hike up the mountain to a nearby village\n"
                    "and you see a huge crowd in the village\n"
                    "and people dancing and playing instruments.")
        print_pause("You go up to a person nearby and learn that it's the\n"
                    "Summer Solstice Festival.\n")
        print_pause("You join in on the festivities and have a lot of fun.\n")
        print_pause("As you're going through the festival you buy a\n"
                    "candy appple and turkey leg at one of the food stalls.\n")
        inventory.append("candy apple")
        inventory.append("turkey leg")
        print_pause("As you're leaving the bazaar you pass by the bazaar\n"
                    "and spot a little shop that may have something useful\n"
                    "for you to buy.")
        shop(inventory)
    walk_toward(inventory)

# function for secret area that is unlocked after beating the secret boss
# gives the best weapon and armor in the game
def northeast_house(inventory):
    print_pause("You follow where the spirit pointed to and found this\n"
                "abandoned house out in the countryside\n")
    print_pause("It looks like it has not been lived in for almost\n"
                "a hundred years.\n")
    print_pause("It is completely covered with greenery and vines.\n")
    print_pause("And the roof and walls are falling apart.\n")
    print_pause("You carefully go inside the house and inside is a trapdoor\n"
                "leading to the basement.")
    print_pause("You remember the spirit dropped a key so you try it.\n")
    inventory.remove("knight's key")
    print_pause("After a few moments you finally unlock the trapdoor\n"
                "and go down into the basement.")
    print_pause("You hear the creaks of the house with each step you take\n"
                "until you're at the bottom.")
    print_pause("Through the floorboards the sun peaks through.\n"
                "Through the bits of light you see in the basement\n"
                "a sword glistening in the light held upright by a\n"
                "skeleton in armor.\n")
    print_pause("You assume it's the body of the spirit of the knight\n"
                "you previously battled and that\n"
                "this is what he wanted you to see.")
    print_pause("You grab the knight's sword and his shield.\n"
                "A sudden burst of energy pours into you.\n")
    print_pause("You have obtained Sword of the Round Table,\n"
                "an ultimate weapon forged by the spirits of all knights\n"
                "and it's pairing shield Shield of the Round Table,\n"
                "the greatest defense in the land.")
    print_pause("Along with a healing potion\n"
                "for your difficult fight ahead.\n")
    inventory.append("secret sword")
    inventory.append("secret shield")
    inventory.append("potion")
    health_change(15, inventory)
    print_pause("With your new gear you leave to never return to this\n"
                "abandoned house,hoping you can free the knight's spirit\n"
                "so he can be at peace.\n")
    walk_toward(inventory)

# function to play game
def play_game():
    inventory = []
    intro(inventory)
    walk_toward(inventory)


play_game()
