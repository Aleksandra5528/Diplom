import configuration
import requests
import data


def post_new_order(new_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=new_order,
                         headers=data.headers)

def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK_PATH,
                        params={'t': track})


