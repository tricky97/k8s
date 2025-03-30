from flask import Flask,render_template, request, redirect
import os

env=os.environ

app= Flask(__name__)

PORT=os.environ.get('PORT',8000)

@app.route('/')
def index():

    env=dict(os.environ)
    print(env)

    return render_template('index.html', env = env)

if __name__ == '__main__':
    app.run(debug=True,port=PORT)     