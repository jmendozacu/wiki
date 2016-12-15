Common Problems
================

.. role:: italic

1. I've uploaded the files to the site. Now when I tried to access to the module get this error message:  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fatal error: Class 'Bss_DeferJS_Block_Adminhtml_Form_Field_Regex' not found in/home/storedep/public_html/includes/src/__default.php on line 28651**

	When installation `Defer Javascript extension <http://bsscommerce.com/magento-defer-js-extension.html>`_ , customers often run into this kind of error as 
	they forget to disable compilation as it's required that before you make any changes to your Magento installation you should 
	always **disable compilation**. To fix this problem, just simply run the compilation process, and then enable it. 

	To disable Compilation in Magento, please navigate to Admin panel Go to System > Tools > Compilation page and click on **Disable** button

2. Configure Defer Javascript with Full Page Cache
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	To configure module Defer Javascript with module Full Page Cache, please follow all following instructions (2 steps).

	step1: In the folder named "Model" of module Full Page Cache, find all functions named "setBody" or "setHtml" (In almost cases, you can find these functions 
	in file "Observer.php")
	
	:italic:`*Note: "setHtml" function just appears in some cases`
	
	-For example in **Lesti_Full Page Cache** module :
	
	.. literalinclude:: code_examples/lesti_full_page_cache.py
	
	step2: Still in this example, add one of the following code defer above function "setBody" or "setHtml" 
	
	:italic:`*Note: there are 3 types of code defer for each type of function:`
	
	For example: 
	
	.. literalinclude:: code_examples/configure_cache_step2.py

	
	After all of these steps, you have done configuring module Defer Javascript to work well with module Full Page Cache.

3. Defer JavaScript cannot interfere JavaScript fills from frames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	For Magento sites including a lot of video embedded for the third parties such as Youtube, Vimeo and so on, site speed is also considerably influenced (slower)and causes 
	customers to wait so long for loading these video. When installing Defer JavaScript extension, there is an issue that the module cannot interfere JavaScript files from frames, so 
	it does not have any effect on deferring these JavaScript files in order to make sites perform faster. 

	To solve this problem, we need to defer video loading to save many file requests and resource downloads, which can improve site performance effectively. It means 
	that we will keep the video from loading all the associated files by not identifying the iframe src until after the page loads.

	**Step 1: Get the embed code of the video you want to defer**

	Take an example:

	<iframe width="853" height="480" src="https://www.youtube.com/embed/7ngPu_kUdN4?rel=0" frameborder="0" allowfullscreen></iframe>

	**Step 2: Alter the embed code by making 2 following changes**

	* Make the "src" empty by removing the url from it as below: src=""
	
	* Put the url that is cut from "src" and add it to "data-src".
	
	data-src=”//www.youtube.com/embed/7ngPu_kUdN4?rel=0”

	Therefore, the code becomes: 

	<iframe width="853" height="480" src="" data-src=”//www.youtube.com/embed/7ngPu_kUdN4?rel=0”frameborder="0" allowfullscreen></iframe>

	**Step 3: Add the script to bottom of page**
	
	.. literalinclude:: code_examples/interfere_javaScript.py

4. The Defer score does not increase in case Magento sites uses Full Page Cache also
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	We need to fix the Full Page Cache module to overcome this problem (Let’s look at the instruction enclosed with installation guide) For more details, it can be explained as below: 

	The purpose of the Full Page Cache extension is saving HTML of Magento sites into Caches and these HTML are set up again by using events when loading sites. Therefore, to fix this 
	module, we firstly use keywords such as setBody and setHTML to search for code snippets that have HTML setup again. Next, we add a code snippet of Defer JavaScript (called from helper) 
	into those HTML codes (have HTLM setup again) and then setBody and setHTML.

5. The Defer score does not increase although JavaScript files stay on </body>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	Let’s set **No** for **Put Javascript In HTML Body Tag** section in the configuration of the module 

	.. image:: images/defer_js_problem_1.jpg
	
6. The Defer score does not increase although JavaScript files stay on the bottom of page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	If the Magento site uses a Minify HTML module, we need to disable it and then check on `GTMetrix <https://gtmetrix.com/>`_
	
	In case this solution does not make the defer score go up, we need to check again to find out which JavaScript is causing this error.

7. Some images from the third parties that are inserted by using JavaScript are pulled down after deferring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

	There are two ways to solve this problem: 
	
		*	Use nodefer tags to make these images not be pulled down
		
		*	Rewrite their JavaScript in case you want to get higher defer scores 




.. raw:: html

	<style>
		.italic {font-weight:bold; font-style:italic;}
		p {text-align: justify;}
	</style>