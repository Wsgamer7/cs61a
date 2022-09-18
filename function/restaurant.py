def search(query, ranking = lambda r : -r.star):
    finded = [r for r in Restaurant.all if query in r.name]
    return sorted(finded, key = ranking)
def reviewed_both(r1, r2):
    aim_people = [m for m in r1.reviewer if m in r2.reviewer]
    return len(aim_people)
class Restaurant:
    all = [ ]
    def __init__(self, name, star):
        self.name = name
        self.star = star
        Restaurant.all.append(self)
    def similar(self, k, similarity = reviewed_both):
        """Return the k most similar restaurants related to self, using similarity function"""
        other = list(Restaurant.all)
        other.remove(self)
        return sorted(other, key =  lambda r : -similarity(r,self))[:k]
    def __repr__(self):
        return '<{0}>'.format(self.name)
r1 = Restaurant('chiken gb', 5)
r2 = Restaurant('yellow chiken', 3)
r3 = Restaurant('fire chion', 4)
r1.reviewer = ['ws', 'lyf']
r2.reviewer = ['ws', 'lyf']
r3.reviewer = ['ws', 'wzy']
result = search('chi') # a list
print(result)
for r in result:
    print(r, 'is similar to ', r.similar(2))