class Maze:
	def __init__(self,im):
		width = im.size[0]
		height = im.size[1]
		data = list(im.getdata(0))

		self.start = [0,0]
		self.end = [height-1,0]
		
		self.mat = []

		
		#start
		for x in range(0,width):
			if data[x] > 0:
				self.start[1] = x
				break
		
	
		f = 0;
				
		for x in range(0,height):
			rowoffset = x * width
			lst = []
			for y in range(0,width):
				
				if data[rowoffset+y] > 0:
					lst.append(1)
				else :
					lst.append(0)
			self.mat.append(lst)
			
			
			
				
				
		
		#end
	
		off = (height-1)*width
		for x in range(0,width):
			if data[x+off] > 0:
				self.end[1] = x
				break
		#print(self.start,self.end)
		
		
			
