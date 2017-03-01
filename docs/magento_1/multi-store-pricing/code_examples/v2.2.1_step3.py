//add modify
if(Mage::helper('core')->isModuleEnabled('Bss_MultiStoreViewPricing') && Mage::helper('multistoreviewpricing')->isScopePrice() == 1) {

    if(!Mage::helper('multistoreviewpricing')->checkProductAdmin()) {
        if($this->getAttribute()->getName() == 'tier_price') {
            $use_tier_default = false;
            $tier_default = Mage::helper('multistoreviewpricing')->getTierPriceOption($storeId);
            if($tier_default == 1) {
                $use_tier_default = true;
            }else {
				$tier_default = Mage::getModel('multistoreviewpricing/tierDefault')->getCollection()
					->addFieldToSelect('*')
					->addFieldToFilter('product_id', $object->getId())
					->addFieldToFilter('store_id', $storeId)
					->getFirstItem();
				if($tier_default && $tier_default->getId() != '' && $tier_default->getStatus() == 0) {
					$use_tier_default = true;
				}
            }

            if($use_tier_default) {
                $data = array();
                $tiers = Mage::getResourceSingleton('multistoreviewpricing/product_attribute_backend_tierprice')->getPriceStoreData($object->getId(), $storeId);
                if(count($tiers) > 0) {
                    foreach($tiers as $tier) {
                        unset($tier['store_id']);
                        $tier['website_id'] = $websiteId;
                        $tier['website_price'] = $tier['price'];
                        if ($tier['all_groups'] == 1) {
                            $tier['cust_group'] = Mage_Customer_Model_Group::CUST_GROUP_ALL;
                        }
                        $data[] = $tier;
                    }
                }
            }
        }
                

        if($this->getAttribute()->getName() == 'group_price') {
            $groups = Mage::getResourceSingleton('multistoreviewpricing/product_attribute_backend_groupprice')->getPriceStoreData($object->getId(), $storeId , $object->getCustomerGroupId());
            if(count($groups) > 0) {
                foreach($groups as $group) {
                    $data = array();
                    $group['website_price'] = $group['price'];
                     $data[] = $group;
                }
            }
        }
    }
}
//end
