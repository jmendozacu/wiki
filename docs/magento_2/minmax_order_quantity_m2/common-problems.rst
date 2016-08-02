Common Problems 
================

**How to show the category name?**

	If customers use the similar theme to default or they customized item section in the cart, comment folder Bss/MinMaxQtyOrderPerCate/view and add file into 
	theme (view/frontend/templates/cart/item/default.phtml)

	.. literalinclude:: code_examples/create_default.py
	
	compared to file   Bss/MinMaxQtyOrderPerCate/view/frontend/templates/cart/item/default.phtml to add exactly

	edit message
	Bss/MinMaxQtyOrderPerCate/Observer/MinMaxQty.php

	.. literalinclude:: code_examples/edit_message.py

.. raw:: html

	<style>
		p {text-align: justify;}
		a[class='reference external'] {font-weight:bold;}
	</style>