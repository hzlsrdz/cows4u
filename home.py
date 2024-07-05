from flask import Flask, render_template, url_for, flash, redirect, request
import git
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/cows4u/cows4u')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
