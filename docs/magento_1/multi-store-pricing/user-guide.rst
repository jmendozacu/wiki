User Guide
=============

.. role:: italic

.. role:: euro

.. role:: pound

Magento Multiple Store View Pricing Extension 
---------------------------------------------------

Being an e-Commerce shop owner, have you ever found a temporary solution to set particular prices for each store view of the whole store system? Nevertheless, what will you do if you have a desire for setting multiple 
prices of the same items in each store view of each local store but all default Magento functions cannot help you handle it?

`Multiple Store View Pricing extension <http://bsscommerce.com/magento-multistore-pricing.html>`_ is a useful tool which allows online shop owners set and display different prices for each product in each store view 
of the corresponding store as wish. With this powerful extension, now you will not face with any trouble in 

How does Magento Multiple Store View Pricing Extension work?
------------------------------------------------------------

1.	Enable Multiple Store View Pricing Extension 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You go to **System** -> **Configuration** -> **Catalog**. Among all sections shown up in the page, find **Price** section to start the customization.
	
.. image:: images/multi_store_pricing_1.jpg

In box **Catalog Price Scope**, there are 3 options for admin to choose: :italic:`Global, Website, Store`. 

You choose :italic:`Store` to enable the module. Then you click **Save Config** and begin to customize prices of products in each store view of each store

2.	Set up price for a product in the English store view: Madison 8GB Digital Media Player, for example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.1		Set up base currency and default currency for English store view
************************************************************************

	In **Configuration**, you go to **General -> Currency Setup** to set up base currency for English store view 

	Choose **English** store view from **Current Configuration Scope**

	.. image:: images/multi_store_pricing_2.jpg

	In **Base Currency:** Choose **British Pound Sterling** as base currency and customers will use this one to checkout. 

	In **Default Display Currency:** you can choose **British Pound Sterling** or any other currency because this one is only displayed in the product or 
	category page, not used in the checkout. 

	In **Allowed Currencies:** Choose **British Pound Sterling**

	Then, click to **Save config** and start to set up price for a product in the English store view


2.2.	Set up price for Madison 8GB Digital Media Player in the English store view
***********************************************************************************

	Go to **Manage Products** and choose Madison 8GB Digital Media Player to edit

	**Step 1**: Choose **English** store view per store (Main Store) in **Choose store view box**

	**Step 2**: In **Price** section (on the left side column), you unmark **"Use Default Value"** and add your wanted price for the product in this 
	English store view: :pound:`600`, for instance 

	.. image:: images/multi_store_pricing_2.2.jpg

	In addition, you can also set up **Group Price, Special Price and Tier Price per store view** for this product if you want.

	* In Group Price For Store View: Click Add Group Price button to add new group prices. You choose each customer group in the drop-down list and set up a particular price of this product

	* In Special Price: Set up a special price of this product in English store view

	* In Tier price For Store View: Click Add Tier for adding new Tier prices

	Finally, you save configuration and see the changes from the frontend page 

	**Prices of Madison 8GB Digital Media Player in the English store view from the product page:** 

	.. image:: images/multi_store_pricing_2.3.jpg

3. Set up price for a product in the French store view: Madison 8GB Digital Media Player, for example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.1. Set up base currency and default currency for French store view
********************************************************************

	In **Configuration**, you go to **General -> Currency Setup** to set up base currency for French store view 

	Choose **French** store view from **Current Configuration Scope**

	.. image:: images/multi_store_pricing_3.jpg

	In **Base Currency:** Choose **Euro** as base currency and customers will use this one to checkout. 

	In **Default Display Currency:** you can choose Euro or any other currency because this one is only displayed in the product or category 
	page, not used in the checkout. 

	In **Allowed Currencies:** Choose **Euro** 
	
	Then, click to **Save config** and start to set up price for a product in the French store view


3.2.	Set up price for Madison 8GB Digital Media Player in the French store view
**********************************************************************************

	Go to **Manage Products** and choose Madison 8GB Digital Media Player to edit
   
	**Step 1**: Choose **French** store view per store (Main Store) in **Choose store view box**

	.. image:: images/multi_store_pricing_3.1.jpg

	**Step 2**: In **Price** section (on the left side column), you unmark **"Use Default Value"** and add your wanted price for the product in this 
	French store view: :euro:`800`, for instance 
	
	For Special prices, Group prices for Store View and Tier Prices For Store View, you do similarly to that in English store view as mentioned before.
	
	Finally you save configuration in go to the frontend to see the changes:

	**Prices of Madison 8GB Digital Media Player in the French store view from the product page:** 

	.. image:: images/multi_store_pricing_3.2.jpg

4. Conclusion
^^^^^^^^^^^^^

After all above settings, you can see differences in prices of Madison 8GB Digital Media Player between English and French store view.


.. raw:: html

   <style>
		.pound:before {content:'\00A3';}
		.euro:before {content:'\20AC';}
		.italic{font-style: italic;font-weight:bold;}
		p {text-align: justify;}
   </style>