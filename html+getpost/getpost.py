from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        phy_mark = float(request.form['physics'])
        chem_mark = float(request.form['chemistry'])
        math_mark = float(request.form['maths'])
        eng_mark = float(request.form['english'])
        pe_mark = float(request.form['physical_edu'])

        perc = ((phy_mark+chem_mark+math_mark+eng_mark+pe_mark)/5)

        return redirect (url_for('result', results = perc))    

@app.route('/result/<float:results>')
def result(results):
    res = "FAILED"
    Marks_obtained = results
    if Marks_obtained > 90:
        res = "Passed with grade S"
    elif Marks_obtained > 80 and Marks_obtained <= 100:
        res = "Passes with grade A"
    elif Marks_obtained > 80 and Marks_obtained <= 90:
        res = "PASSED with grade B" 
    elif Marks_obtained > 70 and Marks_obtained <= 80:
        res = "PASSED with grade C"
    elif Marks_obtained >= 60 and Marks_obtained <= 100:
        res = "PASSED with grade D"
    elif Marks_obtained < 60 :
        res = "Failed"

    final = {'score':Marks_obtained,'result': res}

    return render_template('result.html', results = final)

if __name__ == "__main__":
    app.run(debug=True)