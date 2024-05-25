from quadratic import InputForm1
from prime import InputForm2
from bisection import InputForm3
from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) #Applies to get GET when we load the site and POST
def index():
    form1 = InputForm1(request.form) #Calling the class from the model.py. This is where the GET comes from
    form2 = InputForm2(request.form)
    form3 = InputForm3(request.form)
    if request.method == 'POST' and form1.validate(): 
        result1, result2 = compute(form1.a.data, form1.b.data,form1.c.data) #Calling the variables from the form
        pn = None
        root = None
    elif request.method == 'POST' and form2.validate(): 
        pn = primef(form2.number.data)
        result1 = None
        result2 = None
        root = None
    elif request.method == 'POST' and form3.validate():
        root = bisect(form3.xa.data, form3.xb.data)
        pn = None
        result1 = None
        result2 = None
    else:
        result1 = None #Otherwise is none so no display
        result2 = None
        pn = None
        root = None
    return render_template('index.html',form1=form1, form2=form2, form3=form3, result1=result1, result2=result2,pn = pn, root=root) #Display the page

@app.route("/")
def compute(a,b,c):
    disc = b*b - 4*a*c
    n_format = "{0:.2f}" #Format to 2 decimal spaces
    if disc > 0:
        result1 = (-b + math.sqrt(disc)) / 2*a
        result2 = (-b - math.sqrt(disc)) / 2*a
        result1 = float(n_format.format(result1))
        result2 = float(n_format.format(result2))
    elif disc == 0:
        result1 = (-b + math.sqrt(disc)) / 2*a
        result2 = None
        result1 = float(n_format.format(result1))
    else:
        result1 = "" #Empty string for the purpose of no real roots
        result2 = ""
    return result1, result2

@app.route("/")
def primef(n):
    pc = 0
    n = int(n)
    for i in range(2,n): #From 2 up to the number
        p = n % i #Get the remainder
        if p == 0: #If it equals 0
            pc = 1 #Then its not prime and break the loop
            break
    if pc == 1:
        pn = 1
        return pn
    elif pc == 0:
        pn = 0
        return pn

@app.route("/")
def bisect(xa,xb):
    added = xa + " + " + xb
    c = eval(added)
    c = int(c)/2
    ya = (int(xa)**6) - int(xa) - 1 #f(a)
    yb = (int(xb)**6) - int(xb) - 1 #f(b)
    
    if ya > 0 and yb > 0: #If they are both positive, since we are checking for one root between the points, not two. Then if both positive, no root
        root = 0
        return root
    else:
        e = 0.0001 #When to stop checking, number is really small

        l = 0 #Loop
        while l < 1: #Endless loop until condition is met
            d = int(xb) - c #Variable d to check for e
            if d <= e: #If d < e then we break the loop
                l = l + 1
            else:
                yc = (c**6) - c - 1 #f(c)
                if yc > 0: #If f(c) is positive then we switch the b variable with c and get the new c variable
                    xb = c
                    c = (int(xa) + int(xb))/2
                elif yc < 0: #If (c) is negative then we switch the a variable instead
                    xa = c 
                    c = (int(xa) + int(xb))/2
        c_format = "{0:.4f}"
        root = float(c_format.format(c))
        return root
    
if __name__=="__main__":
    app.run("0.0.0.0",5000)
