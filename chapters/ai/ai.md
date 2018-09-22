# Artificial Intelligence Service with REST :o:

## Unsupervised Learning

Keywords: clustering, kNN, Markov Model

Unsupervised learning is a learning method when the training data is not
labeled. This problem could be more challenging because we are not
supposed to have pre-knowledge and find patterns from the data.

Unsupervised learning could be very computing intensive and it has very
complicated math principles, but very useful. In this chapter, we will
illustrate some most popular unsupervised learning algorithms and raise
examples how we apply them, which includes KMeans, k-NN, Markov Model
and others.

It is important to know that unsupervised learning is just a way how we
look at the problem. Each algorithm is just an example on how we solve a
particular problem. Before you apply an algorithm, attention should be
given to the reason why we apply a specific algorithm.

## KMeans

KMeans is one of the most straight forward unsupervised learning
algorithms.

slides [AI (40) Unsupervised Learning](https://drive.google.com/file/d/1r62DpK-yK0L_v_KEBnmP6tdLfQFD7Lok/view?usp=sharing)

## Lab:Practice on AI

Keywords: Docker, REST Service, Spark

slides
[Practice on AI (40) REST services](https://drive.google.com/file/d/1pD4zbrFKkS7d6SsxIw33NIoDHQLIedXn/view?usp=sharing)

## k-NN

k-NN is a non-parametric statistical method meaning there is no
assumption made about the distribution of the data. Additionally the
distribution is not assumed to be fixed i.e. the distribution may change
through time. These relaxed assumptions make non-parametric tests
extremely valuable when applied to real-world data as a vast majority of
real-world data have dynamic distributions though time, climate data is
an obvious example. Non-Parametric data is often ordinal which means the
variables have an inherent categorical order with unknown distances
between the categories. A common example of a non-parametric statistical
test is the sign test where values are assigned a positive or negative
sign based on being above or below the median. In k-NN predictions are
made about unknown values by matching the unknown values with similar
known values. Naturally the determination of 'similar' is of fundamental
importance. This is done through the application of the Euclidean
distance calculation given by the following equation:

$${d(\mathbf{i},\mathbf{j})} = {d(\mathbf{j},\mathbf{i})} = \sqrt{{(i_1 - j_1)^2 + (i_2 - j_2)^2 +... (i_n - j_n)^2 } }  = \sqrt{\sum_{n=1}^n(i_n - j_n)^2}$$

Now to illustrate an example of calculating similarity we put this
equation to work by exploring if a car is fast or not by using
 [\[T:fast-cars\]](#T:fast-cars){reference-type="ref"
reference="T:fast-cars"}. Lets pretend we know nothing about cars and
are asked if we think a Chevy Corvette is fast or not.


| Car Name |              Horsepower (HP) |  Racing Stripe (Yes or No)|  Fast (Yes or No)  |
|  -------------------- | ----------------- | ------------------------- | ------------------ |
| Toyota Prius            | 120      |               0               |       0          |
|  Tesla Roadster         | 288      |               0               |       1          |
|  Bugatti Veyron         | 1200     |                1              |       1          |
|  Honda Civic            | 158      |               1               |       0          |
|  Lamborghini Aventador  | 695      |               1               |       1          |

> Car make and model with associated horsepower, whether the vehicle
  has a racing stripe and if the author thinks the car is fast or
  not[]{label="T:fast-cars"}

Now lets say our friend wants to know if a Ford Mustang with a racing
stripe is fast or not. This particular friend knows nothing about cars
so decided to put analytics to work. Since a Mustang has roughly 300
horse power the closet car in our dataset to this is the Tesla Roadster
and since the Tesla is fast we would predict the Mustang to be fast.
Remember this is completely dependent on the authors initial
classification of whether a car is fast or not. Clearly the Lamborghini
and the Bugatti are fast but maybe the Tesla is not fast therefore
giving an incorrect answer. An example calculation using the Mustang and
the Tesla is given below:

$${d(\mathbf{i},\mathbf{j})}  = \sqrt{{(300 - 288)^2 + (1 - 0)^2 } }  = 12.04$$

We were able to determine the closest, or first nearest neighbor by
inspection of this data, however with a more robust dataset this may not
be the case. In these situations to find the nearest neighbor the
Euclidean distance is calculated for every unique row entry and then
ordered from smallest to largest distances, naturally the smallest
distances are the most similar. You may notice that the values of
horsepower are significantly larger in magnitude than the values
associated with racing stripes. This could be problematic in many real
world scenarios where the columns associated with large values do not
have as direct of an impact as horsepower does on the variable we are
trying to predict--a car being fast. In the case where each column value
has equal predictive power data normalization should be performed. This
is the process of centering each column to a mean of zero (0) and a
standard deviation of one (1). This is done by taking the column means
and subtracting the column means from each column entry and dividing by
the column standard deviation.

Determine for yourself if we use 2 nearest neighbors what the prediction
about the Mustang would be given the data provided what about 3, 4
nearest neighbors? What is the maximum number of k-nearest neighbors we
could have given the dataset in
 [\[T:fast-cars\]](#T:fast-cars){reference-type="ref"
reference="T:fast-cars"} ?

Calculate the Euclidean Distances for all five row entries with respect
to the Mustang.

Normalize the data and recalculate the first and second nearest
neighbors with respect to the Mustang. Does anything change?

In order to see k-NN in action we will look at an in depth example using
a dataset from the National Basketball Associated (NBA) from 2013,
naturally there are more up to date datasets but as sports analytics
becomes a significant market more and more data is becoming proprietary.
This example will pick an NBA player and determine the most similar NBA
player in the dataset to the selected player using k nearest neighbors.
The following is set up for you to execute in a python command prompt
line by line for instructional purposes.

    # This code was adopted from Dataquest - K nearest neighbors in Python:
    # A tutorial written by: Vik Paruchuri
    import pandas
    import math
    with open("/path/to/the/nba_2013.csv", 'r') as csvfile:
        nba = pandas.read_csv(csvfile)

The above portion of code uses pandas to open the downloaded csv file
and name it nba, naturally you could name the file anything. If you want
to view the columns in the csv file the following command can be used.

    print(nba.columns.values)

Now we need to select a player from the dataset, we will then determine
the most similar player to our selected player. Analysis like this is
becoming more and more prevalent in professional sports due to the large
amounts of money invested in players. Scouts may use this type of
analysis to determine who a given prospect is most similar too. This
following bit of code selects a player from the dataset. Notice that the
column player is first selected followed by the player name.

    selected_player = nba[nba["player"] == "LastName FirstName"].iloc[0]

The next step is to remove any non-numeric columns from our analysis
since we are using the Euclidean distance to calculate proximity and
strings can not be evaluated in such a way. One thing you can do if you
have columns that have values like yes and no is assign zeros and ones
accordingly. In our case we will only select the columns with numeric
values.

    numeric_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p',
    'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.',
    'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

We now have everything we need to calculate the Euclidean distance,
there are built in functions available in python to calculate this
however we will define our own as it is a straight forward computation.
It is also good practice to define your own functions whenever possible.

    def euclidean_distance(row):
        """
        Define our own Euclidean distance function
        """
        euc_distance = 0
        for k in numeric_columns:
            euc_distance += (row[k] - selected_player[k]) ** 2
        return math.sqrt(euc_distance)

Applying our function using the following command will determine the
Euclidean distance between the selected player and all other players in
the dataset.

    selected_player_distance = nba.apply(euclidean_distance, axis=1)

For sake of argument we will assume that all the data columns have equal
predictive capabilities so we wish to normalize. This will often be the
case with sports statistics as total points and field goal percentage
vary in magnitude significantly but total points does not necessarily
hold more predictive power than field goal percentage. In order to
normalize we again most only select the the numeric columns and text
columns can not be normalized in the way described above.

    nba_numeric = nba[numeric_columns]
    #apply normalization formula described above using built in python math
    #functions for the mean and standard deviation
    nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()

We can now use built in functions to calculate the nearest neighbors in
order to compare to our results attained from the above exercise. In
case you did not notice the selected_player_distance array is an array
that lists all the Euclidean distances. We will use this later to see if
the same result is obtained by using the built in functions. First we
will import the necessary libraries shown below.

    from scipy.spatial import distance

If you inspected the the selected_player_distance array you would have
noticed that there were several NaN's present this was due to having an
incomplete dataset and must be avoided. The following bit of code will
replace all NA entries with zeros.

    nba_normalized.fillna(0, inplace=True)

Using the built in Euclidean distance to determine the Euclidean
distances of all players in the data set to our selected player.

     player_normalized = nba_normalized[nba["player"] == "LastName FirstName"]
     euclidean_distances = nba_normalized.apply(lambda row:
       distance.euclidean(row, player_normalized), axis=1)

Here we create a data frame to hold the distances and then sort the
values from lowest to highest. Since our player will naturally be in the
dataset the selected player will be the lowest value, therefore the
second lowest value is associated with the player most closely related
to our selected player.

    distance_frame = pandas.DataFrame(data={"dist": euclidean_distances,
      "idx": euclidean_distances.index})
    distance_frame.sort_values("dist", inplace=True)
    second_smallest = distance_frame.iloc[1]["idx"]
    most_similar_to_player = nba.loc[int(second_smallest)]["player"]

In the python prompt type:

    most_similar_to_player 

The most similar player to your selected player should appear.

## Example Project with SVM

The following code is set up as an example project and will show how to
use a RESTful service to download data. Additionally the differences
between a dynamic and static API will be showcased. First we begin by
importing the appropriate libraries.

    import requests
    from flask import Flask
    import numpy as np
    from sklearn.externals.joblib import Memory
    from sklearn.datasets import load_svmlight_file
    from sklearn.svm import SVC
    from os import listdir
    from flask import Flask, request

Next we define three functions required to run this example: a function
to download the data; a function to partition the data; and a function
to get the data into the appropriate format once downloaded.

    app = Flask(__name__)

    def download_data(url, filename):
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

    def data_partition(filename, ratio):
        file = open(filename,'r')
        training_file=filename+'_train'
        test_file=filename+'_test'
        data = file.readlines()
        count = 0
        size = len(data)
        ftrain =open(training_file,'w')
        ftest =open(test_file,'w')
        for line in data:
            if(count< int(size*ratio)):
                ftrain.write(line)
            else:
                ftest.write(line)
            count = count + 1        

    def get_data(filename):
        data = load_svmlight_file(filename)
        return data[0], data[1]

Defining the first API endpoint with the following lines of code will
allow the user to expose the API. Prove this to yourself by opening a
browser, preferably google, and following the url below the code.

    @app.route('/')
    def index():
        return "Demo Project!"

    if __name__ == '__main__':
        app.run(debug=True)

Now Open the application in your browser with

    http://127.0.0.1:5000/

The first API endpoint we will define is the endpoint to download the
data, which is done by the following lines of code. Note the url is
hardcoded into this portion of the code as passing urls to an API is not
good practice.

    @app.route('/api/download/data')
    def download():
        url =
        'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass/glass.scale'
        download_data(url=url, filename='iris.scale')
        return "Data Downloaded"

The following three api endpoints use the data partition and get data
functions defined above. The partition function splits the datasets into
two sections--testing and training. In this example the testing portion
of the dataset is 20 % and the training is 80 % of the dataset. Later we
will explore how to make this part dynamic, allowing the user to choose
the partitioning percentage.

    @app.route('/api/data/partition')
    def partition():
        data_partition('iris.scale',0.8)
        return "Successfully Partitioned"

    @app.route('/api/get/data/test')
    def gettestdata():
        Xtest, ytest = get_data("iris.scale_test")
        
        return "Return Xtest and Ytest arrays"
        
    @app.route('/api/get/data/train')
    def gettraindata():
        Xtrain, ytrain = get_data("iris.scale_train")
        
        return "Return Xtrain and Ytrain arrays"

The last bit of code is the implementation of SVM into a RESTful API
endpoint. Again this is static and all parameters needed to tune the
algorithm are hardcoded. It will be worth your time to extrapolate the
discussion below about dynamic APIs in order to make these parameters
tunable by the user through the url.

    @app.route('/api/experiment/svm')
    def svm():
        Xtrain, ytrain = get_data("iris.scale_train")
        Xtest, ytest = get_data("iris.scale_test")

        clf = SVC(gamma=0.001, C=100, kernel='linear')
        clf.fit(Xtrain, ytrain)

        test_size = Xtest.shape[0]
        accuarcy_holder = []
        for i in range(0, test_size):
            prediction = clf.predict(Xtest[i])
            print("Prediction from SVM: "+str(prediction)+", Expected
            Label : "+str(ytest[i]))
            accuarcy_holder.append(prediction==ytest[i])

        correct_predictions = sum(accuarcy_holder)
        print(correct_predictions)
        total_samples = test_size
        accuracy =
        float(float(correct_predictions)/float(total_samples))*100
        print("Prediction Accuracy: "+str(accuracy))
        return "Prediction Accuracy: "+str(accuracy)

In order to run this you need to make a directory in a location of your
choice and create a file called main.py that has the code listed above
in it. Then simply type the following command in a terminal where you
have navigated to the location of the directory that your created.

    python main.py

A continuous version of main.py is provided below for ease of use.
Please be careful when copying and pasting as additional characters may
show up, this was noticed in the url sections.

    import requests
    from flask import Flask
    import numpy as np
    from sklearn.externals.joblib import Memory
    from sklearn.datasets import load_svmlight_file
    from sklearn.svm import SVC
    from os import listdir
    from flask import Flask, request

    app = Flask(__name__)

    def download_data(url, filename):
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)

    def data_partition(filename, ratio):
        file = open(filename,'r')
        training_file=filename+'_train'
        test_file=filename+'_test'
        data = file.readlines()
        count = 0
        size = len(data)
        ftrain =open(training_file,'w')
        ftest =open(test_file,'w')
        for line in data:
            if(count< int(size*ratio)):
                ftrain.write(line)
            else:
                ftest.write(line)
            count = count + 1        

    def get_data(filename):
        data = load_svmlight_file(filename)
        return data[0], data[1]

    @app.route('/')
    def index():
        return "Demo Project!"

    @app.route('/api/download/data')
    def download():
        url =
        'https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/multiclass/glass.scale'
        download_data(url=url, filename='iris.scale')
        return "Data Downloaded"

    @app.route('/api/data/partition')
    def partition():
        data_partition('iris.scale',0.8)
        return "Successfully Partitioned"

    @app.route('/api/get/data/test')
    def gettestdata():
        Xtest, ytest = get_data("iris.scale_test")
        
        return "Return Xtest and Ytest arrays"

    @app.route('/api/get/data/train')
    def gettraindata():
        Xtrain, ytrain = get_data("iris.scale_train")
        
        return "Return Xtrain and Ytrain arrays"

    @app.route('/api/experiment/svm')
    def svm():
        Xtrain, ytrain = get_data("iris.scale_train")
        Xtest, ytest = get_data("iris.scale_test")

        clf = SVC(gamma=0.001, C=100, kernel='linear')
        clf.fit(Xtrain, ytrain)

        test_size = Xtest.shape[0]
        accuarcy_holder = []
        for i in range(0, test_size):
            prediction = clf.predict(Xtest[i])
            print("Prediction from SVM: "+str(prediction)+", Expected
            Label : "+str(ytest[i]))
            accuarcy_holder.append(prediction==ytest[i])

        correct_predictions = sum(accuarcy_holder)
        print(correct_predictions)
        total_samples = test_size
        accuracy =
        float(float(correct_predictions)/float(total_samples))*100
        print("Prediction Accuracy: "+str(accuracy))
        return "Prediction Accuracy: "+str(accuracy)

    if __name__ == '__main__':
        app.run(debug=True)

As mentioned above these these are examples of static API endpoints. In
many scenarios having a dynamic API would be preferred. Lets explore the
data partition endpoint and modify the code for the static version to
make a dynamic version. Below is the function definition for the dynamic
version of the data_partition function, and not much has changed. The
only change made was that stings were appended to the testing and
training file names for convenience. The ratio will match the user
defined ratio entered through the url.

    def data_partition(filename, ratio):
        file = open(filename,'r')
        training_file=filename+'_train_'+str(ratio)
        test_file=filename+'_test_'+ str(ratio)
        data = file.readlines()
        count = 0
        size = len(data)
        ftrain =open(training_file,'w')
        ftest =open(test_file,'w')
        for line in data:
            if(count< int(size*ratio)):
                ftrain.write(line)
            else:
                ftest.write(line)
            count = count + 1 

Now for defining the endpoint, naturally it starts the same way as the
static version however now we must add a part that allows for the user
to enter values. This is done by use of brackets \< text \>.

    @app.route('/api/data/partition/<filename>/ratio/<ratio>')
    def partition(filename,ratio):
        ratio = float(ratio)
        path='data/'+filename
        data_partition(path,ratio)
        return "Successfully Partitioned"
