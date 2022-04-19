LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike",
      "phone": "615-555-1234"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive",
      "phone": "615-555-5678"
    },
    {
      "name": "Nashville Kennel west",
      "address": "1234 Elmo St",
      "phone": "615-555-0002",
      "id": 3
    },
    {
      "name": "Nashville Kennel East",
      "address": "369 Mafia Ave",
      "phone": "615-555-8990",
      "id": 4
    },
    {
      "name": "Nashville Kennel Briley",
      "address": "321 Gwen Rd",
      "phone": "615-555-6783",
      "id": 5
    }
  ]

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location
    
    return requested_location

