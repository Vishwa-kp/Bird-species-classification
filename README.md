# 🐦 Bird Species Classification Using Deep Learning

## 📌 Project Overview

Bird Species Classification is a Deep Learning project that identifies the species of a bird from an image.

A Convolutional Neural Network (CNN) was developed using TensorFlow and Keras to classify bird images into **20 different species**.

A Streamlit web application was also created where users can upload a bird image and receive the predicted species along with the model's confidence score.

## 🎯 Objective

The main objective is to build an image classification system that can automatically identify bird species from an uploaded image.

## 📊 Dataset

The project uses a bird image dataset containing **20 bird species**.

The training dataset contains approximately **3,208 images**.

The 20 species include:

- ABBOTTS BABBLER
- ABBOTTS BOOBY
- ABYSSINIAN GROUND HORNBILL
- AFRICAN CROWNED CRANE
- AFRICAN EMERALD CUCKOO
- AFRICAN FIREFINCH
- AFRICAN OYSTER CATCHER
- AFRICAN PIED HORNBILL
- AFRICAN PYGMY GOOSE
- ALBATROSS
- ALBERTS TOWHEE
- ALEXANDRINE PARAKEET
- ALPINE CHOUGH
- ALTAMIRA YELLOWTHROAT
- AMERICAN AVOCET
- AMERICAN BITTERN
- AMERICAN COOT
- AMERICAN FLAMINGO
- AMERICAN GOLDFINCH
- AMERICAN KESTREL

## 🧹 Image Preprocessing

The images were prepared before training the CNN model.

Main preprocessing steps:

- Loaded images from class-based folders
- Resized images to **224 × 224 pixels**
- Normalized pixel values
- Created training, validation and test datasets

## 🧠 Deep Learning Model

### Convolutional Neural Network (CNN)

A CNN model was developed using TensorFlow/Keras.

The architecture includes:

- Rescaling layer
- Convolutional layers
- Max Pooling layers
- Flatten layer
- Dense layer
- Dropout layer
- Softmax output layer

The final layer contains **20 output classes**, representing the 20 bird species.

## 📈 Model Results

The model was trained for **10 epochs**.

- Training Accuracy: **87.13%**
- Validation Accuracy: **82.00%**
- Test Accuracy: **74.00%**

## 🔄 Project Workflow

```text
Bird Image Dataset
       ↓
Image Preprocessing
       ↓
Resize to 224 × 224
       ↓
Pixel Normalization
       ↓
CNN Model
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Bird Species Prediction
       ↓
Confidence Score
```

## 🖥️ Streamlit Application

A Streamlit web application was developed to make the model easy to use.

Users can:

1. Upload a bird image
2. The image is processed by the application
3. The trained CNN model analyzes the image
4. The predicted bird species is displayed
5. The confidence score is displayed

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn
- Pillow
- Matplotlib
- Seaborn
- Streamlit

## 📁 Project Structure

```text
bird-species-classification/
│
├── notebooks/
│   └── bird_classification.ipynb
│
├── app.py
├── class_names.json
├── requirements.txt
└── README.md
```

## 🚀 Future Improvements

- Increase the size of the training dataset
- Improve model accuracy
- Use Transfer Learning models such as MobileNet or EfficientNet
- Add more bird species
- Improve image augmentation
- Deploy the application online

## 👨‍💻 Author

**K.P. Vishwa**

Aspiring Data Scientist | Data Analyst | Machine Learning Enthusiast
