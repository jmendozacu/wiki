//add modify code get store price
            if(Mage::helper('multistoreviewpricing')->isScopePrice() == 1) {
        	 	$select = $this->getSelect();
            	$tableName = Mage::getSingleton('core/resource')->getTableName('catalog_product_entity_decimal');
            	$store_id = $this->getStoreId();
 
            	$minimalExpr = $connection->getCheckSql('bss_price_table_1.value IS NOT NULL', 'bss_price_table_1.value', 'price_index.price');
 
                $select->joinLeft(
                    array('bss_price_table_1' => $tableName),
                    "e.entity_id = bss_price_table_1.entity_id
                	AND bss_price_table_1.attribute_id = (SELECT attribute_id FROM " . Mage::getSingleton('core/resource')->getTableName('eav/attribute') . " WHERE attribute_code = 'price' AND backend_model != '' LIMIT 1) 
           	     AND bss_price_table_1.store_id = ".$store_id,
                    array('price' => $minimalExpr,  'final_price' => 'bss_price_table_1.value','minimal_price'=> 'bss_price_table_1.value')
                	);
 
                $select->joinLeft(
 	               array('bss_price_table_2' => $tableName),
                    "e.entity_id = bss_price_table_2.entity_id
                	AND bss_price_table_2.attribute_id = (SELECT attribute_id FROM " . Mage::getSingleton('core/resource')->getTableName('eav/attribute') . " WHERE attribute_code = 'special_price' AND backend_model != '' LIMIT 1) 
                	AND bss_price_table_2.store_id = ".$store_id."
                	AND bss_price_table_2.value < bss_price_table_1.value",
	                array('final_price' => 'bss_price_table_2.value','minimal_price'=> 'bss_price_table_2.value')
                	);
        	}
        	//end
