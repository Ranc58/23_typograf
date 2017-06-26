from flask import Flask, render_template, request
from typograph_script import format_text

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result_text():
    input_text = request.form['text']
    formated_text = format_text(input_text)
    return render_template('form.html',
                           input_text=input_text,
                           output_text=formated_text)

if __name__ == "__main__":
    app.debug = True
    app.run()

