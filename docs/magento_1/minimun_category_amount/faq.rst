FAQs
====

.. role:: bullet

Features
--------

**1. In what case specifically this module’s function work best?**

:bullet:`When` store owners want to refuse orders with tiny amounts that are not effective to run through the whole process until delivered to save 
shipping costs. 
 

**2. Does this extension have another version compatible with Magento 2 platform?**

:bullet:`Unfortunately`, version for Magento 2 of BSS Minimum Order Amount for Categories extension is still not available until now. However, there is another 
one already having two versions for Magento 1 and Magento 2 which works in a quite similar 
function: `BSS Minimum Order Amount for Customer Group <http://bsscommerce.com/magento-minimum-order-amount-for-customer-group-for-magento-2.html>`_ . Check it 
out if you are interested.


**3. Does this extension allow me to set minimum order amount for every subcategory or just for main categories?**

:bullet:`Yes`. Minimum order amount can be set up for all categories and subcategories of products on your website



**4. Does this extension support a customized notification to customers when their order amount is less than the minimum set?**

:bullet:`Yes`. And remember to follow the structure to create this customized message, for example: "Category "{{category}}" has an 
order minimum of {{price}}". Because {{category}} and {{price}} are added to make sure each name and minimum order amount of a certain category to 
be shown in a specific notification


**5. Does this minimum order amount configuration take effect at website level or store view level?**

:bullet:`Only at store view level`. To change the store view, select which one you want at the section "Current Configuration Scope" on the top left of 
Categories Minimum Amount configuration page


Guide
-----

**1. When a product is shorted into multiple categories and minimum order amounts of them are set differently, which one will be the final minimum order 
amount for that product?**

:bullet:`There are` two options for you to decide the final minimum order amount for a certain product in multiple categories: it will be the min or max price 
among  different minimum order amounts for all those categories. To do so, go to System :bullet:`Configuration` :bullet:`BSS Commerce` :bullet:`Categories Minimum Amount` then 
enable the module, at "Select children categories price" you choose Min Price or Max Price

	* Min Price: The final one will be the lowest among minimum amounts of all categories into which that product is sorted
	
	* NMax Price: The final one will be the highest among minimum amounts of all categories into which that is sorted 

**2. When i don't fill in a specific minimum order amount for a subcategory, does the minimum order amoun of its root category count?**

:bullet:`This is` also can decided by your options: the answer can be Yes or No depending on which one you choose at the section 
"Select minimum order amount of parent categories" (System :bullet:`Configuration` :bullet:`BSS Commerce` :bullet:`Categories Minimum Amount`)

	* Choose Yes: Minimum amount of root category will be counted as minimum amount of that subcategory
	
	* Choose No: Minimum order amount of root category will not be counted, which means that subcategory has no minimum order amount



.. raw:: html

	<style>
		p {text-align: justify;}
		.bullet:before {content:'\2192';margin-right: 5px;}
	</style>

