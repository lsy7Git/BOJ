import sys

input = sys.stdin.readline

N = int(input())

books = {}
for _ in range(0,N):
    book = input().rstrip()
    if book in books: # 딕셔너리에 키가 있다면 권수 +1
        books[book] += 1
    else:             # 딕셔너리에 키가 없다면 새로 추가
        books[book] = 1

max_freq = max(books.values()) # values()로 딕셔너리 내의 모든 값을 반환
                               # max()로 그 중 제일 큰 값을 max_freq에 저장

best_seller = []

for book, number in books.items(): # best_seller 리스트에 가장 많이 팔린 책 저장
    if number == max_freq:
        best_seller.append(book)

print(sorted(best_seller)[0]) # 사전 순으로 가장 앞서는 제목을 출력