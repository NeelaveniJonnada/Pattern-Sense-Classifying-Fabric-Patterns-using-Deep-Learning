from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)

# Load trained model
model = load_model("model_cnn.h5")

# Define labels
labels = ['stripes', 'polka dot', 'plain', 'tribal', 'floral',
          'squares', 'ikat', 'animal', 'geometry', 'cartoon']

# Function to extract prediction from image
def get_model_prediction(image_path):
    img = load_img(image_path, target_size=(255, 255))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x, verbose=0)
    return labels[predictions.argmax()]

# Function to extract true label from filename
def extract_true_label(filename):
    # Extract prefix before underscore (_) or dash (-)
    return filename.split('_')[0].split('-')[0].lower()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/predict_page')
def predict_page():
    return render_template("predict.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/predict', methods=['POST'])
def prediction():
    img = request.files['ump_image']
    img_path = os.path.join("static/assets/uploads/", img.filename)
    img.save(img_path)

    predicted = get_model_prediction(img_path)
    true_label = extract_true_label(img.filename)

    return render_template("predictionpage.html", img_path=img_path,
                           prediction=predicted, true_label=true_label)

if __name__ == "__main__":
    app.run(debug=True)
