Translation Guide for Magento 1 Extensions
===========================================


Guidance to translate text in Magento 1 extensions
--------------------------------------------------

To translate text in a custom module, you can use a language translation csv file.  

**Step 1: You access the  app/locale/en_US/name_of_the_module.csv folder**

	* **name_of_the_module.csv** is the csv file of the module you want to translate 
	
	* **en_US:** This is the language folder. Remember that each site will have different language folders depending on what languages are available on the site. The other site, for examples, uses Japanese, then its language folder will be ja_JP. The module already contains US language folder. 
	
After identifying the language folder of the site, you copy the **name_of_the_module.csv** file and paste it into the language folder. 


**Step 2: You open the name_of_the_module.csv file**

In this file, you will see all text of the module displayed in 2 columns like below:

.. image:: images/translation1.jpg

(This is an example when opening the Bss_FastOrder.csv file of Magento Wholesale Fast Order extension by BSS)

All you need to do is adding the translation in the right column corresponding to the content in left column