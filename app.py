from flask import Flask, render_template, request

app = Flask(__name__)

# Cevap anahtarı
answer_key = {
    'q1': 'a',
    'q2': 'a',
    'q3': 'c',
    'q4': 'b',
    'q5': 'c',
    'classic1': 'for',
    'classic2': 'def'
}

# En yüksek not
highest_score = 0

# Puanlama
def calculate_score(user_answers):
    score = 0
    for question, answer in user_answers.items():
        if question in answer_key and answer == answer_key[question]:
            if question.startswith('q'):
                score += 12
            elif question.startswith('classic'):
                score += 20
    return score

@app.route('/')
def index():
    return render_template('index.html', highest_score=highest_score)

@app.route('/quiz', methods=['POST'])
def quiz():
    global highest_score
    username = request.form['username']
    user_answers = {
        'q1': request.form.get('q1', ''),
        'q2': request.form.get('q2', ''),
        'q3': request.form.get('q3', ''),
        'q4': request.form.get('q4', ''),
        'q5': request.form.get('q5', ''),
        'classic1': request.form.get('classic1', '').lower(),  
        'classic2': request.form.get('classic2', '').lower()   
    }
    score = calculate_score(user_answers)

    
    if score > highest_score:
        highest_score = score

    return render_template('result.html', username=username, user_answers=user_answers, score=score)

if __name__ == '__main__':
    app.run(debug=True)
