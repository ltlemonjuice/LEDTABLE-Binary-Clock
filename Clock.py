#!/usr/bin/env python
#coding: utf8 
import time
import array
import fcntl
import sys
import math
import select
import os
# 
# Open SPI device
spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

#creating 10x10 matrix (last digit may be used later for alpha control)
matrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

cmatrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

			



#Define Functions for Allocation and Display
def allocate():
	#same as imgdisp.py, but with mirror so that 0/0 is at the upper left corner
	#Matrix is technically in reverse. X-Axis is horizontal, Y-Axis Vertical.11¦¦¦
	#print "Allocating..."
	for x in range(0,10):
		for y in range (0,10):
			cmatrix[x][y][0] = matrix[x][y][0] 
			cmatrix[x][y][1] = matrix[x][y][1] 
			cmatrix[x][y][2] = matrix[x][y][2]
			
			#Column 1
			col = 1
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 3
			col = 3
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 5
			col = 5
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
			
			#Column 7
			col = 7
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 9
			col = 9
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
	cmatrix.reverse()
				
def display():
	#allocating
	allocate()
	for x in range(0, 10):
		for y in range(0, 10):	
			rgb[0] = cmatrix[x][y][0]
			rgb[1] = cmatrix[x][y][1]
			rgb[2] = cmatrix[x][y][2]
			spidev.write(rgb)
								
	spidev.flush() 
	
def clear():
	for x in range(0,10):
		for y in range(0,10):
			matrix[x][y][0] = 0
			matrix[x][y][1] = 0
			matrix[x][y][2] = 0

def getClockFace():
	global current
	#falls stdin vorhanden wird es auf input gespeichert
	print sys.argv[:]
	if len(sys.argv) > 1:
		Input = sys.argv[1]
		if Input == "binClock":
			current = 0
		elif Input == "digClock":
			current = 1
		elif Input == "analogClock":
			current = 2
		elif Input == "scrollClock":
			current = 3
		print "Current Face: %s" % Input
	else:
		print("No arguments!")
		current = 0




#CLOCKS
def binClock():
	h= time.localtime(time.time()).tm_hour
	m = time.localtime(time.time()).tm_min
	#LED's to lit -> see picture
	h1 = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9]]
	h2 = [[1,0],[2,0],[1,1],[2,1],[1,2],[2,2],[1,3],[2,3],[1,4],[2,4]]
	h4 = [[1,5],[2,5],[1,6],[2,6],[1,7],[2,7],[1,8],[2,8],[1,9],[2,9]]
	h8 = [[3,8],[3,9],[4,8],[4,9],[5,7],[5,8],[5,9],[6,7],[6,8],[6,9]]

	m1 = [[9,0],[9,1],[9,2],[9,3],[9,4],[9,5],[9,6],[9,7],[9,8],[9,9]]
	m2 = [[7,0],[8,0],[7,1],[8,1],[7,2],[8,2],[7,3],[8,3],[7,4],[8,4]]
	m4 = [[7,5],[8,5],[7,6],[8,6],[7,7],[8,7],[7,8],[8,8],[7,9],[8,9]]
	m8 = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[6,0],[6,1]]
	m16 = [[3,3],[3,4],[4,3],[4,4],[5,2],[5,3],[5,4],[6,2],[6,3],[6,4]]
	m32 = [[3,5],[3,6],[3,7],[4,5],[4,6],[4,7],[5,5],[5,6],[6,5],[6,6]]

	#Combinations for every hour/minute
	hnums = [[h1],[h2],[h1,h2],[h4],[h1,h4],[h2,h4],[h1,h2,h4],[h8],[h1,h8],[h2,h8],
					[h1,h2,h8],[h4,h8]]
		
	mnums =  [[m1],[m2],[m1,m2],[m4],[m1,m4],[m2,m4],[m1,m2,m4],[m8],[m1,m8],[m2,m8],
			[m1,m2,m8],[m4,m8],[m1,m4,m8],[m2,m4,m8],[m1,m2,m4,m8],[m16],[m1,m16],[m2,m16],[m1,m2,m16],[m4,m16],
			[m1,m4,m16],[m2,m4,m16],[m1,m2,m4,m16],[m8,m16],[m1,m8,m16],[m2,m8,m16],[m1,m2,m8,m16],[m4,m8,m16],[m1,m4,m8,m16],[m2,m4,m8,m16],
			[m1,m2,m4,m8,m16],[m32],[m1,m32],[m2,m32],[m1,m2,m32],[m4,m32],[m1,m4,m32],[m2,m4,m32],[m1,m2,m4,m32],[m8,m32],
			[m1,m8,m32],[m2,m8,m32],[m1,m2,m8,m32],[m4,m8,m32],[m1,m4,m8,m32],[m2,m4,m8,m32],[m1,m2,m4,m8,m32],[m16,m32],[m1,m16,m32],[m2,m16,m32],
			[m1,m2,m16,m32],[m4,m16,m32],[m1,m4,m16,m32],[m2,m4,m16,m32],[m1,m2,m4,m16,m32],[m8,m16,m32],[m1,m8,m16,m32],[m2,m8,m16,m32],[m1,m2,m8,m16,m32]]
			

	def hour(time):
		if time == 0:
			time = 12
			
		nums = hnums[(time%12)-1]
		try:
			for i in range(0,3):
				for k in range(0,10):
					x = nums[i][k][0]
					y = nums[i][k][1]
					matrix[x][y][0] = 255
					matrix[x][y][1] = 0
					matrix[x][y][2] = 0
					
		except:
			pass


	def minute(time):
		if time != 0:
			nums = mnums[time-1]
			try:
				for i in range(0,5):
					for k in range(0,10):
						x = nums[i][k][0]
						y = nums[i][k][1]
						matrix[x][y][0] = 0
						matrix[x][y][1] = 0
						matrix[x][y][2] = 255
						
			except:
				pass
		else:
			pass
				
	#MAIN binClock
	hour(h)
	minute(m)

def digClock():
	
	def getPixels(number,x,y):
		dic = {"1":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"2":[[x+0,y+0],[x+0,y+2],[x+0,y+3],[x+0,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+4]],
				"3":[[x+0,y+0],[x+0,y+2],[x+0,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"4":[[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+1,y+2],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"5":[[x+2,y+0],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+4]],
				"6":[[x+2,y+0],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+3],[x+0,y+4]],
				"7":[[x+0,y+0],[x+1,y+0],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"8":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+3],[x+0,y+4]],
				"9":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+4]],
				"0":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+3],[x+0,y+4]],
				":":[[x+1,y+1],[x+1,y+3]],
				" ":[]

				}
		#print dic[str(number)]
		return dic[str(number)]

	
	def setMatrix(parts, color):
	
		for i in range(0, len(parts)):
			try:
				a = parts[i][0]
				b = parts[i][1]
				
				matrix[a][b][0] = color[0]
				matrix[a][b][1] = color[1]
				matrix[a][b][2] = color[2]
				#print("part %i done" % i)
			except:
				#print "not on matrix!"
				pass

	def makeClock():
		h = str(time.localtime(time.time()).tm_hour)
		m = str(time.localtime(time.time()).tm_min)
		sec = time.localtime(time.time()).tm_sec
		
		partsh = []
		partsm = []
		partss = []
		parts = []

		
		if len(h) == 1:
			h = "0" + h
			
		if len(m) == 1:
			m = "0" + m

		#print ("Time: %s:%s:%d" % (h,m,sec))

		partsh.extend(getPixels(h[0],0,0))
		partsh.extend(getPixels(h[1],4,0))
		partsm.extend(getPixels(m[0],3,5))
		partsm.extend(getPixels(m[1],7,5))

		if sec % 2 == 0:
			partss.extend(getPixels(":",0,5))
		else:
			partss.extend(getPixels(" ",0,5))
			
		clear()
		setMatrix(partsh,[255,0,0])
		setMatrix(partsm,[0,0,255])
		setMatrix(partss,[0,255,0])


	while True:
		clear()
		makeClock()
		display()

def analogClock():
	def getPixels(number,x,y):
		dic = {"1":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"2":[[x+0,y+0],[x+0,y+2],[x+0,y+3],[x+0,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+4]],
				"3":[[x+0,y+0],[x+0,y+2],[x+0,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"4":[[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+1,y+2],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"5":[[x+2,y+0],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+4]],
				"6":[[x+2,y+0],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+3],[x+0,y+4]],
				"7":[[x+0,y+0],[x+1,y+0],[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4]],
				"8":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+3],[x+0,y+4]],
				"9":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+2],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+4]],
				"0":[[x+2,y+0],[x+2,y+1],[x+2,y+2],[x+2,y+3],[x+2,y+4],[x+1,y+0],[x+1,y+4],[x+0,y+0],[x+0,y+1],[x+0,y+2],[x+0,y+3],[x+0,y+4]],
				":":[[x+1,y+1],[x+1,y+3]],
				" ":[],
				"h1":[[x+7,y+0],[x+8,y+0]],
				"h2":[[x+9,y+1],[x+9,y+2]],
				"h3":[[x+9,y+4],[x+9,y+5]],
				"h4":[[x+9,y+7],[x+9,y+8]],
				"h5":[[x+7,y+9],[x+8,y+9]],
				"h6":[[x+4,y+9],[x+5,y+9]],
				"h7":[[x+1,y+9],[x+2,y+9]],
				"h8":[[x+0,y+7],[x+0,y+8]],
				"h9":[[x+0,y+4],[x+0,y+5]],
				"h10":[[x+0,y+1],[x+0,y+2]],
				"h11":[[x+1,y+0],[x+2,y+0]],
				"h12":[[x+4,y+0],[x+5,y+0]],

				}
		#print dic[str(number)]
		return dic[str(number)]

	
	def setMatrix(parts, color):
	
		for i in range(0, len(parts)):
			try:
				a = parts[i][0]
				b = parts[i][1]
				
				matrix[a][b][0] = color[0]
				matrix[a][b][1] = color[1]
				matrix[a][b][2] = color[2]
				#print("part %i done" % i)
			except:
				#print "not on matrix!"
				pass

	def makeClock():
		h = str(time.localtime(time.time()).tm_hour % 12)
		m = str(time.localtime(time.time()).tm_min)
		sec = time.localtime(time.time()).tm_sec
		
		partsh = []
		partsm = []
		
		if h == "0":
			h = "12"
		if len(m) == 1:
			m = "0" + m

		#print ("Time: %s:%s:%d" % (h,m,sec))
		for i in range(1,13):
			if i == int(h):
				pass
			else:
				partsh.extend(getPixels(("h%d" %i),0,0))
		
		partsm.extend(getPixels(m[0],2,2))
		partsm.extend(getPixels(m[1],5,3))

		if sec % 2 == 0:
			partsh.extend(getPixels("h%s" %h,0,0))
		else:
			partsh.extend(getPixels(" ",0,0))
			
		clear()
		setMatrix(partsh,[255,0,0])
		setMatrix(partsm,[0,0,255])
		


	while True:
		clear()
		makeClock()
		display()	
	
	#Numbers

def scrollClock():
	h= str(time.localtime(time.time()).tm_hour)
	m = str(time.localtime(time.time()).tm_min)

	if len(h) == 1:
		h = "0" + h
			
	if len(m) == 1:
		m = "0" + m

	os.system("python /home/pi/led/progs10/scrollText.py %s:%s 0.1 [0,0,255] 1" % (h, m) )



#MAIN
h= time.localtime(time.time()).tm_hour
m = time.localtime(time.time()).tm_min

 #0 = Binary, 1 = Digital, 2 = Analog, 3 = Scroll 		


clear()
getClockFace()
if current == 0:
	print ("Binary Clock selected")
	while True:
		binClock()
		display()
elif current == 1:
	print ("Digital Clock selected")
	digClock()
elif current == 2:
	print ("Analog Clock selected")
	analogClock()
elif current == 3:
	print ("Scrolling Clock selected")
	while True:
		scrollClock()


	
