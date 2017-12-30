#-*- coding:utf-8 -*-  
# A dictionary of movie critics and their ratings of a small
# set of movies
#key name,value pair: moive:rating
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,'The Night Listener': 4.5, 'Superman Returns': 4.0,'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt
from math import pow
#欧几里得距离计算相似度
def euclidean_distance(vector1, vector2):
	common = [x for x in vector1 if x in vector2]
	#如果没有重复的key，表示没有交汇的维度，距离为0
	common_len = len(common)
	if common_len == 0:
		return 0
	return 1/(1+sum(pow(vector1[x]-vector2[x],2) for x in common))

#皮尔森相关系数计算相似度,即概率论当中的相关系数
def pearson_distance(vector1, vector2):
	common = [x for x in vector1 if x in vector2]
	#如果没有重复的key，表示没有交汇的维度，距离为0
	common_len = len(common)
	if common_len == 0:
		return 0
	exy=sum([vector1[x] * vector2[x] for x in common]) * common_len
	exey=sum([vector1[x] for x in common]) * sum([vector2[x] for x in common])
	varx = common_len * sum([pow(vector1[x],2) for x in common]) - pow(sum([vector1[x] for x in common]),2)
	vary = common_len * sum([pow(vector2[x],2) for x in common]) - pow(sum([vector2[x] for x in common]),2)

	if varx == 0 or vary == 0 :
		return 0
	return (exy - exey)/sqrt(varx*vary)

#Jaccard相似系数计算相似度（Jaccard similarity coefficient）用于比较有限样本集之间的相似性与差异性。Jaccard系数值越大，样本相似度越高。
def jaccard_distance(vector1, vector2):
	common = [x for x in vector1 if x in vector2]
	#如果没有重复的key，表示没有交汇的维度，距离为0
	common_len = len(common)
	if common_len == 0:
		return 0
	minsum = sum([min(vector1[x], vector2[x]) for x in common])
	maxsum = sum([max(vector1[x], vector2[x]) for x in common])
	return minsum/maxsum

#曼哈顿距离计算相似度
def manhattan_distance(vector1, vector2):
	common = [x for x in vector1 if x in vector2]
	#如果没有重复的key，表示没有交汇的维度，距离为0
	common_len = len(common)
	if common_len == 0:
		return 0
	return 1/(1+sum([abs(vector1[x] - vector2[x]) for x in common]))

#前N个相似匹配项
def top_n_matches(matrix, key, n, similarity=euclidean_distance):
	scores = [(similarity(matrix[key], matrix[other]), other) for other in matrix if other != key]
	scores.sort()
	scores.reverse()
	return scores[:n]

#计算每个人和其他人的相似度
def get_person_similarity(prefs, person, similarity=pearson_distance):
	result = {}
	for person1 in prefs:
		if person1 != person:
			result[person1]=similarity(prefs[person1],prefs[person])
	return result

#计算出person没看过的电影及谁都看过这些电影，对这些电影的评分
def getUnseen(prefs, person):
	unseen = {}
	for person2 in prefs:
		if person2 != person:
			for movie in prefs[person2]:
				if movie not in prefs[person]:
					unseen.setdefault(movie, {})
					unseen[movie][person2] = prefs[person2][movie]
	return unseen


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(p1,p2):
  # Get the list of mutually rated items
  si={}
  for item in p1: 
    if item in p2: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Sums of all the preferences
  sum1=sum([p1[it] for it in si])
  sum2=sum([p2[it] for it in si])
  
  # Sums of the squares
  sum1Sq=sum([pow(p1[it],2) for it in si])
  sum2Sq=sum([pow(p2[it],2) for it in si])	
  
  # Sum of the products
  pSum=sum([p1[it]*p2[it] for it in si])
  
  # Calculate r (Pearson score)
  num=pSum-(sum1*sum2/n)
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0

  r=num/den

  return r

#获取其他人和person的相似度，然后按照相似度对评分进行加权平均，求出没看过的电影的加权评分，然后排序
def getRecommendations(prefs,person,similarity=pearson_distance):
	#获取person和其他人的相似度
	#similarity = get_person_similarity(prefs, person, similarity)
	#print('\n****************************similarity***********************************')
	#print(similarity)
	#获取person没有看过的电影
	#unseen = getUnseen(prefs, person)
	#print('\n****************************unseen***********************************')
	#print(unseen)

	total = {}
	simSum = {}
	for other in prefs:
		if other == person:
			continue
		sim = similarity(prefs[person], prefs[other])
		if sim<=0: 
			continue

		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item]==0:
				total.setdefault(item,0)
				simSum.setdefault(item,0)
				total[item] += sim * prefs[other][item]
				simSum[item] += sim

	rankings=[(sum/simSum[item], item) for item,sum in total.items( )]
	rankings.sort()
	rankings.reverse()
	return rankings

#转置
def transformPrefs(matrix):
	result = {}
	for person in matrix:
		for movie in matrix[person]:
			result.setdefault(movie, {})
			result[movie][person] = matrix[person][movie]
	return result

def calculateSimilarItems(prefs, n=10):
	result = {}
	itemPrefs = transformPrefs(prefs)
	c = 0
	for item in itemPrefs:
		# Status updates for large datasets
		c+=1
		if c%100==0: print "%d / %d" % (c,len(itemPrefs))

		# Find the most similar items to this one
		scores=top_n_matches(itemPrefs,item,n=n,similarity=euclidean_distance)
		result[item]=scores
	return result

def getRecommendedItems(prefs,itemMatch,user):
	userRatings=prefs[user]
	scores={}
	totalSim={}
	# Loop over items rated by this user
	for (item,rating) in userRatings.items():
		# Loop over items similar to this one
		for (similarity,item2) in itemMatch[item]:
			# Ignore if this user has already rated this item
			if item2 in userRatings: 
				continue
			# Weighted sum of rating times similarity
			scores.setdefault(item2,0)
			scores[item2]+=similarity*rating
			# Sum of all the similarities
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity
	# Divide each total score by total weighting to get an average
	rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
	# Return the rankings from highest to lowest
	rankings.sort( )
	rankings.reverse( )
	return rankings






