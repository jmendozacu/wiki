How to Delete Multiple Store View Pricing extension
====================================================

**Step 1: Go to Admin -> System -> Configuration -> Catalog -> Catalog Price Scope**

You change Catalog Price Scope  to Website or Global 

**Step 2:**

Go to **Admin -> Catalog-> Attributes -> Manage Attributes**
 
You need to delete 2 attributes with attribute code as "tier_price_for_store" and  "group_price_for_store"

**Step 3:**

Setup base currency again by navigating to **Admin -> System -> Configuration -> Currency Setup -> Base Currency**

**Step 4: Delete product prices at each store view**

You upload the **delete_price_store.php** file to Magento root folder and run it. It is noticeable that you had better backup 
the **catalog_product_entity_decimal** table in DB before running. 

This is the script of the **delete_price_store.php** file:

.. literalinclude:: code_examples/delete_multiple_store_view_pricing.py

**Step 5: Remove the code of the module**

You delete the folder: **app/code/local/Bss/MultiStoreViewPricing** and 

also remove the file: **app/etc/modules/Bss_MultiStoreViewPricing.xml**

**Step 6: Finally, you should clear all caches**


.. raw:: html

   <style>
		p {text-align: justify;}
   </style>
