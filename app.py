from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from matamata import cari_linkedin


load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    print(f"Received name: {name}")  # Log the received name
    result, image = cari_linkedin(name)
    print(f"Result: {result}, Image: {image}")  # Log the result and image
    return jsonify({
        'summary': result.to_dict(),  # Fixed typo 'summmary' to 'summary'
        'picture_url': image  # Changed 'image' to 'picture_url' to match client-side
    })
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)