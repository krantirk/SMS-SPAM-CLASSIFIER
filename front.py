from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email1 = request.form['email1']
    import main
    main.do_stuff(email,email1)
    return redirect('/')


@app.route('/signup2', methods = ['POST'])
def signup2():
    email2 = request.form['email2']
    email3 = request.form['email3']
    import main1
    main1.do_stuff(email2,email3)
    return redirect('/')    


if __name__ == "__main__":
    app.run()