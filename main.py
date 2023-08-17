

Telephone_book = {'Amal': 1111111111, 'Mohammed': 2222222222, 'Khadijah': 3333333333,
                  'Abdullah': 4444444444, 'Rawan': 5555555555, 'Faisal': 6666666666, 'Layla': 7777777777}
oj = int(input('Enter the number : '))

phone_belong_to = None
for k, v in Telephone_book.items():
    if v == oj:
        print('this phone number', v, 'belong to ', k,)
        phone_belong_to = k
        break
if phone_belong_to is None:
    print('Sorry, the number is not found !')


print('Thank You !')