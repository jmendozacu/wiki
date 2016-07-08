#0 /www/magento2/vendor/magento/framework/Config/Reader/Filesystem.php(127): Magento\Config\Model\Config\Structure\Reader
->_readFiles(Object(Magento\Framework\Config\FileIterator))

#1 /www/magento2/vendor/magento/framework/Config/Data/Scoped.php(103): Magento\Framework\Config\Reader\Filesystem->read('adminhtml')

#2 /www/magento2/vendor/magento/framework/Config/Data/Scoped.php(81): Magento\Framework\Config\Data\Scoped->_loadScopedData()

#3 /www/magento2/vendor/magento/module-config/Model/Config/Structure.php(66): Magento\Framework\Config\Data\Scoped->get()

#4 /www/magento2/var/generation/Magento/Config/Model/Config/Structure/Interceptor.php(14): Magento\Config\Model\Config\Structure
->__construct(Object(Magento\Config\Model\Config\Structure\Data), Object(Magento\Config\Model\Config\Structure\Element\Iterator\Tab), 
Object(Magento\Config\Model\Config\Structure\Element\FlyweightFactory), Object(Magento\Config\Model\Config\ScopeDefiner))

#5 /www/magento2/vendor/magento/framework/ObjectManager/Factory/AbstractFactory.php(103): Magento\Config\Model\Config\Structure\Interceptor
->__construct(Object(Magento\Config\Model\Config\Structure\Data), Object(Magento\Config\Model\Config\Structure\Element\Iterator\Tab),
 Object(Magento\Config\Model\Config\Structure\Element\FlyweightFactory), Object(Magento\Config\Model\Config\ScopeDefiner))
 
#6 /www/magento2/vendor/magento/framework/ObjectManager/Factory/Compiled.php(88): Magento\Framework\ObjectManager\Factory\AbstractFactory
->createObject('Magento\\Config...', Array)
