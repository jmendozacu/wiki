public function indexAction()
    {
      $idProduct = Mage::app()->getRequest()->getParam('product_id');
      $idProduct = Mage::app()->getRequest()->getParam('product')? Mage::app()->getRequest()->getParam('product'): $idProduct;
      $IsProductView = Mage::app()->getRequest()->getParam('IsProductView');
      $params = Mage::app()->getRequest()->getParams();
      $related = $this->getRequest()->getParam('related_product');
      unset($params['product_id']);
      unset($params['IsProductView']);

      if($this->getRequest()->getParam('configurable_grid_table') == 'Yes') {
        $params = $this->getRequest()->getParams();
        $config_super_attributes = $params['super_attribute_quickshop'];
        $cart = Mage::getSingleton('checkout/cart');
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
          if(!isset($config_table_qty[$sId]) || $config_table_qty[$sId]=='' || !is_numeric($config_table_qty[$sId])){
            if($config_table_qty[$sId] != '0'){
              $config_table_qty[$sId] = 1;
            }
          }

          if(isset($config_table_qty[$sId]) && $config_table_qty[$sId]!='' && $config_table_qty[$sId] > 0) {
            $product= $this->_initProduct();
            $related= $this->getRequest()->getParam('related_product');

            if (!$product) {
              $this->_goBack();
              return;
            }

            if(isset($config_table_qty[$sId])) {
              $params = array();
              $params['qty'] = $config_table_qty[$sId];
              $params['super_attribute'] = $config_attribute;

              if($options != null) $params['options'] = $options;

              try {
                if($params['qty'] > 0 && $params['qty']!='') {
                  $cart->addProduct($product, $params);
                  if (!empty($related)) {
                        $cart->addProductsByIds(explode(',', $related));
                  }
                  $cart->save();
                  Mage::getSingleton('checkout/session')->setCartWasUpdated(true);
                  if (!$cart->getQuote()->getHasError()){
                      $responseText = $this->addToCartResponse($product, $cart, $IsProductView, $params,0);    
                  }    
                } else {
                  $responseText = $this->showOptionsResponse($product, $IsProductView);    
                }
              } catch (Exception $e) {
                  $responseText = $this->addToCartResponse($product, $cart, $IsProductView, $params, $e->getMessage());
                  Mage::logException($e);
              } 
            }
          }
        }
      } else {
  	    if($related) unset($params['related_product']);
          $product = Mage::getModel('catalog/product')
                     ->setStoreId(Mage::app()->getStore()->getId())
                     ->load($idProduct);
          $responseText = '';
          if ($product->getId())
          {
              if(!array_key_exists('qty', $params)) {
                  $params['qty'] = $product->getStockItem()->getMinSaleQty();
              }
              try{
                  if(($product->getTypeId() == 'simple' && !($product->getRequiredOptions() || (Mage::getStoreConfig('amcart/general/display_options') && $product->getHasOptions())))
                      || count($params) > 2
                      || ($product->getTypeId() == 'virtual' && !($product->getRequiredOptions() || (Mage::getStoreConfig('amcart/general/display_options') && $product->getHasOptions()))))
                  {
                      $cart = Mage::getSingleton('checkout/cart');
                      $cart->addProduct($product, $params);
  		            if (!empty($related)) {
                          $cart->addProductsByIds(explode(',', $related));
                      }
                      $cart->save();
                      Mage::getSingleton('checkout/session')->setCartWasUpdated(true);
                      if (!$cart->getQuote()->getHasError()){
                          $responseText = $this->addToCartResponse($product, $cart, $IsProductView, $params,0);    
                      }    
                  }
                  else{
                       $responseText = $this->showOptionsResponse($product, $IsProductView);    
                  }
                      
              }
              catch (Exception $e) {
                  $responseText = $this->addToCartResponse($product, $cart, $IsProductView, $params, $e->getMessage());
                  Mage::logException($e);
              }
          }
        }
        $this->getResponse()->setBody($responseText);
    }
