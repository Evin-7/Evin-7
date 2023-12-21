from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow CORS for all routes under /api

# In-memory list to store texts
texts = ['Text 1', 'Text 2', 'Text 3']

# Define the upload folder for images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# In-memory list to store uploaded images
uploaded_images = []

@app.route('/')
def hello():
    return 'Hello, Flask!'

# API endpoint that returns a list of texts
@app.route('/api/texts')
def get_texts():
    return jsonify(texts)

# API endpoint for adding a text
@app.route('/api/add-text', methods=['POST'])
def add_text():
    try:
        # Assuming the new text is sent in the request's JSON body
        new_text = request.json.get('new_text')
        
        # Add the new text to the in-memory list
        texts.append(new_text)
        
        return jsonify({"success": True, "message": "Text added successfully"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# New API endpoint to get the updated list of texts
@app.route('/api/get-updated-texts')
def get_updated_texts():
    return jsonify(texts)

# API endpoint that returns a list of uploaded images
@app.route('/api/images')
def get_images():
    return jsonify(uploaded_images)

# API endpoint for image upload
@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    try:
        # Check if the request contains a file
        if 'image' not in request.files:
            return jsonify({"success": False, "error": "No file part"})

        image = request.files['image']

        # Check if the file name is empty
        if image.filename == '':
            return jsonify({"success": False, "error": "No selected file"})

        # Save the uploaded image to the upload folder
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))

        # Add the image filename to the in-memory list
        uploaded_images.append(image.filename)

        return jsonify({"success": True, "message": "Image uploaded successfully"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# API endpoint to serve uploaded images
@app.route('/api/images/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Existing API endpoint
@app.route('/api/other-endpoint')
def other_endpoint():
    # Your existing code here
    return jsonify({"data": "Some data"})

if __name__ == '__main__':
    app.run(debug=True)
