How to create Magento 2 module
===============================

We create module with Namespace is Magecheckout and Module Name is HelloWorld
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Step 1`` Create **registration.php** in:
``app > code > Magecheckout > HelloWorld`` ::

 \Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrar::MODULE,
    'Magecheckout_HelloWorld',
    __DIR__
 );


``Step 2`` Create **module.xml** in:
``app > code > Magecheckout > HelloWorld > etc`` ::

 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Magecheckout_HelloWorld" setup_version="1.0.0">
    </module>
 </config>

``Step 3`` Declaring a frontend router, create the **routes.xml** file by the following path:
``app > code > Magecheckout > HelloWorld > etc > frontend``::

 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:App/etc/routes.xsd">
    <router id="standard">
        <route id="helloworld" frontName="helloworld">
            <module name="Magecheckout_HelloWorld" />
        </route>
    </router>
 </config>

``Step 4`` Create our Controller action **Index.php** in:
``app > code > Magecheckout > HelloWorld > Controller > HelloWorld``::

 namespace Magecheckout\HelloWorld\Controller\HelloWorld;
 use Magento\Framework\View\Result\PageFactory;
 use Magento\Framework\App\Action\Context;

 use  Magento\Framework\App\Action\Action;
 class Index extends Action
 {
    protected $resultPageFactory;

    public function __construct(
        Context $context,
        PageFactory $resultPageFactory
    ) {
        parent::__construct($context);
        $this->resultPageFactory = $resultPageFactory;
    }


    public function execute()
    {
        $resultPage = $this->resultPageFactory->create();
        return $resultPage;
    }
 }
``Step 5`` Create Layout file **helloworld_helloworld_index.xml** in:
``app > code > Magecheckout > HelloWorld > view > frontend > layout``::

 <page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" layout="1column" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="MageCheckout\HelloWorld\Block\HelloWorld" name="helloworld" template="helloworld.phtml"/>
        </referenceContainer>
    </body>
 </page>


``Step 6`` Create Block **HelloWorld.php** in:
``app > code > Magecheckout > HelloWorld > Block``::

 namespace Magecheckout\HelloWorld\Block;
 use Magento\Framework\View\Element\Template;
 class HelloWorld extends Template
 {
 protected function _prepareLayout()
    {
        $this->pageConfig->getTitle()->set(__('Hello World'));
        return parent::_prepareLayout();
    }
 }

``Step 7`` Create Template **helloworld.phtml** in:
``app > code > Magecheckout > HelloWorld > view > frontend > layout > templates``::

 Welcome



``Step 8`` Open Command line in folder root of magento and run commands ::

 php bin/magento setup:upgrade

the result will be shown as the following
``````````````````````````````````````````
.. image:: https://lh4.googleusercontent.com/uv5HjdNPGmwoKlxMx_QyCv4axxqQ6Dz5mMzeQtixi2Y4QoOANt4K7Cdcybn5C94UjlKJGz2laeyqkTqIg1hl00hNZaAR0afO-HGfpFXrROdMJPnsFBAaO6olmtdMqj4FonD_fdzp



Boost sales with `Magento One Step Checkout extension <https://www.magecheckout.com/magento-one-step-checkout.html>`_ and `Magento One Step Checkout <https://www.magentocommerce.com/magento-connect/one-step-checkout-37-28858.html>`_