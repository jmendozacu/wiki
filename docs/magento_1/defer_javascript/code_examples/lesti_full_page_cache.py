$response = Mage::app()->getResponse();
                $response->setBody($body);
	
	...
	$observer->getEvent()->getResponse()->setBody($body);

	...
	
	$observer->getTransport()->setHtml($placeholder);
