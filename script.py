from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["GET" , "POST"])
def add_memeber():
    if request.method == 'POST':

        first_name = request.form.get("FirstName")
        last_name = request.form.get("LastName")
        email = request.form.get("Email")
        phone_number = request.form.get("Phone")

        context = {
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            "phone_number" : phone_number 
        }

        return render_template("index.html" , **context)
   
    return render_template("form.html")





if __name__ == '__main__':
    app.run(debug=True)