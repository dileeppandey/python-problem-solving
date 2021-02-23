""" Parking Lot

"""

from enum import Enum
from abc import ABC, abstractmethod


# Enums and Constants

# TODO: Convert this to ABC and concrete classes to handle future additions
class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5

# TODO: Convert this to ABC and concrete classes to handle future additions
class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zip_code, country) :
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


# Actors interacting with the system: Admin, ParkingAttnendant
class Account(ABC):
    def __init__(self, user_name, password, person, status = AccountStatus.Active):
        self.__username = user_name
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        pass


class Admin(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        super().__init__(user_name, password, person, status)

    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, floor_name, spot):
        pass

    def add_parking_display_board(self, floor_name, display_board):
        pass

    def add_customer_info_panel(self, floor_name, info_panel):
        pass

    def add_entrance_panel(self, entrance_panel):
        pass

    def add_exit_panel(self, exit_panel):
        pass


class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        super().__init__(user_name, password, person, status)

    def process_ticket(self, ticket):
        pass


# ParkingSpot base class and all it's children
class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False

    def remove_vehicle(self):
        self.__vehicle = None
        self.__free = True

class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)

class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)

class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)

class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)

class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)


# Vehicle base class and all its child classes
class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__vehicle_type = vehicle_type
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self.__ticket = ticket

class Car(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.CAR, ticket)

class Truck(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.TRUCK, ticket)

class Electric(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.ELECTRIC, ticket)

class Van(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.VAN, ticket)

class Motorbike(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.MOTORBIKE, ticket)


# ParkingFloor: encapsulates a parking floor
class ParkingFloor():
    def __init__(self, name, spots: dict[str, ParkingSpot]={}, portals: dict = {}, display_board: ParkingDisplayBoard={}):
        self.__name = name
        # Iterate through ParkingSpotType and ParkingSpot and add to ParkingFloor
        for spot_type, spot in spots.items():
            key = '__' + spot_type.name.lower()
            self.key = spot
        self.__portals = portals
        self.__display_board = display_board

    def add_parking_spot(self, spot):
        pass

    def assign_vehicle_to_spot(self, vehicle, spot):
        pass

    def update_display_boards(self, board, status):
        pass

    def free_spot(self, spot):
        pass


# TODO: Observer Pattern for ParkingDisplayBoard
class ParkingDisplayBoard:
    pass


# TODO: Singleton instance of a parking lot
class ParkingLot:
    pass
