from lib.iphone_check import *
from lib.line_notify import *

def foramt_mag(response):
    msg = "\n"
    for stores in response:
        if len(stores[1]) != 0:
            msg += "{} :\n".format(stores[0])
            for product in stores[1]:
                msg += "{} \n".format(product[0])
    return msg

if __name__=="__main__":
    product_number_list = iphone_check_api().get_partNumber("iphone14")

    response = iphone_check_api().check_store_state("MPW43TA/A")

    line_notify().send_msg(foramt_mag(response))
