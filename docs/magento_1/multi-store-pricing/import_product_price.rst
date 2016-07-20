Import Product Price Per Store View
====================================

**Step 1: Export file**

	* Go to System -> Import/ Export -> Export 
	
	* In Entity Type, choose Product
	
	* Skip unnecessary attributes. If you just want to make change to price attribute, you can skip all entity attributes except SKU, _store, price, special price
	
	.. image:: images/product_price.jpg

	* Click Continue at the right bottom corner of the table to download a CSV file to your computer. 

**Step 2: Set up price for store view**

	* Open the CSV file
	
	* Find SKU of the product you want to set up price for store view
	
	* In the _store column equivalent to each SKU, replace the current store code by code of store view or add a new row to add new code of store view (Check code of store views at System -> Manage Store)  
	
	* Fill in equivalent price and special price for in price and special_price column as you want 
	
	.. image:: images/product_price1.jpg

	* Save file 
	
**Step 3: Import file**

	* Go to System -> Import/ Export -> Import
	
	* In Entity Type, choose Product
	
	* In Import Behavior, choose Append Complex Data
	
	* Upload the CSV file that you have made changes in step 2

	.. image:: images/product_price2.jpg