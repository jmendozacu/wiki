$response = Mage::app()->getResponse();

//code defer
if(Mage::helper('bss_deferjs')->isEnabled()) {
	$body = Mage::helper('bss_deferjs')->deferJs($body);
}
//end

$response->setBody($body);

....

//code defer
if(Mage::helper('bss_deferjs')->isEnabled()) {
	$body = Mage::helper('bss_deferjs')->deferJs($body);
}
//end
$observer->getEvent()->getResponse()->setBody($body);

...

//code defer
if(Mage::helper('bss_deferjs')->isEnabled()) {
	$body = Mage::helper('bss_deferjs')->deferJs($body);
}
//end
$observer->getTransport()->setHtml($placeholder);
