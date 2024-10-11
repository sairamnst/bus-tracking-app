from geopy.distance import geodesic
import requests

# Function to get real-time bus data (latitude, longitude, seats available)
def get_bus_data(bus_id):
    # Replace with actual API call or data source
    return {
        "bus_id": bus_id,
        "latitude": 12.9715987,
        "longitude": 77.594566,
        "seats_available": 5,
        "driver_location": (12.9715987, 77.594566)
    }

# Function to get the route data (bus stops)
def get_route_data(route_id):
    # Replace with actual API call or data source
    return [
        {"stop_id": 1, "latitude": 12.971599, "longitude": 77.594566, "name": "Stop 1"},
        {"stop_id": 2, "latitude": 12.961599, "longitude": 77.594566, "name": "Stop 2"},
        # Add more stops as needed
    ]

# Function to get passenger data (GPS coordinates of passengers who booked)
def get_passenger_data(route_id):
    # Replace with actual API call or data source
    return [
        (12.9715980, 77.594570),  # Passenger 1
        (12.9715990, 77.594565),  # Passenger 2
        (12.9717000, 77.594600),  # Passenger 3 (outside bus range)
    ]

# Function to calculate distance between two GPS coordinates
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).meters

# Function to count the number of people on the bus
def count_passengers_on_bus(driver_location, passenger_locations, bus_length):
    on_bus_count = 0

    for passenger_location in passenger_locations:
        distance = calculate_distance(driver_location, passenger_location)
        if distance <= bus_length:
            on_bus_count += 1
    
    return on_bus_count

# Function to decide whether the bus should stop
def should_stop(bus_data, next_bus_data, is_last_bus):
    if bus_data["seats_available"] > 0:
        return True  # Bus should stop if there are seats
    if is_last_bus or next_bus_data["seats_available"] == 0:
        return True  # Bus should stop if it's the last bus or the next bus is full
    return False  # Bus can skip the stop if the next bus has seats

# Example implementation of the full bus tracking system
def main():
    route_id = "route_123"
    bus_ids = ["bus_1", "bus_2", "bus_3"]
    route_data = get_route_data(route_id)
    bus_length = 10  # Example bus length in meters

    for i, bus_id in enumerate(bus_ids):
        bus_data = get_bus_data(bus_id)
        next_bus_data = get_bus_data(bus_ids[i + 1]) if i + 1 < len(bus_ids) else None
        is_last_bus = (i == len(bus_ids) - 1)

        # Get passenger data and count how many are on the bus
        passenger_locations = get_passenger_data(route_id)
        passengers_on_bus = count_passengers_on_bus(bus_data["driver_location"], passenger_locations, bus_length)
        print(f"Bus {bus_id} has {passengers_on_bus} passengers on board.")

        # Update seats available based on counted passengers
        bus_data["seats_available"] -= passengers_on_bus

        for stop in route_data:
            if should_stop(bus_data, next_bus_data, is_last_bus):
                print(f"Bus {bus_id} should stop at {stop['name']}")
            else:
                print(f"Bus {bus_id} can skip {stop['name']}")

if __name__ == "__main__":
    main()
