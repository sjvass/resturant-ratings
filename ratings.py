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

items = sorted(list(ratings_dict.items()))

for item in items:
    print('{} is rated at {}.'.format(item[0], item[1])) 
