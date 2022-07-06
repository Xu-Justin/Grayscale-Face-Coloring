# Grayscale-Face-Coloring
A generative model that could generate colored face images from grayscale face images.

<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578655-a8bb1aa1-ad94-4f4e-97ac-5d83008e8aa5.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578663-a60c32de-a2e6-42d1-b4c2-7bb2ae34e78e.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578667-13d4b4df-619d-401e-ad16-03e002d87615.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578673-d9101dee-b99b-4f7e-b660-66e329f83504.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578675-d4fd793d-3365-4d69-b185-ead16fe8beb7.jpg"></td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578602-43dafd34-9971-4f25-8bc1-68e8411d24cd.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578607-ef235e45-d7e0-44ff-bab6-072dd52711e3.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578611-89c99c02-d550-436a-909d-bdc935871cdb.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578614-b3e78817-ed4c-4691-8d13-e2aba7ed85f4.jpg"></td>
    <td><img src="https://user-images.githubusercontent.com/56458008/177578619-5fcd8b06-1a92-465d-8a2a-7fc4c4125fbc.jpg"></td>
  </tr>
</table>

Read full report about this project on this [PDF](https://drive.google.com/uc?export=download&id=1T2DBn8IIyOW_ubgOtJ6KG4emHlDgPwtN).

---

#### Download Dataset
The dataset is take from [This Person Does Not Exist](https://thispersondoesnotexist.com/) using [unofficial "API" by David Lorenzo](https://github.com/David-Lor/ThisPersonDoesNotExistAPI). The dataset has been uploaded and is available to download at [Kaggle](https://www.kaggle.com/almightyj/person-face-dataset-thispersondoesnotexist). Run the following code to download the dataset from Kaggle.

    %run Dataset/import_dataset.py

#### Download Trained Model
The model has been trained for 30 epochs (30K iterations) using the 80% of dataset above. Run the following code to download the trained model.


	%run Resources/model_saved/import_trained_model.py

---

Authored by William Justin.
