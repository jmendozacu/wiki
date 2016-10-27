foreach ($data as $k => $v) {
    $data[$k]['website_price'] = $v['price'];
    if ($v['all_groups']) {
        $data[$k]['cust_group'] = Mage_Customer_Model_Group::CUST_GROUP_ALL;
    }
 }
