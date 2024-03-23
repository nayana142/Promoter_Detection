# Promoter_Detection
Promoter Detection for Ecoli Prediction

## Abstract 
         Many advances in the field of computational biology have been made possible by the development of artificial intelligence and
         machine learning. By allowing computers to automatically learn from data without any explicit programming and enhancing their
         capacity to tackle complicated issues via learning and experience, the tremendous advancements in the field of machine learning
         have created opportunities in demanding domains. Machine learning and deep learning finds widespread application in bioinformatics,
         particularly in the classification and identification of DNA patterns for genomics purposes. The goal of this project is to apply 
         and enhance deep learning models, such as neural network-based techniques,for the prediction of DNA promoter (transcription start sites)
         classification for common bacteria, infection with Escherichia coli (E. coli). The performance of the models is optimized through
         hyper-parameter tuning for improved prediction. 

## Web Application frame work
### Home Page
![Screenshot 2024-03-23 114400](https://github.com/nayana142/Promoter_Detection/assets/120770261/848cb30f-e490-466a-84bc-296fea7a9577)
### Input Page
![Screenshot 2024-03-23 140836](https://github.com/nayana142/Promoter_Detection/assets/120770261/595853be-b79a-4ec9-b4ca-77257a296542)
### Result Page
![Screenshot 2024-03-23 140903](https://github.com/nayana142/Promoter_Detection/assets/120770261/40fb47bd-aeda-4a8b-92ef-c46b6a399fe9)
### Previous Data Page
![Screenshot 2024-03-23 140934](https://github.com/nayana142/Promoter_Detection/assets/120770261/74a6e2b2-c885-4438-aa22-ef9f1210da90)


## Objective 
     The purpose of this project is to develop a system for classifying DNA promotor genes to determine if they are affected by a common
     bacterium, Escherichia coli (E. coli) and will be used for taking precautions from these microbes and will be able to feed into another 
     high-level DNA driven problems.

## Project Overview 
    • Objective: Employ advanced deep learning techniques to classify DNA promoter genes affected by E. coli using a Multilayer Perceptron (MLP)
     model. 
    • Model Development: Construct a robust MLP model for precise classification of DNA  sequences, focusing on accurately identifying the influence 
     of E. coli on  promoter genes. 
    • Application Development: Develop a user-friendly Django web application that allows users to input DNA sequences effortlessly. The application 
     should provide real-time classification results, enabling users to interpret the implications of E. coli influence on their promoter genes. 
    • User Empowerment: The final objective of the project is to empower users by providinng a seamless interface for DNA sequence analysis, facilitating
    easy  input, quick classification, and insightful interpretation of the impact of E. coli on their DNA promoter genes.
## Dataset: 
    • The dataset used for this work contains 106 instances in total, with the two classes distributed  equally, 53 being promoter sequences (positive cases)
    and  the other half being non-promoter  sequences (negative cases).  
    •  This dataset was obtained from the UCI machine learning repository collated by Towell to help  evaluate a hybrid learning algorithm, KBANN, that uses 
       examples to inductively refine pre-existing knowledge.  
    • Every instance contains 57 base-pair positions starting at position -50 and ending at position +7. 
## Neural Network Architecture Module: 
    ▪ Input Layer: Preprocessed DNA sequences. It consists of 228 nodes (57*4) 
    ▪ Output Layer: Predicted labels (promoter or non-promoter). 
    ▪ Architecture: Multilayer Perceptron (MLP) with multiple hidden layers. 
    ▪ Activation Functions: ReLU for hidden layers, sigmoid for output layer. 
    ▪ Loss Function: Binary cross-entropy. 
    ▪ Optimizer: Adam optimizer. 
    ▪ Training Process: Mini-batch gradient descent with backpropagation. 
    ▪ Evaluation: Accuracy, Precision, Recall, F1-score. 
    ➢ Explanation: 
         The MLP model will be implemented using TensorFlow/Keras. The input data will be  preprocessed to one-hot encode the DNA sequences and 
         normalize them  before  feeding into the MLP. The model will consist of multiple dense layers (hidden layers:  A hidden layer in a neural
         network is a layer that sits between the input and output  layers and is responsible for learning complex patterns and features in the data.) 
         with ReLU activation functions to capture non-linear relationships in the data. The output layer will have a sigmoid activation function to
         produce binary predictions. Indicating whether the input DNA is promoter or not. During training, the model will  minimize binary cross-entropy
         loss using the Adam optimizer.
                  
## Django Web Application Module: 
    ▪ Features:    
    o Input form for users to submit DNA sequences. 
    o Display predicted labels and probabilities. 
    ▪ Framework: Django web framework. 
    ▪ Templates: HTML templates for user interface. 
    ▪ Views: Django views for handling user requests. 
    ▪ Models: Django models for data storage (if needed). 
    ▪ Forms: Create a form for user input validation. 
    ▪ Static Files: CSS, JavaScript for styling and interactivity. 
    ➢ Explanation: 
    The Django web application will provide a user-friendly interface for users to interact with the DNA promoter classification system. The input form
    will accept DNA sequences as input, and upon submission, the predicted labels and probabilities will be displayed to the user. Django's built-in 
    features for form handling, template rendering, and view management will be utilized to develop the web application. 



## Tools Used
  ![image](https://github.com/nayana142/Promoter_Detection/assets/120770261/9058d7ea-b47d-4de8-9810-cc90750f31e6)
  




