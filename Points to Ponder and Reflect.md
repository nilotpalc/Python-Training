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
<h3 id="decision-trees-and-random-forests">Decision Trees and Random Forests</h3>
<ol>
<li>Data needs to be split based on attributes that can provide a clean split (Entropy and Information Gain math)</li>
<li>Random Forest technique tries to use sample data containing <code>m</code> number of attributes against a total of <code>p</code> attributes to create a MECE decision tree<br>
<span class="katex--inline"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>m</mi><mo>=</mo><msqrt><mi>p</mi></msqrt></mrow><annotation encoding="application/x-tex">m = \sqrt{p}</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.43056em; vertical-align: 0em;"></span><span class="mord mathdefault">m</span><span class="mspace" style="margin-right: 0.277778em;"></span><span class="mrel">=</span><span class="mspace" style="margin-right: 0.277778em;"></span></span><span class="base"><span class="strut" style="height: 1.04em; vertical-align: -0.33694em;"></span><span class="mord sqrt"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 0.70306em;"><span class="svg-align" style="top: -3em;"><span class="pstrut" style="height: 3em;"></span><span class="mord" style="padding-left: 0.833em;"><span class="mord mathdefault">p</span></span></span><span class="" style="top: -2.66306em;"><span class="pstrut" style="height: 3em;"></span><span class="hide-tail" style="min-width: 0.853em; height: 1.08em;"><svg width="400em" height="1.08em" viewBox="0 0 400000 1080" preserveAspectRatio="xMinYMin slice"><path d="M95,702c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,
-10,-9.5,-14c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54c44.2,-33.3,65.8,
-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10s173,378,173,378c0.7,0,
35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429c69,-144,104.5,-217.7,106.5,
-221c5.3,-9.3,12,-14,20,-14H400000v40H845.2724s-225.272,467,-225.272,467
s-235,486,-235,486c-2.7,4.7,-9,7,-19,7c-6,0,-10,-1,-12,-3s-194,-422,-194,-422
s-65,47,-65,47z M834 80H400000v40H845z"></path></svg></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.33694em;"><span class=""></span></span></span></span></span></span></span></span></span></li>
</ol>
<p><em>Random Forests are better equipped and assumed to be more accurate than Decision Trees</em></p>

