from flask import Flask, render_template, url_for
import os

app = Flask(
    __name__,
    template_folder='templates',  
    static_folder='static'
)

@app.route('/')
def home():
    return render_template('a.html')

if __name__ == '__main__':
    app.run(debug=True)