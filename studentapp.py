from flask import Flask, redirect, url_for, render_template, request
import eventlet
import db

app = Flask(__name__)
student_database = db.Student()
tutor_database = db.Tutor()

@app.route("/")
@app.route("/student")
def home():
    return render_template("base.html")

@app.route('/list')
@app.route("/student/list")
def student_list():
    student_list = student_database.getAll()
    print(student_list)
    return render_template("students/list.html", students=student_list)


@app.route("/student/<sid>")
def student_view(sid):
    studentdetail = student_database.getById(sid)
    print(studentdetail)
    return render_template("students/view.html", student = studentdetail)


@app.route("/student/add", methods=['GET', 'POST'])
def student_add():
    if request.method == "POST":
        print(request.form)
        if request.form['studentID'] !='':
            s = dict()
            s['sid'] = request.form['studentID']
            s['sname'] = request.form['studentName'] if request.form['studentName'] != '' else ''
            s['email'] = request.form['email'] if request.form['email'] != '' else ''
            s['tut_id'] = request.form['tutorID'] if request.form['tutorID'] != '' else ''
            student = db.Student()
            if student.addNew(s):
                print("Insert succcesfully")
                return redirect(url_for('student_view', sid=s['sid']))
            else:
                print('Error')
                print(s)
                return redirect(url_for('student_add'))
        return redirect(url_for('student_add'))
    else:
        tutor_list = tutor_database.getAll()
        print(tutor_list)
        return render_template("students/add.html", tutors = tutor_list)


@app.route("/student/edit/<sid>")
def student_edit(sid):
    pass


@app.route("/student/delete/<sid>")
def student_delete(sid):
    pass


@app.route("/student/search")
def student_search():
    pass

if __name__ == "__main__":
    app.run(port=5003, debug=True)
