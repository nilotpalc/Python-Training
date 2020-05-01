---


---

<h1 id="main-functions-under-regular-expressions">Main Functions under Regular Expressions</h1>
<p>These functions are primarily used in code statements for pattern recognition. Simple text search in a string of characters in a single line can be done using <code>find</code> <code>count</code> and <code>index</code>.<br>
Multiple lines will need use of flags and will have to be then, used with these below functions.</p>
<h2 id="search">search</h2>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> re 
re<span class="token punctuation">.</span>search <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span> 
<span class="token comment"># use with start() and end () to return starting position</span>
<span class="token comment"># and the next position where the text ends </span>

re<span class="token punctuation">.</span>search <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">.</span>start<span class="token punctuation">(</span><span class="token punctuation">)</span> 
re<span class="token punctuation">.</span>search <span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">.</span>end<span class="token punctuation">(</span><span class="token punctuation">)</span>

</code></pre>
<p>To search for a word within the phrase, use the <code>r"\b&lt;character&gt;\b"</code> in the string along with prefix <code>r</code></p>
<blockquote>
<p>Escapes are indicated by prefixing the character with a backslash .<br>
Unfortunately, a backslash must itself be escaped in normal Python<br>
strings, and that results in expressions that are difficult to read.<br>
Using raw strings, created by prefixing the literal value with <code>r</code>,<br>
eliminates this problem and maintains readability.</p>
</blockquote>
<pre class=" language-python"><code class="prism  language-python">phrase <span class="token operator">=</span> "This <span class="token keyword">is</span> an example sentence<span class="token punctuation">,</span> \
it <span class="token keyword">is</span> <span class="token keyword">for</span> demonstration only"
<span class="token keyword">print</span> <span class="token punctuation">(</span>re<span class="token punctuation">.</span>search<span class="token punctuation">(</span>r<span class="token string">'\bThis is\b'</span><span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">.</span>start<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">)</span>

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
<p>Captures the position of the repeating text in a string and is a good support to <code>findall</code><br>
The actual list is developed using start() or end() methods to call all positions in the list.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> re
re<span class="token punctuation">.</span>finditer<span class="token punctuation">(</span>text<span class="token punctuation">,</span> phrase<span class="token punctuation">)</span>
<span class="token comment"># this cannot be printed independently. It needs to be used through a list comprehension</span>
<span class="token keyword">print</span> <span class="token punctuation">[</span>item<span class="token punctuation">.</span>start<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token keyword">for</span> item <span class="token keyword">in</span> re<span class="token punctuation">.</span>finditer<span class="token punctuation">(</span>text<span class="token punctuation">,</span>phrase<span class="token punctuation">)</span><span class="token punctuation">]</span>
</code></pre>
<p><strong>This only works on string patterns and not for lists</strong><br>
<a href="https://gist.github.com/nilotpalc/65336cebe72e6c0e6efcdbc371da9c90">Gist link</a></p>
<p><a href="https://www.tutorialspoint.com/How-do-we-use-re-finditer-method-in-Python-regular-expression">finditer doc</a><br>
<a href="https://stackoverflow.com/a/16360404/13218820">stackflow_good_answer</a></p>
<h2 id="repetition-patterns">Repetition Patterns</h2>
<blockquote>
<p>’				 sd*     		&nbsp;&nbsp; # d preceded by zero or more s’s<br>
‘s+d’   			&nbsp;&nbsp; # d preceded by one or more s’s<br>
‘s?d’        	&nbsp;&nbsp; # d preceded by zero or one s’s<br>
‘s{3}d’     	&nbsp;&nbsp; # d preceded by three d’s<br>
‘s{2,3}d’  	&nbsp;&nbsp; # d preceded by two to three s’s</p>
</blockquote>
<blockquote>
<p>‘sd*’ &nbsp;&nbsp;     # s followed by zero or more d’s<br>
‘sd+’ &nbsp;&nbsp;          # s followed by one or more d’s<br>
‘sd?’ &nbsp;&nbsp;         # s followed by zero or one d’s<br>
‘sd{3}’ &nbsp;&nbsp;        # s followed by three d’s<br>
‘sd{2,3}’ &nbsp;&nbsp;      # s followed by two to three d’s</p>
</blockquote>
<p>Points to remember on <strong>Repetition Syntax</strong> -<br>
* 0 or more characters<br>
+ 1 or more characters<br>
? 0 or 1 character<br>
{x} x characters<br>
{x,y} x or y characters</p>
<p>The above patterns are always input in the form of text <code>'sd*'</code> <code>'sd+'</code>; <strong>always within single quotes like a string format</strong></p>
<pre class=" language-python"><code class="prism  language-python">re<span class="token punctuation">.</span>search<span class="token punctuation">(</span><span class="token string">'sd*'</span><span class="token punctuation">,</span>phrase<span class="token punctuation">)</span>
</code></pre>
<h2 id="character-set">Character Set</h2>
<p>The repetition syntax above looks at repetition of one character; the character set looks at repetition of more than one character</p>
<blockquote>
<p>‘[sd]’  &nbsp;&nbsp;  # either s or d<br>
‘s[sd]+’ &nbsp;&nbsp;   # s followed by one or more s or d<br>
‘s[sd]?’ &nbsp;&nbsp;  # s followed by zero or one s or d</p>
</blockquote>
<h2 id="character-ranges">Character Ranges</h2>
<p>These rules looks at repetition of range of characters; the logic around *, + , ? remain the same<br>
[a-z]+’, &nbsp;&nbsp;     # sequences of lower case letters<br>
‘[A-Z]+’,   &nbsp;&nbsp;   # sequences of upper case letters<br>
‘[a-zA-Z]+’ &nbsp;&nbsp;   # sequences of lower or upper case letters<br>
‘[A-Z][a-z]+’ &nbsp;&nbsp; # one upper case letter followed by lower case letters</p>
<h2 id="exclusion">Exclusion</h2>
<p>Use <code>^</code> to exclude terms by incorporating it into the bracket syntax notation. For example: <code>[^...]</code> will match any single character not in the brackets.</p>
<pre class=" language-python"><code class="prism  language-python">test_phrase <span class="token operator">=</span> <span class="token string">'This is a string! But it has punctuation. How can we remove it?'</span>
<span class="token keyword">print</span> <span class="token punctuation">(</span>re<span class="token punctuation">.</span>findall<span class="token punctuation">(</span><span class="token string">'[^!.? ]+'</span><span class="token punctuation">,</span>test_phrase<span class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token comment">### Output</span>
</code></pre>
<h4 id="the-above-re-commands-work-on-a-single-line-advanced-flags-in-re.searchpattern-text-flags-need-to-be-included-for-multiple-lines.-refer-the-link-below-advanced-module-not-covered-now">The above re commands work on a single line; advanced flags in <code>re.search(pattern, text, flags)</code> need to be included for multiple lines. Refer the link below (advanced module; not covered now</h4>
<h2 id="escape-codes">Escape Codes</h2>
<table border="1" class="docutils">
<colgroup>
<col width="14%">
<col width="86%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Code</th>
<th class="head">Meaning</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">\d</span></tt></td>
<td>a digit</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\D</span></tt></td>
<td>a non-digit</td>
</tr>
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">\s</span></tt></td>
<td>whitespace (tab, space, newline, etc.)</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\S</span></tt></td>
<td>non-whitespace</td>
</tr>
<tr class="row-even"><td><tt class="docutils literal"><span class="pre">\w</span></tt></td>
<td>alphanumeric</td>
</tr>
<tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\W</span></tt></td>
<td>non-alphanumeric</td>
</tr>
</tbody>
</table>
<pre class=" language-python"><code class="prism  language-python">test_patterns<span class="token operator">=</span><span class="token punctuation">[</span> r<span class="token string">'\d+'</span><span class="token punctuation">,</span> <span class="token comment"># sequence of digits</span>
                r<span class="token string">'\D+'</span><span class="token punctuation">,</span> <span class="token comment"># sequence of non-digits</span>
                r<span class="token string">'\s+'</span><span class="token punctuation">,</span> <span class="token comment"># sequence of whitespace</span>
                r<span class="token string">'\S+'</span><span class="token punctuation">,</span> <span class="token comment"># sequence of non-whitespace</span>
                r<span class="token string">'\w+'</span><span class="token punctuation">,</span> <span class="token comment"># alphanumeric characters</span>
                r<span class="token string">'\W+'</span><span class="token punctuation">,</span> <span class="token comment"># non-alphanumeric</span>
                <span class="token punctuation">]</span>
</code></pre>
<p>REPEAT NOTE</p>
<h4 id="escapes-are-indicated-by-prefixing-the-character-with-a-backslash-.-unfortunately-a-backslash-must-itself-be-escaped-in-normal-python-strings-and-that-results-in-expressions-that-are-difficult-to-read.-using-raw-strings-created-by-prefixing-the-literal-value-with-r-eliminates-this-problem-and-maintains-readability.">Escapes are indicated by prefixing the character with a backslash . Unfortunately, a backslash must itself be escaped in normal Python strings, and that results in expressions that are difficult to read. Using raw strings, created by prefixing the literal value with <code>r</code>, eliminates this problem and maintains readability.</h4>
<p><a href="https://docs.python.org/3.2/library/re.html">Regular Expressions</a></p>

