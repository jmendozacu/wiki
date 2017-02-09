Installation Guide
==================


For Magento 1.6 and above
-------------------------

**Step 1:**

You copy all files in the extension folder to the Magento root folder.

**Step 2:**

You copy file **app/code/core/Mage/Catalog/Model/Resource/Product/Collection.php** to **app/code/local/Mage/Catalog/Model/Resource/Product/Collection.php**
	
**Step 3:**  

Open file **app/code/local/Mage/Catalog/Model/Resource/Product/Collection.php**, search **"protected function _productLimitationPrice($joinLeft = false)"** 
and find this line:

.. literalinclude:: code_examples/magento_leftjoin_step3.py
	
**- Then, you insert the following code behind that line:**

.. literalinclude:: code_examples/magento_step3.py

**=> After inserting, you will have a code snippet as below:**

.. literalinclude:: code_examples/magento_codesnippet_step3.py

**Step 4:** 

Copy file **app/code/core/Mage/Catalog/Model/Product/Attribute/Backend/Groupprice/Abstract.php** to **app/code/local/Mage/Catalog/Model/Product/Attribute/Backend/Groupprice/Abstract.php**

**Step 5:** 

Open file **app/code/local/Mage/Catalog/Model/Product/Attribute/Backend/Groupprice/Abstract.php** , search **"public function afterLoad($object)"** and find this line:

.. literalinclude:: code_examples/megento_group_price_step5.py

**- Then, you insert the following code behind that line:**

.. literalinclude:: code_examples/magento_step5.py

(You can see the example file in the example folder if you have not still got it well and please note that you use it only for Magento 1.9.2.x)

For Magento 1.5 
--------------------

**Step 1:**

You copy file **app/code/core/Mage/Catalog/Model/Resource/Eav/Mysql4/Product/Collection.php** to 
**app/code/local/Mage/Catalog/Model/Resource/Eav/Mysql4/Product/Collection.php**

**Step 2:**

Open file **app/code/local/Mage/Catalog/Model/Resource/Eav/Mysql4/Product/Collection.ph**, search **"protected function _productLimitationJoinPrice()"** 
and find this line: 

.. literalinclude:: code_examples/magento1.5_join_step3.py

**- Then, you insert the following code behind that line**:

.. literalinclude:: code_examples/magento1.5_step3.py

**=>  After inserting, you will have a code snippert as below:**

.. literalinclude:: code_examples/magento1.5_codesnippet_step3.py

*Note: This installation guide is only used for Magento Multiple Store View Pricing version 2.1.6*
