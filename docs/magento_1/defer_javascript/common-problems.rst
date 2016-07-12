Common Problems
================

I've uploaded the files to the site. Now when I tried to access to the module get this error message:  
Fatal error: Class 'Bss_DeferJS_Block_Adminhtml_Form_Field_Regex' not found in/home/storedep/public_html/includes/src/__default.php on line 28651 

When installation Defer Javascript extension, customers often run into this kind of error as they forget to disable compilation as it's required that before 
you make any changes to your Magento installation you should always **disable compilation**. To fix this problem, just simply run the compilation process, andthen 
enable it. 

To disable Compilation in Magento, please navigate to Admin panel Go to System > Tools > Compilation page and click on **Disable** button


.. raw:: html

	<style>
		p {text-align: justify;}
	</style>