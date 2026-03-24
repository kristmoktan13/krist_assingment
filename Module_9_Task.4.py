import random
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
def get_leader(car_list):
    leader = car_list[0]
    for car in car_list:
        if car.travelled_distance > leader.travelled_distance:
            leader = car
    return leader
print("Creating 10 cars for the race")
cars = []
for i in range(1, 11):
    reg_number = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(reg_number, max_speed)
    cars.append(car)
    print(f"{reg_number}: max speed {max_speed} km/h")
print("\nTHE RACE BEGINS\n")
hours = 0
race_finished = False
winner = None
while not race_finished:
    hours += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000 and not race_finished:
            race_finished = True
            winner = car
    if hours % 100 == 0:
        leader = get_leader(cars)
        print(f"Hour {hours}: Leading car {leader.registration_number} at {leader.travelled_distance:.1f} km")
print(f"\nRACE FINISHED AFTER {hours} HOURS")
print(f"Winner: {winner.registration_number} with {winner.travelled_distance:.1f} km\n")
for i in range(len(cars)):
    for j in range(len(cars) - 1):
        if cars[j].travelled_distance < cars[j + 1].travelled_distance:
            temp = cars[j]
            cars[j] = cars[j + 1]
            cars[j + 1] = temp
print("=" * 70)
print("FINAL RACE RESULTS")
print("=" * 70)
print(f"{'Rank':<6}{'Registration':<15}{'Max Speed':<12}{'Current Speed':<15}{'Distance (km)':<15}")
print("-" * 70)
for rank in range(len(cars)):
    car = cars[rank]
    print(
        f"{rank + 1:<6}{car.registration_number:<15}{car.max_speed:<12}{car.current_speed:<15}{car.travelled_distance:<15.1f}")
print("=" * 70)