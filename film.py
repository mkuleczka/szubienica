import random
import string
import wiki_films

# letters which can appear in a title to guess
letters_set = ''.join([i for i in string.ascii_lowercase] + ['ąćęłńóśźż'])

# a title from the list of polish films
def draw_polish_film(film_list=wiki_films.get_list_polish_fairy_tails()):
    which_film = random.randint(0, len(film_list))
    film_title = film_list[which_film].lower()
    return film_title


# a title from the list of american films
def draw_american_film(film_list=wiki_films.get_list_american_fairy_tails()):
    which_film = random.randint(0, len(film_list))
    film_title = film_list[which_film].lower()
    return film_title

# a title from the lists of polish and american films
def draw_all_film(film_list=wiki_films.get_list_american_fairy_tails()+wiki_films.get_list_polish_fairy_tails()):
    which_film = random.randint(0, len(film_list))
    film_title = film_list[which_film].lower()
    return film_title


# change title to hidden_title
def change_into_hidden_title(title):
    hidden_title = ''.join([char if char in (string.punctuation + ' ') else '_' for char in title])
    return hidden_title