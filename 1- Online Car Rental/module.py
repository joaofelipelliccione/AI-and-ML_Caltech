from typing import Literal
from datetime import datetime

CarModel = Literal["Toyota Corolla", "Ford F-150", "Volkswagen Golf", "Honda Civic"]
RentalMode = Literal["Hourly", "Daily", "Weekly"]

Stock = dict[CarModel, int]
# {"Toyota Corolla": 5, "Ford F-150": 10, "Volkswagen Golf": 15, "Honda Civic": 20}

RentInfo = list[tuple[int, CarModel, int, RentalMode]]
# [(Units to Rent, Ford F-150, Amount of RentalMode, "Hourly",)]

History = list[tuple[int, CarModel, int, RentalMode, str, str]]
# [(Units to Rent, Ford F-150, Amount of RentalMode, "Hourly", Rental Start Date, Rental End Date)]


class CarRental:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.stock: Stock = {
            "Toyota Corolla": 5,
            "Ford F-150": 10,
            "Volkswagen Golf": 15,
            "Honda Civic": 20,
        }
        self.history: History = []

    def _register_rent(self, rent_info: RentInfo) -> History:
        rental_summary: History = []

        for units, car_model, rental_mode_amount, rental_mode in rent_info:
            if units <= self.stock[car_model]:
                self.stock[car_model] -= units

                current_time = datetime.now()
                rental_summary.append(
                    (
                        units,
                        car_model,
                        rental_mode_amount,
                        rental_mode,
                        str(current_time),
                        "FINAL_DATE",
                    )
                )
            else:
                print(
                    f"[Error] [{car_model}] --> Required units: {units} | Available units: {self.stock[car_model]}"
                )

        self.history.extend(rental_summary)
        return rental_summary

    def show_available_cars(self, car_model: CarModel = None) -> None:
        if car_model is None:
            print("Available cars:")
            for car_model, quantity in self.stock.items():
                print(f"{car_model}: {quantity} units available")
        else:
            print(f"Available {car_model} units: {self.stock[car_model]}.")

    def hourly_rent(self, rent_info: RentInfo) -> None:
        rental_summary: History = self._register_rent(rent_info)
        print(f"Rental summary: {rental_summary}")


rental = CarRental("John Doe")
rental.hourly_rent(
    [
        (2, "Toyota Corolla", 12, "Hourly"),
        (100, "Ford F-150", 5, "Hourly"),
    ]
)
print(rental.history)
rental.show_available_cars()
