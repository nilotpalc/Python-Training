---


---

<h2 id="collections-module">Collections Module</h2>
<p>Always run the command</p>
<blockquote>
<p>from <strong>collections</strong> import <strong>command name</strong></p>
</blockquote>
<ol>
<li>Counter</li>
<li>defaultdict</li>
<li>OrderedDict</li>
<li>namedtuple</li>
</ol>
<h3 id="counter">Counter</h3>
<p>Counter primarily returns a dictionary containing the element name and the count of the element as a dictionary. Note the capital C in Counter.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">from</span> collections <span class="token keyword">import</span> Counter
a <span class="token operator">=</span> <span class="token string">'string'</span>
Counter<span class="token punctuation">(</span>a<span class="token punctuation">)</span>
</code></pre>
<p>The output is as follows -<br>
Counter({‘s’: 1, ‘t’: 1, ‘r’: 1, ‘i’: 1, ‘n’: 1, ‘g’: 1})<br>
This is a dict object that can be used as a dictionary to call relevant items as needed.</p>
<h3 id="defaultdict">defaultdict</h3>
<p>A  <strong>defaultdict</strong>  works exactly like a normal dict, but it is initialized with a function (“default factory”) that takes no arguments and provides the default value for a nonexistent key.<br>
A  <strong>defaultdict</strong>  will never raise a  <strong>KeyError</strong>. Any key that does not exist gets the value returned by the default factory.<br>
Good <a href="https://www.accelebrate.com/blog/using-defaultdict-python"></a></p>
<h3 id="ordereddict">OrderedDict</h3>
<p>A regular dict looks at its contents when testing for equality. An OrderedDict also considers the order the items were added.</p>
<h3 id="namedtuple">namedtuple</h3>
<p>Each kind of <code>namedtuple</code> is represented by its own class, created by using the namedtuple() factory function. The arguments are the name of the new class and a string containing the names of the elements.<br>
You can basically think of <code>namedtuple</code> as a very quick way of creating a new object/class type with some attribute fields.</p>
<h2 id="datetime-module">DateTime module</h2>
<blockquote>
<p>import datetime</p>
</blockquote>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> datetime
<span class="token comment"># can go upto microseconds</span>
t <span class="token operator">=</span> datetime<span class="token punctuation">.</span>time<span class="token punctuation">(</span>hh<span class="token punctuation">,</span>mm<span class="token punctuation">,</span>ss<span class="token punctuation">)</span>

d <span class="token operator">=</span> datetime<span class="token punctuation">.</span>date<span class="token punctuation">(</span>yyyy<span class="token punctuation">,</span>mm<span class="token punctuation">,</span>d<span class="token punctuation">)</span>
<span class="token comment"># code for generating today's date</span>
today <span class="token operator">=</span> datetime<span class="token punctuation">.</span>date<span class="token punctuation">.</span>today<span class="token punctuation">(</span><span class="token punctuation">)</span>

<span class="token comment"># The difference in dates is always expressed in timedelta object</span>
d3 <span class="token operator">=</span> d1 <span class="token operator">-</span> d2
<span class="token comment"># The difference in days is expressed as below</span>
d3<span class="token punctuation">.</span>days
</code></pre>

