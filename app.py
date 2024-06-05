from flask import Flask, render_template, request
import math

app = Flask(__name__)
def cot(x):
    return 1/math.tan(x)

def toradians(x):
    pi=3.141
    return x*pi/180

func={'sin':math.sin,'cos':math.cos,'tg':math.tan,'ctg':cot}


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        fun = (request.form.get('func'))
        num = float(request.form.get('num_2'))
        degrees = request.form.get('units')=='degrees'
        accuracy = int(request.form.get("accuracy"))
        if  degrees:
            num_2=toradians(num)
            answer = f"{fun}({num}°)={func[fun](num_2):.{accuracy}f}"
        else:
            num_2=num
            answer = f"{fun}({num})={func[fun](num_2):.{accuracy}f}"
        return render_template('index.html', ans=answer,val=num)

@app.route('/hello')
def hello():
    return render_template("hello.html");


if __name__ == '__main__':
    app.run()