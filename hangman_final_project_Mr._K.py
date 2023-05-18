import random

def board(a):
    if a == 0:
        print(" ______")
        print("|     |     ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|___________")

    elif a == 1:
        print(" ______")
        print("|     |     ")
        print("|    ( )    ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|___________")

    elif a == 2:
        print(" ______")
        print("|     |     ")
        print("|    ( )    ")
        print("|     |     ")
        print("|           ")
        print("|           ")
        print("|___________")

    elif a == 3:
        print(" ______")
        print("|     |     ")
        print("|    ( )    ")
        print("|    /|     ")
        print("|           ")
        print("|           ")
        print("|___________")

    elif a == 4:
        print(" ______")
        print("|     |     ")
        print("|    ( )    ")
        print("|    /|\    ")
        print("|           ")
        print("|           ")
        print("|___________")

    elif a == 5:
        print(" ______")
        print("|     |     ")
        print("|    ( )    ")
        print("|    /|\    ")
        print("|    /      ")
        print("|           ")
        print("|___________")

    elif a == 6:
        print(" ______")
        print("|     |     ")
        print("|    ( )    ")
        print("|    /|\    ")
        print("|    / \    ")
        print("|           ")
        print("|___________")
        print("You dead boy")


def getGuess(alreadyGuessed):
    while True:
        print(alreadyGuessed)
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz ':
            print('Please enter a LETTER.')
        else:
            alreadyGuessed.append(guess)
            return guess

def blankword(word, alreadyGuessed):
    guess = ""
    for k in word:
        if k in alreadyGuessed:
            guess = guess + k

        else:
            guess = guess + "0"
    return guess




def secret():
    b = ["alocodon", "sarmientosaurus", "ningyuansaurus", "marshosaurus", "lourinhanosaurus", "machairoceratops", "khetranisaurus", "lanzhousaurus", "nanshiungosaurus", "metriacanthosaurus", "narambuenatitan", "phuwiangosaurus", "ornithomimoides", "plateosauravus", "qianzhousaurus", "sigilmassasaurus", "zizhongosaurus", "talenkauen", "Sigilmassasaurus", "tsagantegia", "trigonosaurus", "torvosaurus", "zhejiangosaurus", "zizhongosaurus", "nodocephalosaurus", "yuanmousaurus", "xuanhanosaurus", "xianshanosaurus", "wulagasaurus", "vulcanodon", "unescoceratops", "thecodontosaurus", "suzhousaurus", "sarmientosaurus", "sinornithosaurus", "sefapanosaurus", "riabininohadros", "oryctodromeus", "quaesitosaurus", "pycnonemosaurus", "plateosauravus", "panamericansaurus", "ceratosaurus", "malarguesaurus", "lapparentosaurus" "datonglong", "gideonmantellia", "koutalisaurus" "jingshanosaurus", "incisivosaurus", "hierosaurus", "apple", "pear", "poop", "meat", "allosaurus", "ankylosaurus", "baryonyx", "brontosaurus", "dunkleosteus", "plesiosaur", "stegosaurus"]
    e = random.randrange(0, len(b))
    print(e)
    return b[e]

def check(word, c):
    for k in word:
        if k == c:
            return True
    return False

def winner(word, d):
    if word == d:
        return True
    else:
        return False

def trun():

    word = secret()

    alreadyGuessed = [" "]

    c = ""

    a = 0

    while a < 6:
        board(a)
        d = blankword(word, alreadyGuessed)
        print(d)
        c = getGuess(alreadyGuessed)
        d = blankword(word, alreadyGuessed)
        print(d)

        if(check(word, c) == False):
            a = a + 1
        if winner(word, d) == True:
            print("You win!")
            return 0
        board(a)
        if(a == 6):
            return 0
        

def main():
    trun()
    return 0

main()
