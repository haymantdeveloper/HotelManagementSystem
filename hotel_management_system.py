# File: hotel_management_system.py
# Author: Haymant Singh
# Description: A console-based hotel management system for LANGHAM Hotels.
# Date: 26.06.2024

import os
from datetime import datetime

# Room structure
class Room:
    def __init__(self, room_number, features):
        """
        Initialize a new Room object.

        Parameters:
        room_number (str): The number of the room.
        features (list): A list of features for the room.
        """
        self.room_number = room_number
        self.features = features
        self.is_allocated = False
        self.customer_name = ""

    def __str__(self):
        """
        Return a string representation of the Room object.
        """
        return f"Room {self.room_number} - Features: {', '.join(self.features)} - Allocated: {self.is_allocated} - Customer: {self.customer_name}"


# Hotel Management System
class HotelManagementSystem:
    def __init__(self):
        """
        Initialize a new HotelManagementSystem object.
        """
        try:
            self.rooms = []  # List to store room objects
            self.file_name = "LHMS_764708175.txt"  # Name of the file to store data
            self.ensure_file_exists()  # Ensure the file exists
            self.load_data()  # Load data from the file
        except SyntaxError as e:
            print(f"SyntaxError caught: {e}")
        except ImportError as e:
            print(f"ImportError caught: {e}")

    def ensure_file_exists(self):
        """
        Ensure that the main file exists. If it doesn't, create an empty file.
        """
        try:
            if not os.path.exists(self.file_name):  # Check if the file exists
                with open(self.file_name, "w") as file:
                    pass  # Create an empty file if it doesn't exist
        except IOError as e:
            print(f"IOError caught: {e}")

    def load_data(self):
        """
        Load room data from the file into the system.
        """
        try:
            with open(self.file_name, "r") as file:  # Open the file in read mode
                lines = file.readlines()  # Read all lines from the file
                for line in lines:
                    parts = line.strip().split('|')  # Split the line by '|'
                    room = Room(parts[0], parts[1].split(','))  # Create a Room object
                    room.is_allocated = parts[2] == 'True'  # Set allocation status
                    room.customer_name = parts[3]  # Set customer name
                    self.rooms.append(room)  # Add room to the list
        except FileNotFoundError as e:
            print(f"FileNotFoundError caught: {e}")
        except IOError as e:
            print(f"IOError caught: {e}")
        except IndexError as e:
            print(f"IndexError caught: {e}")
        except ValueError as e:
            print(f"ValueError caught: {e}")

    def save_data(self):
        """
        Save the current room data to the file.
        """
        try:
            with open(self.file_name, "w") as file:  # Open the file in write mode
                for room in self.rooms:
                    file.write(
                        f"{room.room_number}|{','.join(room.features)}|{room.is_allocated}|{room.customer_name}\n")  # Write room data to file
        except IOError as e:
            print(f"IOError caught: {e}")

    def add_room(self, room_number, features):
        """
        Add a new room to the system.

        Parameters:
        room_number (str): The number of the room.
        features (list): A list of features for the room.
        """
        try:
            if not isinstance(features, list):
                raise TypeError("Features should be a list.")  # Raise an error if features is not a list
            self.rooms.append(Room(room_number, features))  # Add new room to the list
            self.save_data()  # Save data to the file
            print(f"Room {room_number} is successfully added.")
        except ValueError as e:
            print(f"ValueError caught: {e}")
        except TypeError as e:
            print(f"TypeError caught: {e}")

    def delete_room(self, room_number):
        """
        Delete a room from the system.

        Parameters:
        room_number (str): The number of the room to be deleted.
        """
        try:
            self.rooms = [room for room in self.rooms if room.room_number != room_number]  # Remove room from the list
            self.save_data()  # Save data to the file
            print(f"Room {room_number} is successfully deleted.")
        except ValueError as e:
            print(f"ValueError caught: {e}")

    def display_room_details(self):
        """
        Display details of all rooms.
        """
        try:
            for room in self.rooms:
                print(room)  # Print details of each room
        except Exception as e:
            print(f"An error occurred while displaying room details: {e}")

    def allocate_room(self, room_number, customer_name):
        """
        Allocate a room to a customer.

        Parameters:
        room_number (str): The number of the room to be allocated.
        customer_name (str): The name of the customer.
        """
        try:
            for room in self.rooms:
                if room.room_number == room_number:  # Check if room number matches
                    if not room.is_allocated:  # Check if room is not allocated
                        room.is_allocated = True  # Allocate the room
                        room.customer_name = customer_name  # Set customer name
                        print(f"Room {room_number} allocated to {customer_name}.")
                        self.save_data()  # Save data to the file
                    else:
                        print(f"Room {room_number} is already allocated.")
                    return
            print(f"Room {room_number} not found.")
        except NameError as e:
            print(f"NameError caught: {e}")
        except Exception as e:
            print(f"An error occurred while allocating room: {e}")

    def display_room_allocation_details(self):
        """
        Display details of allocated rooms.
        """
        try:
            for room in self.rooms:
                if room.is_allocated:  # Check if room is allocated
                    print(room)  # Print details of allocated room
        except Exception as e:
            print(f"An error occurred while displaying room allocation details: {e}")

    def bill_and_deallocate(self, room_number):
        """
        Bill the customer and deallocate the room.

        Parameters:
        room_number (str): The number of the room to be deallocated.
        """
        try:
            for room in self.rooms:
                if room.room_number == room_number and room.is_allocated:  # Check if room is allocated
                    print(f"Billing customer {room.customer_name} for Room {room_number}.")
                    room.is_allocated = False  # Deallocate the room
                    room.customer_name = ""  # Clear customer name
                    self.save_data()  # Save data to the file
                    print(f"Room {room_number} is de-allocated for the customer.")
                    return
            print(f"Room {room_number} not found or not allocated.")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError caught: {e}")
        except Exception as e:
            print(f"An error occurred while billing and deallocating room: {e}")

    def save_room_allocation_to_file(self):
        """
        Save the room allocation data to the file.
        """
        try:
            self.save_data()  # Save data to the file
            print("Room allocation saved to file.")
        except IOError as e:
            print(f"IOError caught: {e}")

    def show_room_allocation_from_file(self):
        """
        Show the room allocation data from the file.
        """
        try:
            with open(self.file_name, "r") as file:  # Open the file in read mode
                print(file.read())  # Print the file content
        except FileNotFoundError as e:
            print(f"FileNotFoundError caught: {e}")
        except EOFError as e:
            print(f"EOFError caught: {e}")

    def backup_file(self):
        """
        Backup the room allocation data to a new file and clear the original file.
        """
        try:
            backup_filename = f"LHMS_764708175_Backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"  # Generate backup filename
            with open(self.file_name, "r") as file:  # Open the original file in read mode
                data = file.read()  # Read the file content
            with open(backup_filename, "w") as backup_file:  # Open the backup file in write mode
                backup_file.write(data)  # Write data to the backup file
            with open(self.file_name, "w") as file:  # Clear the original file
                file.write("")
            print(f"Backup created and data cleared from original file. Backup filename: {backup_filename}")
        except IOError as e:
            print(f"IOError caught: {e}")
        except OverflowError as e:
            print(f"OverflowError caught: {e}")


def main():
    """
    Main function to run the hotel management system.
    """
    system = HotelManagementSystem()  # Create an instance of HotelManagementSystem

    while True:
        # Display menu options
        print("\nHotel Management System Menu")
        print("1. Add Room")
        print("2. Delete Room")
        print("3. Display Room Details")
        print("4. Allocate Room")
        print("5. Display Room Allocation Details")
        print("6. Billing & De-Allocation")
        print("7. Save Room Allocation to File")
        print("8. Show Room Allocation from File")
        print("9. Backup Room Allocation File")
        print("0. Exit Application")

        choice = input("Enter your choice: ")  # Get user choice

        # Perform the action based on user's choice
        try:
            if choice == '1':
                room_number = input("Enter room number: ")  # Get room number
                features = input("Enter room features (comma-separated): ").split(',')  # Get room features
                system.add_room(room_number, features)  # Add room
            elif choice == '2':
                room_number = input("Enter room number to delete: ")  # Get room number to delete
                system.delete_room(room_number)  # Delete room
            elif choice == '3':
                system.display_room_details()  # Display room details
            elif choice == '4':
                room_number = input("Enter room number to allocate: ")  # Get room number to allocate
                customer_name = input("Enter customer name: ")  # Get customer name
                system.allocate_room(room_number, customer_name)  # Allocate room
            elif choice == '5':
                system.display_room_allocation_details()  # Display room allocation details
            elif choice == '6':
                room_number = input(
                    "Enter room number to bill and deallocate: ")  # Get room number to bill and deallocate
                system.bill_and_deallocate(room_number)  # Bill and deallocate room
            elif choice == '7':
                system.save_room_allocation_to_file()  # Save room allocation to file
            elif choice == '8':
                system.show_room_allocation_from_file()  # Show room allocation from file
            elif choice == '9':
                system.backup_file()  # Backup room allocation file
            elif choice == '0':
                break  # Exit application
            else:
                print("Invalid choice, please try again.")
        except ValueError as e:
            print(f"ValueError caught in main: {e}")
        except TypeError as e:
            print(f"TypeError caught in main: {e}")


if __name__ == "__main__":
    main()
