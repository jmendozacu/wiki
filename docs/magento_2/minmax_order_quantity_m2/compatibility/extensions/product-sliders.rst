Product Sliders
==================

In this guide, we will show you how to insert a specific products into Checkout page of `One Step Checkout extension <https://www.magecheckout.com/magento-one-step-checkout.html>`_
The product collection such as: product in category, featured products, new products, bestseller products, On sa_le products or random products from `Product slider extension <https://www.magentocommerce.com/magento-connect/product-sliders-new-featured-on-sale-most-view-best-seller-product.html>`_


Go to file::

	app/design/frontend/base/default/template/magecheckout/securedcheckout/checkout/form.phtml:61

	


Insert the following code into end of form.phtml file::

	$this->getLayout()->createBlock('productslider/productslider')->setTemplate('mageplaza/productslider/productslider.phtml')->setProductsliderId('1')->toHtml();




.. tip:: You should change Product Slider ID to your own ID in product slider list.

