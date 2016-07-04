     function convertPrice(price) {
              price = parseFloat(price).toFixed(2).replace(/(\d)(?=(\d{3})+\.)/g, "$1,");
              return price;
     }
