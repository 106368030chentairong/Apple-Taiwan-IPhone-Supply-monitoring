import os
from lib.iphone_check import *
from lib.line_notify import *

def foramt_mag(response,msg):
    msg = "\n"
    for stores in response:
        msg += "{} :\n".format(stores[0])
        for product in stores[1]:
            msg += "{} \n".format(product[0])
    return msg

def get_order():
    check_list = list(str(os.environ.get("check_list")))
    msg = ""
    for partNumber in check_list:
        print(partNumber)
        #product_number_list = iphone_check_api().get_partNumber("iphone14")
        response = iphone_check_api().check_store_state(partNumber)
        msg += foramt_mag(response,msg)
    line_notify().send_msg(msg)

