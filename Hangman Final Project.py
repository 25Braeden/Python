#Zach Brotzman and John Wolfe
#Hangman Final Project
import random
def main(): #this creates the introduction
    welcome = ['Hi, This code was made by Zachy B and Johnny Boi. Have fun and start guessing']
    for line in welcome:
        print(line, sep='\n')
    play_again = True
    while play_again: #this creates the dictionary used to get the words from
        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo", "boomerang",'Adult' ,'Airplane' ,'Air','Aircraft' ,'Carrier','Airforce','Airport','Album','Alphabet','Apple','Arm','Army','Baby','Backpack','Balloon','Banana','Bank','Barbecue','Bathroom','Bathtub','Bed','Bee','Bible','Bird','Bomb','Book','Boss','Bottle','Bowl','Box','Boy','Brain','Bridge',
                 'Butterfly','Button','Cappuccino','Car','Carpet','Carrot','Cave','Chair','Chess','Chief','Child','Chisel','Chocolates','Church','Circle','Circus','Clock','Clown','Coffee','Comet','Compact','Compass','Computer','Crystal','Cup','Cycle','Data','Desk','Diamond','Dress','Drill','Drink','Drum','Dung','Ears','Earth','Egg','Electricity','Elephant','Eraser','Explosive',
                 'Eyes','Family','Fan','Feather','Festival','Film','Finger','Fire','Floodlight','Flower','Foot','Fork','Freeway','Fruit','Fungus','Game','Garden','Gas','Gate','Gemstone','Girl','Gloves','God','Grapes','Guitar','Hammer','Hat','Hieroglyph','Highway','Horoscope','Horse','Hose','Ice','Insect','Jet','Junk','Kaleidoscope','Kitchen','Knife','Leather','Leg','Library','Liquid',
                 'Magnet','Man','Map','Maze','Meat','Meteor','Microscope','Milk','Milkshake','Mist','Money','Monster','Mosquito','Mouth','Nail','Navy','Necklace','Needle','Onion','Paint','Pants','Parachute','Passport','Pebble','Pendulum','Pepper','Perfume','Pillow','Plane','Planet','Pocket','Post','Potato','Printer','Prison','Pyramid','Radar','Rainbow','Record','Restaurant',
                 'Rifle','Ring','Robot','Rock','Rocket','Roof','Room','Rope','Saddle','Salt','Sandpaper','Sandwich','Satellite','School','Ship','Shoes','Shop','Shower','Signature','Skeleton','Slave','Snail','Software','Solid','Space','Spectrum','Sphere','Spice','Spiral','Spoon','Sports','Spot','Square','Staircase','Star','Stomach','Sun','Sunglasses','Surveyor','Swimming','Sword',
                 'Table','Tapestry','Teeth','Telescope','Television','Tennis','Thermometer','Tiger','Toilet','Tongue','Torch','Torpedo','Train','Treadmill','Triangle','Tunnel','Typewriter','Umbrella','Vacuum','Vampire','Videotape','Vulture','Water','Weapon','Web','Wheelchair','Window','Woman',"Worm","X-ray"]
        chosen_word = random.choice(words).lower()
        playerGuess = None
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word: #createsd dashes for each number of letters in the word
            word_guessed.append("-")
        joined_word = None
        HANGMAN = ( #this creates the character that hangs from the gallows
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  | |
|
--------
""")
        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1
        while (attempts != 0 and "-" in word_guessed): #works for thw number of incorrect guesses and projects them in the box
            print(("\nYou have {} guesses left").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                playerGuess = str(input("\nChoose a letter" + "\n> ")).lower() #gives them the option to choose a letter to guess the word
            except:
                print("Not a valid guess")
                continue
            else:
                if not playerGuess.isalpha():
                    print("That is not a real letter, stupid")
                    continue
                elif len(playerGuess) > 1:
                    print("That is more than one letter, stupid")
                    continue
                elif playerGuess in guessed_letters:
                    print("You have already guessed that letter, stupid")
                    continue
                else:
                    pass
            guessed_letters.append(playerGuess)
            for letter in range(len(chosen_word)):
                if playerGuess == chosen_word[letter]:
                    word_guessed[letter] = playerGuess
            if playerGuess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])
        if "-" not in word_guessed:
            print(("\nCongratulations! {} was the word, you're a weeeeeeeeiner").format(chosen_word)) #if the word is right then this message is printed
        else:
            print(("\nStupid! The word was {}.").format(chosen_word))
        print("\nWould you like to play again?")
        response = input("> ").lower() #if the word is not right then these messages are printed
        if response not in ("yes", "y"):
            play_again = False
if __name__ == "__main__":
    main()