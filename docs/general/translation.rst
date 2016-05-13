Translation
===========


How to transalte to my language?
-------------------------------------------------------------------------------------------


Translate inline
-----------------------------------

This is simple but effect solution for store own.

From Magento Admin Panel, go to ``System > Configuration > Developer``

You can see "Translate inline" section. Let's enable them in Frontend or Admin.

Then Save Config and flush cache by going to ``System > Cache Management > Flush Magento Cache``.

Now go to frontend and translate text into your language.

 

CSV file
---------

In this tutorial, I am going to translate an extension to French.

CSV file name: ``Magecheckout_EXTENSION_NAME.csv``

CSV File path: ``/app/locale/en_US/Magecheckout_EXTENSION_NAME.csv``

Copy ``/app/locale/en_US/Magecheckout_EXTENSION_NAME.csv`` into ``/app/locale/fr_FR/Magecheckout_EXTENSION_NAME.csv``

Open ``Magecheckout_EXTENSION_NAME.csv`` in French folder and edit them.

 

All strings should start and end with double quotes and should be separated with comma (,), not a semicolon or any other sign.


		"My Cart","Mon panier"



.. Available languages: https://www.magecheckout.com/csv_files/