from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            if a.name > b.name:
                return 1
            elif a.name < b.name:
                return -1
            else:
                return 0
def main():
    inputs = [
        ('smith', 20),
        ('jones', 15),
        ('jones', 20)]

    items = []
    for item in inputs:
        items.append(Player(item[0], item[1]))

    sorted_items = sorted(items, key=cmp_to_key(Player.cmp))
    for item in sorted_items:
        print(item.name, item.score)