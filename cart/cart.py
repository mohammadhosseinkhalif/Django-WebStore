from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] = self.cart[product_id].get("quantity", 1) + 1
        else:
            self.cart[product_id] = {"price": str(product.price), "quantity": 1}
        self.session.modified = True
    def __len__(self):
        return len(self.cart)

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def clear(self):
        self.cart = dict()
        self.session.modified = True

    def chek_product(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            return False
        else:
            return True



