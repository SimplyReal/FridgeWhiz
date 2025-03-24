from flask import Flask, render_template, request, redirect, url_for
import os
from recipe_model import extract_ingredients, generate_recipes

app = Flask(__name__)

UPLOAD_FOLDER = 'images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return "No image uploaded"

    image = request.files['image']
    if image.filename == '':
        return "No image selected"

    # Save the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    # Get user filters
    filters = request.form.getlist('filters')

    # Extract ingredients from the image
    ingredients_text = extract_ingredients(image_path)

    # Generate recipes based on ingredients and filters
    recipes = generate_recipes(ingredients_text, filters)

    # Pass recipes to process.html
    return render_template('process.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)