movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']

def get_movie_recommendation(rating):
    if rating >= 9:
        return movies[0]
    elif rating >= 8:
        return movies[1]
    elif rating >= 7:
        return movies[2]
    else:
        return movies[3]
    
if __name__ == '__main__':
    rating = int(input('Enter your movie rating (0-10): '))
    movie_title = get_movie_recommendation(rating)
    print(f'Recommended movie: {movie_title}')