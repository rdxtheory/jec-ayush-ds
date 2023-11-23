from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__,)

@app.route('/')
def welcome():
    return render_template('submission.html')

@app.route('/about')
def about_page():
    return 'about us '

@app.route('/numbers/<int:marks>')
def numbers(marks):
    return "your score is "+str(marks) 

@app.route('/data_valid',methods=['GET','POST'])
def data_valid():
    if request.method=='POST':
        size=request.form['size']
    return "the size of house is "+str(size)

@app.route('/shwpass/<int:marks>')
def pass_page(marks):
    return 'You have Passed with marks '+str(marks)
@app.route('/shwfail/<int:marks>')
def fail_page(marks):
    return "You have failed with marks"+str(marks)+" .Better luck next time"

@app.route('/result_chk/<int:marks>')
def result_chk(marks):
    res=""
    if marks>=50:
        res='pass_page'
    else:
        res='fail_page'
    return redirect(url_for(res,marks=marks))
    
if __name__=='__main__':
    app.run(debug=True)