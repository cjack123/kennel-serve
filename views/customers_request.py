CUSTOMERS = [
    {
      "id": 1,
      "name": "Sydney Noh",
      "address": "976 Software School Rd.",
      "phone": "615-555-0369",
      "email": "queenOfCats@email.com",
      "locationId": 1,
      "animalId": 1
    },
    {
      "id": 2,
      "name": "Trevor Guinn",
      "address": "123 NSS Ln",
      "phone": "615-555-7159",
      "email": "locAndKey@email.com",
      "locationId": 2,
      "animalId": 2
    },
    {
      "id": 3,
      "name": "Jaime Foster",
      "address": "436 April Dr",
      "phone": "615-555-8612",
      "email": "jFoster@email.com",
      "locationId": 5,
      "animalId": 3
    },
    {
      "id": 4,
      "name": "April Kepner",
      "address": "19 Mainland st",
      "phone": "615-555-8612",
      "email": "aKepnery@email.com",
      "locationId": 4,
      "animalId": 4
    },
    {
      "name": "Jo Wilson",
      "address": "123 Hope St ",
      "phone": "615-555-3856",
      "email": "jwilson@test.com",
      "animalId": 5,
      "locationId": 3,
      "id": 5
    },
    {
      "email": "t@t.com",
      "name": "test test",
      "id": 6
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer in CUSTOMERS:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break