Uninstallation
==============


Disable Extension
-------------------------------------

To completely uninstall any extension, first start from disabling it. 
*To disable the extension, please follow the next steps*

- Edit ``app/etc/modules/Magecheckout_EXTENSION_NAME.xml``
- Change ``true`` to ``false``
- Clear the cache

At this point the extension is completely disabled and is not visible for Magento.

Now you can safely remove the extension files, although it is not necessary.



Uninstall an extension completely
--------------------------------------------------------------------------------------------------

Delete the following files, folders::

	app/etc/modules/Magecheckout_EXTENSION_NAME.xml
	app/code/local/Magecheckout/EXTENSION_NAME
	app/design/adminhtml/default/default/layout/magecheckout/EXTENSION_NAME.xml
	app/design/adminhtml/default/default/template/magecheckout/EXTENSION_NAME
	app/design/frontend/base/default/layout/magecheckout
	app/design/frontend/base/default/template/magecheckout/EXTENSION_NAME
	js/magecheckout/EXTENSION_NAME
	skin/frontend/base/default/css/magecheckout/EXTENSION_NAME
	skin/frontend/base/default/js/magecheckout/EXTENSION_NAME


