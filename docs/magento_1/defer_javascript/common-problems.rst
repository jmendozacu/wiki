Common Problems
================

.. role:: italic

**1. I've uploaded the files to the site. Now when I tried to access to the module get this error message:  
Fatal error: Class 'Bss_DeferJS_Block_Adminhtml_Form_Field_Regex' not found in/home/storedep/public_html/includes/src/__default.php on line 28651**

When installation `Defer Javascript extension <http://bsscommerce.com/magento-defer-js-extension.html>`_ , customers often run into this kind of error as they forget to disable compilation as it's required that before 
you make any changes to your Magento installation you should always **disable compilation**. To fix this problem, just simply run the compilation process, andthen 
enable it. 

To disable Compilation in Magento, please navigate to Admin panel Go to System > Tools > Compilation page and click on **Disable** button

**2. Configure Defer Javascript with Full Page Cache**

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
	
.. raw:: html

	<style>
		.italic {font-weight:bold; font-style:italic;}
		p {text-align: justify;}
	</style>