from my_datatypes.hotel_datatypes import hotels_data

def get_hotel_instructions(hotel_name: str) -> str:
    """Generate dynamic instructions based on hotel data"""
    if hotel_name in hotels_data:
        hotel = hotels_data[hotel_name]
        return f"""
You are a helpful hotel customer care assistant.
- Hotel name is {hotel_name}.
- Hotel Owner name is {hotel.get('owner', 'Not Available')}.
- Hotel total rooms {hotel.get('rooms', 'Not Available')}.
- {hotel.get('special_rooms', 'Not Available')} rooms not available for public, reserved for special guests.
- Location: {hotel.get('location', 'Not Available')}.
"""
    else:
        return f"You are a hotel assistant. Sorry, information for {hotel_name} is not available."
