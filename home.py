from flask import Flask, render_template, request, redirect, url_for
import git

app = Flask(__name__)

# Home page route
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

# Route to display cow creation page
@app.route("/createCow", methods=['GET', 'POST'])
def createCow():
    if request.method == 'POST':
        selected_cow_image = request.form['cow_image']
        return redirect(url_for('herd', selected_cow_image=selected_cow_image))
    return render_template('createcow.html', subtitle='Create A Cow!', text='This is cow creation menu')

# Route to handle form submission from createcow.html
@app.route("/herd")
def herd():
    selected_cow_image = request.args.get('selected_cow_image', '/static/images/default_cow.png')  # Default image if not provided
    return render_template('herd.html', selected_cow_image=selected_cow_image)

# Webhook route for updating server
@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/cows4u/cows4u')  # Replace with your actual repo path
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
