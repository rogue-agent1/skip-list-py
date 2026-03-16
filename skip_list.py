import random
class SkipNode:
    def __init__(s, key=None, val=None, level=0):
        s.key = key; s.val = val; s.forward = [None] * (level + 1)
class SkipList:
    def __init__(s, max_level=16, p=0.5):
        s.max_level = max_level; s.p = p; s.level = 0
        s.header = SkipNode(level=max_level); s.size = 0
    def _random_level(s):
        lvl = 0
        while random.random() < s.p and lvl < s.max_level: lvl += 1
        return lvl
    def insert(s, key, val=None):
        update = [None] * (s.max_level + 1); cur = s.header
        for i in range(s.level, -1, -1):
            while cur.forward[i] and cur.forward[i].key < key: cur = cur.forward[i]
            update[i] = cur
        cur = cur.forward[0]
        if cur and cur.key == key: cur.val = val; return
        lvl = s._random_level()
        if lvl > s.level:
            for i in range(s.level + 1, lvl + 1): update[i] = s.header
            s.level = lvl
        node = SkipNode(key, val, lvl)
        for i in range(lvl + 1):
            node.forward[i] = update[i].forward[i]; update[i].forward[i] = node
        s.size += 1
    def search(s, key):
        cur = s.header
        for i in range(s.level, -1, -1):
            while cur.forward[i] and cur.forward[i].key < key: cur = cur.forward[i]
        cur = cur.forward[0]
        return cur.val if cur and cur.key == key else None
    def to_list(s):
        result = []; cur = s.header.forward[0]
        while cur: result.append((cur.key, cur.val)); cur = cur.forward[0]
        return result
def demo():
    random.seed(42); sl = SkipList()
    for x in [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]:
        sl.insert(x, x * 10)
    print(f"Search 19: {sl.search(19)}")
    print(f"Search 15: {sl.search(15)}")
    print(f"Sorted: {[k for k, v in sl.to_list()]}")
    print(f"Size: {sl.size}, Levels: {sl.level}")
if __name__ == "__main__": demo()
