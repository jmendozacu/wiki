     function convertPrice(price) {
              price = parseFloat(price).toFixed(2);
              price = price.replace(".",",");
              price = price.replace(/(\d)(?=(\d{3})+\,)/g, "$1.")
              return price;
     }
