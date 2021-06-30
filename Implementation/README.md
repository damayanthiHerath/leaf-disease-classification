## Image dataset

The models are trained using images collected from the PlantVillage dataset. The PlantVillage dataset consists of 54303 healthy and unhealthy leaf images divided into 38 categories by species and disease.
Tomato crop leaf diseases dataset is selected from the dataset to train the models. From the 9 different disease classes, 4 diseases classes were selected which has affected the most in Sri Lanka's tomato cultivation.
  
Tomato leaf images belonging to 5 classes has been used as the following list.
  - Healthy class 	
  - Bacterial spot disease class
  - Late blight disease class
  - Septoria leaf spot disease class
  - Yellow leaf curl virus class

## Image split ratios 

* Number of images per class = 1591 (maximum number of images such that each class contain same amount of images)

| Train(80%)    | Validation(10%) | Test(10%)      |
|:-------------:|:---------------:|:--------------:|
| 6360 images   | 795 images      | 800 images     |

## Hyperparamters

* Image input size = 224x224x3
* Batch size = 32
* Optimizer = Adam optimizer
* Loss function = Categorical cross entropy
* Learning rate = 0.0001
* number of epochs = 15


