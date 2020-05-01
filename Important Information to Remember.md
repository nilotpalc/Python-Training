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
<h3 id="zero-value-or-empty-listtuple-variable-is-assumed-to-be-false-in-while-loop-function">Zero value or empty list/tuple variable is assumed to be False in While loop function</h3>
<pre class=" language-python"><code class="prism  language-python">aces <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token comment"># the output will be the same for [], 0</span>
<span class="token keyword">while</span> aces<span class="token punctuation">:</span>
    <span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">'True'</span><span class="token punctuation">)</span>
<span class="token keyword">else</span><span class="token punctuation">:</span>
    <span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">'False'</span><span class="token punctuation">)</span>

<span class="token comment"># Output is 'False'</span>
</code></pre>
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
<h3 id="class-definition-and-usage-of-attributes-in-other-functions">Class Definition and usage of attributes in other functions</h3>
<p>We can define a class object in the code and then, use a variable that might be of the class object type in subsequent functions</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">Card</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	<span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span>suit<span class="token punctuation">,</span>rank<span class="token punctuation">)</span><span class="token punctuation">:</span>     <span class="token comment"># Card object defined by 2 \</span>
	                                  <span class="token comment"># attributes suit and rank</span>
		self<span class="token punctuation">.</span>suit <span class="token operator">=</span> suit
		self<span class="token punctuation">.</span>rank <span class="token operator">=</span> rank

<span class="token keyword">def</span> <span class="token function">func</span><span class="token punctuation">(</span>var<span class="token punctuation">)</span><span class="token punctuation">:</span>            <span class="token comment"># Variable var is a card class \</span>
                          <span class="token comment"># and will be used as below</span>
	<span class="token keyword">if</span> var<span class="token punctuation">.</span>suit <span class="token operator">==</span> <span class="token string">"Aces"</span><span class="token punctuation">:</span>
		<span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">'True'</span><span class="token punctuation">)</span>
	<span class="token keyword">else</span><span class="token punctuation">:</span>
		<span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">'False'</span><span class="token punctuation">)</span>

<span class="token keyword">class</span> <span class="token class-name">Deck</span><span class="token punctuation">:</span>
<span class="token comment"># Creating a deck of playing cards and using the card class object /</span>
<span class="token comment"># type to populate the empty list    </span>
    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>deck <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>  <span class="token comment"># start with an empty list</span>
        <span class="token keyword">for</span> suit <span class="token keyword">in</span> suits<span class="token punctuation">:</span>
            <span class="token keyword">for</span> rank <span class="token keyword">in</span> ranks<span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>deck<span class="token punctuation">.</span>append<span class="token punctuation">(</span>Card<span class="token punctuation">(</span>suit<span class="token punctuation">,</span>rank<span class="token punctuation">)</span><span class="token punctuation">)</span>

<span class="token comment"># Blackjack Assignment Example Udemy Course</span>
</code></pre>
<h3 id="nested-for-loops-and-item-definitions">Nested For loops and item definitions</h3>
<p>For <code>item</code> in <strong>nested for</strong> loops, choosing a different item name can allow us to reference both items in a combined function.</p>
<pre class=" language-python"><code class="prism  language-python"> <span class="token keyword">for</span> suit <span class="token keyword">in</span> suits<span class="token punctuation">:</span>
	 <span class="token keyword">for</span> rank <span class="token keyword">in</span> ranks<span class="token punctuation">:</span>
	     self<span class="token punctuation">.</span>deck<span class="token punctuation">.</span>append<span class="token punctuation">(</span>Card<span class="token punctuation">(</span>suit<span class="token punctuation">,</span>rank<span class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token comment"># Reference the usage from example above</span>
</code></pre>
<h3 id="using-custom-defined-objects-classes-in-lists-tuples-and-dictionaries">Using custom-defined objects (classes) in lists, tuples and dictionaries</h3>
<p>A user defined object can be used in any list, tuple or dictionary. However, calling the entire object directly may not give the right output. It will need to be combined with a pre-defined class methods or any other default methods to generate a valid output.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">Card</span><span class="token punctuation">:</span>
    
    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span>suit<span class="token punctuation">,</span>rank<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>suit <span class="token operator">=</span> suit
        self<span class="token punctuation">.</span>rank <span class="token operator">=</span> rank
    
    <span class="token keyword">def</span> <span class="token function">__str__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        <span class="token keyword">return</span> <span class="token punctuation">(</span>f<span class="token string">'{self.suit} of {self.rank}'</span><span class="token punctuation">)</span> 

s <span class="token operator">=</span> Card<span class="token punctuation">(</span><span class="token string">'Heart'</span><span class="token punctuation">,</span><span class="token string">'Two'</span><span class="token punctuation">)</span>
d <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>
d<span class="token punctuation">.</span>append<span class="token punctuation">(</span>s<span class="token punctuation">)</span>
d<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span>
<span class="token comment"># Returns Output &lt;__main__.Card at 0x159d1743b08&gt;</span>
<span class="token comment"># This is similar behavior to map and filter functions</span>

d<span class="token punctuation">[</span><span class="token number">0</span><span class="token punctuation">]</span><span class="token punctuation">.</span>suit
<span class="token comment"># Returns 'Heart'</span>
</code></pre>
<h3 id="ideally-the-init-should-not-return-any-list-tuple-or-dictionary-as-output.-it-can-only-print-strings-or-in-most-cases-return-is-not-coded-into-the-function-definition">Ideally the <strong>init</strong> should not return any list, tuple or dictionary as output. It can only print strings or in most cases, <code>return</code> is not coded into the function definition</h3>
<p>Also, refer to the below distinction between <code>return</code> and <code>print</code>; <code>print</code> returns a nonetype object and hence, can be used in <code>__init__</code> code<br>
<a href="https://stackoverflow.com/a/15441904/13218820">StackOverflow Link</a></p>
<pre class=" language-python"><code class="prism  language-python">suits <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token string">'Hearts'</span><span class="token punctuation">,</span> <span class="token string">'Diamonds'</span><span class="token punctuation">,</span> <span class="token string">'Spades'</span><span class="token punctuation">,</span> <span class="token string">'Clubs'</span><span class="token punctuation">)</span>
ranks <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token string">'Two'</span><span class="token punctuation">,</span> <span class="token string">'Three'</span><span class="token punctuation">,</span> <span class="token string">'Four'</span><span class="token punctuation">,</span> <span class="token string">'Five'</span><span class="token punctuation">,</span> <span class="token string">'Six'</span><span class="token punctuation">,</span> <span class="token string">'Seven'</span><span class="token punctuation">,</span> <span class="token string">'Eight'</span><span class="token punctuation">,</span> <span class="token string">'Nine'</span><span class="token punctuation">,</span> <span class="token string">'Ten'</span><span class="token punctuation">,</span> <span class="token string">'Jack'</span><span class="token punctuation">,</span> <span class="token string">'Queen'</span><span class="token punctuation">,</span> <span class="token string">'King'</span><span class="token punctuation">,</span> <span class="token string">'Ace'</span><span class="token punctuation">)</span>

<span class="token keyword">class</span> <span class="token class-name">Deck</span><span class="token punctuation">:</span>
    
    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>deck <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span>  <span class="token comment"># start with an empty list</span>
        <span class="token keyword">for</span> suit <span class="token keyword">in</span> suits<span class="token punctuation">:</span>
            <span class="token keyword">for</span> rank <span class="token keyword">in</span> ranks<span class="token punctuation">:</span>
                self<span class="token punctuation">.</span>deck<span class="token punctuation">.</span>append<span class="token punctuation">(</span>Card<span class="token punctuation">(</span>suit<span class="token punctuation">,</span>rank<span class="token punctuation">)</span><span class="token punctuation">)</span>
        <span class="token comment"># last statement under __init__</span>
        <span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">'Done'</span><span class="token punctuation">)</span>
test <span class="token operator">=</span> Deck<span class="token punctuation">(</span><span class="token punctuation">)</span>
<span class="token comment"># Prints 'Done'</span>

<span class="token comment"># Replace Print statement</span>
		<span class="token keyword">return</span> self<span class="token punctuation">.</span>deck
<span class="token comment"># Returns below error</span>
<span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>
TypeError                                 Traceback <span class="token punctuation">(</span>most recent call last<span class="token punctuation">)</span>
<span class="token operator">&lt;</span>ipython<span class="token operator">-</span><span class="token builtin">input</span><span class="token operator">-</span><span class="token number">26</span><span class="token operator">-</span><span class="token number">9645fa500790</span><span class="token operator">&gt;</span> <span class="token keyword">in</span> <span class="token operator">&lt;</span>module<span class="token operator">&gt;</span>
<span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">&gt;</span> <span class="token number">1</span>  test <span class="token operator">=</span> Deck<span class="token punctuation">(</span><span class="token punctuation">)</span>

TypeError<span class="token punctuation">:</span> __init__<span class="token punctuation">(</span><span class="token punctuation">)</span> should <span class="token keyword">return</span> <span class="token boolean">None</span><span class="token punctuation">,</span> <span class="token operator">not</span> <span class="token string">'list'</span>
<span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span><span class="token operator">-</span>

<span class="token comment"># Remove Returns statement</span>
<span class="token comment"># Returns nothing as output under test = Deck()</span>
</code></pre>
<h3 id="methods-defined-under-class-to-call-objects">Methods defined under Class to call objects</h3>
<ol>
<li>Methods defined under <strong>init</strong> function do not need to be followed with round brackets</li>
<li>Methods or Functions defined otherwise need to be used in association with round brackets <code>()</code></li>
<li>A method can also be defined as a measure under <strong>init</strong> function with a default value that can be reassigned during the course of the code through other functions</li>
</ol>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">class</span> <span class="token class-name">Chips</span><span class="token punctuation">:</span>
    
    <span class="token keyword">def</span> <span class="token function">__init__</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>total <span class="token operator">=</span> <span class="token number">100</span>  <span class="token comment"># This can be set to a default value or supplied by a user input</span>
        self<span class="token punctuation">.</span>bet <span class="token operator">=</span> <span class="token number">0</span>
        
    <span class="token keyword">def</span> <span class="token function">win_bet</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>total <span class="token operator">+=</span>self<span class="token punctuation">.</span>bet
    
    <span class="token keyword">def</span> <span class="token function">lose_bet</span><span class="token punctuation">(</span>self<span class="token punctuation">)</span><span class="token punctuation">:</span>
        self<span class="token punctuation">.</span>total <span class="token operator">-=</span>self<span class="token punctuation">.</span>bet

<span class="token keyword">def</span> <span class="token function">take_bet</span><span class="token punctuation">(</span>chips<span class="token punctuation">)</span><span class="token punctuation">:</span>
    
    <span class="token keyword">while</span> <span class="token boolean">True</span><span class="token punctuation">:</span>
        <span class="token keyword">try</span><span class="token punctuation">:</span>
            chips<span class="token punctuation">.</span>bet <span class="token operator">=</span> <span class="token builtin">int</span><span class="token punctuation">(</span><span class="token builtin">input</span><span class="token punctuation">(</span><span class="token string">"Please place your bet: "</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
            <span class="token comment"># Note the use of method chips.bet where chips is a variable\</span>
            <span class="token comment"># of class object Chips and chips.bet is initially\</span>
            <span class="token comment"># assigned zero value in __init__ function</span>
        <span class="token keyword">except</span><span class="token punctuation">:</span>
            <span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">"Please enter an integer value for your bet"</span><span class="token punctuation">)</span>
            <span class="token keyword">continue</span>
        <span class="token keyword">else</span><span class="token punctuation">:</span>
            <span class="token keyword">if</span> chips<span class="token punctuation">.</span>bet <span class="token operator">&gt;</span> chips<span class="token punctuation">.</span>total<span class="token punctuation">:</span>
                <span class="token keyword">print</span> <span class="token punctuation">(</span>f<span class="token string">'You dont have sufficient chips. Please enter a lower number than {chips.total}'</span><span class="token punctuation">)</span>
                <span class="token keyword">continue</span>
            <span class="token keyword">else</span><span class="token punctuation">:</span>
                <span class="token keyword">return</span> chips<span class="token punctuation">.</span>bet
                <span class="token keyword">break</span>
<span class="token comment"># Refer Blackjack assignment on Udemy Course</span>
</code></pre>
<h3 id="difference-between-return-and-print">Difference between Return and Print</h3>
<p>For <code>__str__</code> function in the class object definition, always use <code>return</code> function. The print function generates the output but, the same is an object of <strong>nonetype</strong> and <code>__str__</code> function will not be able to work with other functions.<br>
<a href="https://stackoverflow.com/a/15441904/13218820">StackOverflow Link</a></p>
<h3 id="the-__init__-command-statement-is-expected-to-return-an-object-of-nonetype">The <code>__init__</code> command statement is expected to return an object of nonetype</h3>
<h3 id="print-command-format-for-printing-all-items-in-the-list">Print Command format for printing all items in the list</h3>
<p>Refer to the Blackjack Example</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">print</span> <span class="token punctuation">(</span><span class="token string">'general text string'</span><span class="token punctuation">,</span> <span class="token operator">*</span>player<span class="token punctuation">.</span>cards<span class="token punctuation">,</span> sep <span class="token operator">=</span> <span class="token string">'\n'</span><span class="token punctuation">)</span>
<span class="token comment"># general text sting can also be omitted</span>
<span class="token comment"># this print input format does not work with return command</span>
</code></pre>
<h2 id="remember-the-section-on-listtuple-assignment-for-function-assignment-for-multiple-variables-in-functions">Remember the section on List/Tuple Assignment for function assignment for multiple variables in functions</h2>
<p><a href="https://github.com/nilotpalc/Python-Training/blob/master/List_Tuple_Variable_Assignment.ipynb">Code Snippet</a> on Github</p>
<h1 id="my-section-guidelines-for-writing-codes">My section guidelines for writing Codes</h1>
<p><strong>Section 1</strong><br>
Contains all the packages and modules imported into the overall code<br>
<strong>Section 2</strong><br>
Contains all the global variables<br>
<strong>Section 3</strong><br>
Contains all the custom Class Object definitions<br>
<strong>Section 4</strong><br>
Contains all the user-specific function definitions<br>
<strong>Section 5</strong><br>
Contains the final execution code</p>
<h5 id="always-use-the--comments-to-indicate-the-reason-for-defining-an-object-function-and-broad-sections-at-different-points-of-the-code-dont-forget-to-outline-the-logic-for-defining-the-user-specific-functions-within-doc-string">Always use the # comments to indicate the reason for defining an object, function and broad sections at different points of the code; dont forget to outline the logic for defining the user-specific functions within doc-string</h5>

