import images


# finding index of chosen letter in title
# example 'a' in title 'Bajka o smoku' -> index: [1, 4]
def find_index(letter, title):
    letter_index_list = [i for i, char in enumerate(title) if char == letter]
    return letter_index_list


# looking for indexes of chosen letter in a title and then change '_' into chosen letter in a hiddentitle
def replace_hidden_title(letter, title, hidden_title):
    hidden_title = list(hidden_title)
    for i in find_index(letter, title):
        hidden_title[i] = title[i]
    hidden_title = ''.join(hidden_title)
    return hidden_title


# looking for a chosen letter in title or check guessing a whole title
# drawing an image of a hangman if chosen letter doesn't appear in title or chosen of a letter repeats itself
def guess_title_or_letter(letter, title, hidden_title, letters_set, trial):
    message = ""
    if letter == title:
        hidden_title = title
        message = "Gratulacje! Wygrałeś!"
        trial = 12
    elif letter in letters_set:
        letters_set = letters_set.replace(letter, '')
        if letter in title:
            hidden_title = replace_hidden_title(letter, title, hidden_title)
            if "_" not in hidden_title:
                message = "Gratulacje! Wygrałeś!"
                trial = 12
            else:
                message = ""
        else:
            trial += 1
            images.draw_image(trial)
            message = "Litera nie występuje w tytule filmu."
    elif letter not in letters_set:
        trial += 1
        images.draw_image(trial)
        message = "Litera została już użyta lub nie jest poprawnym znakiem."
    if trial == 0:
        message = ""
    if trial == 12 and message != "Gratulacje! Wygrałeś!":
        images.draw_image(trial)
        message = "Przegrałeś!"
    return title, hidden_title, letters_set, trial, message