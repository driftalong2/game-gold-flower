from flask import Flask
from flask import render_template
from rule import Rule

app = Flask(__name__)

@app.route('/game')
def game():
    rule = Rule()
    status, player1, player2 = rule.compare()
    return render_template('game.html', status=status, player1=player1, player2=player2)


if __name__ == '__main__':
    app.run(debug=True)