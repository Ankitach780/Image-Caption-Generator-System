import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow.keras.preprocessing import image as keras_image
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import preprocess_input, VGG16
from PIL import Image
import matplotlib.pyplot as plt
import os

model = load_model("caption_model.keras", safe_mode=False)

# Load tokenizer and max_len
with open("tokenizer.pkl", "rb") as f:
    data = pickle.load(f)
    if isinstance(data, dict):
        tokenizer = data["tokenizer"]
        max_len = data["max_len"]
    else:
        tokenizer, max_len = data

# Load VGG16 for feature extraction
vgg_model = VGG16(weights='imagenet')
feature_extractor = Model(inputs=vgg_model.inputs, outputs=vgg_model.get_layer('fc2').output)

def extract_features(img_path):
    img = keras_image.load_img(img_path, target_size=(224, 224))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    features = feature_extractor.predict(img_array, verbose=0)
    return features

# Generate a caption for an image
def predict_caption(model, image_features, tokenizer, max_len):
    in_text = 'start'
    for _ in range(max_len):
        seq = tokenizer.texts_to_sequences([in_text])
        seq = pad_sequences(seq, maxlen=max_len, padding='post')
        yhat = model.predict([image_features, seq], verbose=0)
        yhat = np.argmax(yhat)
        word = tokenizer.index_word.get(yhat, '')

        if word == 'end':
            break

        in_text += ' ' + word

    return in_text.split()[1:]  


def generate_caption(image_name):
    image_features = extract_features(image_name) 
    

    caption = predict_caption(model, image_features, tokenizer, max_len)


    print("Predicted Caption:", ' '.join(caption))
    return caption