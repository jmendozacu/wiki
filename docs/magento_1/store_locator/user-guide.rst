User Guide
=============

.. role:: bullet

.. role:: green

.. role:: italic

BSS Store Locator Overview
---------------------------

`Magento Store Locator <http://bsscommerce.com/magento-store-locator-extension.html>`_ is an effective extension that efficiently supports your customers to 
search for store locations in any eligible positions by using Google Map API. Equipped with various searching tools, this extension allows customers to find 
stores by nation, state, zip code, suburb, their current location or a specific address in n-km radius. Magento Store Locator is also designed to display the 
overview of stores so that customers can see and link to these stores right when they find out them. As for admins, Magento Store Locator allows them to operate it as they wish in the backend. By and large, this searching tool is an efficient extension that can surely motivate your trading in the way that it supports customers to find your stores without difficulty.

How BSS Store Locator works?
----------------------------

1. Instruction Manual
^^^^^^^^^^^^^^^^^^^^^

**1.1. Store Setting**

As an admin, you can set up your own store in the way that it can most effectively support your trading aim. To set up your store, go 
to **“Store Locator -> Store Setting”**

.. image:: images/wholesale_fast_order_m2_1_1.jpg

A screen will appear like as follow:

.. image:: images/wholesale_fast_order_m2_1_2.jpg

* In **“Enable for Filter”** box, you can choose more than one criterion by pressing **“Ctrl”** and click on criteria you want.

.. image:: images/wholesale_fast_order_m2_1_3.jpg

* In “template” box, there are two templates for the frontend. The admins can choose between template 1 and template 2 freely.

:bullet:`Template 1:  Art template`

.. image:: images/wholesale_fast_order_m2_1_4.jpg

:bullet:`Template 2: There are 2 types of interface: two-column & one-column`

	* Two-column interface 

	.. image:: images/wholesale_fast_order_m2_1_5.jpg
	
	* One-column interface: In case the first seven criteria of “Enable for filter” box are not chosen, the store will be automatically changed into one-column interface one 

	.. image:: images/wholesale_fast_order_m2_1_6.jpg
	
	Backend: choose **3 final criteria** ->	Frontend: **One-column Interface**
	
	.. image:: images/wholesale_fast_order_m2_1_7.jpg
	
		* Remember to save your setting by pressing **“Save Configuration”** button in the right top of the screen, and wait until the 
		green line :bullet:`“The configuration has been saved”` appears.
	
		.. image:: images/wholesale_fast_order_m2_1_8.jpg
		
		* To see the change in the frontend, **reload** the frontend.
		
**1.2. Store Management**

This mode enables you to:

* Add new stores 

* Reset stores 

* Export store’s database to csv file 

To use this function, go through **“Store Locator => Manage Stores”**

.. image:: images/wholesale_fast_order_m2_2_1.jpg


* Add A New Store:

There are two ways to add stores: add a new store manually or import stores using csv file when you want to add stores in mass.

To add stores manually, please go to Store Locator – Manage stores

.. image:: images/wholesale_fast_order_m2_2_2.jpg

then Choose Add New Store button

.. image:: images/wholesale_fast_order_m2_2_3.jpg

Then, fill in required fields such as Business, Country, State, Postcode, Suburb and Address

**NOTE:** :italic:`If admin does not provide longitude and latitude, BSS Store Locator will automatically search store locations by Google map based on 
address. Thus, remember to check this carefully as Google may misunderstand your address.`

**1.3. Export and Import:**

:italic:`1.3.1. Export:` **BSS Store Locator** allows admins to export database from store to csv file or XML file.

* To export database to csv file, go through **“Store Locator -> Manage Store. In “Export to”** box, choose **“csv file -> Export”.** 

.. image:: images/wholesale_fast_order_m2_3_1.jpg

* After exporting, a csv file will be created and you can save it on your computer. When the file is opened, it appear like this: 

.. image:: images/wholesale_fast_order_m2_3_2.jpg

	:italic:`Example of Exporting Database To csv File`

:italic:`1.3.2. Import:`

* Firstly, **export** to see the file structure 

* Secondly, **add database** into appropriate cells on file exported. 

* Import into the system by going through: **“Store Locator -> Import/Export -> Import** 

You can choose freely overwriting existing files or not -> select file from your computer, then, press “Import”.

.. image:: images/wholesale_fast_order_m2_3_3.jpg

Unless you input co-ordinates, the system will automatically search through Google Map. However, if customers use the system too many 
times **on a daily basis**, the system may be **locked for one day.** Unless you input longitude and latitude of your stores, the system should be 
use **less than 100 times per day.**

2. Algorithms for finding stores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once users choose input cells, the system will work out all the results that perfectly match the information users wish to filter (country, state, city, postcode, or suburb).

* If no stores in the target location can be found, the BSS Store Locator will automatically find information about the location in Google Maps and work 
out **n nearest stores**(in case the system can find the store in Google Maps. If not, **“0 Store Found”** will be displayed). 

* If customers use module “Use My Location”, the system will find **n nearest stores** in the vicinity of their location. 

* If users **input the radius**, the system will automatically search for locations of store within the provided radius (via filter or location). 

**NOTE:** :italic:`n is the number of results to be shown in the frontend set by admins in the Store setting.`


.. raw:: html

   <style>
		p {text-align: justify;}
		.italic {font-weight:bold; font-style:italic;}
		.bullet:before {content:"\u2217"; margin-left: 5px;}
		.green {color: #00cc00}
   </style>

