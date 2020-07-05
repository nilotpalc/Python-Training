---


---

<h3 id="what-is-the-difference-between-knn-and-logistic-regression-">What is the difference between KNN and Logistic Regression ?</h3>
<p>K-Nearest-Neighbours and Logistics Regression are used to classify an outcome linked to set of attributes into categories.<br>
Logistic Regression<br>
The KNN method follows a Euclidean distance (minimizing the distance from k-points) and applying majority votes on the selected k-data points between classes to classify a given object with a pre-determined set of attributes.</p>

<table>
<thead>
<tr>
<th>Att.A</th>
<th>Att.B</th>
<th>Att.C</th>
<th>Att.D</th>
<th>Class</th>
</tr>
</thead>
<tbody>
<tr>
<td>10</td>
<td>20</td>
<td>24</td>
<td>35</td>
<td>0</td>
</tr>
<tr>
<td>30</td>
<td>40</td>
<td>24</td>
<td>65</td>
<td>1</td>
</tr>
<tr>
<td>100</td>
<td>200</td>
<td>240</td>
<td>350</td>
<td>0</td>
</tr>
<tr>
<td>150</td>
<td>230</td>
<td>140</td>
<td>250</td>
<td>1</td>
</tr>
</tbody>
</table><p>KNN table classes can have more than 2 classes and we can use class-notation in numerals as [0,1,2] for 3 classes or more, as needed.</p>
<blockquote>
<p>KNN performs better with a lower number of features than a large<br>
number of features. You can say that when the number of features<br>
increases than it requires more data. Increase in dimension also leads<br>
to the problem of overfitting. To avoid overfitting, the needed data<br>
will need to grow exponentially as you increase the number of<br>
dimensions. This problem of higher dimension is known as the Curse of Dimensionality. <a href="https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn">Article Link</a></p>
</blockquote>
<blockquote>
<p>Denser Data is more hopeful as compared to the widely distributed data for classification algorithm <a href="https://www.mathworks.com/matlabcentral/answers/373364-can-k-nearest-neighbor-classify-more-than-two-classes#comment_517121">Link here</a></p>
</blockquote>
<p><strong>Another important point to remember is that KNN is better used when the existence of a pattern of attributes leads to an outcome with the probability of close to 1.0 associated with one of the classification categories.</strong></p>
<p><strong>Classification is best used with non-stochastic/deterministic outcomes that occur frequently, and not when two individuals with identical inputs can easily have different outcomes. For the latter, modeling tendencies (i.e., probabilities) is key.</strong></p>
<p>A good read elaborating on classification and prediction (linked to logistic regression) is available <a href="https://www.fharrell.com/post/classification/">here</a></p>

