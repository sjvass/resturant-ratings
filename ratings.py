"""Restaurant rating lister."""

def get_ratings(filename):

    ratings = {}

    file = open(filename)

    for line in file:
        line = line.rstrip()
        line_data = line.split(":")

        #if ratings[line_data[0]] not in ratings:
        ratings[line_data[0]] = line_data[1]

    file.close()

    return ratings


ratings_dict = get_ratings('scores.txt')

items = sorted(ratings_dict.items())
# print (type(ratings_dict.items()))

for restaurant, rating in items:
    print('{} is rated at {}.'.format(restaurant, rating)) 
