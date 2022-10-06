class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Bus = Vehicle('School Volvo', 180, 12)

print(f'Vehicle Name: {Bus.name} Speed: {Bus.max_speed} Mileage: {Bus.mileage}')
      
