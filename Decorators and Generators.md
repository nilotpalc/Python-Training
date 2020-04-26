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
<h3 id="generators">Generators</h3>
<p>Generators are used to capture a list of items in a function. The command used is <code>yield</code> and is used in place of <code>return</code> in a function where we want to capture multiple values. <code>return</code> command can only return a single value and breaks the function once it is assigned the value while yield is actually able to store a list of values.<br>
However, we cannot use yield to directly return a variable. It needs to be used with list or tuple function to print or generate the desired output in the actual code.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token comment"># Generating a Fibonacci sequence</span>
<span class="token keyword">def</span> <span class="token function">fibonacci</span><span class="token punctuation">(</span>n<span class="token punctuation">)</span><span class="token punctuation">:</span>
	a <span class="token operator">=</span> <span class="token number">0</span>
	b <span class="token operator">=</span> <span class="token number">1</span>
	<span class="token keyword">for</span> i <span class="token keyword">in</span>  <span class="token builtin">range</span><span class="token punctuation">(</span>n<span class="token punctuation">)</span><span class="token punctuation">:</span>
		<span class="token keyword">yield</span> a
		a<span class="token punctuation">,</span> b <span class="token operator">=</span> b<span class="token punctuation">,</span> b <span class="token operator">+</span> a

<span class="token keyword">print</span><span class="token punctuation">(</span><span class="token builtin">list</span><span class="token punctuation">(</span>fibonacci<span class="token punctuation">(</span><span class="token number">10</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">)</span>

</code></pre>
<p>Running the fibonacci function will not yield anything. The output needs to printed using the list command on the fibonacci function.<br>
See the code <a href="https://repl.it/@nilotpalc/using-generator-functionyield">here</a></p>

