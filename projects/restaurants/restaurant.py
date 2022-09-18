import json
def fast_overlap1(s, t):
    if s == [] or t == []:
        return 0
    else:
        if s[0] == t[0]:
            return 1 + fast_overlap1(s[1:], t[1:])
        elif s[0] < t[0]:
            return fast_overlap1(s[1:], t)
        elif s[0] > t[0]:
            return fast_overlap1(s,t[1:])
def fast_overlap(s, t):
    """Return the overlap between sorted S and sorted T.

    >>> fast_overlap([2, 3, 5, 6, 7], [1, 4, 5, 6, 7, 8])
    3
    """
    count, i, j = 0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count + 1, i + 1, j + 1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count

def search(query, ranking = lambda r : -r.star):
    finded = [r for r in Restaurant.all if query in r.name]
    return sorted(finded, key = ranking)
def reviewed_both(r1, r2):
    return fast_overlap1(r1.reviewers, r2.reviewers)
class Restaurant:
    all = [ ]
    def __init__(self, name, star,reviewers):
        self.name = name
        self.star = star
        self.reviewers = reviewers
        Restaurant.all.append(self)
    def similar(self, k, similarity = reviewed_both):
        """Return the k most similar restaurants related to self, using similarity function"""
        other = list(Restaurant.all)
        other.remove(self)
        return sorted(other, key =  lambda r : -similarity(r,self))[:k]
    def __repr__(self):
        return '<{0}>'.format(self.name)
def load_reviews(reviews_file): 
    reviewers_for_restaurants = {}
    for line in open(reviews_file):
        review = json.loads(line)
        bzs = review['business_id']
        if bzs not in reviewers_for_restaurants:
            reviewers_for_restaurants[bzs] = [review['user_id']]
        else:
            reviewers_for_restaurants[bzs].append(review['user_id'])
    return reviewers_for_restaurants
def load_restaurants(restaurants_file, reviewers_for_restaurants):
    for line in open(restaurants_file):
        res = json.loads(line)
        reviewers = reviewers_for_restaurants[res['business_id']]
        Restaurant(res['name'], res['stars'], sorted(reviewers))
reviewers_fianl = load_reviews('reviews.json')
load_restaurants('restaurants.json', reviewers_fianl)
result = search('Thai') # a list
print(result)
for r in result:
    print(r, 'is similar to ', r.similar(2))