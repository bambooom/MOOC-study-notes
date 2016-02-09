# MITx IntroCS Problem Set 3
#
# Hangman game
#



import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    letters_word = list(set(list(secretWord))) # split to letters and del duplicate
    for i in letters_word:
        if i in lettersGuessed:
            pass
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    letters_word = set(list(secretWord))
    list_word = list(secretWord)
    guessed_letter=set()
    for i in letters_word:
        if i in lettersGuessed:
            guessed_letter.add(i)
    noguess = list(letters_word - guessed_letter)
    for j in noguess:
        idx = list_word.index(j)
        list_word[idx] = "_ "
    guessed = "".join(list_word)
    return guessed


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lowercase = list(string.ascii_lowercase)
    left_letters = sorted(list(set(lowercase) - set(lettersGuessed)))
    return "".join(left_letters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secretWord = secretWord.lower()
    mistakesMade = 0
    totalguess = 8
    lettersGuessed = []
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long." % len(secretWord)

    while mistakesMade <= totalguess:
        print "--------------------"
        print "You have %d guesses left." %(totalguess - mistakesMade)
        print "Available letters:", getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter: ")

        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: ", getGuessedWord(
            secretWord, lettersGuessed)
        else:
            lettersGuessed.append(guess)
            if guess in list(secretWord):
                print "Good guess: ", getGuessedWord(secretWord, lettersGuessed)
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print "--------------------"
                    print "Congratulations, you won!"
                    break
            else:
                mistakesMade += 1
                print "Oops! That letter is not in my word:", getGuessedWord(
                secretWord, lettersGuessed)
                if mistakesMade == 8:
                    print "--------------------"
                    print "Sorry, you ran out of guesses. The word was %s." % secretWord
                    break


wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
