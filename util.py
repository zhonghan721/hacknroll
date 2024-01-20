import googlemaps, spacy
from data import CATEGORIES, EXACT_CATEGORIES
from googlemaps import places

gmaps = googlemaps.Client(key="")
nlp = spacy.load('en_core_web_md')

test_loc = (1.2949111110307086, 103.77368865180391)
LIMIT = 10

def get_nearby_places(location, type, limit):
    request = places.places_nearby(gmaps, location=location, rank_by="distance", type=type)
    result = request["results"]
    dist_time = get_distance_time(origin=location, location_info=result, limit=limit)
    current_loc = gmaps.reverse_geocode(location)
    output = "You are currently at {0}.\nHere are the nearby places:\n".format(current_loc[0]["formatted_address"])
    for i in range(min(limit, len(result))):
        output += "({0}) {1}\n".format(str(i + 1), result[i]["name"])
        output += "Address: {0}\n".format(result[i]["vicinity"])
        output += "Distance: {0}, Travelling Time: {1}\n\n".format(dist_time[0]["elements"][i]["distance"]["text"], dist_time[0]["elements"][i]["duration"]["text"])
    print(output)
    

def get_distance_time(origin, location_info, limit):
    dest_list = list()
    for i in range(min(limit, len(location_info))):
        dest_loc = location_info[i]["geometry"]["location"]
        dest_list.append((dest_loc["lat"], dest_loc["lng"]))
    result = gmaps.distance_matrix(origin, dest_list, mode="transit", transit_mode=["bus", "rail"])
    return result["rows"]

def check_similarity(word1, word2):
    doc1 = nlp(word1)
    doc2 = nlp(word2)

    similarity_score = doc1.similarity(doc2)

    return similarity_score

def parse_category_input(input):
    max_index = -1
    max = 0
    for i in range(len(CATEGORIES)):
        curr = check_similarity(input, CATEGORIES[i])
        if curr > max:
            max_index = i
            max = curr
    if max_index == -1:
        raise ValueError("No matching category found")
    return EXACT_CATEGORIES[max_index]

# if __name__ == "__main__":
#     category = input("Type: \n")
#     correct = parse_category_input(category)
#     get_nearby_places(test_loc, correct, LIMIT)
