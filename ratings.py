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

def get_user_rating():
    user_restaurant = input("Please enter a restaurant name: ")
    user_rating = input("Enter your restaurant's rating: ")

    return (user_restaurant, user_rating)

user_ratings = get_user_rating()

ratings_dict[user_ratings[0]] = user_ratings[1]

items = sorted(ratings_dict.items())
# print (type(ratings_dict.items()))

for restaurant, rating in items:
    print('{} is rated at {}.'.format(restaurant, rating)) 
