# 1
N = int(input())
books = [input() for _ in range(N)]
book_num = {}
for i in set(books):
    book_num[i] = books.count(i) 
book = sorted(book_num.items(), key=lambda x:x[1], reverse=True)
print(book[0][0])

# 2
N = int(input())
books = [input() for _ in range(N)]
book_num = {}
for i in set(books):
    book_num[i] = books.count(i) 
max = 0
best = dict(sorted(book_num.items()))
for i in best:
    if (best[i]) > max:
        max = best[i]
        book = i
print(book)
