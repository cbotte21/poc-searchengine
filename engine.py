from collections import Counter
import string
import math

class SearchEngine:
    def __init__(self) -> None:
        self.database = []

    def transformToDocument(self, s):
        s = s.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
        return Counter(s.lower().split(" "))

    def insert(self, s):
        res = {"text": s}
        res["dimensions"] = self.transformToDocument(s)
        self.database.append(res)

    def query(self, s):
        q = self.transformToDocument(s)

        currMax = 0
        resTxt = None

        for document in self.database:
            total = 0
            for word in document["dimensions"].keys():
                if word in q.keys():
                    total += math.sqrt(
                        math.pow(q[word], 2) + math.pow(document["dimensions"][word], 2)
                    )
            if total > currMax:
                currMax = total
                resTxt = document["text"]
    
        return resTxt

    def describe(self):
        print(self.database)