# Grayscale-Face-Coloring
Given a grayscale facial image as the input, then the deep learning model will try to generate a colored version of the image as the output.

Read full reports about this project on this [PDF](https://drive.google.com/uc?export=download&id=1T2DBn8IIyOW_ubgOtJ6KG4emHlDgPwtN).

---

#### Download Dataset
The dataset is take from [This Person Does Not Exist](https://thispersondoesnotexist.com/) using [unofficial "API" by David Lorenzo](https://github.com/David-Lor/ThisPersonDoesNotExistAPI). The dataset has been uploaded and is available to download at [Kaggle](https://www.kaggle.com/almightyj/person-face-dataset-thispersondoesnotexist). Run the following code to download the dataset from Kaggle.

    %run Dataset/import_dataset.py

#### Download Trained Model
The model has been trained for 30 epochs (30K iterations) using the 80% of dataset above. Run the following code to download the trained model.


	%run Resources/model_saved/import_trained_model.py

---

Authored by William Justin.
