import random_word

name = input("Enter your name: ")
print("All the best "+name)

# Return a single random word
word = random_word.RandomWords().get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=3, maxLength=6)
word = word.lower()
# print(word)

guesses = ""
turns = int(len(word)*2)    # Number of turns
# print(turns)
print("\nYou have "+ str(turns) +" guesses to guess the correct word")
print("\n_____ Let's Start _____")


while turns> 0 :
    failed = 0  # counts the number of times a user fails
    # all characters from the input word taking one at a time.
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            # for every failure I will be
            # incremented in failure
            failed += 1

    if failed == 0:
        print("\n\nCongratulations! You win!")
        print("The word is: "+word)
        break

    guess = input("\n\nGuess the character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        # if the character doesn't match the word
        # then "Wrong guess" will be given as output
        print("Wrong guess")
        # this will print the number of
        # turns left for the user
        print("\nYou have", +turns, "more guesses")
        if turns == 0:
            print("\nYou lose the game")
            print("The word is: " + word)

print("\nThanks for playing 🌝")
