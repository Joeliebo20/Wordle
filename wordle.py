import random
from valid_words import valid_words
from collections import Counter, OrderedDict
import enchant
import pandas as pd


class OrderedCounter(Counter, OrderedDict): pass


end_df = pd.DataFrame(columns=['Name', 'Score'])
end_df.style.set_caption('Scoreboard')


def addToDF(data):
    global end_df
    end_df = end_df.append(data, ignore_index=True)


def game():
    length = len(valid_words)
    index = random.randint(0, length)
    word = valid_words[index]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    win = False
    guess0, guess1, guess2, guess3, guess4 = '0', '0', '0', '0', '0'

    print("Welcome to Wordle!")
    print("Rules: ")
    print("You will have 6 guesses to guess a 5 letter word.")
    print("If you get the letter in the correct spot, it will appear in that spot")
    print("If you get the letter in the wrong spot but it's in the word, it will appear as a '1'")
    print("Keep in my mind that there always may be two or more instances of a letter! Ex: fever")
    print("Enjoy the game!")
    print("________________________________________________________________________")
    print()

    while True:
        guess = input("Enter a guess: ")
        guess = guess.lower()
        if len(guess) >= 6 or len(guess) <= 4:
            print("Guess must be 5 letters, try again!")
            continue
        d = enchant.Dict("en_US")
        true_word = d.check(guess)
        if not true_word:
            print("This is not an english word, try again!")
            continue
        count += 1
        if guess == word and count <= 6:
            print(f"The word was {word}, you got it in {count} tries!")
            name = input("Please enter your name: ")
            data = {'Name': name, 'Score': str(count) + "/6"}
            addToDF(data)
            win = True
            want_more = input("Do you want to keep playing?: type 'y' for yes and 'n' for no: ")
            if want_more == 'y':
                game()
            else:
                print(end_df.head())
                exit()
        if count >= 6 and win is not True:
            print(f"You lose! The word was {word}")
            name = input("Please enter your name: ")
            data = {'Name': name, 'Score': 'X/6'}
            addToDF(data)
            want_more = input("Do you want to keep playing?: type 'y' for yes and 'n' for no: ")
            if want_more == 'y':
                game()
            else:
                print(end_df.head())
                exit()
        else:
            guess0, guess1, guess2, guess3, guess4 = '0', '0', '0', '0', '0'
            for i in range(5):
                if guess[0] in word:
                    if guess[0] in word[0]:
                        guess0 = guess[0]
                    else:
                        guess0 = '1'
                if guess[1] in word:
                    if guess[1] in word[1]:
                        guess1 = guess[1]
                    else:
                        guess1 = '1'
                if guess[2] in word:
                    if guess[2] in word[2]:
                        guess2 = guess[2]
                    else:
                        guess2 = '1'
                if guess[3] in word:
                    if guess[3] in word[3]:
                        guess3 = guess[3]
                    else:
                        guess3 = '1'
                if guess[4] in word:
                    if guess[4] in word[4]:
                        guess4 = guess[4]
                    else:
                        guess4 = '1'

        print(guess[0], guess[1], guess[2], guess[3], guess[4])
        print(guess0, guess1, guess2, guess3, guess4)
        guesses = [guess0, guess1, guess2, guess3, guess4]
        for i in range(5):
            try:
                if int(guesses[i]) <= 0:
                    letters.remove(guess[i])
            except:
                Exception(f"letter {guess[i]} already removed")
        print("Remaining letters are: ", letters)


def main():
    game()


main()
