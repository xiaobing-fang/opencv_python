import cv2
'''
网址： https://www.pianshen.com/article/7034104097/
目的;把logo添上到fisherman上 
思路：1 将logo 灰度化————>二值化 有logo的像素位置黑色，没logo的为白色
     2 二值化后的logo 和 fisherman相应位置 进行and 位运算 得到前景
     3 反转二值化后的logo 将其和 logo原图像作 and位运算 得到背景
     4 前景+背景————》赋值到fisherman相应位置

cv2.bitwise_and   cv2.bitwise_or  cv2.bitwise_not cv2.bitwise_xor
cv2.bitwise_and(InputArray src1, InputArray src2, InputArray mask=noArray());//dst = src1 & src2
四种计算后面都有一个mask参数，当mask参数 = Mat（）时，不参加运算；否则输入图像完成按位运算后与之进行运算得到输出图像
利用掩膜（mask）进行“与”操作，即掩膜图像白色区域是对需要处理图像像素的保留，黑色区域是对需要处理图像像素的剔除，其余按位操作原理类似只是效果不同而已。
下面介绍下mask作用：
图像掩膜用选定的图像、图形或物体，对处理的图像（全部或局部）进行遮挡，来控制图像处理的区域或处理过程。
数字图像处理中,掩模为二维矩阵数组,有时也用多值图像，图像掩模主要用于：
①提取感兴趣区,用预先制作的感兴趣区掩模与待处理图像相乘,得到感兴趣区图像,感兴趣区内图像值保持不变,而区外图像值都为0。
②屏蔽作用,用掩模对图像上某些区域作屏蔽,使其不参加处理或不参加处理参数的计算,或仅对屏蔽区作处理或统计。
③结构特征提取,用相似性变量或图像匹配方法检测和提取图像中与掩模相似的结构特征。
④特殊形状图像的制作。
在所有图像基本运算的操作函数中，凡是带有掩膜（mask）的处理函数，其掩膜都参与运算（输入图像运算完之后再与掩膜图像或矩阵运算）。
如果一个给定的像素的值大于零，那么这个像素会被打开，如果它的值为零，它就会被关闭。按位功能在这些二进制条件下运行。

 AND：当且仅当两个像素都大于零时，按位AND才为真，相与取较大值为结果
 OR：如果两个像素中的任何一个大于零，则按位“或”为真，相或取较小值为结果
 XOR 异或功能：当且仅当两个像素转化为二进制进行异或计算
 NOT 取反：倒置图像中的“开”和“关”像素。
————————————————
版权声明：本文为CSDN博主「zhouzongzong」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zhouzongzong/java/article/details/93028651
'''


img1 = cv2.imread('opencvlogo.jpg')
img2 = cv2.imread('fisherman.jpg')

rows,cols,channels = img1.shape  #获取img1的行和列、通道数
roi = img2[0:rows,0:cols]   #ROI 是彩图 没有转成灰度图

img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)  #将img1 ——>灰度图  像素0——>255
ret,mask = cv2.threshold(img1_gray,170,255,cv2.THRESH_BINARY)  # ret：True或False，代表有没有读到图片； dst： 目标图像
'''
cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst  
• src：表示的是图片源
• thresh：表示的是阈值（起始值）
• maxval：表示的是最大值
• type：表示的是这里划分的时候使用的是什么类型的算法**，常用值为0（cv2.THRESH_BINARY）**

• cv2.THRESH_BINARY（黑白二值） 像素大于阈值归最大  其余归0
• cv2.THRESH_BINARY_INV（黑白二值反转） 是上面这个函数的反转
• cv2.THRESH_TRUNC （得到的图像为多像素值） 像素大于阈值归阈值  否则不变
• cv2.THRESH_TOZERO    像素大于阈值归像素 其余归0
• cv2.THRESH_TOZERO_INV   是上面函数的反转
'''

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
img1_fg = cv2.bitwise_and(img1,img1,mask = mask_inv)

dst = cv2.add(img1_fg,img1_bg)

img2[0:rows,0:cols] = dst
'''
cv2.imshow('img1g',img1_gray)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_fg',img1_fg)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('dst',dst)
 
'''

'''
cv2.imwrite('img1_gray.jpg',img1_gray)
cv2.imwrite('mask.jpg',mask)
cv2.imwrite('mask_inv.jpg',mask_inv)
cv2.imwrite('img1_fg.jpg',img1_fg)
cv2.imwrite('img1_bg.jpg',img1_bg)
cv2.imwrite('dst.jpg',dst)
cv2.imwrite('das.jpg',img2)
cv2.imwrite('roi.jpg',roi)
'''

cv2.imshow('das',img2)
#cv2.imshow('res',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()