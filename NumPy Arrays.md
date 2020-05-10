---


---

<h2 id="numpy-array">NumPy Array</h2>
<p>Use the below import logic</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> numpy <span class="token keyword">as</span> np
np<span class="token punctuation">.</span>array<span class="token punctuation">(</span>listname<span class="token punctuation">)</span> <span class="token comment"># generates a 1-d array structure with 1 row and n columns</span>
np<span class="token punctuation">.</span>array<span class="token punctuation">(</span><span class="token punctuation">[</span>list1<span class="token punctuation">,</span>list2<span class="token punctuation">,</span>list3<span class="token punctuation">]</span><span class="token punctuation">)</span> <span class="token comment"># generates a matrix; note the use of square brackets to enclose the lists</span>
</code></pre>
<p>The above indicates that the input type will be a <strong>list of lists</strong> to create a <em>Matrix</em> structure</p>
<p>Other array generating functions</p>
<pre class=" language-python"><code class="prism  language-python">np<span class="token punctuation">.</span>arange<span class="token punctuation">(</span>start<span class="token punctuation">,</span>stop<span class="token punctuation">,</span> step<span class="token punctuation">)</span> <span class="token comment"># generates an array of numbers between start</span>
<span class="token comment"># and stop excluding stop</span>

np<span class="token punctuation">.</span>linspace<span class="token punctuation">(</span>start<span class="token punctuation">,</span>stop<span class="token punctuation">,</span> n<span class="token punctuation">)</span> <span class="token comment"># generates an array of 'n' numbers (float type) </span>
<span class="token comment"># between start and stop inclusive</span>

np<span class="token punctuation">.</span>linspace <span class="token punctuation">(</span>start<span class="token punctuation">,</span>stop<span class="token punctuation">,</span>n<span class="token punctuation">,</span>dtype <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">)</span> <span class="token comment"># generates an output of integer values only</span>
</code></pre>
<p><code>linspace</code> means linearly spaced</p>
<p>Stackflow link to using dtype for integer <a href="https://stackoverflow.com/q/36064207/13218820">Link</a></p>
<h3 id="using-random-function-to-generate-arrays-with-random-numbers">Using random function to generate arrays with random numbers</h3>
<p>The below functions are defined under the module ‘random’ within ‘numpy’ package</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> numpy <span class="token keyword">as</span> np
np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>rand<span class="token punctuation">(</span>y<span class="token punctuation">)</span> <span class="token comment"># generates 1D array of 1 row and y columns</span>
<span class="token comment"># with values between 0 and 1</span>

np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>rand<span class="token punctuation">(</span>x<span class="token punctuation">,</span>y<span class="token punctuation">)</span> <span class="token comment"># generates 2D array of x rows and y columns</span>
<span class="token comment"># with values between 0 and 1</span>

np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>randn<span class="token punctuation">(</span>x<span class="token punctuation">)</span> <span class="token comment"># generates 1D array of 1 row and y columns</span>
<span class="token comment"># from normal distribution with mean 0 and standard deviation 1</span>

np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>randn<span class="token punctuation">(</span>x<span class="token punctuation">,</span>y<span class="token punctuation">)</span> <span class="token comment"># generates 2D array of x rows and y columns</span>

np<span class="token punctuation">.</span>random<span class="token punctuation">.</span>randint<span class="token punctuation">(</span>low<span class="token punctuation">,</span>high<span class="token punctuation">,</span>n<span class="token punctuation">)</span> <span class="token comment"># generates 'n' random numbers</span>
<span class="token comment"># in a 1D array</span>
</code></pre>
<p>In case the size n is more than the numbers within the range, the function duplicates the elements within the range to complete size ‘n’ . This is with reference to <code>linspace</code> and <code>randint</code> commands</p>
<h3 id="reshaping-1d-arrays">Reshaping 1D Arrays</h3>
<pre class=" language-python"><code class="prism  language-python">arrname<span class="token punctuation">.</span>reshape<span class="token punctuation">(</span>x<span class="token punctuation">,</span>y<span class="token punctuation">)</span>
<span class="token comment"># the setup always considers the array as 1D and then,</span>
<span class="token comment"># renders it as suggested based on x,y arguments</span>
<span class="token comment"># Check the Colab link</span>

</code></pre>
<p>Other functions are -</p>
<pre class=" language-python"><code class="prism  language-python">arrname<span class="token punctuation">.</span><span class="token builtin">max</span><span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># returns the max value in the array</span>
arrname<span class="token punctuation">.</span>argmax<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># returns the position of the max value assuming the</span>
<span class="token comment"># array is 1D</span>
arrname<span class="token punctuation">.</span><span class="token builtin">min</span><span class="token punctuation">(</span><span class="token punctuation">)</span>
arrname<span class="token punctuation">.</span>argmin<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>
<p>Github <a href="https://github.com/nilotpalc/Python-Training/blob/master/Numpy_Arrays.ipynb">Link</a></p>
<h2 id="numpy-indexing-and-slicing">NumPy Indexing and Slicing</h2>
<p>Indexing different types of array</p>
<pre class=" language-python"><code class="prism  language-python">arrname <span class="token punctuation">[</span>x<span class="token punctuation">]</span> <span class="token comment"># x indicates index position of the output value</span>
arrname <span class="token punctuation">[</span>row<span class="token punctuation">,</span>col<span class="token punctuation">]</span> <span class="token comment"># returns single value at the junc of row and column in 2D array/matrix</span>
arrname <span class="token punctuation">[</span>x<span class="token punctuation">;</span>y<span class="token punctuation">,</span>a<span class="token punctuation">:</span>b<span class="token punctuation">]</span> <span class="token comment"># returns a sub-matrix within a 2D array/matrix</span>
arrname <span class="token punctuation">[</span>arrname <span class="token operator">&gt;</span> num<span class="token punctuation">]</span> <span class="token comment"># returns 1D array with True conditions met inside #arrname array</span>
</code></pre>
<h3 id="broadcasting-an-array">Broadcasting an Array</h3>
<p>This works within a 1D array</p>
<pre class=" language-python"><code class="prism  language-python">arrname<span class="token punctuation">[</span>a<span class="token punctuation">,</span>b<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token number">9</span> <span class="token comment"># this changes the current set of values indexed between a and b positions to be equal to 9; </span>
<span class="token comment"># the change is reflected permanently within arrname array</span>
</code></pre>
<h3 id="copying-an-array">Copying an Array</h3>
<pre class=" language-python"><code class="prism  language-python">arr_na <span class="token operator">=</span> arrname<span class="token punctuation">.</span>copy<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token comment"># this creates a new array arr_na which is an exact copy of arrname</span>
</code></pre>
<h2 id="numpy-operations">NumPy Operations</h2>

<table>
<thead>
<tr>
<th>Operation</th>
<th align="center">Standard</th>
<th align="right">Built-in Func</th>
</tr>
</thead>
<tbody>
<tr>
<td>Addition</td>
<td align="center">arr1 + arr2</td>
<td align="right">np.add (arr1,arr2)</td>
</tr>
<tr>
<td>Subtraction</td>
<td align="center">arr1 - arr2</td>
<td align="right">np.subtract (arr1,arr2)</td>
</tr>
<tr>
<td>Multiplication</td>
<td align="center">arr1 * arr2</td>
<td align="right">np.multiply (arr1,arr2)</td>
</tr>
<tr>
<td>Scalar Addition</td>
<td align="center">arr1 + 10</td>
<td align="right">np.add (arr1,10)</td>
</tr>
<tr>
<td>Scalar Multiplication</td>
<td align="center">arr1 * 10</td>
<td align="right">np.multiply (arr1,10)</td>
</tr>
<tr>
<td>Power</td>
<td align="center">arr1 **2</td>
<td align="right">np.add (arr1,arr2)</td>
</tr>
</tbody>
</table><pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> numpy <span class="token keyword">as</span> np
np<span class="token punctuation">.</span>function<span class="token punctuation">(</span>array1<span class="token punctuation">,</span>array2<span class="token punctuation">)</span>
<span class="token comment"># using built-in functions in code writing</span>
</code></pre>
<p>More functions can be found in the documentation at this <a href="https://docs.scipy.org/doc/numpy/reference/ufuncs.html">link</a></p>

