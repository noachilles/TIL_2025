movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]

movies_info = []
for i in range(len(movies)):
    movies_info.append({'title': movies[i], 'rating': ratings[i]})
    
def get_high_rated_movies(threshold):
    movie_list = []
    for movie in movies_info:
        if movie['rating'] >= threshold:
            movie_list.append(movie['title'])
    return movie_list

if __name__ == "__main__":
    threshold = int(input('Enter the rating threshold: '))
    movie_list = get_high_rated_movies(threshold)
    print(f'Movies with a rating of {threshold:.1f} or higher:')
    for movie in movie_list:
        print(movie)