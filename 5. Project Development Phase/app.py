from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the index.html template which contains the Tableau Public embed code
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask server on port 5000
    app.run(debug=True, port=5000)
