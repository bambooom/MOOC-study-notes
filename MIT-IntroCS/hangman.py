# MITx IntroCS Problem Set 3
# Hangman game

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
