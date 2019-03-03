class Node:
    address_components = [];

    # Constructure off Point
    def __init__(self, Place_id, Point, Address_components, Formatted_address):
        self.place_id = Place_id;
        self.point = Point;
        self.address_components.append(Address_components);
        self.formatted_address = Formatted_address;

    def __str__(self):
        return (self.place_id, self.point, self.address_components, self.formatted_address);
