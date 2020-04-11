---


---

<h5 id="formatting-tips-for-markdown-cells">Formatting Tips for Markdown Cells</h5>
<p><a href="https://www.datacamp.com/community/tutorials/markdown-in-jupyter-notebook">https://www.datacamp.com/community/tutorials/markdown-in-jupyter-notebook</a><br>
<a href="https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html#Embedded-code">https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html#Embedded-code</a></p>
<h4 id="create-a-list-from-an-existing-list-by-division">Create a List from an Existing List by DIVISION</h4>
<p>Generate a list using  <strong>FOR</strong>  and  <strong>Range</strong>  function<br>
The below image also highlights the use of  <code>append</code>  code</p>
<pre class=" language-python"><code class="prism  language-python">
<span class="token comment"># Using the above logic to generate a list of numbers from a range</span>
<span class="token comment"># Calculations can also be performed for individual iterations</span>
abc <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
<span class="token keyword">for</span> item <span class="token keyword">in</span> <span class="token builtin">range</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span><span class="token number">101</span><span class="token punctuation">,</span><span class="token number">20</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	abc<span class="token punctuation">.</span>append<span class="token punctuation">(</span>item<span class="token operator">/</span><span class="token number">100</span><span class="token punctuation">)</span>
<span class="token keyword">print</span><span class="token punctuation">(</span>abc<span class="token punctuation">)</span>
</code></pre>
<h4 id="using--for-loop-for-dictionary-and-tuple-unpacking">Using  <code>For</code> loop for Dictionary and Tuple Unpacking</h4>
<p>Normal Use:</p>
<pre class=" language-python"><code class="prism  language-python">d<span class="token operator">=</span><span class="token punctuation">{</span><span class="token string">'a'</span><span class="token punctuation">:</span><span class="token number">1</span><span class="token punctuation">,</span><span class="token string">'b'</span><span class="token punctuation">:</span><span class="token number">2</span><span class="token punctuation">,</span><span class="token string">'c'</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">,</span><span class="token string">'d'</span><span class="token punctuation">:</span><span class="token number">4</span><span class="token punctuation">,</span><span class="token string">'e'</span><span class="token punctuation">:</span><span class="token number">5</span><span class="token punctuation">}</span>
<span class="token keyword">for</span> item <span class="token keyword">in</span> d<span class="token punctuation">:</span>
    <span class="token keyword">print</span> <span class="token punctuation">(</span>item<span class="token punctuation">)</span> <span class="token comment"># Prints the Keys Only</span>
</code></pre>
<p>Dictionary Unpacking Code:</p>
<pre class=" language-python"><code class="prism  language-python">
<span class="token comment"># Dictionary Unpacking helps to seek the relevant key or value</span>
d<span class="token operator">=</span><span class="token punctuation">{</span><span class="token string">'a'</span><span class="token punctuation">:</span><span class="token number">1</span><span class="token punctuation">,</span><span class="token string">'b'</span><span class="token punctuation">:</span><span class="token number">2</span><span class="token punctuation">,</span><span class="token string">'c'</span><span class="token punctuation">:</span><span class="token number">3</span><span class="token punctuation">,</span><span class="token string">'d'</span><span class="token punctuation">:</span><span class="token number">4</span><span class="token punctuation">,</span><span class="token string">'e'</span><span class="token punctuation">:</span><span class="token number">5</span><span class="token punctuation">}</span>
<span class="token keyword">for</span> i<span class="token punctuation">,</span>v <span class="token keyword">in</span> d<span class="token punctuation">.</span>items<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">print</span> i   <span class="token comment"># will print the key value</span>
	<span class="token keyword">print</span> v   <span class="token comment"># will print the key value</span>
</code></pre>
<h4 id="using--enumerate-code">Using  <code>Enumerate</code> Code</h4>

