from flask import Flask
from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                font-size:40px;

            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post">
          <label for"rot">Rotate by:</label>
          <input type="text" name="rot" id="rot" value="0">
          <textarea name="text" id="text">{}</textarea>
          <input type="submit" value="Submit">
      </form>
    </body>
</html>'''
@app.route("/")
def index():
    return form.format()

@app.route("/", methods=['post'])
def encrypt():
    text=request.form['text']
    rot=int(request.form['rot'])
    fin_text=rotate_string(text, rot)
    return form.format(fin_text)
app.run()