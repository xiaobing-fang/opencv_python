import cv2
import numpy as np
'''
x = np.uint8([240])
y = np.uint8([38])
res = x+y
res_1 = cv2.add(x,y)
print(res,'\n',res_1)

#[22] 
# [[255]]
可以看到Opencv中的加法，溢出后取的是饱和值也就是最大范围值，而numpy中加法饱和后重新计数（模操作），所以一般用Opencv的加法比较好。
'''


