### Create a BMI Calculation Application
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio.input import *
from pywebio.output import *

app = Flask(__name__)

def bmicalculator():
    height=input("Please enter your height in centimetres",type=FLOAT)
    weight=input("Please enter your weight in kilograms",type=FLOAT)
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16, 'severely underweight'), (18.5, 'underweight'),
                  (25, 'normal'), (30, 'overweight'),
                  (35, 'moderately obese'), (float('inf'), 'severely obese')]
    
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('Your BMI is %.1f. You are %s.'%(bmi,tuple2))
            break
        

app.add_url_rule('/','webio_view',webio_view(bmicalculator),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
