$this->getSelect()->join(
		array('price_index' => $this->getTable('catalog/product_index_price')),
                $joinCond,
                array('price', 'tax_class_id', 'final_price', 'minimal_price' => $minimalExpr ,'min_price', 'max_price','tier_price')
            );
