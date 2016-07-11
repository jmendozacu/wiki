{quote}public function addAction()
    {
		header("Content-type: application/json");

        if($this->getRequest()->getParam('callback')) {
            $cart   = $this->_getCart();
            $ajaxData = array();
            $productInfo = array();
            $params = $this->getRequest()->getParams();

            try {
                if($this->getRequest()->getParam('configurable_grid_table') == 'Yes') {
                    $params = $this->getRequest()->getParams();
                    $config_super_attributes = $params['super_attribute_quickshop'];
                    $cart   = $this->_getCart();
                    $config_table_qty = $params['config_table_qty'];
                    $options = isset($params['options']) ? $params['options'] : null;
                    $qty_config = array();
                    foreach($config_table_qty as $sup_qty => $_super_qty) {
                        $qty_config[$sup_qty] =$_super_qty;
                        $required += $_super_qty;
                    }
                    if($required == 0) {
                      $this->_getSession()->addError($this->__('Cannot add the item to shopping cart.'));
                      $this->_goBack();
                      return;
                    }
                    $config_table_qty = $qty_config;
                    foreach($config_super_attributes as $sId => $config_attribute) {
                      if(isset($config_table_qty[$sId]) && $config_table_qty[$sId]!='' && $config_table_qty[$sId] > 0) {
                        $product= $this->_initProduct();
                        $related= $this->getRequest()->getParam('related_product');
                        if (!$product) {
                          $this->_goBack();
                          return;
                        }
                        if(isset($config_table_qty[$sId])) {
                          $params2 = array();
                          $params2['qty'] = $config_table_qty[$sId];
                          $params2['super_attribute'] = $config_attribute;
                          if($options != null) $params2['options'] = $options;
                          if($params2['qty'] > 0 && $params2['qty']!='') {
                            $cart->addProduct($product, $params2);
                            if (!empty($related)) {
                              $cart->addProductsByIds(explode(',', $related));
                            }
                          }
                        }
                      }
                    }
                } else {
                    if (isset($params['qty'])) {
                        $filter = new Zend_Filter_LocalizedToNormalized(
                            array('locale' => Mage::app()->getLocale()->getLocaleCode())
                        );

                        $params['qty'] = $filter->filter($params['qty']);
                    }

                    $product = $this->_initProduct();
                    if($params['type_product']==1) {
                        $productInfo['type_product'] = $product->getTypeId();
                        $this->getResponse()->setBody(Mage::helper('core')->jsonEncode($productInfo));
                        return ;

                    }

                    $related = $this->getRequest()->getParam('related_product');

                    /**
                     * Check product availability
                     */
                    if (!$product) {
                        	$ajaxData['status'] = 0;
                            $ajaxData['message'] = $this->__('Unable to find Product ID');
                    }

                    $cart->addProduct($product, $params);

                    if (!empty($related)) {
                        $cart->addProductsByIds(explode(',', $related));
                    }
                }

                $cart->save();
                $this->_getSession()->setCartWasUpdated(true);

                /**

                 * @todo remove wishlist observer processAddToCart

                 */

                Mage::dispatchEvent('checkout_cart_add_product_complete',

                    array('product' => $product, 'request' => $this->getRequest(), 'response' => $this->getResponse())

                );



                if (!$this->_getSession()->getNoCartRedirect(true)) {
                    if (!$cart->getQuote()->getHasError()){
                        $message = $this->__('%s was added to your shopping cart.', Mage::helper('core')->escapeHtml($product->getName()));
                       // $this->_getSession()->addSuccess($message);
                        $ajaxData['status'] = 1;
                        $this->loadLayout();
                        $sidebarCart = "";
                        $mini_cart = "";
                        $toplink = "";
						
                        if ($this->getLayout()->getBlock('cart_sidebar')) {
                            $sidebarCart = $this->getLayout()->getBlock('cart_sidebar')->toHtml();
                        }

                        if ($this->getLayout()->getBlock('cart_sidebar_mini')) {
                            $mini_cart = $this->getLayout()->getBlock('cart_sidebar_mini')->toHtml();
                        }

                        if ($this->getLayout()->getBlock('top.links')) {
                            $toplink = $this->getLayout()->getBlock('top.links')->toHtml();
                        }

                        $pimage = Mage::helper('catalog/image')->init($product, 'small_image')->resize(55);
                        $ajaxData['sidebar_cart'] = $sidebarCart;
                        $ajaxData['top_link'] = $toplink;
                        $ajaxData['mini_cart'] = $mini_cart;
                        //show or hide cofirmbox when add product to cart

                        if (Mage::getStoreConfig('ajaxcartsuper/ajaxcartsuper_config/show_confirm')) {
                            $ajaxData['product_info'] = Mage::helper('ajaxcartsuper/data')->productHtml($product->getName(), $product->getProductUrl(), $pimage);
                        }

                    }

                }
            } catch (Mage_Core_Exception $e) {
                $msg = "";
				
                if ($this->_getSession()->getUseNotice(true)) {
                    $msg = $e->getMessage();
                } else {
                    $messages = array_unique(explode("\n", $e->getMessage()));
                    foreach ($messages as $message) {
                        $msg .= $message . '<br/>';
                    }
                }

                $ajaxData['status'] = 0;
                $ajaxData['message'] = $msg;
                $ajaxData['type_product_ajax'] = 1;

            } catch (Exception $e) {
                $ajaxData['status'] = 0;
                $ajaxData['message'] = $this->__('Cannot add the this product to shopping cart.');
            }
           $this->getResponse()->setBody($this->getRequest()->getParam('callback').'('.Mage::helper('core')->jsonEncode($ajaxData).')');
           return;

        }  else {
            parent::addAction();
        }
    }{quote}
