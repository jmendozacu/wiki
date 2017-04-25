// If some stuff requires api authentification,
// then get a session token
$session = $client->login('api', 'api123');
$result = $client->catalogProductUpdate(
	$session,
	{product_sku}, 
	array(
    		'price' => {price}, 
	),
	{store}  
);
