<?php
// get session and show cate
$objectManager = \Magento\Framework\App\ObjectManager::getInstance();
$customerSession = $objectManager->get('Magento\Customer\Model\Session');
$_catename = $customerSession->getCatecheckoutcart();
?>
 
<!-- add category name -->
<?php if (!empty($_catename)): ?>
	<span> Category name: <?php echo $block->escapeHtml($_catename[$product->getSku()])?></span>
<?php endif ?>
<!--  -->
