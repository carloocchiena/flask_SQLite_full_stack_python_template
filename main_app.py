from datetime import date

from flask import Flask, request, render_template

from insert_user import insert_user

app = Flask(__name__)
app.config["DEBUG"] = True

# render error page 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>OOPS</h1> <p> Page not found </p>", 404

# render admin page # ok siamo arriva qui, a validare la password
@app.route('/admin', methods = ["GET", "POST"])
def admin():
    
    if request.method == "POST":
        psw = request.form['password']
        
    """
    def api_all():
    conn = sqlite3.connect(DB)
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_album = cur.execute("SELECT * FROM album;").fetchall()
    
    return jsonify(all_album)
    """
    return render_template("admin.html")

# render main page
@app.route('/', methods = ["GET", "POST"])
def input_page():
    
    errors = ""
    today = date.today()
    
    if request.method == "POST":
        user = request.form['user']
      
        if user != "":
            try:
                insert_user(user)
                return render_template("results.html", user=user, today_date=today)
            
            except Exception as e:
                errors = f"[!] Errors found: {e}"
        else:
            errors = "You must insert a username first"

    return render_template("main.html", today=today, errors=errors)

if __name__ == '__main__':
    app.run(use_reloader=False)
