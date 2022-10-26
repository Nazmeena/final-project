# This is where your CREATE, READ, UPDATE AND DELETE functionality is going to go. 
from asyncio import Task
from flask import render_template, url_for, redirect, request 
from application import app, db 
from application.models import Students, Classes
from application.forms import StudentForm, ClassForm

#READ BOTH DATABASES
#Location of this functionality: ip_address:5000/
@app.route('/', methods=['POST', 'GET'])
def index():
    classes = Classes.query.all()
    students = Students.query.all()
    return render_template('index.html', title="Student Enrollment", teams=teams, players=players)

# CREATE class 
@app.route('/addclass', methods=['POST', 'GET'])
def addclass():
    form = ClassForm() 
    if form.validate_on_submit(): 
        classes = Classes(
            name = form.name.data
        )
        db.session.add(classes)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addclasses.html', title="Add a new Class", form=form)

#CREATE student
#Location of this functionality: ip_address:5000/add
@app.route('/addstudent', methods=['POST','GET'])
def addstudent():
    # This points to TodoForm
    form = StudentForm()
    # Checks that we have clicked the submit button
    if form.validate_on_submit():
        # the variable tasks becomes what is put on the form 
        # todos becomes what we are going to be adding to the database
        students = Students(
            name = form.name.data,
            set = form.set.data,
            # Foreign key as a option to add to the create process. 
            fk_classid = form.fk_classid.data
        )
        # This performs the add to database
        db.session.add(classes)
        # This commits those changes
        db.session.commit()
        # This one redirects to the index functions url
        return redirect(url_for('index'))
    # Otherwise return the template of add.html
    return render_template('addstudent.html', title="Add a new Student", form=form)

#UPDATE classes 
@app.route('/updateclass/<int:id>', methods=['GET', 'POST'])
def updateclass(id):
    form = ClassForm()

    classes = Classes.query.get(id)

    if form.validate_on_submit():
        classes.name = form.name.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = classes.name
    return render_template('updateclass.html', title='Update the class', form=form)


#UPDATE student
@app.route('/updatestudent/<int:id>', methods=['GET', 'POST'])
def updatestudent(id):
    form = StudentForm()
    # Get one name from the specified ID
    name = Students.query.get(id)
    # POST method
    # If the user clicks submit
    if form.validate_on_submit():
        # What is put in the form gets ammended to the database
        name.name = form.name.data,
        name.set = form.set.data,
        name.fk_classid = form.fk_classid.data
        # Commit the changes
        db.session.commit()
        # Redirect to the url for index function 
        return redirect(url_for('index'))
    # Else if the request method is a GET
    elif request.method == 'GET':
        # Update the form with whats in the database
        form.name.data = name.name 
        form.set.data = name.set
        form.fk_classid.data = name.fk_classid
    # If we go to the url return the template updateplayer.html
    return render_template('updatestudent.html', title='Update the student', form=form)


#DELETE class
@app.route('/deleteclass/<int:id>')
def deleteclass(id):
    class = Classes.query.get(id)
    db.session.delete(class)
    db.session.commit()
    return redirect(url_for('index'))

#DELETE student
#Location of this functionality: ip_address:5000/delete/1
@app.route('/deletestudent/<int:id>')
def deletestudent(id):
    # Collecting the task we want to delete based on its id
    name = Students.query.get(id)
    # deleting this item from the database
    db.session.delete(name)
    # committing this change
    db.session.commit()
    # returning the url in the index function. 
    return redirect(url_for('index'))
