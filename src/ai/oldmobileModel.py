import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
import numpy as np

# Load the MobileNet model
model = MobileNet(weights='imagenet')

def is_recyclable(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make predictions
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Check if any of the top predictions are recyclable items
    recyclable_items = ['bottle', 'can', 'carton', 'paper_towel', 'plastic_bag']
    for _, label, _ in decoded_predictions:
        if label in recyclable_items:
            return True
    return False

# Path to the image
image_path = './images/big.jpg'

# Check if the item in the image is recyclable
if is_recyclable(image_path):
    print("The item in the image is recyclable.")
else:
    print("The item in the image is not recyclable.")