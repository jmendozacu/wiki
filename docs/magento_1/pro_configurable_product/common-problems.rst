Common Problems
================

How to fix "Please specify the product's option(s)" error?

Common error with `Pro configurable product grid table view extension <http://bsscommerce.com/magento-pro-magento-configurable-product-grid-table-view.html>`_ is 
conflict with ajax add to cart extension. The conflict is shown with error message "Please specify the product's option(s)"

Please find below some ways to fix this issue with some ajax add to cart extension from various extension’s provider.

**1. Conflict with Smartwave_Ajaxcart**

Edit file : Smartwave/Ajaxcart/controller/IndexController.php
	
	* Edit function addAction();
	
	* Edit extends => Bss_ConfigurableProductTabTable_CartController

Sample file: https://www.dropbox.com/s/r1d0eddma7jfhqy/IndexController.php?dl=0


**2. Conflict with PT_Ajax**

edit file: PT/Ajax/controllers/Checkout/CartController.php

	* Edit extends Bss_Configurablegridview_CartController
	
	* Edit function addAction();
	
	* Edit function updateItemOptionsAction();

Sample file: https://www.dropbox.com/s/qvlfx1jg2z6743r/PT_Ajax_CartController.php?dl=0

**3. Conflict with Amasty Ajax add to cart**

In the file: app/code/local/Amasty/Cart/controllers/AjaxController.php

Add  function: _initProduct();

Edit function indexAction() into:

.. literalinclude:: code_examples/conflict_amasty_ajax.py
	
Sample file: https://www.dropbox.com/s/vz9bjgx9rd2ue97/AjaxController.php?dl=0

**4. Conflict with Magentothem_Ajaxcartsuper**

Edit file: /app/code/local/Magentothem/Ajaxcartsuper/controllers/AjaxcartController.php

Edit function addAction() to:

.. literalinclude:: code_examples/conflict_magentothem_ajaxcartsuper.py

Sample file: https://www.dropbox.com/s/frkidfqdke3p5kp/AjaxcartController.php?dl=0



.. raw:: html

	<style>
		p {text-align: justify;}
	</style>