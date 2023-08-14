from framework.filters.filters import length_filter
from framework.vehicle_data import VehicleData

obj = VehicleData('framework/data.npy')

filtered_segments = obj.filter(length_filter)
obj.plot(filtered_segments)
