# PruebaTecnicaArkangelAI

Este repositorio se creo con el objetivo de contener los archivos correspondientes a la resolucion de la prueba tecnica para Arkangel AI #AIChallenge.
Este reto contenia los siguientes requerimientos:

# AI-Challenge
This is a repo for an open AI challenge held by Arkangel AI. The problems stands as follows:

> As a Machine Learning Engineer at Arkangel AI, you receive a project from a biometric data company. This project aims to develop a computer vision model to be able to recognize the workers of a company while detecting the emotion or feeling of each individual. The biometric data company that hires Arkangel AI only imposes two requirements, which are: First, the number of workers will be fixed and to obtain a database, each individual can be asked for several photographs with which to develop the model. And as a second, the developed model must be deployed in the cloud to be able to make inferences to it, from any physical point where the system is deployed. However, this deployment can be done programmatically or through a UI, as Arkangel AI provides.

Para este reto se hizo uso del DATASET FER2013

* Fer2013 dataset is a common dataset used for facial expression recognition. The dataset contains 35,887 grayscale facial images containing 7 different emotions (anger, disgust, fear, happiness, neutral, sad, and surprise).

* VGG19 is a deep learning model known as the Convolutional Neural Network (CNN) architecture. The VGG19 model has 19 layers and consists of 16 layers of convolutional layers and 3 layers of fully connected layers. Convolutional layers extract features from the input image using filters.

* Transfer learning can be performed using the pre-trained weights of the VGG19 model. Transfer learning is the use of the weights of a pre-trained model to help solve a problem in a new dataset.

* For the VGG19 model, pre-trained weights are often used to classify images in the ImageNet dataset. Therefore, the last layer of the VGG19 model is retrained to make it suitable for facial expressions in the fer2013 dataset.

* The last layer of the VGG19 model consists of fully connected layers. These layers are used to classify facial expressions in the dataset. Since there are 7 different emotion classes in the Fer2013 dataset, the last layer of the VGG19 model is retrained to have a 7-output classifier.

* Retraining of the VGG19 model is performed with multiple epochs to achieve higher accuracy rates. An epoch is a complete scan of the training data by the model once.

* During training, performance metrics such as model accuracy and loss are tracked. At the end of the training, the accuracy of the model is evaluated by its performance on the test data.
* The VGG19 model gives very good results for the classification of facial expressions in the Fer2013 dataset. However, there may be imbalance between classes in the dataset. Therefore, taking into account the imbalance of training data between classes can help improve the performance of the model.
 
* To further improve the performance of the model, data preprocessing techniques can be used. For example, the sizes of faces in the dataset can be standardized and filtering techniques can be applied to reduce noise.
 depending on the characteristics of the data set and the problem area.
 
* Finally, different metrics can be used to evaluate the performance of the model. For example, metrics such as accuracy, sensitivity, specificity, F1 score, and ROC curve can help evaluate model performance from different perspectives.

![](https://www.researchgate.net/publication/349055345/figure/fig3/AS:987834383085568@1612529478973/FER-2013-sample-images-for-facial-emotion-recognition.jpg)
