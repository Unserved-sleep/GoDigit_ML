import collections
movie = collections.namedtuple('Movie', 'genre rating lead_actor')
print(movie)
print(type(movie))
ironman = movie(genre= 'action', rating = 8.5, lead_actor = 'robert')
titanic = movie(genre='romance', rating = 8, lead_actor = 'leonardo dicaprio')
print(titanic)
print(type(titanic))
print(titanic.lead_actor)
print(ironman.rating)



book = collections.namedtuple('book',['price','no_of_pages','author'])
harry_potter = book('500','367','JK ROWLING')
pride_and_prejudice = book('300','200','jane_austen')
print(harry_potter.price)
print(harry_potter)
print(pride_and_prejudice[1])


dictionary=dict({'price':567,'no_of_pages':878,'author': 'cathy thomas'})
print(dictionary)
book = collections.namedtuple('book',['price','no_of_pages','author'])
book_ = book(**dictionary)
print(book_)
book_ = book_._replace(price=800)
print(book_)
