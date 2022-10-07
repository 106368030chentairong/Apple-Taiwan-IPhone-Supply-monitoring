import os
from lib.iphone_check import *
from lib.line_notify import *

product_number_list = 

print(product_number_list)

response = iphone_check_api().check_store_state("MQ9R3TA/A")
for stores in response:
    if stores[1] != []:
        print(stores)
    