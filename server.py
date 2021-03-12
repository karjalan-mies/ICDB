from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    title = 'Банк данных страховой компании'
    return render_template('index.html', title=title)

@app.route('/')
@app.route('/login')
def login():
    title = 'Страница авторизации'
    return render_template('login.html', title=title)

@app.route('/people')
def people():
    title = 'Ввод физических лиц'
    return render_template('people.html', title=title)

@app.route('/policy')
def policy():
    title = 'Ввод полисов'
    return render_template('policy.html', title=title)

@app.route('/organization')
def organization():
    title = 'Ввод организаций'
    return render_template('organization.html', title=title)

@app.route('/address')
def address():
    title = 'Ввод адресов'
    return render_template('address.html', title=title)

@app.route('/transport')
def transport():
    title = 'Ввод транспортных средств'
    return render_template('transport.html', title=title)

@app.route('/event')
def event():
    title = 'Страховой случай'
    return render_template('event.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)