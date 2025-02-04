from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Database setup
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/Library"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Create an object
db = SQLAlchemy(app)


class Members(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String(20))
    LastName = db.Column(db.String(20))
    Email = db.Column(db.String(30))
    Phone = db.Column(db.String(11))


with app.app_context():
    db.create_all()



@app.route("/")
def index():
    result = Members.query.all()
    return render_template("index.html", result=result)


@app.route("/add", methods=["GET" , "POST"])
def add_memeber():
    if request.method == 'POST':

        first_name = request.form.get("FirstName")
        last_name = request.form.get("LastName")
        email = request.form.get("Email")
        phone_number = request.form.get("Phone")

        user_input = Members(
            FirstName = first_name,
            LastName = last_name,
            Email = email,
            Phone = phone_number
         )
        
        db.session.add(user_input)
        db.session.commit()

        return redirect(url_for("index"))
   
    return render_template("form.html")


@app.route("/edit/<int:id>" ,  methods=["GET" , "POST" ])
def edit_member(id):
    member = Members.query.get_or_404(id)

    if request.method == 'POST':
       member.FirstName = request.form.get("FirstName")
       member.LastName = request.form.get("LastName")
       member.Email = request.form.get("Email")
       member.Phone = request.form.get("Phone") 
       
       db.session.commit()
       return redirect(url_for("index"))
    
    return render_template("edit_form.html", member=member)




if __name__ == '__main__':
    app.run(debug=True)