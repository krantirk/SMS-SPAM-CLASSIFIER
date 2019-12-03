from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email1 = request.form['email1']
    import main1
    main1.do_stuff(email,email1)
    return redirect('/')

if __name__ == "__main__":
    app.run()