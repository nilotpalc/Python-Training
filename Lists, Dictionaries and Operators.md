---


---

<h5 id="formatting-tips-for-markdown-cells">Formatting Tips for Markdown Cells</h5>
<p><a href="https://www.datacamp.com/community/tutorials/markdown-in-jupyter-notebook">https://www.datacamp.com/community/tutorials/markdown-in-jupyter-notebook</a><br>
<a href="https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html#Embedded-code">https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html#Embedded-code</a></p>
<h4 id="create-a-list-from-an-existing-list-by-division">Create a List from an Existing List by DIVISION</h4>
<p>Generate a list using  <strong>FOR</strong>  and  <strong>Range</strong>  function<br>
The below image also highlights the use of  <code>append</code>  code</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token comment"># Using the above logic to generate a list of numbers from a range</span>
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
<h1 id="solving-the-same-problem-with-different-code-solutions">Solving the same problem with different code solutions</h1>
<p><a href="https://gist.github.com/nilotpalc/0b1c7285292e479d809415626e0c2595">https://gist.github.com/nilotpalc/0b1c7285292e479d809415626e0c2595</a></p>
<p>We can add elements to a dictionary using <code>dict['keyname]=value</code> . The value can be an integer or a string.<br>
We can delete items from a dictionary using <code>dict.pop(keyname)</code> . This removes the key-value logic from the dictionary.<br>
<a href="https://thispointer.com/different-ways-to-remove-a-key-from-dictionary-in-python/">Info Link on .pop()</a></p>
<p>Indexing any item from a list or a tuple returns an output which is a single value or a one-item list. If we need to use the same, it will need to be converted into a list using the <code>list(outputvariable)</code> function. Also, the <code>list</code> function cannot reference multiple arguments but can only take a single input which could be a value or variable (preferably variable when using to define functions).</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token comment"># Input</span>
lisin <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span><span class="token number">2</span><span class="token punctuation">,</span><span class="token number">3</span><span class="token punctuation">]</span>
lisin<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span> 
<span class="token comment"># Output</span>
<span class="token number">2</span>
<span class="token comment"># Input</span>
<span class="token builtin">type</span><span class="token punctuation">(</span>lisin<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span><span class="token punctuation">)</span>
<span class="token comment"># Output</span>
<span class="token builtin">int</span>
</code></pre>
<p>In case the above returned a string input, running sum operations based on the above will lead to a string rather than a list.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token comment"># Input</span>
lisin <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token string">'a'</span><span class="token punctuation">,</span><span class="token string">'b'</span><span class="token punctuation">,</span><span class="token string">'c'</span><span class="token punctuation">]</span>
lisin<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token operator">+</span>lisin<span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">]</span>
<span class="token comment"># Output</span>
<span class="token string">'ab'</span>
</code></pre>
<blockquote>
<p>This mistake was done during the Tic-Tac-Toe assignment where the above operation was expected to generate a list [a,b] which created errors in coding. The right way was <code>list(lisin[0]+lisin[1])</code></p>
</blockquote>
<p>This basically breaks the string ab into its constituent elements at a character level. If we had a sentence, we use <code>.split()</code> to break it based on spaces to get a list of words.</p>
<blockquote>
<p>Important Note <br> It is important to note that appending to a list or popping the item from the list changes the parent list itself. There is no need to assign another variable name to the <code>list.append(input)</code> OR <code>list.pop(input)</code>statement.</p>
</blockquote>
<h4 id="but-remember">But Remember</h4>
<p>Slicing from the list returns a list and not a value</p>
<p>One of the ways to connect variable names to items in a list or tuple is as follows -</p>
<pre class=" language-python"><code class="prism  language-python">x<span class="token punctuation">,</span>y<span class="token punctuation">,</span>z <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token string">'a'</span><span class="token punctuation">,</span><span class="token string">'b'</span><span class="token punctuation">,</span><span class="token string">'c'</span><span class="token punctuation">]</span>
x<span class="token punctuation">,</span>y<span class="token punctuation">,</span>z <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token string">'a'</span><span class="token punctuation">,</span><span class="token string">'b'</span><span class="token punctuation">,</span><span class="token string">'c'</span><span class="token punctuation">)</span>
<span class="token comment"># The above cases show a list and tuple where the variable name x,y,z are automatically linked to a,b,c</span>
</code></pre>

