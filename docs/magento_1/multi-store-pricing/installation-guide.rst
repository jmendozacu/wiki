Installation Guide
==================

**Step 1:**

Copy all files in the extension folder to the Magento root folder.

**Step 2:**

Copy file **app/code/core/Mage/Catalog/Model/Resource/Product/Collection.php** to **app/code/local/Mage/Catalog/Model/Resource/Product/Collection.php**

**Step 3:**  

Open file **app/code/local/Mage/Catalog/Model/Resource/Product/Collection.php**, search **"protected function _productLimitationPrice($joinLeft = false)"** 
and insert code below to after this line:

	if ($joinLeft) {
	
					$select->joinLeft($tableName, $joinCond, $colls);
					
				} else {
				
					$select->join($tableName, $joinCond, $colls);
					
	}

	
Code to insert: 

//add modify code get store price

.. literalinclude:: code_examples/magento_step3.py

//end


	
