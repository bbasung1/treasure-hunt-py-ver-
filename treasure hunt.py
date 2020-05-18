import random
x,y=0,0
a=int(input("범위를 지정하세요"))
b=random.randint(0, a)
c=random.randint(0, a)
e=input("힌트 기능을 사용하겠습니까?")
if(e=='y'):
    e=1

while True:
    d=input("wasd중 하나를 입력하세요")
    if(d=='w'):
        y=y+1
    elif(d=='a'):
        y=y-1
    elif(d=='d'):
        x=x+1
    elif(d=='a'):
        x=x-1
    else:
        print("잘못된 입력입니다.")
    if(y>a or y<0):
        print("벽에 막혔습니다. y를 0으로 초기화 합니다.")
        y=0
    if(x>a or x<0):
        print("벽에 막혔습니다. x를 0으로 초기화 합니다.")
        x=0
    print("x좌표:",x,"y좌표",y)
    if(e==1):
        if(x==b):
            print("x좌표는 맞췄습니다.")
        if(y==c):
            print("y좌표는 맞췄습니다.")
    if(x==b and y==c):
        print("맞췄습니다!")
        break
    