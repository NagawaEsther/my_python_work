from flask import Flask,render_template,request,redirect,url_for

#creating the app instance
app = Flask(__name__,template_folder="templates")

tasks=[]

#Routing
@app.route('/')
def home():
    return render_template("index.html")

#creating a new task
@app.route('/add_task',methods=['POST'])
def create_task():
    task = request.form.get("task") 
    tasks.append(task)# Adding task to our list
    return redirect(url_for("home"))
    
#enabling the debug mode
if __name__== "__main__":
    app.run(debug=True)
    
