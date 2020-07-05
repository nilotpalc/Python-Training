### What is the difference between KNN and Logistic Regression ?
K-Nearest-Neighbours and Logistics Regression are used to classify an outcome linked to set of attributes into categories.
Logistic Regression  
The KNN method follows a Euclidean distance (minimizing the distance from k-points) and applying majority votes on the selected k-data points between classes to classify a given object with a pre-determined set of attributes.

Att.A|Att.B|Att.C|Att.D|Class
----|----|----|----|----|----
10|20|24|35|0
30|40|24|65|1
100|200|240|350|0
150|230|140|250|1

KNN table classes can have more than 2 classes and we can use class-notation in numerals as [0,1,2] for 3 classes or more, as needed.

>KNN performs better with a lower number of features than a large
number of features. You can say that when the number of features
increases than it requires more data. Increase in dimension also leads
to the problem of overfitting. To avoid overfitting, the needed data
will need to grow exponentially as you increase the number of
dimensions. This problem of higher dimension is known as the Curse of Dimensionality. [Article Link](https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn)

>Denser Data is more hopeful as compared to the widely distributed data for classification algorithm [Link here](https://www.mathworks.com/matlabcentral/answers/373364-can-k-nearest-neighbor-classify-more-than-two-classes#comment_517121)

**Another important point to remember is that KNN is better used when the existence of a pattern of attributes leads to an outcome with the probability of close to 1.0 associated with one of the classification categories.**  

**Classification is best used with non-stochastic/deterministic outcomes that occur frequently, and not when two individuals with identical inputs can easily have different outcomes. For the latter, modeling tendencies (i.e., probabilities) is key.**

A good read elaborating on classification and prediction (linked to logistic regression) is available [here](https://www.fharrell.com/post/classification/)

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTA4OTczNjQ4XX0=
-->