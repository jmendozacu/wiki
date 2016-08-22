public function getShippingRates()
{
  $modules = Mage::getConfig()>getNode('modules')>children();
  $modulesArray = (array)$modules;
  if(isset($modulesArray['Bss_Methods']) && Mage::helper('core')->isModuleEnabled('Bss_Methods')) {
    if (empty($this->_rates)) {
      $this->getAddress()>collectShippingRates()>save();
      $groups = $this->getAddress()->getGroupedAllShippingRates();
      // checking methods visibility for customer groups
      foreach ($groups as $methodCode => $method){
        if (!Mage::helper('bssmethods')->canUseMethod($methodCode, 'shipping')){
          unset($groups[$methodCode]); 
		}
 
      }
      return $this->_rates = $groups;
    }
    return $this->_rates;
  }
  return parent::getShippingRates();
}
