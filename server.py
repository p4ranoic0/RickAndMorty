from flask import Flask, render_template, request, redirect, session, url_for, flash



app = Flask(__name__, template_folder='templates', static_folder='templates/')

# settings
app.secret_key = 'mykey'

@app.route('/')
def index():

    return render_template('index.html') 

   
if __name__ == '__main__':
    app.run(host = "0.0.0.0" , port = 3000, debug = True)