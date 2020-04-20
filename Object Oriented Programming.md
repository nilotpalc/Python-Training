---


---

<h2 id="object-oriented-programming">Object-Oriented Programming</h2>
<h3 id="classes-attributes-and-methods">Classes, Attributes and Methods</h3>
<p>Class is a way to define user-built object types<br>
Each class is defined by attributes<br>
Each class can contain functions that can be used as methods to run operations</p>
<h3 id="note">Note</h3>
<blockquote>
<p>Class name is written in camel casing <em>NameOfClass</em><br>
Variables are written in snake casing</p>
</blockquote>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">ClassName</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
		<span class="token keyword">def</span> <span class="token function">__init__</span> <span class="token punctuation">(</span>self<span class="token punctuation">,</span> attribute1<span class="token punctuation">,</span> attribute2<span class="token punctuation">)</span><span class="token punctuation">:</span>
			self<span class="token punctuation">.</span>attribute1 <span class="token operator">=</span> attribute1  <span class="token comment"># defines var.attribute1 method to call the variable value	</span>
			self<span class="token punctuation">.</span>attribute2 <span class="token operator">=</span> attribute2
		
	<span class="token comment"># Defining Methods to run operations</span>
	<span class="token keyword">def</span> <span class="token function">new</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
		<span class="token keyword">return</span> self<span class="token punctuation">.</span>attribute1 <span class="token operator">+</span> self<span class="token punctuation">.</span>attribute2
	
	<span class="token keyword">def</span> <span class="token function">new</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> number<span class="token punctuation">)</span><span class="token punctuation">:</span>
		<span class="token keyword">return</span> self<span class="token punctuation">.</span>attribute1 <span class="token operator">+</span> self<span class="token punctuation">.</span>attribute2 <span class="token operator">+</span> number <span class="token comment"># number input will be entered during the code run</span>
</code></pre>
<p>Classes can also be defined as Base and Derived</p>
<pre class=" language-python"><code class="prism  language-python">
<span class="token keyword">class</span> <span class="token class-name">Base</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
		<span class="token keyword">pass</span>
	<span class="token comment"># Defining a method</span>
	<span class="token keyword">def</span> <span class="token function">arr</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span>num<span class="token punctuation">)</span><span class="token punctuation">:</span>
		<span class="token keyword">return</span> num<span class="token operator">**</span><span class="token number">2</span>

<span class="token keyword">class</span> <span class="token class-name">Derived</span><span class="token punctuation">(</span>Base<span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> attribute<span class="token punctuation">)</span> <span class="token comment"># derived classes can include additional attributes over and above passed by Base; if not written, the Base __init__ condition is applied</span>

	<span class="token keyword">def</span> <span class="token function">arr</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> num<span class="token punctuation">)</span><span class="token punctuation">:</span>
		<span class="token keyword">return</span> num<span class="token operator">**</span><span class="token number">3</span> <span class="token comment"># arr function would have by default written num**2 if no new arr would have been written; in this case, arr is now revised to num**3</span>
</code></pre>
<h3 id="magic--dunder-functions">Magic / Dunder Functions</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">def</span> <span class="token function">__str__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>value to be printed<span class="token punctuation">)</span> <span class="token comment"># Used to return a result that can be printed using print(variable) in the coding statement for this class object</span>

<span class="token keyword">def</span> <span class="token function">__len__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>value<span class="token punctuation">)</span> <span class="token comment"># Used to return a result that can be printed using len(variable) in the coding statement for this class object</span>

def__del__<span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">return</span> <span class="token punctuation">(</span>value<span class="token punctuation">)</span> <span class="token comment"># Used to return a string of information when the variable is deleted</span>

<span class="token keyword">del</span> <span class="token punctuation">(</span>variablename<span class="token punctuation">)</span>  <span class="token comment"># Used to delete the variable and any message is displayed using __del__ statement</span>

</code></pre>

