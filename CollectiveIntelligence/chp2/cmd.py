from distance import critics
from distance import euclidean_distance

print(euclidean_distance(critics['Toby'],critics['Claudia Puig']))

from distance import pearson_distance
print(pearson_distance(critics['Toby'],critics['Claudia Puig']))

from distance import jaccard_distance
print(jaccard_distance(critics['Toby'],critics['Claudia Puig']))

from distance import manhattan_distance
print(manhattan_distance(critics['Toby'],critics['Claudia Puig']))

from distance import top_n_matches
print('\n****************************top_n_matches(critics,Toby,n=3, similarity=euclidean_distance)***********************************')
print(top_n_matches(critics,'Toby',n=3, similarity=pearson_distance))


from distance import getRecommendations
print('\n****************************getRecommendations(critics,Toby,euclidean_distance)***********************************')
print(getRecommendations(critics, 'Toby', similarity=euclidean_distance))
print('\n****************************getRecommendations(critics,Toby,pearson_distance)***********************************')
print(getRecommendations(critics, 'Toby', similarity=pearson_distance))
from distance import sim_pearson
print('\n****************************getRecommendations(critics,Toby,sim_pearson)***********************************')
print(getRecommendations(critics, 'Toby', similarity=sim_pearson))
