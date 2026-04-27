vehicle = {'bicycle': 'hercules', 'car': 'Maruti', 'bike': ' Harley', 'scooter': 'bajaj'}
for key,value in vehicle.items():
    print(key,value)
print()

from collections import OrderedDict

ordered_vehicle = OrderedDict()
ordered_vehicle['bicycle'] = 'hercules'
ordered_vehicle['car'] = 'Maruti'
ordered_vehicle['bike'] = 'Harley'
for key,value in ordered_vehicle.items():
    print(key,value)
print()


ordered_vehicle["car"] = 'BMW'
print(ordered_vehicle)
ordered_vehicle.pop("car")
print(ordered_vehicle)
ordered_vehicle["car"] = 'BMW'
print(ordered_vehicle)
print()


print(sorted(ordered_vehicle.items(), key=lambda item: item[0], reverse=True))
print(sorted(ordered_vehicle.items(), key=lambda item: item[1]))
print(sorted(ordered_vehicle.items(), key=lambda item: len(item[1])))
