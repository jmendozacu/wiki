How to create Magento 2 facebook login module
=============================================


We can create the module with Namespace - ``Magecheckout`` and Module Name- ``FacebookLogin``


**First**, Need to create **registration.php** in:
``app > code > Magecheckout > FacebookLogin`` ::

 \Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrar::MODULE,
    'Magecheckout_FacebookLogin',
    __DIR__
 );

**Second**, Create **module.xml** in:
``app > code > Magecheckout > FacebookLogin > etc`` ::

 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Magecheckout_FacebookLogin" setup_version="1.0.0">
    </module>
 </config>

**Third**, Let declar a frontend router by creating the **routes.xml** file as the following path:
``app > code > Magecheckout > FacebookLogin > etc > frontend``::

 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:App/etc/routes.xsd">
    <router id="standard">
        <route id="facebooklogin" frontName="facebooklogin">
            <module name="Magecheckout_FacebookLogin" />
        </route>
    </router>
 </config>


**Next**, In ``app > code > Magecheckout > FacebookLogin > etc > adminhtml``, create 3 files:

**menu.xml** ::

 <?xml version="1.0"?>
 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Backend:etc/menu.xsd">
    <menu>
        <add id="Magecheckout_FacebookLogin::magecheckout_facebooklogin" title="Facebook Login" module="Magecheckout_FacebookLogin" sortOrder="100" resource="Magecheckout_FacebookLogin::facebooklogin"/>
        <add id="Magecheckout_FacebookLogin::settings" title="Settings" module="Magecheckout_FacebookLogin" sortOrder="20" parent="Magecheckout_FacebookLogin::magecheckout_facebooklogin" action="adminhtml/system_config/edit/section/facebooklogin" resource="Magecheckout_FacebookLogin::settings"/>
    </menu>
 </config>

**routes.xml** ::

 <?xml version="1.0"?>
 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:App/etc/routes.xsd">
    <router id="admin">
        <route id="facebooklogin" frontName="facebooklogin">
            <module name="Magecheckout_FacebookLogin" before="Magento_Adminhtml" />
        </route>
    </router>
 </config>

**system.xml** ::

 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Config:etc/system_file.xsd">
    <system>
        <tab id="magecheckout" translate="label" sortOrder="400">
            <label>magecheckout</label>
        </tab>
        <section id="facebooklogin" translate="label" type="text" sortOrder="300" showInDefault="1" showInWebsite="1" showInStore="1">
            <class>separator-top</class>
            <label>Facebook Login</label>
            <tab>magecheckout</tab>
            <resource>Magecheckout_FacebookLogin::facebooklogin</resource>
            <group id="general" translate="label" type="text" sortOrder="5" showInDefault="1" showInWebsite="1" showInStore="1">
                <label>General</label>
                <field id="is_enabled" translate="label comment" type="select" sortOrder="10"  showInDefault="1" showInWebsite="1" showInStore="1">
                    <label>Enable</label>
                    <source_model>Magento\Config\Model\Config\Source\Yesno</source_model>
                </field>
                <field id="app_id" type="text" sortOrder="20" showInDefault="1" showInWebsite="1" showInStore="1">
                    <label>Facebook App Id</label>
                </field>
                <field id="app_secret" type="text" sortOrder="30" showInDefault="1" showInWebsite="1" showInStore="1">
                    <label>Facebook App Secret</label>
                </field>
                <field id="redirect_url" type="text" sortOrder="35" showInDefault="1" showInWebsite="1" showInStore="1">
                    <frontend_model>Magecheckout\FacebookLogin\Block\System\Config\Form\Field\Redirect</frontend_model>
                    <label>Valid OAuth redirect URIs</label>
                </field>
                <field id="send_password" translate="label comment" type="select" sortOrder="40"  showInDefault="1" showInWebsite="1" showInStore="1">
                    <label>Send Password To Customer</label>
                    <source_model>Magento\Config\Model\Config\Source\Yesno</source_model>
                </field>
            </group>
        </section>
    </system>
 </config>

**After that**, Must create **Redirect.php** in ``app > code > Magecheckout > FacebookLogin > Block > System > Config > Form > Field``
::

 namespace Magecheckout\FacebookLogin\Block\System\Config\Form\Field;

 use Magento\Framework\Data\Form\Element\AbstractElement;
 use Magento\Config\Block\System\Config\Form\Field as FormField;
 use Magecheckout\FacebookLogin\Helper\Data as DataHelper;
 use Magento\Backend\Block\Template\Context;

 class Redirect extends FormField
 {
    protected $dataHelper;

    public function __construct(
        Context $context,
        DataHelper $dataHelper,
        array $data = []
    ) {
        $this->dataHelper = $dataHelper;
        parent::__construct($context, $data);
    }

    protected function _getElementHtml(AbstractElement $element)
    {
        $html_id     = $element->getHtmlId();
        $redirectUrl = $this->dataHelper->getAuthUrl();
        $redirectUrl = str_replace('index.php/', '', $redirectUrl);
        $html        = '<input style="opacity:1;" readonly id="' . $html_id . '" class="input-text admin__control-text" value="' . $redirectUrl . '" onclick="this.select()" type="text">';

        return $html;
    }
 }

**Simultaneously**, In ``app > code > Magecheckout > FacebookLogin > etc``, create 2 files:
**acl.xml** ::

 <?xml version="1.0"?>
 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Acl/etc/acl.xsd">
    <acl>
        <resources>
            <resource id="Magento_Adminhtml::admin">
                <resource id="Magento_Adminhtml::stores">
                    <resource id="Magento_Adminhtml::stores_settings">
                        <resource id="Magento_Adminhtml::config">
                            <resource id="Magecheckout_FacebookLogin::facebooklogin_config" title="Facebook Login Section" />
                        </resource>
                    </resource>
                </resource>
            </resource>
        </resources>
    </acl>
 </config>

**config.xml** ::

 <?xml version="1.0"?>
 <config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Store:etc/config.xsd">
    <default>
        <facebooklogin>
            <general>
                <is_enabled>1</is_enabled>
            </general>
        </facebooklogin>
    </default>
 </config>

**Next**, Create Helper **Data.php** in ``app > code > Magecheckout > FacebookLogin > Helper`` ::

 namespace Magecheckout\FacebookLogin\Helper;

 use Magento\Framework\App\Helper\AbstractHelper;
 use Magento\Framework\App\Helper\Context;
 use Magento\Customer\Model\CustomerFactory;
 use Magento\Store\Model\StoreManagerInterface;
 use Magento\Framework\ObjectManagerInterface;

 class Data extends AbstractHelper
 {
    const XML_PATH_FACEBOOK_ENABLED = 'facebooklogin/general/is_enabled';
    const XML_PATH_FACEBOOK_APP_ID = 'facebooklogin/general/app_id';
    const XML_PATH_FACEBOOK_APP_SECRET = 'facebooklogin/general/app_secret';
    const XML_PATH_FACEBOOK_SEND_PASSWORD = 'facebooklogin/general/send_password';
    const XML_PATH_SECURE_IN_FRONTEND = 'web/secure/use_in_frontend';
    protected $customerFactory;
    protected $storeManager;
    protected $objectManager;

    public function __construct(
        Context $context,
        ObjectManagerInterface $objectManager,
        CustomerFactory $customerFactory,
        StoreManagerInterface $storeManager
    ) {
        $this->objectManager   = $objectManager;
        $this->customerFactory = $customerFactory;
        $this->storeManager    = $storeManager;
        parent::__construct($context);
    }

    public function getConfigValue($field, $storeId = null)
    {
        return $this->scopeConfig->getValue(
            $field,
            \Magento\Store\Model\ScopeInterface::SCOPE_STORE,
            $storeId
        );
    }

    public function isEnabled($storeId = null)
    {
        return $this->getConfigValue(self::XML_PATH_FACEBOOK_ENABLED, $storeId);
    }

    public function getAppId($storeId = null)
    {
        return $this->getConfigValue(self::XML_PATH_FACEBOOK_APP_ID, $storeId);
    }

    public function sendPassword($storeId = null)
    {
        return $this->getConfigValue(self::XML_PATH_FACEBOOK_SEND_PASSWORD, $storeId);
    }

    public function getAppSecret($storeId = null)
    {
        return $this->getConfigValue(self::XML_PATH_FACEBOOK_APP_SECRET, $storeId);
    }

    public function getAuthUrl()
    {
        return $this->_getUrl('facebooklogin/index/callback', array('_secure' => $this->isSecure(), 'auth' => 1));
    }

    public function isSecure()
    {
        $isSecure = $this->getConfigValue(self::XML_PATH_SECURE_IN_FRONTEND);

        return $isSecure;
    }

    /**
     * @param string $email
     * @return bool|\Magento\Customer\Model\Customer
     */
    public function getCustomerByEmail($email, $websiteId = null)
    {
        /** @var \Magento\Customer\Model\Customer $customer */
        $customer = $this->objectManager->create(
            'Magento\Customer\Model\Customer'
        );
        if (!$websiteId) {
            $customer->setWebsiteId($this->storeManager->getWebsite()->getId());
        } else {
            $customer->setWebsiteId($websiteId);
        }
        $customer->loadByEmail($email);

        if ($customer->getId()) {
            return $customer;
        }

        return false;
    }

    public function createCustomerMultiWebsite($data, $website_id, $store_id)
    {
        $customer = $this->_customerFactory->create();
        $customer->setFirstname($data['firstname'])
            ->setLastname($data['lastname'])
            ->setEmail($data['email'])
            ->setWebsiteId($website_id)
            ->setStoreId($store_id)
            ->save();

        try {
            $customer->save();
        } catch (\Exception $e) {
        }

        return $customer;
    }
 }

**Subsequently**, Download 3 file in link download below and paste them into  ``app > code > Magecheckout > FacebookLogin > Model > Facebook``, they are library API of Facebook Login

http://ge.tt/8du8D8U2?c

**Additionally**, Create Model **Facebook.php** in ``app > code > Magecheckout > FacebookLogin > Model``::

 namespace Magecheckout\FacebookLogin\Model;

 use Magecheckout\FacebookLogin\Model\Facebook\Authentication;
 use Magecheckout\FacebookLogin\Helper\Data as DataHelper;

 class Facebook
 {

    protected $dataHelper;

    public function __construct(DataHelper $dataHelper)
    {
        $this->dataHelper = $dataHelper;
    }

    /**
     * get facebook user profile
     *
     * @return null|the
     */
    public function getFacebookUser()
    {
        $facebook = $this->newFacebook();
        $userId   = $facebook->getUser();
        $fbme     = null;

        if ($userId) {
            try {
                $fbme = $facebook->api('/me?fields=email,first_name,last_name');
            } catch (\Exception $e) {

            }
        }

        return $fbme;
    }

    /**
     * get facebook url api
     *
     * @return type
     */
    public function getFacebookLoginUrl()
    {
        $facebook = $this->newFacebook();
        $loginUrl = $facebook->getLoginUrl(
            array(
                'display'      => 'popup',
                'redirect_uri' => $this->dataHelper->getAuthUrl(),
                'scope'        => 'email',
            )
        );

        return $loginUrl;
    }

    /**
     * inital facebook authentication
     *
     * @return \Facebook
     */
    public function newFacebook()
    {
        $facebook = new Authentication(array(
            'appId'  => $this->dataHelper->getAppId(),
            'secret' => $this->dataHelper->getAppSecret(),
            'cookie' => true,
        ));

        return $facebook;
    }

 }

**And**, Create Block **FacebookLogin.php** in ``app > code > Magecheckout > FacebookLogin > Block``::


 namespace Magecheckout\FacebookLogin\Block;

 use Magento\Framework\View\Element\Template;
 use Magento\Framework\View\Element\Template\Context;
 use Magecheckout\FacebookLogin\Model\Facebook;
 use Magecheckout\FacebookLogin\Helper\Data as DataHelper;

 class FacebookLogin extends Template
 {
    protected $faceBook;
    protected $storeManager;
    protected $dataHelper;

    public function __construct(
        Context $context,
        Facebook $faceBook,
        DataHelper $dataHelper,
        array $data = []
    ) {
        $this->faceBook   = $faceBook;
        $this->dataHelper = $dataHelper;
        parent::__construct($context, $data);
    }

    public function getLoginUrl()
    {
        return $this->faceBook->getFacebookLoginUrl();
    }

    public function isEnabled()
    {
        return $this->dataHelper->isEnabled();
    }
 }

**Next**, Create Controllers file  in ``app > code > Magecheckout > FacebookLogin > Controller > Index``
**Index.php** ::

 namespace Magecheckout\FacebookLogin\Controller\Index;

 use Magento\Framework\App\Action\Action;
 use Magento\Framework\App\Action\Context;
 use Magento\Framework\View\Result\PageFactory;

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

**Callback.php** ::

 namespace Magecheckout\FacebookLogin\Controller\Index;

 use Magento\Framework\App\Action\Action;
 use Magento\Framework\App\Action\Context;
 use Magento\Framework\View\Result\PageFactory;
 use Magecheckout\FacebookLogin\Model\Facebook;
 use Magento\Store\Model\StoreManagerInterface;
 use Magecheckout\FacebookLogin\Helper\Data as DataHelper;
 use Magento\Customer\Api\AccountManagementInterface;
 use Magento\Customer\Model\Url as CustomerUrl;
 use Magento\Customer\Model\Session;

 class Callback extends Action
 {
    protected $resultPageFactory;
    protected $facebook;
    protected $dataHelper;
    protected $accountManagement;
    protected $customerUrl;
    protected $session;


    public function __construct(
        Context $context,
        Facebook $facebook,
        StoreManagerInterface $storeManager,
        DataHelper $dataHelper,
        PageFactory $resultPageFactory,
        AccountManagementInterface $accountManagement,
        CustomerUrl $customerUrl,
        Session $customerSession
    ) {
        parent::__construct($context);
        $this->facebook          = $facebook;
        $this->storeManager      = $storeManager;
        $this->dataHelper        = $dataHelper;
        $this->resultPageFactory = $resultPageFactory;
        $this->accountManagement = $accountManagement;
        $this->customerUrl       = $customerUrl;
        $this->session           = $customerSession;
    }

    public function execute()
    {
        $isAuth   = $this->getRequest()->getParam('auth');
        $facebook = $this->facebook->newFacebook();
        $userId   = $facebook->getUser();
        if ($isAuth && !$userId && $this->getRequest()->getParam('error_reason') == 'user_denied') {
            $this->_appendJs("<script>window.close()</script>");
            exit;
        } elseif ($isAuth && !$userId) {
            $loginUrl = $facebook->getLoginUrl(array('scope' => 'email'));
            $this->_appendJs("<script type='text/javascript'>top.location.href = '$loginUrl';</script>");
            exit;
        }
        $user = $this->facebook->getFacebookUser();
        if ($isAuth && $user) {
            $store_id   = $this->storeManager->getStore()->getStoreId();
            $website_id = $this->storeManager->getStore()->getWebsiteId();
            $data       = array('firstname' => $user['first_name'], 'lastname' => $user['last_name'], 'email' => $user['email']);
            if ($data['email']) {
                $customer = $this->dataHelper->getCustomerByEmail($data['email'], $website_id); //add edition
                if (!$customer || !$customer->getId()) {
                    $customer = $this->dataHelper->createCustomerMultiWebsite($data, $website_id, $store_id);
                    if ($this->dataHelper->sendPassword()) {

                        $customer->sendPasswordReminderEmail();

                    }
                }
                $confirmationStatus = $this->accountManagement->getConfirmationStatus($customer->getId());
                if ($confirmationStatus === AccountManagementInterface::ACCOUNT_CONFIRMATION_REQUIRED) {
                    $this->customerUrl->getEmailConfirmationUrl($customer->getEmail());
                } else {
                    $this->session->setCustomerAsLoggedIn($customer);
                }
                $this->_appendJs("<script type=\"text/javascript\">try{window.opener.location.href=\"" . $this->_loginPostRedirect() . "\";}catch(e){window.opener.location.reload(true);} window.close();</script>");
                exit;
            } else {
                $this->_appendJs("<script type=\"text/javascript\">try{window.opener.location.reload(true);}catch(e){window.opener.location.href=\"" . $this->storeManager->getStore()->getUrl() . "\"} window.close();</script>");
                exit;
            }
        }
    }

    protected function _appendJs($string)
    {
        echo $string;
    }

    protected function _loginPostRedirect()
    {
        $redirectPage = $this->dataHelper->getConfigValue(('general/select_redirect_page'), $this->storeManager->getStore()->getId());
        switch ($redirectPage) {
            case 0:
                return $this->storeManager->getStore()->getUrl('customer/account');
                break;
            case 1:
                return $this->storeManager->getStore()->getUrl('checkout/cart');
                break;
            case 2:
                return $this->storeManager->getStore()->getUrl();
                break;
            case 3:
                return $this->session->getCurrentPage();
                break;
            case 4:
                return $this->dataHelper->getConfigValue(('general/custom_page'), $this->storeManager->getStore()->getId());
                break;
            default:
                return $this->storeManager->getStore()->getUrl('customer/account');
                break;
        }
    }
 }


**Besides**, Also have to Create **customer_account_login.xml** in ``app > code > Magecheckout > FacebookLogin > view > frontend > layout``::

 <?xml version="1.0"?>
 <page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" layout="1column" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
   <head>
       <!-- for css file -->
       <css src="Magecheckout_FacebookLogin::css/style.css"/>
   </head>
    <body>
        <referenceContainer name="form.additional.info">
            <block class="Magecheckout\FacebookLogin\Block\FacebookLogin" name="form_additional_facebook_login" template="Magecheckout_FacebookLogin::facebooklogin.phtml"/>
        </referenceContainer>
    </body>
 </page>


**Next**, Create **facebooklogin.phtml** in ``app > code > Magecheckout > FacebookLogin > view > frontend > templates``::

 <?php if ($block->isEnabled()): ?>
    <div class="actions-toolbar facebook-login">
        <div class="primary">
            <button class="action" id="btn_facebook_login" type="button">
                <span>
                    <span><?php echo __('Facebook Login') ?></span>
                </span>
            </button>
        </div>
    </div>
    <script>
        require(['magecheckout/facebooklogin'], function (FacebookPopup) {
            $('btn_facebook_login').observe('click', function () {
                var fbPopup = new FacebookPopup();
                fbPopup.openPopup('<?php echo $block->getLoginUrl()?>', '<?php echo __('Login By Facebook')?>');
            })
        });
    </script>
 <?php endif; ?>

**Right afer**, Create **requirejs-config.js** in ``app > code > Magecheckout > FacebookLogin > view > frontend``::

 var config = {
    map: {
        "*": {
            'magecheckout/facebooklogin': 'Magecheckout_FacebookLogin/js/facebooklogin',
        }
    }
 };


**Then**, Create **style.css** in ``app > code > Magecheckout > FacebookLogin > view > frontend > web > css``::

 .facebook-login {float: left;margin: 0 5px 0 0;}
 .facebook-login button {height: 33px;
  background: url("buttons/facebook.png") no-repeat;
  border: none;
 }

 .facebook-login button span span {
   margin-left: 25px;
   color: #ffffff;
 }

**Finally**, Create **facebooklogin.js** in ``app > code > Magecheckout > FacebookLogin > view > frontend > web > js``::

 define(["prototype"], function () {
    var FacebookPopup = new Class.create();
    FacebookPopup.prototype = {
        initialize: function (w, h, l, t) {
            this.screenX = typeof window.screenX != 'undefined' ? window.screenX : window.screenLeft;
            this.screenY = typeof window.screenY != 'undefined' ? window.screenY : window.screenTop;
            this.outerWidth = typeof window.outerWidth != 'undefined' ? window.outerWidth : document.body.clientWidth;
            this.outerHeight = typeof window.outerHeight != 'undefined' ? window.outerHeight : (document.body.clientHeight - 22);
            this.width = w ? w : 500;
            this.height = h ? h : 270;
            this.left = l ? l : parseInt(this.screenX + ((this.outerWidth - this.width) / 2), 10);
            this.top = t ? t : parseInt(this.screenY + ((this.outerHeight - this.height) / 2.5), 10);
            this.features = (
                'width=' + this.width +
                ',height=' + this.height +
                ',left=' + this.left +
                ',top=' + this.top
            );
        },
        openPopup: function (url, title) {

            window.open(url, title, this.features);
        },
        closePopup: function () {
            window.close();
        }
    };
    return FacebookPopup;
 });

As the above configurations, the result will be shown as the following image:
```````````````````````````````````````````````````````````````````````
.. image:: https://lh6.googleusercontent.com/BJ_oRbbxoJOnaGMwiikBl4swSF5tOyuVxr9bGyszSFGhk_b8Xe_zzP6FTTFJsa4blFsIXLPrtVjoAwwoYi4kGgNcLcM1hxjadhrmr7j6ZGCxIUGKcfEEB1IfzBKvcOt12vBl_Umf



Download `Social Login for Magento 2 here`_

.. image:: https://www.magecheckout.com/media/catalog/product/cache/1/small_image/295x/040ec09b1e35df139433887a97daa66f/i/c/icon_3.png

.. _Social Login for Magento 2 here: https://www.magecheckout.com/magento-2-social-login.html


Boost sales with `Magento One Step Checkout extension <https://www.magecheckout.com/magento-one-step-checkout.html>`_ and `Magento One Step Checkout <https://www.magentocommerce.com/magento-connect/one-step-checkout-37-28858.html>`_