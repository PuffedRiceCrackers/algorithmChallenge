# 이거 원래 hash 인데 아무도 hash 로 안 풂

def solution(phone_book):
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        prefix = phone_book[i]
        prefixIdx = len(phone_book[i])
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][:prefixIdx] == prefix:
                return False
    return True

phone_book = ['12','234','345']
print(solution(phone_book))