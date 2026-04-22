import operator

from binstar_client.pprintb import user_list

reviews = [
  {"movie": "Inception",  "user": "alice", "rating": 9},
  {"movie": "Dune",       "user": "bob",   "rating": 8},
  {"movie": "Inception",  "user": "bob",   "rating": 7},
  {"movie": "Interstellar","user":"alice",  "rating": 10},
  {"movie": "Dune",       "user": "charlie","rating": 9},
  {"movie": "Interstellar","user":"charlie","rating": 8},
]

reviews_list = []
for review in reviews:
    reviews_list.append(list(review.items()))

movies = {}
for i in range(len(reviews_list)):
    movies[reviews_list[i][0][1]] = movies.get(reviews_list[i][0][1], []) + [reviews_list[i][2][1]]
for movie, ratings in movies.items():
    avg = sum(ratings)/len(ratings)
    movies[movie] = avg
print("avg_rating = ", movies)  #1

movies_sorted = list(movies.items())
for i in range(0, len(movies_sorted)-1):
    for j in range(i+1, len(movies_sorted)):
       if movies_sorted[i][1] < movies_sorted[j][1]:
         movies_sorted[i], movies_sorted[j] = movies_sorted[j], movies_sorted[i]

print("top_movie = " + movies_sorted[0][0])

must_watch = []
for movie, ratings in movies_sorted:
    if ratings >= 8.5:
        must_watch.append(movie)
print("must_watch = ",must_watch)

user = {}
for i in range(len(reviews_list)):
    user[reviews_list[i][1][1]] = user.get(reviews_list[i][1][1], []) + [[reviews_list[i][2][1],reviews_list[i][0][1]]]

max = 0
for i in user:
    for j in user[i]:
        if j[0] > max:
            fav_movie = j[1]
    user[i] = fav_movie
print("user_favs = ",user)


