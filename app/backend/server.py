from flask import Flask, request
import os

app = Flask(__name__)

# Set the directory where the images will be saved
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    # Get the raw binary data from the POST request
    image_data = request.get_data()

    if not image_data:
        return 'No image data found in request', 400

    # You can assign a name based on the request (for example, a timestamp or a random name)
    # For simplicity, let's name it 'uploaded_image.jpg' (You can choose a more specific name)
    image_filename = 'uploaded_image.jpg'
    image_path = os.path.join(UPLOAD_FOLDER, image_filename)

    # Save the binary image data to a file
    with open(image_path, 'wb') as f:
        f.write(image_data)

    # call command line ffmpeg shrink image down by 4
    os.system(f'ffmpeg -i {image_path} -vf scale=iw/4:-1 {image_path}')

    return {'cat': 'recycle'}, 200

ids = {
        1: 'Matt',
        2: 'Harsha',
        3: 'Gowtham'
}

@app.route('/id_card', methods=['POST'])
def id_card():
    # get id number from json body
    id_number = int(request.json.get('id'))

    # respond with user email
    return {'name': ids[id_number]}, 200

if __name__ == '__main__':
    app.run(debug=True)
