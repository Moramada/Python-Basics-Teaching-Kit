# ==============================================================================
# Topic: Data Structures - Tuples
# Level: Foundational
# Description: Demonstrating immutability in Tuples and practical use cases.
# ==============================================================================

# Defining a Tuple (Immutable Data Structure)
sample_tuple = (1, 2, 3)
print("Tuple Elements:", sample_tuple)

# Note on Immutability:
# Tuples cannot be modified after creation.
# Un-commenting the following line will raise a TypeError:
# sample_tuple[0] = 5

# Common Use Case: Fixed data like GPS coordinates, days of the week, or constants.
location_coordinates = (30.0444, 31.2357)
print("Location Coordinates (Latitude, Longitude):", location_coordinates)