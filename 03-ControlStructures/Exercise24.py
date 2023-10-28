Current_product_price = 140.00
Previous_product_price = 200.00
if Current_product_price/Previous_product_price < 0.9:
    print("Buy the product!!\n","Product price reduced by",round((1-Current_product_price/Previous_product_price)*100),"%")