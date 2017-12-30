def loadMovies():
	result = {}
	movies = {}
	for line in open('movies.csv'):
		rindex = line.rfind(',')
		lindex = line.find(',')
		movie_id = line[0:lindex]
		movie_title = line[lindex+1 : rindex]
		movies[movie_id] = movie_title

	for line in open('ratings.csv'):
		(userid,moveid,rating,timestamp) = line.split(',')
		result.setdefault(userid, {})
		result[userid][movies[moveid]]=float(rating)

	return result

import json
movies = loadMovies()
file_object = open('similarity.txt', 'w')
file_object.write(json.dumps(movies))
file_object.close( )

file_object = open('similarity.txt', 'r')
try:
	all_the_text = file_object.read()
	movies = json.loads(all_the_text)
	print(movies)
finally:
	file_object.close( )
