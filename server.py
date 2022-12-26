from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pages(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a', newline='') as database:
        message = data['message']
        email = data['email']
        subject = data['subject']
        file = database.write(f'\n{email}, {subject}, {message}')
 
@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('./thankyou.html')
    else:
        return 'something went wrong. Try again!'

if __name__ == '__main__':
    app.run(debug=True)