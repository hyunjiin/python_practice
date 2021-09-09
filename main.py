
# a, b = map(int, input().split())
# for i in range(a, b):
#     if i % 5 == 0:
#         print('Fizz')
#     if i % 7 == 0:
#         print('Buzz')
#     if i % 35 == 0:
#         print('FizzBuzz')
#     else:
#         print(i)


a, b = map(int, input().split())
for i in range(a, b + 1):          # for i in range(횟수) 이므로 +1 까먹지 말 것
    if i % 35 == 0:                # 공배수 처리를 먼저 해줘야 공배수일 때 Fizz나 Buzz 출력안됨
        print('FizzBuzz')
    if i % 5 == 0:
        print('Fizz')
    if i % 7 == 0:
        print('Buzz')
    else:
        print(i)