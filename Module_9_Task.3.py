class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled
car = Car("ABC-123", 142)
print("Acceleration Test")
print(f"Initial speed: {car.current_speed} km/h")
car.accelerate(30)
print(f"After +30 km/h: {car.current_speed} km/h")
car.accelerate(70)
print(f"After +70 km/h: {car.current_speed} km/h")
car.accelerate(50)
print(f"After +50 km/h: {car.current_speed} km/h")
print(f"\nCurrent speed before emergency brake: {car.current_speed} km/h")
car.accelerate(-200)
print(f"Speed after emergency brake (-200 km/h): {car.current_speed} km/h")
print("\nDrive Method Test")
car2 = Car("ABC-123", 142)
car2.travelled_distance = 2000
car2.current_speed = 60
print(f"Initial travelled distance: {car2.travelled_distance} km")
print(f"Current speed: {car2.current_speed} km/h")
car2.drive(1.5)
print(f"After driving 1.5 hours: {car2.travelled_distance} km")