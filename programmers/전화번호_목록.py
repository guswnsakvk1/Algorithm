def solution(phone_book):
    # phone_book.sort()
    # for i in range(len(phone_book)-1):
    #     if len(phone_book[i]) < len(phone_book[i+1]):
    #         if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
    #             return False

    # return True

    hashMap = {}
    for number in phone_book:
        hashMap[number] = 1
    
    for number in phone_book:
        prefix = ""
        for pre in number:
            prefix += pre
            if prefix in hashMap and prefix != number:
                return False
    
    return True