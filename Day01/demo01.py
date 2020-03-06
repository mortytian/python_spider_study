import  random
'''
模拟剪刀石头布 0 剪刀 1 石头 2布
'''
computer = random.randint(0,2)
player = input()
player = int(player)

if player == computer:
    print('平局')

if player == 0:
    if computer == 1:
        print('computer win')

    else:
        print('player win')

elif player == 1:
    if computer == 2:
        print('computer win')

    else:
        print('player win')

elif player == 2:
    if computer == 0:
        print('computer win')

    else:
        print('player win')

print('player= ' + str(player))
print('computer = ' +str(computer))


# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i*j,end = '\t')
    print()


