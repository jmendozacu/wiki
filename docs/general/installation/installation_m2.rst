Installation Guide for Magento 2 Extensions
==========================================================

.. role:: step

.. role:: mail
	


:step:`Step 1:`

Unzip the file

:step:`Step 2:`

Create another directory called app/code/Bss/MODULENAME/ where MODULENAME must be replaced by the modules internal identifier. You can find it in the "composer.json" file 
in the extension ZIP file you downloaded, look at the node "psr-4". 

For example, it could say "Bss\\AjaxCart\\" or "Bss\\OneStepCheckout\\" there, then the MODULENAME is the part after \\ and before \\, so in our examples AjaxCart" or "OneStepCheckout". This 
is what you call the directory, then, for example app/code/Bss/AjaxCart, and you put the contents of the extension ZIP file in there.

:step:`Step 3:`

Upload the directory app/code/Bss/MODULENAME/ into the root directory of your Magento installation. The root directory of Magento is the directory that contains the
directories "app", "bin", "lib" and more. All directories should match the existing directory structure.
	
:step:`Step 4:`

Go to Magento 2 root directory.

Run: php bin/magento setup:upgrade

:step:`Step 5:`

Run: php bin/magento setup:static-content:deploy

:step:`Step 6:`

Clear all Cache
	
:step:`*Note`

After purchasing it, you should add our skype account at **support.bsscommerce** to contact us if you cannot install the extension by yourself. 
BSS Support Team will help you to install the **Magento** module and the installation fee will follow our 
`Terms and Condition <http://bsscommerce.com/terms-conditions>`_ in Installation Policy section. Further assistance is available via Email and Skype.
In case, you have followed all above steps but the extension doesn't work properly, you can delete the file or change the module's filename extension 
to keep your website function as normal. Then please contact us at :mail:`support@bsscommerce.com` or Skype: support.bsscommerce. Our supporters will assist you 
in resolving any issues within 24 hours.

Installation guides for Magento 2 extensions purchased from `Magento Marketplace <https://marketplace.magento.com/developer/Bsscommerce>`_ 

You can also see an example about the installation guide of `Quick View for Magento 2 extension <http://bsscommerce.com/magento-2-quick-view.html>`_ in the following video:


.. raw:: html

   <iframe width="560" height="315" style="margin-left:calc(25% - 	100px); margin-bottom: 30px" src="https://www.youtube.com/embed/xLumGKcKYVQ" frameborder="0" allowfullscreen></iframe>
   <style>
		.step{font-size:125%; font-weight: bold;}
		.mail{text-decoration: none; color: #3091d1;}
		p {text-align: justify;}
		a[class='reference external'] {font-weight:bold; text-decoration:underline;}
   </style>
   
