import sys
def judge(s):
    if s=="":
        sys.exit()

def gregorian(y1,y2,m,d):
    h=(d+(26*(m+1))/10+y1+y1/4-2*(y2/100)+y2/400)%7
    return h

h = {1:"日",2:"月",3:"火",4:"水",5:"木",6:"金",0:"土"}
y=input("あなたの誕生年を西暦で入力してください：")
judge(y)
y=int(y)
if y <1900:
    print("長生きすぎます")
    sys.exit()

elif y >2022:
    print("産まれていません")
    sys.exit()
    
y_1 = y/100
y_2 = y%100
m=input("あなたの誕生月を入力してください：")
judge(m)
m=int(m)
if m <1 or m>12:
    print("入力が不適切です")
    sys.exit()
d=input("あなたの生まれた日を入力してください：")
judge(d)
d=int(d)
if d <1 or d >31:
    print("入力が不適切です")
    sys.exit()
judge = int(gregorian(y_1,y_2,m,d))
if judge in h:
    day = h[judge]
s=str(y) + "年"+ str(m) + "月"+ str(d) +"日は"+day+"曜日です。"
print(s)



        
