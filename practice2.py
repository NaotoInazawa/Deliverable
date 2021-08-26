def ruijou_2(n):
    return 2**n

def ruijou_3(n):
    return 3**n

for i in range(1,6):
    print("3の{}乗と2の{}乗の差は{}です。".format(i,i,3**i-2**i))
