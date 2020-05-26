---


---

<h2 id="main-code">Main Code</h2>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> matplotlib
<span class="token keyword">import</span> matplotlib<span class="token punctuation">.</span>pyplot <span class="token keyword">as</span> plt
fig<span class="token punctuation">,</span>axes <span class="token operator">=</span> plt<span class="token punctuation">.</span>subplots<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token comment"># the above commands set the canvas </span>
<span class="token comment"># for plotting the graphs</span>
</code></pre>
<p>Axes is an object on which the x-axis variable is plotted. This only sets the space through the four main parameters</p>
<ol>
<li>Left Margin</li>
<li>Bottom Margin</li>
<li>Width</li>
<li>Height<br>
All the above are set between 0 and 1. Note that Left + Width, if exceeding 1 means that the visual will go out of view, same goes for Bottom + Height.</li>
</ol>
<blockquote>
<p>The axes design is set through default settings once the above command is called and need not be changed</p>
</blockquote>
<h4 id="focus-on-running-the-data-transformation-operations-in-excel-powerpivot">Focus on running the data transformation operations in Excel, PowerPivot</h4>
<p>Running the dataplots with specific legend requirements can be done using the <code>for</code> loop based on the legend column<br>
The example is available <a href="https://gist.github.com/nilotpalc/3a440e56b54acbc4bed8e2c0760769b9">here</a></p>
<blockquote>
<p>The input to various plots can be in the form of a list or array.<br>
Hence, we can use commands like <code>df[col].unique()</code> to plot the x-axis<br>
while using <code>df[col]</code> to plot the y-axis. Also, note we can also use<br>
conditional selection to select the y-axis <code>df[df[col] &gt; a][col3]</code>.<br>
<strong>Point to remember - Use the independent columns for creating the plots. Focus on generating the complete dataframe through excel and use Python as a wrapper for plotting</strong></p>
</blockquote>

