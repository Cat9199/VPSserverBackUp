from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
      data = request.get_json()
      return jsonify(data)
@app.route("/")
def func():
      return "Hello World"

if __name__ == '__main__':
      app.run(debug=True)