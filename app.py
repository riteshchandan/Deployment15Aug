#import libraries
from flask import Flask, render_template, request
import joblib
#instance of Flask
app = Flask(__name__)

@app.route('/')
def hello():
    #return "hello world"
    #return render_template('landing.html')
    return render_template('diabetes.html')

@app.route('/contact')
def contact():
    #return "hello world.. this is the contact page"
    return render_template('contact.html')

@app.route('/feedback')
def feedback():
    #return "hello world.. this is the feedback page"
    return render_template('feedback.html')

@app.route('/gallery')
def gallery():
    #return "hello world.. this is the Gallery page"
    return render_template('gallery.html')
@app.route('/form')
def form():
    #return "hello world.. this is the Gallery page"
    return render_template('diabetes.html')

@app.route('/data', methods=['POST'])
def data():
    firstname = request.form.get('First_Name')
    lastname = request.form.get('Second_Name')
    contactNo = request.form.get('Number')
    EmailId = request.form.get('email')

    print(f'User created for {firstname} {lastname}. Details: /n Contact Number: {contactNo}, EmailId: {EmailId}')
    print(firstname)
    print(lastname)
    print(contactNo)
    print(EmailId)
    
    return "Form submitted successfully"
@app.route('/diabetes', methods=['POST'])

def diabetes():
    model = joblib.load('diabetic_79.pkl')
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)
    
    #return "Form Submitted"
    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if result[0]==0:
        output = 'not diabetic'
    else:
        output = 'diabetic'
    
    return render_template('result.html', output=output)
if __name__ == '__main__':
    app.run(debug=True)
