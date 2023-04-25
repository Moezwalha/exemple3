from flask import Flask, request
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get the base64 image string from the request
        base64_image = request.json['image']
        
        # Decode the base64 image string to bytes
        image_bytes = base64.b64decode(base64_image)
        
        # Open the image from bytes using PIL
        image = Image.open(BytesIO(image_bytes))
        
        # Process the image as needed
        
        # Return a response if needed
        return {'status': 'success'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

if __name__ == '__main__':
    app.run()
