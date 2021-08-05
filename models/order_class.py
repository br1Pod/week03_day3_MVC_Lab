class Order:
    def __init__(self, id, customer, order_date, title, author, quantity):
        
        self.id = id
        self.customer = customer
        self.order_date = order_date
        self.title = title
        self.author = author
        self.quantity = quantity