from flask import Flask , render_template , request , redirect , url_for
import os


app = Flask(__name__, static_url_path='/static')

@app.route('/<filename>')
def hello_world(filename):
    # put application's code here
    file_name = f"{filename}"
    return render_template('index.html', file_name=file_name)
if __name__ == '__main__':
    app.run()
