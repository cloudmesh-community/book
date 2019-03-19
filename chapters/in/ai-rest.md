# Artificial Intelligence Service with REST

## Machine Learning on Text using Naive Bayes Algorithm

Naive Bayes is a simple yet powerful classification machine learning algorithm.
In this section we demonstrate the implementation of Naive Bayes 
algorithm on text documents to classify a review as positive or negative.

Example setup:

Training data: 

We will utilize a pre-processed training data with labels attached to each review as 
*positive* or *negative*  The data can be downlaoded [here](https://azuremallikresourcediag.blob.core.windows.net/mltest/ProcessedTrain.csv).

Test data:

Test data is available [here](https://azuremallikresourcediag.blob.core.windows.net/mltest/testSet.txt).
Test data file has been setup in such a way that first 2989 reviews are positive and from 2990 to 4321 are negative.
Test data needs to pre-processed and the file needs to cleaned before the algorithm is implemented.
After the test data is cleaned, we will label the test data as per the information given.
Finally, we will implement Multinomial Naive Bayes classifier algorithm and calculate the accuracy of the test prediction.

Before we start, note that, to implement machine learning algorithm on text documents we will use  
scikit-learn feature extraction modules. Please refer to related documentation
in the following link for details - [Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html).

For the current example we will use the following specific modules:

```python
sklearn.feature_extraction.text.CountVectorizer
sklearn.feature_extraction.text.TfidfTransformer
```



