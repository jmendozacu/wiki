How to install Magento 2 via Command Line
====================================

#. Download latest version at : https://www.magentocommerce.com/download
#. After download, you can upload to your server then extract it into xampp/htdocs/magento20
#. Open phpmyadmin and create database with name ‘magento20’
#. Move to folder xampp/htdocs/magento20/bin
#. Hold Shift key then right click to folder: 
    .. image:: https://lh6.googleusercontent.com/rrDgn4RLSHJiWh6G2Cs4Aiz-3I0IzF_ScP2CIxDpVWRyzt9prrHSnVt8jDpRrH5_AxXOWB_XpuRlF-XiCjN72Hux0Kut4PJNykwmEVTo7ZD7EFCFxbXMkAXdjORQtzE4002uZGP4
#. Run this command line 
 
   ``php magento setup:install --base-url=http://localhost.com/magento20/ --db-host=localhost --db-name=magento20 --db-user=root --admin-firstname=Magento --admin-lastname=User --admin-email=user@example.com --admin-user=admin --admin-password=admin123 --language=en_US --currency=USD --timezone=America/Chicago --use-rewrites=1``
#. Final, run this command line to create static content:

   ``php magento setup:static-content:deploy``
	
   .. image:: https://lh3.googleusercontent.com/RK2bvU8vJVIumkpNTe6A3aFzTFj63uzbYY6fSgmZe9ZbYqnS0MatgecSMrmuNILoYaJFU6O56EEUN-jOpJXZADWtTDA6j-AYViV4grsTUx7r2bwyNPgMjPvlPHuAlP9-zgjMIHgG

**Home Page**

.. image:: https://lh3.googleusercontent.com/6pwTq2N_iOKv6HeiWs94tBy4BQxbrc-wZrkLxhql77PRH3TUS5uBhWcBODTc89WMh_9XBrt39DZ2SFb8XAg6EQGwGhjnklL-zHtfTnugM_IkfDxh_UqdT4D8dr7TvgRWxHMXJRbV

**Products Page**

.. image:: https://lh4.googleusercontent.com/WhWtHH6Cc1MiQEvWSvO9s4nxKI3RbX8YYfGXK9MEkMxOib3PNDVxKYEQ2dhBCC-8pYG1fwRkgCX-nxNFa77g6xzDDqcMA4cUAS9dpKRnXUYCDVIFNB_dYBiD-y3sDZ-R9FKzwOnh

**Admin**

.. image:: https://lh5.googleusercontent.com/r57srF9DPVLPEbUF5Hni91vQ5uNUJ8-LI7x0KQwO5nWkSKu7DvVip19zagk39nt0utd6PEtjtvLP_eVhM97QyR2uehM3Dr9DqrK1Dal-W3hb4igSJc6ikG9YDNG7SSK1lqCnShRS



Boost sales with `Magento One Step Checkout extension <https://www.magecheckout.com/magento-one-step-checkout.html>`_ and `Magento One Step Checkout <https://www.magentocommerce.com/magento-connect/one-step-checkout-37-28858.html>`_