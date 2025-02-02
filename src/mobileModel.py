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
    recyclable_items = [
    'bottle', 'can', 'carton', 'paper_towel', 'plastic_bag', 'paper_bag', 
    'paper', 'cardboard', 'glass_jar', 'plastic_container', 'aluminum_foil', 
    'newspaper', 'plastic_bottle', 'food_packaging', 'magazines', 'egg_cartons', 
    'phone_books', 'milk_cartons', 'tin_can', 'pizza_box', 'tissue_box', 
    'wrapping_paper', 'glass_bottle', 'straws', 'plastic_lid', 'yogurt_container', 
    'detergent_bottle', 'cereal_box', 'soda_can', 'juice_box', 'plastic_wrap', 
    'toilet_paper_roll', 'battery', 'shoebox', 'plastic_wrap', 'styrofoam', 
    'broken_mirror', 'light_bulb', 'old_clothing', 'fabric_scraps', 'tote_bag', 
    'plastic_tray', 'clamshell_container', 'electronics', 'printer_ink_cartridges', 
    'soda_cans', 'takeout_container', 'cardboard_box', 'paint_can', 'aluminum_can', 
    'metal_foil', 'furniture', 'coffee_cups', 'wood', 'furniture', 'broken_appliances', 
    'foam_peanuts', 'shampoo_bottle', 'toothpaste_tube', 'plastic_knife_fork_spoon']

    for _, label, _ in decoded_predictions:
        if label in recyclable_items:
            return True
    return False



def main():
    # Path to the image
    image_path = './images/big.jpg'

    # Check if the item in the image is recyclable
    if is_recyclable(image_path):
        print("The item in the image is recyclable.")
    else:
        print("The item in the image is not recyclable.")

if __name__ == '__main__':
    main()

