from flask import Flask, request, jsonify
from text_generator import generate_text

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Random Text Generator</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                }
                .container {
                    text-align: center;
                    background: #fff;
                    padding: 2rem;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    margin-bottom: 1rem;
                    color: #333;
                }
                form {
                    display: flex;
                    flex-direction: column;
                }
                input[type="text"] {
                    padding: 0.5rem;
                    font-size: 1rem;
                    margin-bottom: 1rem;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    width: 100%;
                }
                input[type="submit"] {
                    padding: 0.5rem 1rem;
                    font-size: 1rem;
                    color: #fff;
                    background-color: #007BFF;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
                .result-container {
                    margin-top: 1rem;
                }
                .result-block {
                    padding: 1rem;
                    border-radius: 5px;
                    margin-bottom: 1rem;
                }
                .input-block {
                    background-color: #d4edda;
                    color: #155724;
                }
                .output-block {
                    background-color: #f8d7da;
                    color: #721c24;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Random Text Generator</h1>
                <form id="text-form">
                    <input type="text" id="input_string" name="input_string" placeholder="Enter a string" required>
                    <input type="submit" value="Generate">
                </form>
                <div id="result" class="result-container"></div>
            </div>
            <script>
                document.getElementById('text-form').addEventListener('submit', async function(event) {
                    event.preventDefault();
                    const formData = new FormData(event.target);
                    const response = await fetch('/generate', {
                        method: 'POST',
                        body: formData
                    });
                    const result = await response.json();
                    document.getElementById('result').innerHTML = `
                        <div class="result-block input-block">Input: ${result.input}</div>
                        <div class="result-block output-block">Random Text: ${result.random_text}</div>
                    `;
                });
            </script>
        </body>
        </html>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    input_string = request.form['input_string']
    random_text = generate_text(input_string)
    return jsonify({"input": input_string, "random_text": random_text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
