//add modify
if(!Mage::app()->getStore()->isAdmin() && Mage::helper('core')->isModuleEnabled('Bss_MultiStoreViewPricing') 
	&& Mage::helper('multistoreviewpricing')->isScopePrice() == 1) {

    if($this->getAttribute()->getName() == 'tier_price') {
        $use_tier_default = false;
        $tier_default = Mage::helper('multistoreviewpricing')->getTierPriceOption();
        if($tier_default == 1) {
            $use_tier_default = true;
		}else {
            $tier_default = Mage::getModel('multistoreviewpricing/tierDefault')->getCollection()
            ->addFieldToSelect('*')
            ->addFieldToFilter('product_id', $object->getId())
            ->addFieldToFilter('store_id', Mage::app()->getStore()->getId())
            ->getFirstItem();
            if($tier_default && $tier_default->getId() != '' && $tier_default->getStatus() == 0) {
                $use_tier_default = true;
            }
		}

		if($use_tier_default) {
			$data = array();
			$tiers = Mage::getResourceSingleton('multistoreviewpricing/product_attribute_backend_tierprice')->getPriceStoreData($object->getId(), 
				Mage::app()->getStore()->getId());
			if(count($tiers) > 0) {
				foreach($tiers as $tier) {
					unset($tier['store_id']);
					$tier['website_id'] = $websiteId;
					$tier['website_price'] = $tier['price'];
					$data[] = $tier;
				}
			}
		}
	}
            

    if($this->getAttribute()->getName() == 'group_price') {
        $groups = Mage::getResourceSingleton('multistoreviewpricing/product_attribute_backend_groupprice')->getPriceStoreData($object->getId(), 
			Mage::app()->getStore()->getId() , Mage::getSingleton('customer/session')->getCustomerGroupId());
        if(count($groups) > 0) {
            foreach($groups as $group) {
                $data = array();
                $group['website_price'] = $group['price'];
                $data[] = $group;
            }
        }
    }
}
//end
