#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    email = request.form.get('email')
    text = request.form.get('text')
    if email != None and text != None:
        with open('feedback.txt', 'a', encoding="UTF-8") as f:
            f.write(f'\nE-mail: {email}\n')
            f.write(f'Text: {text}\n')
            f.write("---------------------")
        return redirect('/')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True, port=5050)