
travel_log = [
    {
        "country": "France",
        "visits": 10,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Nepal",
        "visits": 12,
        "cities": ["Kathmandu", "Bhaktapur", "Lalitpur", "Pokhara"]
    }
]

# Function to add a new country
def add_new_country(name, times_visits, cities_visited):
    new_country = {
        "country": name,
        "visits": times_visits,
        "cities": cities_visited
    }
    travel_log.append(new_country)

# Get user input
country = input("Enter the name of the country: \n")
times_of_visits = int(input("Enter the number of times you visited: \n"))
cities = input("Enter the names of cities you visited, separated by commas: \n").split(',')

# Add the new entry to the travel log
add_new_country(country, times_of_visits, [city.strip() for city in cities])

new_entry_index = len(travel_log) - 1
print(f"I've been to {travel_log[new_entry_index]['country']} {travel_log[new_entry_index]['visits']} times.")
print(f"My favorite city was {travel_log[new_entry_index]['cities'][0]}.")
