from geopy.geocoders import Nominatim

# Initialize the geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return "Address not found"
    except Exception as e:
        return str(e)

# Example addresses
addresses = [
    "1600 Pennsylvania Ave NW, Washington, DC 20500",
    "Eiffel Tower, Paris, France",
    "Invalid Address"
]

for address in addresses:
    coordinates = geocode_address(address)
    print(f"Address: {address}")
    print(f"Coordinates: {coordinates}")
    print()
