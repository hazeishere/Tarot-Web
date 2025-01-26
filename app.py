from flask import Flask, request, redirect, url_for, render_template, jsonify
from cards import get_cards

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        return redirect(url_for('result', question=question))
    return render_template('home.html')

@app.route('/result')
def result():
    question = request.args.get('question')
    return render_template('result.html', question=question)

@app.route('/get_card')
def get_card():
    card, card_value = get_cards()
    return jsonify({'name': card, 'keywords': card_value['keywords'], 'image': card_value['image']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5017)

    # add asked q to result.html