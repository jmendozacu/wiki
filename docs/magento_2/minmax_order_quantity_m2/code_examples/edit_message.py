--message Min Qty
if(!empty($_qty['min_qty'])) {
     	.................
     		$message = "The min quantity allowed for purchase at category ".$cate_name." is
				".$qtylimit.' [ Product Name : '.$product_name.' ]';
     	.................
}
--message Max Qty
if(!empty($_qty['max_qty'])) {
     	.................
     		$message = "The max quantity allowed for purchase at category ".$cate_name." is 
				".$qtylimit.' [ Product Name : '.$product_name.' ]';
     	.................
}
