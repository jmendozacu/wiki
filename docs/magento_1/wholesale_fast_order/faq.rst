FAQs
=====
.. role:: red

:red:`General`
--------------

**Is this extension compatible with Magento rwd theme?**

Yes, it is compatible with rwd theme of Magento

**How can I get user guide of Wholesale Fast Order?**

You can get user guide in the PDF file right on the product page of `Wholesale Fast Order <http://bsscommerce.com/magento-wholesale-fast-order.html>`_ or user guide in 
this `wiki <http://wiki.bsscommerce.com/en/latest>`_

**Do you provide free support and free installation for Wholesale Fast Order?** 

Yes, we will install and support you for free. When you request for installation, we will contact you for your credential information (admin information, 
FTP account). However, free installation offer for Wholesale Fast Order is just valid for 3 weeks since the purchase date, so after this period, you will pay 
an extra fee ($40) for installation request.

**How can I install this module by myself?** 

You can follow Installation guide and carry out as instructed to install on your own. 



:red:`Features`
-----------------

**What types of products does your Magento extension support?**

Magento Wholesale Fast Order extension by BSSCommerce can be applied to not only simple products but also configurable products with custom options and virtual products.

**Can I apply Magento Wholesale Fast Order for some certain customer groups?**

Yes, you can. You configure it in "Enable for customer group" in the Magento admin panel and you select groups as your wish.


**I want to hide some products from retailer group but they still appear on Magento Wholesale Product list. Can the extension do this? And how?**

Yes. The extension supports the feature. You can hide some products from particular customer group. To do this, click "Add" button on "Hide products with 
customer group" and complete information there.

**Do I need to complete the product names when searching them?**

No, you don't. The only thing you need to do is typing the configured number of initial letters configured from the backend of product names or SKUs, 
the AJAX search equipped shall automatically find the product as your needs.

For example, when you set "2" on "Autocomplete minimum characters" on the backend, AJAX search will find the product when your customers type 2 initial 
letters of the product name or SKU on the frontend.

**Can I search products by category, price or by description?**

No, you cannot. Our extension allows you to search products by name and SKU.

**Can I enable Jquery Library in your extension?**

Yes, it supports you to enable Jquery Library.




:red:`Guide` 
-------------

**I want Magento Fast Order to display as a page instead of Popup. What should I do?**

You may go to the Magento backend, create a "Fast Order" page on CMS page. Then, complete page information including page information, content, design and meta 
data. It is important for inserting the code string: "" on "Content" bar of the page and complete page layout and custom design 
on "Design" bar. Afterward, click "Save and Continue Edit".

The next step, please go to Configuration. On Fast Order Display choose CMS Page and save. After that, go to frontend and scroll down the page, you can 
click "QUICK ORDER" shortcut in your Magento site footer and see the result.


**How are the configurable products set on Magento Wholesale Fast Order popup?**

When a configurable product is searched and chosen, the popup showing different variants of the products with different attributes will appear.

**I do not want Fast Order to be shown in Shopping Cart, what should I do?**

You just configure the setting from backend

Go through System-> Configuration-> BSSCommerce-> Fast Order

In Number of lines (Shopping cart), you set it to 0 or leave it blank and Fast Order Function will disappear in your shopping cart page.


**I do not want Magento Fast Order Popup shortcut to be displayed in Homepage, what should I do?**

Please go to the backend, you can set 0 or leave it blank on "Number of lines (Popup)" to make Fast Order shortcut disappear from Magento Homepage.

**I have a list of products that I want to buy, how can I use Fast Order to buy all listed products without typing each name or SKU one by one?**

Magento Wholesale Fast Order Extension supports importing a CSV file containing product SKU and quantity for a faster buying process. With this function, there 
is no need for you to insert product information one by one, which save time.

You only need to save your list into a CSV file and upload this file in the Fast order pop up and then all listed products are processed. Remember that 
products' SKU and quantity are required in the CSV file.

**How to manage the number of results shown in Fast Order popup?**

In "Max results to show" from the Magento admin, you choose the number of results shown.

:red:`Common Problems` 
----------------------

Having problems with Currency Decimal separator?

In some countries Currency separator is "," while "." is used in US or UK. To fix problem when installing Wholesale Fast Order on the store using 
Decimal separator as "," please follow below changes:

Edit file: /skin/frontend/base/default/js/bss/fastorder.js

Change: 

      finalprice   = Number(finalprice.replace(/[^0-9\.]+/g,""));
	  
Into

      finalprice   = Number(finalprice.replace(",","."));


Change:

     function convertPrice(price) {
	 
              price = parseFloat(price).toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, "$1,");
			  
              return price;
     }
	 
Into:

     function convertPrice(price) {
	 
              price = parseFloat(price).toFixed(2);
			  
              price = price.replace(".",",");
			  
              price = price.replace(/(\d)(?=(\d{3})+\,)/g, "$1.")
			  
              return price;
     }



.. raw:: html

	<style>
		.red {color:red;}
		p {text-align: justify;}
	</style>