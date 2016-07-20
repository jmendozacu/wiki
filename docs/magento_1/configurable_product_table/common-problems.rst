Common Problems
================

**1. How to resolve conflict with Ajax Shopping Cart extension by Amasty?**

	https://amasty.com/ajax-shopping-cart.html 

	**Edit file:**
 
	app/code/local/Amasty/Cart/controllers/AjaxController.php

	**Add function:** _initProduct();

	**Edit function** indexAction() **into:**

	.. literalinclude:: code_examples/common_example_ajax.py

	Sample file:

	https://www.dropbox.com/s/vz9bjgx9rd2ue97/AjaxController.php?dl=0


.. raw:: html

	<style>
		p {text-align: justify;}
	</style>