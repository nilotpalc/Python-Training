---


---

<h1 id="pandas">Pandas</h1>
<h2 id="series">Series</h2>
<p>A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). What differentiates the NumPy array from a Series, is that a Series can have axis labels, meaning it can be indexed by a label, instead of just a number location.</p>
<p>Series is built on NumPy and hence, using pandas requires us to import NumPy and Pandas</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> numpy <span class="token keyword">as</span> np
<span class="token keyword">import</span> pandas <span class="token keyword">as</span> pd
</code></pre>
<p>Series is characterized by two key inputs -</p>
<ol>
<li>Data<br>
- List<br>
- Array</li>
<li>Labels (or Index position)</li>
</ol>
<p>Using a Dictionary as input to Series automatically assigns the key to labels and value to data in the output series</p>
<pre class=" language-python"><code class="prism  language-python">pd<span class="token punctuation">.</span>Series<span class="token punctuation">(</span>data<span class="token punctuation">,</span>label<span class="token punctuation">)</span>
pd<span class="token punctuation">.</span>Series<span class="token punctuation">(</span>dictname<span class="token punctuation">)</span>
</code></pre>
<p>Grabbing data from Series</p>
<pre class=" language-python"><code class="prism  language-python">ser1<span class="token punctuation">[</span><span class="token string">'label'</span><span class="token punctuation">]</span>
</code></pre>
<p><em>While running operations on series, all integers are converted into <code>float</code> types in the result output</em></p>
<p>Series is a collection of labels and values in a column format</p>

<table>
<thead>
<tr>
<th>Label</th>
<th align="right">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>label1</td>
<td align="right">value1</td>
</tr>
<tr>
<td>label2</td>
<td align="right">value2</td>
</tr>
<tr>
<td>label3</td>
<td align="right">value3</td>
</tr>
</tbody>
</table><h2 id="dataframes">DataFrames</h2>
<h3 id="creating-a-dataframe">Creating a DataFrame</h3>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> numpy <span class="token keyword">as</span> np
<span class="token keyword">import</span> pandas <span class="token keyword">as</span> pd
df <span class="token operator">=</span> pd<span class="token punctuation">.</span>DataFrame<span class="token punctuation">(</span>data<span class="token punctuation">,</span><span class="token punctuation">[</span>row<span class="token operator">-</span>labels<span class="token punctuation">]</span><span class="token punctuation">,</span><span class="token punctuation">[</span>column<span class="token operator">-</span>labels<span class="token punctuation">]</span><span class="token punctuation">)</span>
<span class="token comment"># data is a 2D array with rows equal to</span>
<span class="token comment"># no of row-labels and columns equal to</span>
<span class="token comment"># no of column labels</span>

<span class="token comment"># row-labels are a list object</span>
<span class="token comment"># column-labels are a list object</span>
</code></pre>
<h3 id="adding-a-new-column-to-a-dataframe">Adding a new column to a DataFrame</h3>
<pre class=" language-python"><code class="prism  language-python">df <span class="token operator">=</span> pd<span class="token punctuation">.</span>DataFrame<span class="token punctuation">(</span>data<span class="token operator">-</span>arr<span class="token punctuation">,</span> <span class="token punctuation">[</span>row<span class="token operator">-</span>labels<span class="token punctuation">]</span><span class="token punctuation">,</span><span class="token punctuation">[</span>col<span class="token operator">-</span>labels<span class="token punctuation">]</span><span class="token punctuation">)</span> 

df<span class="token punctuation">[</span>'new col<span class="token operator">-</span>label<span class="token punctuation">]</span> <span class="token operator">=</span> <span class="token builtin">list</span> <span class="token operator">/</span> <span class="token number">1D</span><span class="token operator">-</span>array <span class="token builtin">object</span>

df<span class="token punctuation">[</span><span class="token string">'new col-label'</span><span class="token punctuation">]</span> <span class="token operator">=</span> df<span class="token punctuation">[</span>col1<span class="token punctuation">]</span> <span class="token operator">+</span> df<span class="token punctuation">[</span>col2<span class="token punctuation">]</span>
</code></pre>
<h3 id="selecting-and-indexing-dataframes">Selecting and Indexing DataFrames</h3>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">[</span>col<span class="token operator">-</span>label<span class="token punctuation">]</span> <span class="token comment"># returns a single column</span>
df<span class="token punctuation">[</span><span class="token punctuation">[</span>col1<span class="token punctuation">,</span>col2<span class="token punctuation">]</span><span class="token punctuation">]</span> <span class="token comment"># returns multiple columns</span>

df<span class="token punctuation">.</span>loc<span class="token punctuation">[</span><span class="token string">'row-label'</span><span class="token punctuation">]</span> <span class="token comment"># returns a single row</span>
df<span class="token punctuation">.</span>loc<span class="token punctuation">[</span><span class="token punctuation">[</span><span class="token string">'row1,'</span>row2<span class="token punctuation">]</span><span class="token punctuation">]</span> <span class="token comment"># returns a multiple rows</span>

df<span class="token punctuation">.</span>iloc<span class="token punctuation">[</span><span class="token string">'row-index'</span><span class="token punctuation">]</span> <span class="token comment"># returns a single row based on _i_ index input</span>

df<span class="token punctuation">.</span>loc<span class="token punctuation">[</span>row<span class="token punctuation">,</span>col<span class="token punctuation">]</span> <span class="token comment"># returns a value at intersection of row-col</span>
df<span class="token punctuation">.</span>loc<span class="token punctuation">[</span><span class="token punctuation">[</span>row1<span class="token punctuation">,</span>row2<span class="token punctuation">]</span><span class="token punctuation">,</span><span class="token punctuation">[</span>col1<span class="token punctuation">,</span>col2<span class="token punctuation">]</span><span class="token punctuation">]</span> <span class="token comment"># returns 2D matrix from DataFrame</span>
</code></pre>
<h3 id="dropping-rows-and-columns">Dropping Rows and Columns</h3>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>drop<span class="token punctuation">(</span><span class="token string">'row-label'</span><span class="token punctuation">,</span>axis <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">,</span> inplace <span class="token operator">=</span> <span class="token boolean">True</span><span class="token punctuation">)</span> <span class="token comment"># change the dataframe permanently</span>
df<span class="token punctuation">.</span>drop<span class="token punctuation">(</span><span class="token string">'row-label'</span><span class="token punctuation">,</span>axis <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">)</span> <span class="token comment"># will not permanently change the dataframe </span>

df<span class="token punctuation">.</span>drop<span class="token punctuation">(</span><span class="token string">'col-label'</span><span class="token punctuation">,</span>axis <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">,</span> inplace <span class="token operator">=</span> <span class="token boolean">True</span><span class="token punctuation">)</span> <span class="token comment"># change the dataframe permanently</span>
df<span class="token punctuation">.</span>drop<span class="token punctuation">(</span><span class="token string">'col-label'</span><span class="token punctuation">,</span>axis <span class="token operator">=</span> <span class="token number">0</span><span class="token punctuation">)</span> <span class="token comment"># will not permanently change the dataframe </span>
</code></pre>
<h3 id="reset-and-set-index">Reset and Set Index</h3>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>reset_index<span class="token punctuation">(</span><span class="token punctuation">)</span>

df<span class="token punctuation">.</span>set_index<span class="token punctuation">(</span><span class="token string">'colname'</span><span class="token punctuation">)</span> <span class="token comment"># make a column as an index and delete the existing index</span>
<span class="token comment"># this needs to be used with `inplace` to be permanent</span>

df<span class="token punctuation">.</span>set_index<span class="token punctuation">(</span><span class="token punctuation">[</span>Col1<span class="token punctuation">,</span>Col2<span class="token punctuation">]</span><span class="token punctuation">)</span> <span class="token comment"># resulting df is a multi-level index</span>

df<span class="token punctuation">.</span>index<span class="token punctuation">.</span>names <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token string">'name'</span><span class="token punctuation">]</span> <span class="token comment"># adds a name to the existing index</span>
</code></pre>
<p>Also, check out the documentation that shows how to create multi-level index using <code>df.set_index method</code> <a href="https://pandas.pydata.org/pandas-docs/version/0.23.1/generated/pandas.DataFrame.set_index.html">link</a></p>
<h3 id="returning-a-list-of-column-and-index-label-headers-for-a-dataframe">Returning a list of column and index label headers for a DataFrame</h3>
<p>Use the following commands -</p>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>columns<span class="token punctuation">.</span>values<span class="token punctuation">.</span>tolist<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># returns a list of column headers</span>

df<span class="token punctuation">.</span>index<span class="token punctuation">.</span>unique<span class="token punctuation">(</span>level <span class="token operator">=</span> <span class="token string">'name'</span><span class="token operator">/</span>integer<span class="token punctuation">)</span> <span class="token comment"># returns the list of index labels</span>
<span class="token comment"># under the level; default is zero or the outer layer</span>
<span class="token comment"># Providing a index name generates a list for that index label</span>
</code></pre>
<h3 id="conditional-selection">Conditional Selection</h3>
<p>The method is similar to array indexing</p>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">[</span>df<span class="token punctuation">[</span>col<span class="token punctuation">]</span><span class="token operator">&gt;</span><span class="token string">'n'</span><span class="token punctuation">]</span> <span class="token comment"># generates the dataframe which omits all rows containing </span>
<span class="token comment"># values &lt; 'n' under col label</span>

df<span class="token punctuation">[</span><span class="token punctuation">(</span>df<span class="token punctuation">[</span>col1<span class="token punctuation">]</span><span class="token operator">&gt;</span><span class="token string">'n1'</span><span class="token punctuation">)</span> <span class="token operator">&amp;</span> <span class="token punctuation">(</span>df<span class="token punctuation">[</span>col2<span class="token punctuation">]</span><span class="token operator">&lt;</span><span class="token string">'n2'</span><span class="token punctuation">)</span><span class="token punctuation">]</span> <span class="token comment"># generates the dataframe that meets both</span>
<span class="token comment"># conditions</span>
<span class="token comment"># Note that `and` and `or` use is replaced by `&amp;` and `|` use in DataFrames</span>
</code></pre>
<h4 id="top-n-filter">Top N Filter</h4>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>nlargest<span class="token punctuation">(</span>N<span class="token punctuation">,</span>colnam<span class="token punctuation">)</span>
</code></pre>
<p>More details available <a href="https://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.nlargest.html">here</a></p>
<h3 id="multi-level-index-and-hierarchy">Multi-level Index and Hierarchy</h3>
<p>Indexing multi-layer data frames</p>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>xs<span class="token punctuation">(</span>row<span class="token operator">-</span>label<span class="token punctuation">,</span> level <span class="token operator">=</span> row header<span class="token operator">/</span>position<span class="token punctuation">)</span>
<span class="token comment"># generates sections of the data linked to row-level</span>
<span class="token comment"># subsequent column level indexing happens as shared previously</span>

df<span class="token punctuation">.</span>xs<span class="token punctuation">(</span>row<span class="token operator">-</span>label<span class="token punctuation">,</span> level <span class="token operator">=</span> index label<span class="token punctuation">)</span><span class="token punctuation">[</span>col<span class="token operator">-</span>name<span class="token punctuation">]</span>
</code></pre>
<p>Also, check out the documentation that helps to indicate how to use it for multiple levels and across columns <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html">here</a></p>
<h3 id="missing-data">Missing Data</h3>
<p>There are 2 main functions to identify and correct missing data</p>
<ol>
<li><code>dropna</code> method</li>
<li><code>fillna</code> method</li>
</ol>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>dropna<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># drops all rows with Nan value</span>

df<span class="token punctuation">.</span>dropna<span class="token punctuation">(</span>axis <span class="token operator">=</span> <span class="token number">1</span><span class="token punctuation">)</span> <span class="token comment"># drops all columns with Nan value</span>

df<span class="token punctuation">.</span>dropna<span class="token punctuation">(</span>thresh <span class="token operator">=</span> <span class="token number">2</span><span class="token punctuation">)</span> <span class="token comment"># drops all rows where the number</span>
<span class="token comment"># of non Nan values is less than 2</span>
</code></pre>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>fillna<span class="token punctuation">(</span>value <span class="token operator">=</span> <span class="token string">'input'</span><span class="token punctuation">)</span> <span class="token comment"># fills all Nan values in the </span>
<span class="token comment"># dataframe with input value</span>

df<span class="token punctuation">[</span>col<span class="token operator">-</span>label<span class="token punctuation">]</span><span class="token punctuation">.</span>fillna<span class="token punctuation">(</span>value <span class="token operator">=</span> <span class="token string">'input'</span><span class="token punctuation">)</span> <span class="token comment"># fills all Nan values in the </span>
<span class="token comment"># column with input value</span>
</code></pre>
<h3 id="groupby">Groupby</h3>
<p><em>Groupby</em> groups data based on the index header which is defined by the column name used for grouping</p>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>groupby<span class="token punctuation">(</span><span class="token string">'ColNam'</span><span class="token punctuation">)</span> <span class="token comment"># the resulting df has ColNam as new index</span>

df<span class="token punctuation">.</span>groupby<span class="token punctuation">(</span><span class="token punctuation">[</span>Col1<span class="token punctuation">,</span>Col2<span class="token punctuation">]</span><span class="token punctuation">)</span> <span class="token comment"># resulting df is multi-level index w/ </span>
<span class="token comment"># Col1 and Col2</span>

df<span class="token punctuation">.</span>groupby<span class="token punctuation">(</span><span class="token punctuation">[</span>Col1<span class="token punctuation">,</span>Col2<span class="token punctuation">]</span><span class="token punctuation">,</span> as_index<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span> <span class="token comment"># resulting df does not</span>
<span class="token comment"># add col1 and col2 to index</span>
</code></pre>
<h4 id="aggregation-for-groupby-columns">Aggregation for Groupby Columns</h4>
<pre class=" language-python"><code class="prism  language-python">groupdf<span class="token punctuation">.</span>agg <span class="token punctuation">(</span>np<span class="token punctuation">.</span><span class="token builtin">sum</span><span class="token punctuation">)</span> <span class="token comment"># runs on all columns</span>

groupdf<span class="token punctuation">.</span>agg<span class="token punctuation">(</span>Col1<span class="token punctuation">:</span> np<span class="token punctuation">.</span><span class="token builtin">sum</span><span class="token punctuation">,</span> Col2<span class="token punctuation">:</span> np<span class="token punctuation">.</span>mean<span class="token punctuation">)</span> <span class="token comment"># new groupdf with 2 col</span>

groupdf<span class="token punctuation">.</span>agg<span class="token punctuation">(</span><span class="token string">'NewCol'</span><span class="token operator">=</span><span class="token punctuation">(</span>Col1<span class="token punctuation">,</span>func<span class="token punctuation">)</span><span class="token punctuation">,</span><span class="token string">'NewCol2'</span><span class="token operator">=</span><span class="token punctuation">(</span>Col2<span class="token punctuation">,</span>func<span class="token punctuation">)</span><span class="token punctuation">)</span>
<span class="token comment"># generates new column names for agg. columns</span>
</code></pre>
<h3 id="concatenate-dataframes">Concatenate DataFrames</h3>
<p>This is the same as <code>append</code> in Power BI</p>
<pre class=" language-python"><code class="prism  language-python">pd<span class="token punctuation">.</span>concat<span class="token punctuation">(</span><span class="token punctuation">[</span>df1<span class="token punctuation">,</span>df2<span class="token punctuation">,</span>df3<span class="token punctuation">]</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="merge-and-join">Merge and Join</h3>
<p>This are same as <code>merge</code> functionality in Power BI</p>
<pre class=" language-python"><code class="prism  language-python">pd<span class="token punctuation">.</span>merge<span class="token punctuation">(</span>df1<span class="token punctuation">,</span>df2<span class="token punctuation">,</span>how<span class="token operator">=</span><span class="token string">'inner'</span><span class="token punctuation">,</span>on<span class="token operator">=</span><span class="token string">'key'</span><span class="token punctuation">)</span> <span class="token comment"># common key</span>

pd<span class="token punctuation">.</span>merge<span class="token punctuation">(</span>df1<span class="token punctuation">,</span>df2<span class="token punctuation">,</span>how<span class="token operator">=</span><span class="token string">'inner'</span><span class="token punctuation">,</span>on<span class="token operator">=</span><span class="token punctuation">[</span><span class="token string">'key1'</span><span class="token punctuation">,</span><span class="token string">'key2'</span><span class="token punctuation">]</span><span class="token punctuation">)</span> <span class="token comment"># will join based </span>
<span class="token comment"># on common combinations between key1 and key2</span>
</code></pre>
<p>More details on <code>join</code> available <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html">here</a><br>
This works on the premise that the joining key is the <strong>index</strong> label between 2 dataframes or else, use <code>merge</code> (useful to use column labels)<br>
In case of overlapping column labels, <code>lsuffix</code> and <code>rsuffix</code> need to be indicated.</p>
<h3 id="pandas-dataframes-operations-and-data-input-output">Pandas DataFrames Operations and Data Input-Output</h3>
<p>Head</p>
<pre class=" language-python"><code class="prism  language-python">df<span class="token punctuation">.</span>head <span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># will show sample of the dataset </span>
<span class="token comment"># with default 5 rows</span>
</code></pre>
<p>Refer to the link <a href="https://www.mindomo.com/mindmap/0a313fed6d2d4003abfd254e2fe3d963#">here</a></p>
<p>Specific to HTML, the html link has table references built into the code. The <code>pd.read_html</code> creates a list object of the table references which can be called through the indexing method</p>

