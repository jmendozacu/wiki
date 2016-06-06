FAQs
====

.. role:: red

:red:`Features`
-----------------

**What is the difference between Configurable product grid table view and Pro configurable product grid table view?**

The differences are mainly concentrated on some advanced features of Pro configurable product grid table view compared with normal version: 

* Support tier prices: specific price for each range of quantity 

* Support Color Swatch 

* Support Simple product pricing


**What is Color Swatch function?**

Color swatch is the function that helps customers to show configurable products with different colors and designs when they click to each attribute 
such as color, fabric or size (attributes depend on your configurable products)

**What does color swatch function do?**
 
**What is the function of simple product pricing?**

Simple product pricing means that the module will display different prices and tier prices of simple products instead of configurable products in the table 
 
**Can I add multiple products to cart at once?**

Yes, of course. You absolutely add a lot of products to cart at one time just by choosing your desired quantities. 
 
*When using this pro configurable product grid table view, what kind of images does color swatch support?**

Color swatch 
 
**In what cases does color swatch display as a label or as a picture?**

* Color swatch displays as label with Magento version 1.4.x to 1.8.x

* Color swatch displays as picture with Magento version 1.9.x

 
**Can I show price ranges in the category page?**

Yes, you can. Price ranges of configurable products are displayed in the category page under both grid list and product list. 

**How is the price range of a configurable product shown in the category page determined?**

The price range of configurable product is determined by the lowest price (or tier prices) and the highest price (or tier prices) of children products  


:red:`Guide` 
-------------

**Can I enable Jquery Library in your extension?**

Yes, it supports you to enable Jquery Library.

**If I set Yes for Configurable products use simple price, what will I have to do next?**

When you use simple product pricing for your configurable products, you have to set up prices and tier prices for children product by going 
through **Catalog-> Manage Product** and choose each simple product to set up these prices in the Price section. 

**If I do not choose to use Simple product pricing, so what are the prices of children products displayed in the table and May I make any configuration 
in the Price section of children products?**

In case you do not want to use simple product pricing, prices of children products are prices of your configurable products. It means that these 
prices (or tier prices) of simple products are the same in the table. 

So you needn’t configure anything in the price section of each simple product other than set No for Configurable products use simple price 

**How to disable Color Swatch for my configurable products?**

You go through System->Configuration->Configurable Grid View 

In Use Option Swatch, you set No to disable this function 


.. raw:: html

	<style>
		.red {color:red;}
		p {text-align: justify;}
	</style>

