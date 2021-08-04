from models.order_class import Order
from models.customers import *

order1 = Order("AA01",cust1, "04/08/21","IT","Steven King", 1)
order2 = Order("AA02", cust2, "03/08/21","Life of Pi", "Pi",2)
order3 = Order("AA03",cust3,"30/07/21","Zen","Buddha",15)

orders_list = [order1,order2,order3]
