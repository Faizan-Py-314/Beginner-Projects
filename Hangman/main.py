import random

def print_pattren(pattren, word):
    if len(pattren) == 0:
        for _ in word:
            pattren.append("_")

    for char in pattren:
        print(char, end="")

def chack_char(word, guess_word, pattren, points):
    for i, char in enumerate(word):
        if char in guess_word:
            pattren[i] = char
            print("You chose correct character\n")
    if guess_word not in word:
        points -= 1
        print(f"You lose one point and {points} points is left\n")
    
    return points


def main():
    print("\n--------------------- Welcome To Hangman Game --------------------- ")

    words = ["python", "java", "javascript", "rust", "django", "react", "express", "agular"]
    points = 6

    word = random.choice(words)
    pattren_list = []

    print_pattren(pattren_list, word)
    while 0 < points and ("_" in pattren_list or len(pattren_list) == 0):
        guess_char = input("\nGuess the Character: ")

        if len(guess_char) == 1:
            points = chack_char(word, guess_char, pattren_list, points)
            print_pattren(pattren_list, word)
        else:
            print("You have permission to Enter only one or atleast one Character")
    
    if points == 0:
        print("\n\nYou lose This game")
    else:
        print("\n\nCongratulation You win This game!!!")

if __name__ == "__main__":
    main()
