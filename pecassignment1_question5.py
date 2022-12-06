import math
print('''The sine and cosine of the angles are as follows respectively''')
for i in  range(0,360,15):

#values of angles in sine and cosine respectively


    print(f"{i}  = {round(math.sin(math.radians(i)),4) }  , {round(math.cos(math.radians(i)),4)}")
