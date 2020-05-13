class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self,id):
        del_index = -1
        for i in range(len(self.products)):
            if self.products[i].id == id:
                print(f"Product sold:\nName: {self.products[id].name}\nPrice: {self.products[id].price}\nCategory: {self.products[id].category}\n")
                del_index = i
        if del_index == -1:
            print(f"Product {id} not found")
        else:
            self.products.pop(del_index)
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.price = round(product.price * (1 + percent_increase/100), 2)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.price = round(product.price * (1-percent_discount/100), 2)
        return self

if __name__ == "__main__":
    chicago = Store("Chicago")
    print(chicago.name)
    print(chicago.products)