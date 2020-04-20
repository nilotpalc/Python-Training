---


---

<h3 id="return">Return</h3>
<p>The <code>return</code> command breaks the function at the first instance that it fetches a value in the execution stage. Any lines of codes written after <code>return</code> within the defined function will no longer run after return breaks the function.</p>
<p>The <code>return</code> function does not run the <code>\n</code> command while returning output for string statements. The <code>\n</code> function is limited to <code>print</code> command only</p>
<p>Hierarchy of Terms</p>
<blockquote>
<p>Function</p>
<blockquote>
<p>Code</p>
<blockquote>
<p>Command</p>
</blockquote>
</blockquote>
</blockquote>
<h3 id="while-loop">While loop</h3>
<p>Whenever we write a <code>while</code> loop, the loop runs till the true condition reverts to false or there is a break in the loop. More importantly, whenever we use a condition like <code>while True:</code>the below coding statement needs to involve a <code>break</code> command to avoid creating an infinite loop. <em>This can follow the <code>return</code> command in case a function is defined within the loop.</em></p>
<h3 id="try-except-finally">Try, Except, Finally</h3>
<p>When we use <code>try</code>, <code>except</code>, <code>else</code> and <code>finally</code> commands within a function, they need to be nested within the function</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">func</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">try</span><span class="token punctuation">:</span>
		<span class="token comment"># mention the function code here</span>
	<span class="token keyword">except</span><span class="token punctuation">:</span>
		<span class="token comment"># error message</span>
	<span class="token keyword">else</span><span class="token punctuation">:</span>
		<span class="token comment"># outcome of the correct message; in case there is a while loop before </span>
		<span class="token comment"># try, break command might be nested in this function along with return </span>
		<span class="token comment"># command</span>
</code></pre>
<h3 id="using-else-with-while-and-for-loops">Using Else with While and For loops</h3>
<p>In case <code>while</code> and <code>for</code> loops run with a nested <code>break</code> command, the <strong>successful completion of the entire loop</strong> can be programmed to return a specific result with the <code>else</code> command nested under the same indent level as <code>while</code> and <code>for</code></p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">for</span> i <span class="token keyword">in</span> <span class="token punctuation">[</span><span class="token number">1</span><span class="token punctuation">,</span><span class="token number">2</span><span class="token punctuation">,</span><span class="token number">3</span><span class="token punctuation">,</span><span class="token number">4</span><span class="token punctuation">,</span><span class="token number">5</span><span class="token punctuation">]</span><span class="token punctuation">:</span>
	<span class="token keyword">if</span> num <span class="token operator">%</span> <span class="token number">7</span> <span class="token operator">==</span> <span class="token number">0</span><span class="token punctuation">:</span>
		<span class="token keyword">return</span> num
<span class="token keyword">else</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span><span class="token string">"No number is divisible by 7"</span><span class="token punctuation">)</span>
<span class="token comment"># The function for the above list will return the else </span>
<span class="token comment"># output once the entire for loop is completed and </span>
<span class="token comment"># break at the first instance if any number in </span>
<span class="token comment"># the list is divisible by 7</span>
</code></pre>

