# app.py
from flask import Flask, request, jsonify # type: ignore
from text_generator import generate_text

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Random Text Generator</h1>
        <form action="/generate" method="post">
            <label for="input_string">Enter a string:</label><br>
            <input type="text" id="input_string" name="input_string"><br><br>
            <input type="submit" value="Generate">
        </form>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    input_string = request.form['input_string']
    random_text = generate_text(input_string)
    return jsonify({"input": input_string, "random_text": random_text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
