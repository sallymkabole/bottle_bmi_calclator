import os
from bottle import route, run, template, request, redirect

index_html = '''My first web app! By <strong>{{ author }}</strong>.'''
@route('/')
def index():
    return template(index_html, author='Real Python')


@route('/bmi', method = ['POST', 'GET'])
def calculate_bmi():
    height = request.forms.get("height")
    weight = request.forms.get("weight")
    
    height=int(height)
    weight=int(weight)
    bmi= round((weight / (height* height))* 703 )

    if ( bmi  < 18.5):
            print("underweight")

    elif ( bmi >= 18.51 and bmi < 24.9):
        print("Normal")

    elif ( bmi >= 25 and bmi < 29.9):
        print("overweight")

    elif ( bmi >=30):
        print('obese')

    #redirect('/results')
    return template('input.tpl', bmi = bmi)

"""@route('/results', method = ['POST', 'GET'])
def calculate_bmi():
    height = request.forms.get("height")
    weight = request.forms.get("weight")
    h= float(height)
    w= float(weight)
    bmi=((w *703) / (h * h))
    return template('result.tpl', bmi)"""


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)