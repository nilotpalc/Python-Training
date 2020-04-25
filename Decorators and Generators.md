---


---

<h3 id="decorators">Decorators</h3>
<p>Decorators are primarily used to run additional code instructions other than the defined functions.<br>
These primarily act as a wrap or add-on to the defined function and are used with the prefix <code>@decoratorname</code> added to the preceding line to the function definition</p>
<pre class=" language-python"><code class="prism  language-python">@decoratorname
<span class="token keyword">def</span> <span class="token function">funcname</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token comment"># code instructions</span>
	<span class="token comment"># return</span>
</code></pre>
<p>Another important concept is ability of functions to be have as objects and be used as required</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">hello</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">'This is a test'</span><span class="token punctuation">)</span>
<span class="token comment"># the below code transfers the functionality of hello to greet without execution</span>
greet <span class="token operator">=</span> hello
greet<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token string">'This is a test'</span>   <span class="token comment"># Output of greet</span>
</code></pre>
<p><a href="https://repl.it/@nilotpalc/Decorators">Repl.it</a> link for seeing a decorator in-principle</p>

