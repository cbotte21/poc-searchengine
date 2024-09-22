from engine import SearchEngine
import time


def toRoundedMs(begin, end):
    return round((end - begin) * 100, 2)

startProgram = time.time()
searchEngine = SearchEngine()

startInsertion = time.time()
# Read documents from file and insert
with open("documents.txt", "r") as doc_file:
    for line in doc_file.readlines():
        searchEngine.insert(line.strip())
endInsertion = time.time()

startQueries = time.time()
# Read queries from file and run
with open("queries.txt", "r") as query_file:
    for line in query_file.readlines():
        start = time.time()
        res = searchEngine.query(line.strip())
        elapsed = toRoundedMs(start, time.time())
        print(f"Query: {line.strip()}\nResult: {res}\nElapsed time: {elapsed}ns")
endQueries = time.time()

print(f"\nInsertion runtime: {toRoundedMs(startInsertion, endInsertion)}ms")
print(f"Query runtime: {toRoundedMs(startQueries, endQueries)}ms")
print(f"Program runtime: {toRoundedMs(startProgram, endQueries)}s")
