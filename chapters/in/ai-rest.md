# Artificial Intelligence Service with REST

## Naive Bayes Algorithm for Text classification

Naive Bayes is a simple yet powerful classification machine learning algorithm.
In this section we demonstrate the implementation of Naive Bayes algorithm 
on text documents in a RESTful service to classify a review as positive or negative.

Example setup: In this example we will consider a text document containing  
reviews of a restaurant. Data is split into two datasets - 
training dataset and test datset. Following are details of the datasets: 

* Training data: We will utilize a pre-processed training dataset with labels attached 
to each review as *positive* or *negative*.  Training data can be downloaded [here](https://azuremallikresourcediag.blob.core.windows.net/mltest/ProcessedTrain.csv).

* Test data: Test data is available 
[here](https://azuremallikresourcediag.blob.core.windows.net/mltest/testSet.txt).
Test dataset has been setup in such a way that first 2989 reviews are positive and 
rows from 2990 to 4321 are negative reviews. Test data needs to pre-processed and 
cleaned before the algorithm is implemented. After the test data is cleaned, 
we will label the test data as per the information given. Finally, we will implement 
Multinomial Naive Bayes classifier algorithm and calculate the accuracy of the 
test prediction.

To implement machine learning algorithm on text documents we will use 
scikit-learn feature extraction modules. Please refer to related documentation 
in the following link - 
[Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html).

For the current example we will use the following specific modules:

```python
sklearn.feature_extraction.text.CountVectorizer
sklearn.feature_extraction.text.TfidfTransformer
```

Solution will be implemented in following steps:

* **Step-1:** Define a function to pre-process Test dataset.
* **Step-2:** Define a function to implement Niave Bayes algorithm.
* **Step-3:** Define an OpenAPI speficification in a YAML file. 
The specification will have endpoints for the following:
  * Pre-processing Test data
  * Build Naive Bayes classification model and return test accuracy
* **Step-4:** Create a simple module to use the connexion service and read 
in the specification from the yaml file.




