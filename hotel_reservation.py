# Enhanced Hotel Reservation System in Python

# Dictionary to store room availability and details
rooms = {
    '101': {'type': 'Single', 'status': 'available'},
    '102': {'type': 'Double', 'status': 'available'},
    '103': {'type': 'Suite', 'status': 'available'},
    '104': {'type': 'Single', 'status': 'available'},
}

# Dictionary to store reservations
reservations = {}

# Function to display the menu
def menu():
    print("\n--- Hotel Reservation Menu ---")
    print("1. View Available Rooms")
    print("2. Book a Room")
    print("3. Check Reservations")
    print("4. Cancel a Reservation")
    print("5. Add Room Type")
    print("6. Remove Room Type")
    print("7. Update Room Type")
    print("8. View Reservation Details")
    print("9. Search Reservations")
    print("10. Exit")

# Function to view available rooms
def view_available_rooms():
    print("\n--- Available Rooms ---")
    for room_number, details in rooms.items():
        if details['status'] == 'available':
            print(f"Room {room_number}: {details['type']}")

# Function to book a room
def book_room():
    view_available_rooms()
    room_number = input("Enter room number to book: ")
    if room_number in rooms and rooms[room_number]['status'] == 'available':
        name = input("Enter your name: ")
        rooms[room_number]['status'] = 'booked'
        reservations[room_number] = name
        print(f"Room {room_number} successfully booked under the name '{name}'!")
    else:
        print("Room not available or invalid room number.")

# Function to check reservations
def check_reservations():
    if not reservations:
        print("No current reservations.")
    else:
        print("\n--- Current Reservations ---")
        for room_number, guest_name in reservations.items():
            print(f"Room {room_number}: Reserved by {guest_name}")

# Function to cancel a reservation
def cancel_reservation():
    room_number = input("Enter room number to cancel: ")
    if room_number in reservations:
        name = reservations.pop(room_number)
        rooms[room_number]['status'] = 'available'
        print(f"Reservation for Room {room_number} under the name '{name}' has been cancelled.")
    else:
        print("No reservation found for the specified room number.")

# Function to add a room type
def add_room_type():
    room_number = input("Enter new room number: ")
    if room_number in rooms:
        print("Room number already exists.")
    else:
        room_type = input("Enter room type (Single/Double/Suite): ")
        rooms[room_number] = {'type': room_type, 'status': 'available'}
        print(f"Room {room_number} of type '{room_type}' added successfully!")

# Function to remove a room type
def remove_room_type():
    room_number = input("Enter room number to remove: ")
    if room_number in rooms:
        if room_number in reservations:
            print("Room is currently reserved and cannot be removed.")
        else:
            del rooms[room_number]
            print(f"Room {room_number} removed successfully!")
    else:
        print("Room number not found.")

# Function to update a room type
def update_room_type():
    room_number = input("Enter room number to update: ")
    if room_number in rooms:
        new_type = input("Enter new room type (Single/Double/Suite): ")
        rooms[room_number]['type'] = new_type
        print(f"Room {room_number} type updated to '{new_type}'.")
    else:
        print("Room number not found.")

# Function to view reservation details
def view_reservation_details():
    room_number = input("Enter room number to view details: ")
    if room_number in reservations:
        guest_name = reservations[room_number]
        print(f"Room {room_number} is reserved by '{guest_name}'.")
    else:
        print("No reservation found for the specified room number.")

# Function to search reservations by guest name
def search_reservations():
    name = input("Enter guest name to search: ")
    found = False
    for room_number, guest_name in reservations.items():
        if guest_name.lower() == name.lower():
            print(f"Room {room_number}: Reserved by {guest_name}")
            found = True
    if not found:
        print("No reservations found for the specified guest name.")

# Main program loop
while True:
    menu()
    choice = input("Enter your choice (1-10): ")
    
    if choice == '1':
        view_available_rooms()
    elif choice == '2':
        book_room()
    elif choice == '3':
        check_reservations()
    elif choice == '4':
        cancel_reservation()
    elif choice == '5':
        add_room_type()
    elif choice == '6':
        remove_room_type()
    elif choice == '7':
        update_room_type()
    elif choice == '8':
        view_reservation_details()
    elif choice == '9':
        search_reservations()
    elif choice == '10':
        print("Exiting Hotel Reservation System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
