import math
nums = list(map(int,input('range of input:').split()))

for i in range(nums[0],nums[1]+1):
    # 通過兩點之座標資訊區
    a1 = 474721             # 701.3^2 (二次項)
    a2 = 491821.69          # 689^2   (二次項)
    b1 = 689
    b2 = 701.3
    c1 = 317.3 - i
    c2 = 305 - i

    # 拋物線聯立方程式 => c1 = x_2(a1) + x_1(b1) /// c2 = x_2(a2) + x_1(b2)
    
    # 係數計算區
    x_2 = (c2*b1 - c1*b2)/(a2*b1 - a1*b2)
    x_1 = (a1*c2 - a2*c1)/(b2*a1 - a2*b1)
    
    print('height:%d  x^2係數:%f  x係數:%f'%(i,x_2,x_1),end='  ')
    
    angle = math.degrees(math.atan(x_1))
    print('射出角度:%f'%angle,end='  ')

    g = 980.665
    cos_angle = math.cos(math.radians(angle))
    speed = math.sqrt(g/((-2)*x_2*(cos_angle**2)))/100
    print('初速:%f m/s'%speed)
