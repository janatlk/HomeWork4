from Cars.create_cars import Car
from Cars.get_car_info import get_car_info

w = Car("BMW", 123)
w.start_engine()
w.stop_engine()
get_car_info(w)
