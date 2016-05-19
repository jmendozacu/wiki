Installation Guide
==================

.. role:: header

**Step 1:**

Copy all files in the extension folder to the Magento root folder.

**Step 2:**

Copy file **app/code/core/Mage/Catalog/Model/Resource/Product/Collection.php** to **app/code/local/Mage/Catalog/Model/Resource/Product/Collection.php**
	
**Step 3:**  

Open file **app/code/local/Mage/Catalog/Model/Resource/Product/Collection.php**, search **"protected function _productLimitationPrice($joinLeft = false)"** 
and insert code below to after this line:

.. literalinclude:: code_examples/magento_leftjoin_step3.py
	
* Code to insert: 

.. literalinclude:: code_examples/magento_step3.py

(You can show example in folder example- file it only for Magento 1.9.2.x)

:header:`For Magento 1.5:` 

**Step 1:**

Copy all files in the extension folder to the Magento root folder.

**Step 2:**

Copy file **app/code/core/Mage/Catalog/Model/Resource/Eav/Mysql4/Product/Collection.php** to 
**app/code/local/Mage/Catalog/Model/Resource/Eav/Mysql4/Product/Collection.php**

**Step 3:**

Open file **app/code/local/Mage/Catalog/Model/Resource/Eav/Mysql4/Product/Collection.ph**, search **"protected function _productLimitationJoinPrice()"** 
and insert code below after this line: 

.. literalinclude:: code_examples/magento1.5_join_step3.py

* Code to insert:

.. literalinclude:: code_examples/magento1.5_step3.py


.. raw:: html

   <style>
		.header{font-size: 1.3333em; font-weight: bold;}
   </style>
