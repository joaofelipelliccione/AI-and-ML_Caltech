from datetime import datetime


class CarRental:
    def __init__(self, inventory):
        self.inventory = inventory
        self.rented_cars = {}

    def display_available_cars(self):
        print("Available Cars:")
        for car, quantity in self.inventory.items():
            print(f"{car}: {quantity}")

    def rent(self, car, num_cars, rental_type):
        if car in self.rented_cars:
            return f"You already have a rental record for {car}. Try returning it or renting a different model."

        if car in self.inventory and self.inventory[car] >= num_cars and num_cars > 0:
            self.rented_cars[car] = {
                "rental_type": rental_type,
                "start_time": datetime.now(),
                "num_cars": num_cars,
            }
            self.inventory[car] -= num_cars
            return f"Rented Car(s): {num_cars} {car}(s) | Rental Type: {rental_type}"

        return "Invalid rental request. Please check availability and/or the number of cars requested."

    def return_cars(self, car):
        if car in self.rented_cars:
            return self._process_return(car)
        return "Invalid return request. Car not found in rented cars."

    def _calculate_rental_period(self, rental_period, rental_type):
        if rental_type == "hourly":
            return f"{rental_period.seconds // 3600} hours."
        elif rental_type == "daily":
            return f"{rental_period.days} days."
        elif rental_type == "weekly":
            return f"{rental_period.days // 7} weeks."

    def _process_return(self, car):
        rental_info = self.rented_cars.pop(car)
        start_time = rental_info["start_time"]
        num_cars = rental_info["num_cars"]
        rental_type = rental_info["rental_type"]

        rental_period = datetime.now() - start_time
        print(f"RENTAL_PERIOD_DEBUG: {str(rental_period)}")  # TO DEBUG
        specific_rental_period = self._calculate_rental_period(
            rental_period, rental_type
        )

        self.inventory[car] += num_cars
        return f"{num_cars} {car}(s) returned | Rental period: {specific_rental_period}"


class Customer:
    def __init__(self, name):
        self.name = name

    def rent_car(self, rental, car, num_cars, rental_type):
        return rental.rent(car, num_cars, rental_type)

    def return_car(self, rental, car):
        return rental.return_cars(car)
