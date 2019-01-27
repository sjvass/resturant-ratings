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


def get_user_rating():
    user_restaurant = input("Please enter a restaurant name: ")
    user_rating = input("Enter your restaurant's rating: ")

    if user_rating.isdigit():
        user_rating = int(user_rating)

    while user_rating not in range(1,6):
        print ("Rating not valid. Please enter an integer between 1 and 5 inclusive.")
        user_rating = int(input(">"))
        
    return (user_restaurant, user_rating)


ratings_dict = get_ratings('scores.txt')


def print_ratings():    
    items = sorted(ratings_dict.items())
    # print (type(ratings_dict.items()))

    for restaurant, rating in items:
        print('{} is rated at {}.'.format(restaurant, rating)) 


while True:
    print ('\nTo see a list of ratings type "ratings"')
    print ('To enter a new restaurant rating type "new"')
    print ('To exit the program type "q"')

    response = input(">")

    if response == 'ratings':
        print_ratings()
    elif response == 'new':
        user_ratings = get_user_rating()
        ratings_dict[user_ratings[0]] = user_ratings[1]
    elif response == 'q':
        quit()
    else:
        print('Not a valid input. Please choose from one of the above options.\n')




# def print_ratings():
#     user_ratings = get_user_rating()

#     ratings_dict[user_ratings[0]] = user_ratings[1]

#     items = sorted(ratings_dict.items())
#     # print (type(ratings_dict.items()))

#     for restaurant, rating in items:
#         print('{} is rated at {}.'.format(restaurant, rating)) 
