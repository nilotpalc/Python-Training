---


---

<h5 id="my-current-usage-in-the-office-laptop-allows-me-to-use-the-conda-environment.-despite-multiple-efforts-the-windows-command-prompt-option-for-using-pip-method-is-not-working.-i-will-need-to-continue-to-use-the-conda-environment-to-install-and-use-packages">My current usage in the office laptop allows me to use the conda environment. Despite multiple efforts, the windows command prompt option for using pip method is not working. I will need to continue to use the conda environment to install and use packages</h5>
<p>Main Aspects on Modules and Packages</p>
<blockquote>
<p>Package</p>
<blockquote>
<p>Module</p>
<blockquote>
<p>Function</p>
</blockquote>
</blockquote>
</blockquote>
<p><strong>Packages</strong> is a folder that contains multiple .py files which are call <strong>Modules</strong>. Modules are sometimes also referred to as python scripts.<br>
Modules contain the coding statements that define functions that are used in our progams.</p>
<p>Sometimes, packages can have sub-folders defined within them.</p>
<blockquote>
<p>Package</p>
<blockquote>
<p>Sub-Package</p>
<blockquote>
<p>Module</p>
</blockquote>
</blockquote>
</blockquote>
<h4 id="these-files-need-to-be-.py-files-and-not-.ipnb-files">These files need to be .py files and not <em>*.ipnb</em> files</h4>
<blockquote>
<p>Whenever a Package or Sub-Package Folder is created, it should be in the same environment as the working directory environment. Also, a file name <code>__.init__.py</code> needs to be created in these folders to allow python to understand their setup. The blank file can be created through ATOM Editor.</p>
</blockquote>
<p>The working directory can be found by typing <code>pwd</code> in</p>
<p>To call functions into the main file, the following syntax is used -</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">from</span> packagename <span class="token keyword">import</span> modulename
<span class="token keyword">def</span> <span class="token function">abc</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	modulename<span class="token punctuation">.</span>functionname<span class="token punctuation">(</span><span class="token punctuation">)</span> <span class="token comment"># Function is referenced along with </span>
	                      <span class="token comment"># module name</span>
<span class="token comment"># Importing from </span>
<span class="token keyword">from</span> packagename<span class="token punctuation">.</span>subpackage <span class="token keyword">import</span> modulename
<span class="token keyword">def</span> <span class="token function">abc</span><span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span>
	modulename<span class="token punctuation">.</span>functionname<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>

