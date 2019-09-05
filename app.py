from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)

horoscopes = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/horoscope')
def get_horoscopes():
        """Give the user a horoscopes"""
        name = request.args.get('name')
        num_horoscopes = int(request.args.get('num_horoscopes'))
        show_horoscopes = (request.args.get('show_horoscopes'))
        nice_things = ','.join(sample(horoscopes, num_horoscopes))

        return render_template(
            'horoscope.html',
            name=name,
            show_horoscopes=show_horoscopes,
            horoscopes=horoscopes)
        

        """if show_horoscopes:
            return f"Hello there,{name}! you are so {nice_things}!"
        else:
            return f"Hello there, {name}! Have a niec day!"""

if __name__ == "__main__":
    app.run(debug=True)

