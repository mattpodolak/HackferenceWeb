from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    s_abc = 10
    s_abc2 = 20
    top = []
    if top[2] < 1:
        print ('y')
    return render_template('index.html', s_abc = s_abc, s_abc2 = s_abc2)
def insert(num):
    return render_template('index.html', s_abc2=num)
if __name__ == '__main__':
    app.run()

    insert(input('Pick a num '))