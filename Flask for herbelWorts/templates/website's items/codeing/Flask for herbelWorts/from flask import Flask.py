from flask import Flask, render_template
app = Flask(__name__)

@app.route('/HerbelWorts')
def hello_world():
    return render_template('index.html')
    return 'HerbelWorts'

if __name__== "__main__":
    app.run(debug=True, port=8000)