destinations = ["Paris, France", "Shanghai, China",
                "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# print(test_traveler)


def get_destination_index(destination):

    # for i in range(0, len(destinations), 1):
    #     # if destination != destinations[i]:
    #     #     return 'Did not find the entered destination'
    #     if destination == destinations[i]:
    #         destination_index = i
    destination_index = destinations.index(destination)
    return destination_index


# print(get_destination_index(test_traveler[1]))
# print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Paris, France"))
# print(get_destination_index("Hyderabad, India"))


def get_traveler_location(traveler):
    traveler_destination = str(traveler[1])
    # print(traveler_destination)
    traveler_destination_index = get_destination_index(traveler_destination)
    # print(traveler_destination_index)
    return traveler_destination_index


test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

attractions = [[] for destination in destinations]

# print(attractions)


def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(
            attraction)
    except ValueError:
        print("Error caught!")
        return


# add_attraction('Paris, France', 'hello')
# print(attractions)
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
# print(attractions)

add_attraction("Paris, France", ["Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Orsay", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", [
               "historical site", "monument", "museum"]])
add_attraction("Shanghai, China", ["Yu Garden", [
               "garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", [
               "skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", [
               "monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print(attractions)


def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    for attraction in attractions_in_city:
        possible_attraction = attraction
        # print(possible_attraction)
        attraction_tags = attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


print(find_attractions("Los Angeles, USA", ['art']))


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(
        traveler_destination, traveler_interests)
    interests_string = "Hi " + \
        traveler[0] + ", we think you'll like these places around " + \
        traveler_destination + ": "
    for i in range(len(traveler_attractions)):
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += "the " + traveler_attractions[i] + "."
        else:
            interests_string += "the " + traveler_attractions[i] + ", "
    return interests_string


smills_france = get_attractions_for_traveler(
    ['Dereck Smill', 'Paris, France', ['museum']])


print(smills_france)
