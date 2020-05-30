#!/usr/bin/python
# -*- coding: UTF-8 -*-

#只需要生成4个随机数，范围为[0,360],这4个随机数的最大减去最小，θ<x1<x2<x3<x4<θ+180即为在同一个半圆内
#最大的x4-最小的x1<180
#第一个参数是几个点；第二个参数是实验几次

from __future__ import division
import sys
import random


count = 0
print(sys.argv[2])
for i in range(int(sys.argv[2])):
	l = []
	for node in range(int(sys.argv[1])):
		l.append(random.uniform(0,360))		
	#maxx = max(x1,x2,x3,x4)
	#minx = min(x1,x2,x3,x4)
	l.sort()
	
	if(l[-1] - l[0] < 180):
		count = count + 1
	else:
		for i in range(1,int(sys.argv[1])):
			if(l[i]-l[i-1])>180:
				count = count+1

total = int(sys.argv[2])
#print type(total)
print("The probability is:")
print(count/total)

	

