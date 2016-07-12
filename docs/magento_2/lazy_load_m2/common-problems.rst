Common Problems 
================

**1. Having a problem when installing `Magento 2 Lazy Load extension <http://bsscommerce.com/magento2/magento-lazy-image-loader-extension-for-magento-2.html>`_ on magento 2.1?**

	**Error message**
	
	Invalid XML in file /www/magento2/app/code/Bss/LazyImageLoader/etc/adminhtml/system.xml:
	
	Element 'field', attribute 'validate': The attribute 'validate' is not allowed.
	
	Line: 52
	
	Element 'field', attribute 'validate': The attribute 'validate' is not allowed.
	
	Line: 56

	.. literalinclude:: code_examples/install_error.py

	**How to fix?**
	
	Delete validate tag in app/code/Bss/LazyImageLoader/etc/adminhtml/system.xml
	
	Example :
	
	.. literalinclude:: code_examples/install_error_linechange.py

	change to :
	
	.. literalinclude:: code_examples/install_error_fix.py

.. raw:: html

	<style>
		p {text-align: justify;}
	</style>