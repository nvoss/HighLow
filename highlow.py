from random import randint
from flask import Flask, current_app, jsonify
from config import host
app = Flask(__name__, static_url_path='')


level_1_secret = 0
level_1_guesses = 10
attempts = 0


def generate_random_number(max):
    secret = randint(1,max)
    return secret


def attempt_a_guess(guess, secret, flag):

    if guess == secret:
        return flag
    elif guess < secret:
        return "Higher"
    elif guess > secret:
        return "Lower"


@app.route('/level1/<guess>')
def level_1_guess(guess):
    global level_1_guesses
    if level_1_guesses > 0:
        level_1_guesses -= 1
        return jsonify(attempt_a_guess(int(guess), level_1_secret, "FLAG{Pr3s5_YoUr_lUck}"), str(level_1_guesses))
    else:
        return jsonify("Game Over", "0")


@app.route('/level1')
def level1():
    global level_1_secret
    global level_1_guesses
    level_1_guesses = 10
    level_1_secret = generate_random_number(1000)
    return current_app.send_static_file('level1.html')


@app.route('/level2/flag')
def level2_flag():
    return current_app.send_static_file('flag2.png')


@app.route('/level2')
def level2():
    return current_app.send_static_file('level2.html')


@app.route('/level3')
def level3():
    return current_app.send_static_file('level3.html')

if __name__ == '__main__':
    app.run(host=host, debug=True)