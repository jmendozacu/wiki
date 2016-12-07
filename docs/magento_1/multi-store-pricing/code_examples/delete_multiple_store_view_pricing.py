<?php
require_once('app/Mage.php');
umask(0);
Mage::app();
 
 
$resource = Mage::getSingleton('core/resource');
$readConnection = $resource->getConnection('core_read');
$writeConnection = $resource->getConnection('core_write');
 
 
$query = "SELECT attribute_id FROM " . Mage::getSingleton('core/resource')->getTableName('eav/attribute') . " 
WHERE attribute_code = 'price' AND backend_model != '' LIMIT 1";

$attribute_id = $readConnection->fetchOne($query);
 
if($attribute_id) {
    $query = "DELETE FROM ".Mage::getSingleton('core/resource')->getTableName('catalog_product_entity_decimal')." 
	WHERE `attribute_id` = ".$attribute_id." AND `store_id` != '0'";
	
    $writeConnection->query($query);
}
 
echo 'Delete price per store view success.';
echo '<br>';
 
 
$query = "SELECT attribute_id FROM " . Mage::getSingleton('core/resource')->getTableName('eav/attribute') . " 
WHERE attribute_code = 'special_price' AND backend_model != '' LIMIT 1";

$attribute_id = $readConnection->fetchOne($query);
if($attribute_id) {
    $query = "DELETE FROM ".Mage::getSingleton('core/resource')->getTableName('catalog_product_entity_decimal')." 
	WHERE `attribute_id` = ".$attribute_id." AND `store_id` != '0'";
	
    $writeConnection->query($query);
}
 
echo 'Delete special price per store view success.';