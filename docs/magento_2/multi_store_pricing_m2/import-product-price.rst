Import Product Price Per Store View
====================================================

**Step 1: Get the SKU of product you want to import price**

* Go to Product -> Catalog -> Manage Products

* Then choose a product you want to import price -> copy its SKU


**Step 2: Get the export file**

* Go to **System -> Data Transfer -> Export**

* In **Entity Type**, choose **Products**

* Paste the SKU on SKU box

* Click **Continue**, then a CSV file will be exported

* Open the downloaded CSV file

* Skip unnecessary attributes and leave 3 important attributes: SKU, store_view_code, price

**Step 3: Get store view code and paste in CSV file**

* Get store view code:  **Store -> All stores -> choose a store view** to get its code

* Open the CSV file, in the **store_view_code** column equivalent to each SKU, replace the current store code by code of store view or add a new row to add 
new code of store view

* Fill in price in the **price** column as you want

* Save the CSV file

Step 4: Import the CSV file to site

* Go to **System -> Data Transfer -> Import**

* In **Import Settings**, choose **Products** for **Entity Type**

* In **Import Behavior**, choose **Add/Update**

* In **File to import**,  select a  CSV file to import

* Click **Check Data** and then click Import

There will be a note shown up: *File is valid! To start import process press "Import" button*

It is the end of import price process for multiple store views.

Now you will check again your product on each store view.

