How to add a new checkout step in Magento 2
============================================

Checkout is one of the most important part of online business. To collect more customer information or customize user interface you have to modity the checkout process. In this guide, we will show you **how to add a new checkout step**

Overview
--------

By default there are two main steps:

- Shipping Information
- Review and Paymetns Information

You can add a new custom checkout step. For further upgradability, compatibily you SHOULD not edit code in Magento core folder. In this guide, we will tell you how to do that easily.

Getting started: Adding new checkout step
--------------------------------------------------------------------------------------------------------------------------

To create the view part of the new checkout step:

    Before you getting started, you should read this guide :doc:`how-to-create-magento-2-module` . All custom files must be stored there.
    Create the ``.js`` file implementing the view model.
    Create an ``.html`` template for the component.

Adding javascript file in new step
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creating a new javascript file call ``new-step-view.js`` in ``view`` folder. The file must be saved in `my_module/view` folder. So the full path should be ``my_module/view/new-step-view.js``


**new-step-view.js** content::
	
	define(
	    [
	        'ko',
	        'uiComponent',
	        'underscore',
	        'Magento_Checkout/js/model/step-navigator'
	    ],
	    function (
	        ko,
	        Component,
	        _,
	        stepNavigator
	    ) {
	        'use strict';
	        /**
	        *
	        * mystep - is the name of the component's .html template, 
	        * my_module - is the name of the your module directory.
	        * 
	        */
	        return Component.extend({
	            defaults: {
	                template: 'my_module/mystep'
	            },
	 
	            //add here your logic to display step,
	            isVisible: ko.observable(true),
	 
	            /**
				*
				* @returns {*}
				*/
	            initialize: function () {
	                this._super();
	                // register your step
	                stepNavigator.registerStep(
	                    //step code will be used as step content id in the component template
	                    'step_code',
	                    //step alias
	                    null,
	                    //step title value
	                    'Step Title',
	                    //observable property with logic when display step or hide step
	                    this.isVisible,
	                     
	                    _.bind(this.navigate, this),
	 
	                    /**
						* sort order value
						* 'sort order value' < 10: step displays before shipping step;
						* 10 < 'sort order value' < 20 : step displays between shipping and payment step
						* 'sort order value' > 20 : step displays after payment step
						*/
	                    15
	                );
	 
	                return this;
	            },
	 
	            /**
				* The navigate() method is responsible for navigation between checkout step
				* during checkout. You can add custom logic, for example some conditions
				* for switching to your custom step 
				*/
	            navigate: function () {
	 
	            },
	 
	            /**
				* @returns void
				*/
	            navigateToNextStep: function () {
	                stepNavigator.next();
	            }
	        });
	    }
	);


Add the ``.html`` template
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the module directory, add the ``.html`` template for the component. It must be located under the ``<my_module>/view/frontend/web/template`` directory.

A sample ``mystep.html`` follows::

	<!--The 'step_code' value from the .js file should be used-->
	<li id="step_code" data-bind="fadeVisible: isVisible">
	<div class="step-title" data-bind="i18n: 'Step Title'" data-role="title"></div>
	    <div id="checkout-step-title"
	         class="step-content"
	         data-role="content">
	 
	        <form data-bind="submit: navigateToNextStep" novalidate="novalidate">
	            <div class="actions-toolbar">
	                <div class="primary">
	                    <button data-role="opc-continue" type="submit" class="button action continue primary">
	                        <span><!-- ko i18n: 'Next'--><!-- /ko --></span>
	                    </button>
	                </div>
	            </div>
	        </form>
	    </div>
	</li>


Update checkout layout
^^^^^^^^^^^^^^^^^^^^^^^^

For the new step to be displayed on the page, you need to declare it in the Checkout page layout, which is defined in ``checkout_index_index.xml``.

So you need to add an extending ``checkout_index_index.xml`` layout file in the following location: ``<my_module>/view/frontend/layout/checkout_index_index.xml``

A sample ``checkout_index_index.xml`` follows::

	<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" layout="1column" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
	    <body>
	        <referenceBlock name="checkout.root">
	                <arguments>
	                    <argument name="jsLayout" xsi:type="array">
	                        <item name="components" xsi:type="array">
	                            <item name="checkout" xsi:type="array">
	                                <item name="children" xsi:type="array">
	                                    <item name="steps" xsi:type="array">
	                                        <item name="children" xsi:type="array">
	                                            <item name="my-new-step" xsi:type="array">
	                                                <item name="component" xsi:type="string">Magento_Your_Module_Name/js/view/my-step-view</item>
	                                                    <!--To display step content before shipping step "sortOrder" value should be < 1-->
	                                                    <!--To display step content between shipping step and payment step  1 < "sortOrder" < 2 -->
	                                                    <!--To display step content after payment step "sortOrder" > 2 -->
	                                                <item name="sortOrder" xsi:type="string">2</item>
	                                                <item name="children" xsi:type="array">
	                                                    <!--add here child component declaration for your step-->
	                                                </item>
	                                            </item>
	                                        </item>
	                                    </item>
	                                </item>
	                            </item>
	                        </item>
	                    </argument>
	                </arguments>
	        </referenceBlock>
	    </body>
	</page>






Boost sales with `Magento One Step Checkout extension <https://www.magecheckout.com/magento-one-step-checkout.html>`_ and `Magento One Step Checkout <https://www.magentocommerce.com/magento-connect/one-step-checkout-37-28858.html>`_