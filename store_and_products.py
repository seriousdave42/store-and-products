from modules import store
from modules import product


if __name__ == "__main__":
    chicago = store.Store("chicago")
    banana = product.Product("banana", 10.00, "fruit")
    switch = product.Product("switch", 200.00, "gaming console")
    combos = product.Product("combos", 1.50, "snacks")
    ps4 = product.Product("ps4", 400, "gaming console")
    chicago.add_product(switch).add_product(banana).add_product(combos).add_product(ps4)
    for product in chicago.products:
        print(product.name, product.price, product.category, product.id)
    chicago.inflation(10)
    banana.update_price(20)
    for product in chicago.products:
        print(product.name, product.price, product.category, product.id)
    chicago.sell_product(1)
    for product in chicago.products:
        print(product.name, product.price, product.category, product.id)
    chicago.set_clearance("gaming console", 50)
    for product in chicago.products:
        print(product.name, product.price, product.category, product.id)
    