from flask import Flask, render_template, request, redirect, url_for
import json

import film
import guess_title
import images


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        with open('static/pl_title.json', 'w') as json_file:
            title = film.draw_polish_film()
            details = {'title': title,
                       'hidden_title': film.change_into_hidden_title(title),
                       'letters_set': film.letters_set,
                       'trial': -1}
            json.dump(details, json_file, ensure_ascii=False)

        with open('static/am_title.json', 'w') as json_file:
            title = film.draw_american_film()
            details = {'title': title,
                       'hidden_title': film.change_into_hidden_title(title),
                       'letters_set': film.letters_set,
                       'trial': -1}
            json.dump(details, json_file, ensure_ascii=False)

        with open('static/all_title.json', 'w') as json_file:
            title = film.draw_all_film()
            details = {'title': title,
                       'hidden_title': film.change_into_hidden_title(title),
                       'letters_set': film.letters_set,
                       'trial': -1}
            json.dump(details, json_file, ensure_ascii=False)

        images.empty_image()

    return render_template('home.html')


@app.route('/Polskie-filmy-dla-dzieci-i-młodziezy', methods=['GET', 'POST'])
def polish_film():
    with open('static/pl_title.json', 'r') as json_file:
        file_content = json.load(json_file)
    title = file_content['title']
    hidden_title = file_content['hidden_title']
    letters_set = file_content['letters_set']
    trial = file_content['trial']
    message = ""

    if request.method == 'POST':

        letter = str(request.form.get('letter'))

        data = guess_title.guess_title_or_letter(letter, title, hidden_title, letters_set, trial)

        with open('static/pl_title.json', 'w') as json_file:
            details = {'title': data[0],
                       'hidden_title': data[1],
                       'letters_set': data[2],
                       'trial': data[3]}
            json.dump(details, json_file, ensure_ascii=False)

        if data[3] > 12:
            return redirect(url_for('home'))

    return render_template('polish_film.html', hidden_title=data[1], trial=12 - data[3], message=data[4])


@app.route('/Amerykanskie-filmy-dla-dzieci-i-mlodziezy', methods=['GET', 'POST'])
def american_film():
    with open('static/am_title.json', 'r') as json_file:
        file_content = json.load(json_file)
    title = file_content['title']
    hidden_title = file_content['hidden_title']
    letters_set = file_content['letters_set']
    trial = file_content['trial']
    message = ""

    if request.method == 'POST':

        letter = str(request.form.get('letter'))

        data = guess_title.guess_title_or_letter(letter, title, hidden_title, letters_set, trial)

        with open('static/am_title.json', 'w') as json_file:
            details = {'title': data[0],
                       'hidden_title': data[1],
                       'letters_set': data[2],
                       'trial': data[3]}
            json.dump(details, json_file, ensure_ascii=False)

        if data[3] > 12:
            return redirect(url_for('home'))

    return render_template('american_film.html', hidden_title=data[1], trial=12 - data[3], message=data[4])


@app.route('/Wszystkie-filmy', methods=['GET', 'POST'])
def all_type_films():
    with open('static/all_title.json', 'r') as json_file:
        file_content = json.load(json_file)
    title = file_content['title']
    hidden_title = file_content['hidden_title']
    letters_set = file_content['letters_set']
    trial = file_content['trial']
    message = ""

    if request.method == 'POST':

        letter = str(request.form.get('letter'))

        data = guess_title.guess_title_or_letter(letter, title, hidden_title, letters_set, trial)

        with open('static/all_title.json', 'w') as json_file:
            details = {'title': data[0],
                       'hidden_title': data[1],
                       'letters_set': data[2],
                       'trial': data[3]}
            json.dump(details, json_file, ensure_ascii=False)

        if data[3] > 12:
            return redirect(url_for('home'))

    return render_template('all_type_films.html', hidden_title=data[1], trial=12-data[3], message=data[4])


if __name__ == "__main__":
    app.run(debug=True)