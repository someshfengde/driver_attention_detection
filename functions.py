from fastai.vision.all import * 
from fastai import *  
from PIL import Image

def label_func(x): return x.parent.name    
def load_model():
    model = load_learner('./export.pkl')
    return model




output_label = {'c0': 'normal driving',
'c1': 'texting - right',
'c2': 'talking on the phone - right',
'c3': 'texting - left',
'c4': 'talking on the phone - left',
'c5': 'operating the radio',
'c6': 'drinking',
'c7':' reaching behind',
'c8': 'hair and makeup',
'c9': 'talking to passenger'}

def predict_with_image(image):
    
    model = load_model()
    prediction  = model.predict(image)
    label = f'model predicted uploaded image is {output_label[prediction[0]]} with probability {prediction[2].max()}'
    return label