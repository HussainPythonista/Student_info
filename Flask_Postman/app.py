from flask import Flask, render_template,url_for,request,redirect,flash
from crud_operation import CRUD



app = Flask(__name__)

app.secret_key="abc123"
db = CRUD()

@app.route("/")
def home():
    datas = db.get_all_data()
    return render_template("home.html")#, datas=datas)



@app.route("/info")
def stu_info():
    datas = db.get_all_data()
    return render_template("student_info.html", datas=datas)

#User addition
@app.route("/add",methods=["GET","POST"])
def addUsers():
    if request.method=="POST":
        roll_no=request.form["roll No"]
        age=request.form["age"]
        class_=request.form["class"]
        section=request.form["section"]
        name=request.form["name"]
        flash("Student created")
        db.insert_details(name=name,age=age,class_=class_,roll_no=roll_no,section=section)
        return redirect(url_for("stu_info"))

    return render_template("add_students.html",)


@app.route("/edit/<roll_no>",methods=["GET","POST"])
def edit_info(roll_no):
    if request.method == "POST":
        roll_no = request.form["roll No"]
        age = request.form["age"]
        class_ = request.form["class"]
        section = request.form["section"]
        name = request.form["name"]
        flash("Student Information Updated",category='success')
        db.update_info(roll_no=roll_no, name=name, age=age, class_=class_, section=section)
        return redirect(url_for("stu_info"))

    info_existing_user = db.get_one_data(roll_no)
    return render_template("edit_students.html", info=info_existing_user)

@app.route("/delete/<roll_no>")
def delete_stu(roll_no):

    db.delete_info(roll_no)
    flash("Student Information Deleted",)
    return redirect(url_for("stu_info"))
    
if __name__ == "__main__":
    app.run(port=5500)

