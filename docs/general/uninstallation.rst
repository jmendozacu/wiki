Uninstallation
==============

**How to uninstall magento 2 extension?**

Here's our steps to uninstall this module:

**Step 1**: Connect via SSH to your magneto installation and execute below commands:

php bin/magento module:disable <ExtensionProvider_ExtensionName> --clear-static-content
php bin/magento setup:upgrade

**Step 2**: Remove extension files

cd app/code/<ExtensionProvider>/
rm -rf <ExtensionName>

!Note: If you are using more extensions from the same provider make sure not to remove the shared extension, most providers use a shared extension or dependancy pack as a base for all their extensions.

