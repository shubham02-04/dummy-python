from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('careers.html')

# Run the local development server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
