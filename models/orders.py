from models.order_class import Order
from models.customers import *

order1 = Order("AA01",cust1, "04/08/21","Expert Guitar Picking", "BB King", 1)
order2 = Order("AA02", cust2, "03/08/21","Piano Riffs", "JS Bach",2)
order3 = Order("AA03",cust3,"30/07/21","Learn to play Sitar","R. Shankar",15)
order4 = Order("AA04",cust4,"30/07/21","Begining Drums","Mr Cowbell",15)

orders_list = [order1, order2, order3, order4]
