class Order:
    def __init__(self,id, cust_name,order_date,book_name,book_author,quantity):
        
        self.id = id
        self.cust_name = cust_name
        self.order_date = order_date
        self.book_name = book_name
        self.book_author = book_author
        self.quantity = quantity