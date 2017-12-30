# from distance import critics
# from distance import euclidean_distance

# print(euclidean_distance(critics['Toby'],critics['Claudia Puig']))

# from distance import pearson_distance
# print(pearson_distance(critics['Toby'],critics['Claudia Puig']))

# from distance import jaccard_distance
# print(jaccard_distance(critics['Toby'],critics['Claudia Puig']))

# from distance import manhattan_distance
# print(manhattan_distance(critics['Toby'],critics['Claudia Puig']))

# from distance import top_n_matches
# print('\n****************************top_n_matches(critics,Toby,n=3, similarity=euclidean_distance)***********************************')
# print(top_n_matches(critics,'Toby',n=3, similarity=pearson_distance))


# from distance import getRecommendations
# print('\n****************************getRecommendations(critics,Toby,euclidean_distance)***********************************')
# print(getRecommendations(critics, 'Toby', similarity=euclidean_distance))
# print('\n****************************getRecommendations(critics,Toby,pearson_distance)***********************************')
# print(getRecommendations(critics, 'Toby', similarity=pearson_distance))
# from distance import sim_pearson
# print('\n****************************getRecommendations(critics,Toby,sim_pearson)***********************************')
# print(getRecommendations(critics, 'Toby', similarity=sim_pearson))

# from distance import transformPrefs
# movies =transformPrefs(critics)
# print('\n****************************movies***********************************')
# print(movies)

# print('\n****************************top_n_matches(movies,Superman Returns)***********************************')
# print(top_n_matches(movies,'Superman Returns', 3, pearson_distance))

# print('\n****************************getRecommendations(movies,Just My Luck)***********************************')
# print(getRecommendations(movies,'Just My Luck',pearson_distance))


from distance import calculateSimilarItems
# itemsim = calculateSimilarItems(critics)
# print('\n****************************itemsim***********************************')
# print(itemsim)

from distance import getRecommendedItems
# print('\n****************************getRecommendedItems(critics,itemsim,Toby)***********************************')
# print(getRecommendedItems(critics,itemsim,'Toby'))

from movies import loadMovies
# print('\n****************************movies***********************************')
movies = loadMovies()
# print(movies['87'])
# print('\n****************************getRecommendations(movies,87)[0:30]***********************************')
# print(getRecommendations(movies,'87')[0:30])
import json
itemsim=calculateSimilarItems(movies,n=50)
file_object = open('similarity.txt', 'w')
file_object.write(json.dumps(itemsim))
file_object.close( )
print(getRecommendedItems(movies,itemsim,'87')[0:30])
