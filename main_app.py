from flask import Flask, request, render_template

from datetime import date

from insert_user import insert_user

app = Flask(__name__)
app.config["DEBUG"] = True

#routing error page 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>OOPS</h1> <p> Page not found </p>", 404

#render main page
@app.route('/', methods = ["GET", "POST"])
def input_page():
    errors = ""
    today = date.today()
    
    if request.method == "POST":
        user = None
        user = request.form['user']
      
        if user is not None:
            try:
                insert_user(user)
                return render_template("results.html", user=user, today_date=today)     
            
            except Exception as e:
                #errors = "🐸 The anti-bug frog has caught something! Can you try? Sorry, it's still a beta version!"
                errors = e   

    return render_template("main.html", today=today, errors=errors)

app.run(use_reloader=False)
