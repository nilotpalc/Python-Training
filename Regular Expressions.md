---


---

<p>Main Functions under Regular Expressions</p>
<h2 id="search">search</h2>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> re 
re<span class="token punctuation">.</span>search <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span> 
<span class="token comment"># use with start() and end () to return starting position</span>
<span class="token comment"># and the next position where the text ends </span>

re<span class="token punctuation">.</span>search <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">.</span>start<span class="token punctuation">(</span><span class="token punctuation">)</span> 
re<span class="token punctuation">.</span>search <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">.</span>end<span class="token punctuation">(</span><span class="token punctuation">)</span>

</code></pre>
<p>To search for a word within the phrase, use the <code>\\b&lt;character&gt;\\b</code> in the string along with prefix <code>r</code></p>
<pre class=" language-python"><code class="prism  language-python">phrase <span class="token operator">=</span> "This <span class="token keyword">is</span> an example sentence<span class="token punctuation">,</span> \
it <span class="token keyword">is</span> <span class="token keyword">for</span> demonstration only"
<span class="token keyword">print</span> <span class="token punctuation">(</span>re<span class="token punctuation">.</span>search<span class="token punctuation">(</span>r<span class="token string">'\\bThis is\\b'</span><span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">.</span>start<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>

</code></pre>
<h2 id="split">split</h2>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> re 
re<span class="token punctuation">.</span>split <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span> 
<span class="token comment"># generates a list of the phrase divided by the position </span>
<span class="token comment"># of the text mentioned</span>
</code></pre>
<h2 id="findall">findall</h2>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> re 
re<span class="token punctuation">.</span>findall <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span> 
<span class="token comment"># generates a list conatining the text and repeated </span>
<span class="token comment"># the number of times the text occurs</span>
</code></pre>
<h2 id="finditer">finditer</h2>
<p>Captures the position of the repeating text in a string and is a good support to <code>findall</code></p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> re
re<span class="token punctuation">.</span>finditer<span class="token punctuation">(</span>text<span class="token punctuation">,</span> phrase<span class="token punctuation">)</span>
<span class="token comment"># this cannot be printed independently. It needs to be used through a list comprehension</span>
<span class="token keyword">print</span> <span class="token punctuation">[</span>item<span class="token punctuation">.</span>start<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">for</span> item <span class="token keyword">in</span> re<span class="token punctuation">.</span>finditer<span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">]</span>
</code></pre>
<p><a href="https://www.tutorialspoint.com/How-do-we-use-re-finditer-method-in-Python-regular-expression">finditer doc</a><br>
<a href="https://www.tutorialspoint.com/How-do-we-use-re-finditer-method-in-Python-regular-expression">stackflow_good_answer</a></p>

