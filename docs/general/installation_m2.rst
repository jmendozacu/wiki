Installation Guide for Magento 2 Extensions
==========================================================

.. role:: step

.. role:: mail
	


:step:`Step 1:`

Copy code to magento 2 root folder .

:step:`Step 2:`

run php bin/magento setup:upgrade in ssh in folder root of magento 2. 

login to ssh 
	
cd <magento>/<root>/<folder> 
	
php bin/magento setup:upgrade

:step:`Step 3:`

deloy statis content. 

login to ssh
	
cd <magento>/<root>/<folder>
	
php bin/magento setup:static-content:deploy
	
:step:`Step 4:`

delete folder var

login to ssh 
 
cd <magento>/<root>/<folder> 
 
cd var
 
rm –Rf *
	
:step:`*Note`

After purchasing it, you should add our skype account at **support.bsscommerce** to contact us if you cannot install the extension by yourself. 
BSS Support Team will help you to install the **Magento** module and the installation fee will follow our 
`Terms and Condition <http://bsscommerce.com/terms-conditions>`_ in Installation Policy section. Further assistance is available via Email and Skype.
In case, you have followed all above steps but the extension doesn't work properly, you can delete the file or change the module's filename extension 
to keep your website function as normal. Then please contact us at :mail:`support@bsscommerce.com` or Skype: support.bsscommerce. Our supporters will assist you 
in resolving any issues within 24 hours.
You also can see the example about installation guide for `Store Locator <http://bsscommerce.com/magento-store-locator-extension.html>`_ exention's video below: 

.. raw:: html

   <iframe width="560" height="315" style="margin-left:calc(25% - 	100px); margin-bottom: 30px" src="https://www.youtube.com/embed/8mmGt24cU_0" frameborder="0" allowfullscreen></iframe>
   <style>
		.step{font-size:125%; font-weight: bold;}
		.mail{text-decoration: none; color: #3091d1;}
		p {text-align: justify;}
		a[class='reference external'] {font-weight:bold; text-decoration:underline;}
   </style>
   
Installation guides for Magento 2 extensions purchased from `Magento Marketplace <https://marketplace.magento.com/developer/Bsscommerce>`_ 