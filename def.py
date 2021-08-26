def hi():
    print("こんにちは")
hi()

def posi_nega_zero(val):
    if val>0:
        print(val,"は正の数です")
    elif val>0:
        print(val,"は負の数です")
    else:
        print(val,"は０です")
posi_nega_zero(0.8)
posi_nega_zero(-5)

def volume_sphere(r):
    v = 3.14*r*r*r/3
    return v
vs=volume_sphere(10)
print("半径10cmの球は",vs,"cm3")
print("半径20cmの球は",volume_sphere(20),"cm3")
total=0
def test_func():
    loops = 20
    global total
    for i in range(loops):
        total +=10

print("totalの初期値",total)
test_func()
print("関数実行後のtotalの値",total)
