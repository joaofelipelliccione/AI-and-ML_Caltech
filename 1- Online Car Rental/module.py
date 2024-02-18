from typing import Literal
from datetime import datetime

"""Types"""
CarModel = Literal["Toyota Corolla", "Ford F-150", "Volkswagen Golf", "Honda Civic"]
RentalMode = Literal["Hourly", "Daily", "Weekly"]

Stock = dict[CarModel, int]
# {"Toyota Corolla": 5, "Ford F-150": 10, "Volkswagen Golf": 15, "Honda Civic": 20}
RentalDetails = list[tuple[int, CarModel, int, RentalMode]]
# [(Units to Rent, Ford F-150, Amount of RentalMode, "Hourly",)]
Control = dict[CarModel, list[tuple[int, int, RentalMode, str, str]]]
# {"Toyota Corolla": [(Units to Rent, Amount of RentalMode, "Hourly", Rental Start Date, Rental End Date)],


class CarRental:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.stock: Stock = {
            "Toyota Corolla": 5,
            "Ford F-150": 10,
            "Volkswagen Golf": 15,
            "Honda Civic": 20,
        }
        self.history: Control = {model: [] for model in self.stock}

    def _add_to_history(self, rental_summary: Control) -> None:
        for car_model, rental_summary_list in rental_summary.items():
            self.history[car_model].extend(rental_summary_list)

    def _create_rent(self, rental_details: RentalDetails) -> Control:
        rental_summary: Control = {model: [] for model in self.stock}

        for units, car_model, rental_mode_amount, rental_mode in rental_details:
            if units <= self.stock[car_model]:
                self.stock[car_model] -= units
                current_time = datetime.now()

                rental_summary[car_model].append(
                    (
                        units,
                        rental_mode_amount,
                        rental_mode,
                        str(current_time),
                        "END_DATE",
                    )
                )
            else:
                print(
                    f"[Error] [{car_model}] --> Required units: {units} | Available units: {self.stock[car_model]}"
                )

        self._add_to_history(rental_summary)
        return rental_summary

    def show_available_cars(self, car_model: CarModel = None) -> None:
        if car_model is None:
            print("Available cars:")
            for car_model, quantity in self.stock.items():
                print(f"{car_model}: {quantity} units available")
        else:
            print(f"Available {car_model} units: {self.stock[car_model]}.")

    def hourly_rent(self, rental_details: RentalDetails) -> None:
        rental_summary: Control = self._create_rent(rental_details)
        print(f"Rental summary: {rental_summary}")


rental = CarRental("John Doe")
rental.hourly_rent(
    [(2, "Toyota Corolla", 12, "Hourly"), (1, "Toyota Corolla", 5, "Hourly")]
)
rental.hourly_rent([(1, "Ford F-150", 10, "Hourly")])
print(rental.history)
rental.show_available_cars()
