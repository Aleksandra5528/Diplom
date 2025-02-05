#Александра Мостовик, 26А-Earth когорта,Финальный проект, Инженер по тестированию плюс
import create_order
import data

def get_order_track():
    track = create_order.post_new_order(data.new_order)
    return track.json()['track']
    
def test_get_order_number_track():
    track = get_order_track()
    order_status = create_order.get_order_track(track)
    assert order_status.status_code == 200
