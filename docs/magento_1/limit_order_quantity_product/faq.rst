FAQs
====

.. role:: bullet

.. role:: red

:red:`Features`
---------------

**Can Limit Order Quantity per Product take effects independently on different store views?**

No. These limits are all applied to global scope

 

**What limits this extension let me set for order quantity per product?**

BSS Limit Order Quantity per Product extension enables configuration of lowest and highest order quantity for each product that is valid for a 
customer to procced to check out.


**For each product, are maximum and minimum limits of order quantity fixed for every customer? What if I only want to set order quantity limits to 
some specific customers?**

Using this extension, limit order quantity per product can be set up differently among your customer groups, even when only one group is set up limits 
and others aren't. But you can also use a fixed limit for all customers by setting the same limits for all customer groups


**Does this extension support a customized message to notice customers about the limits of order quantity per product?**

With this extension, only the default notification of Magento is used to notice customers when limit order quantity is not satisfied

:red:`Guide`
------------

**How to set up order quantity limits per product in this extension?**

This extension is very easy to handle:

	* You just need to enable the module. To do that, go to System :bullet:`Configuration` :bullet:`BSS Commerce` :bullet:`Sales QTy for Customer Group`, then at General settings section of this module you choose Yes
	
	* Then go set up limits for which product you want (Catalog :bullet:`Manage Products` :bullet:`(choose the product)` :bullet:`Inventory` :bullet:`Set up Min/Max Sales Qty` for customer groups as picture below:



.. raw:: html

	<style>
		p {text-align: justify;}
		.bullet:before {content:'\2192';margin-right: 9px;}
		.red {color: red;}
	</style>

