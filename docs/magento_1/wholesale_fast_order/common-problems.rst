Common Problems 
================

**1. Having problems with Currency Decimal separator?**

	In some countries Currency separator is " , " while " . " is used in US or UK. To fix problem when installing Wholesale Fast Order on the store using 
	Decimal separator as " , " please follow below changes:

	**Edit file:** /skin/frontend/base/default/js/bss/fastorder.js

	**Change:** 

		finalprice   = Number(finalprice.replace(/[^0-9\.]+/g," "));
	  
	**Into:**

		finalprice   = Number(finalprice.replace(" , " , " . "));


	**Change:**

.. literalinclude:: code_examples/common_problem_change.py
	 
	**Into:**

.. literalinclude:: code_examples/common_problem_into.py


.. raw:: html

	<style>
		p {text-align: justify;}
	</style>