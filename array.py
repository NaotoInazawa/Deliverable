subject = ["国語","数学","英語","理科","社会"]
score = [80,100,92,96,74]
total = 0
for i in range(5):
    print(subject[i],"の点数は",score[i])
    total += score[i]
print("合計点は",total)

data =[
    [10,20,30,40,50],
    [-1,-2,-3,-4,-5],
    [55,66,77,88,99]
    ]
print(data[0][0])
print(data[2][2])
print(data[2][4])
