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
print(attractions)
