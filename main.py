import os
from lib.iphone_check import *
from lib.line_notify import *

def foramt_mag(response, msg, num):
    num += num
    msg = "\n"
    for stores in response:
        if len(stores[1]) > 0: 
            msg += "{} :\n".format(stores[0])
            for product in stores[1]:
                msg += "{} \n".format(product[0])
                num += 1
        else:
            msg = ""
    return msg, num

def get_order():
    check_list = os.environ.get("check_list").split(",")
    msg = ""
    num = 0
    for partNumber in check_list:
        print(partNumber)
        #product_number_list = iphone_check_api().get_partNumber("iphone14")
        response = iphone_check_api().check_store_state(partNumber)
        print(response)
        msg,num = foramt_mag(response,msg, num)
        msg += msg
        num += num

    if num > 0:
        line_notify().send_msg(msg)

