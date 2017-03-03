Translation Guide for Magento 2 Extensions
===========================================


Guidance to translate text in Magento 2 extensions
--------------------------------------------------

To translate text in a custom module, you can use a language translation csv file.  

**Step 1: You access the app/code/Bss/name_of_the_module/i18n/en_US.csv folder**

	* **i18n:** This is the language folder. Remember that each site will have different language folders depending on what languages are available on the site. The other site, for examples, uses Japanese, then its language folder will be ja_JP. The module already contains US language folder.
	
	* Create a csv file in the **app/code/Bss/name_of_the_module/i18n/** folder. For example: You create a file called **app/code/Bss/extensionname/i18n/fr_FR.csv**
	
**Step 2: You open the fr_FR.csv file**

In this file, you will see all text of the module displayed in 2 columns like below:

.. image:: images/translation1.jpg

(This is an example when opening the Bss_FastOrder.csv file of Magento Wholesale Fast Order extension by BSS)

All you need to do is adding the translation in the right column corresponding to the content in left column