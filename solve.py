from PIL import Image
import MazeCR
import BFS
import time
Image.MAX_IMAGE_PIXELS = None

def main():
	#load image
	print("Loading Image ...")
	im = Image.open("1.png")
	
	# creating maze
	t0 = time.time()
	print("creating maze ...")

	maze = MazeCR.Maze(im)
	
	print("Maze created ...")
	t1 = time.time()
	
	print("Time elapsed : ",(t1-t0))
	
	path = BFS.solve(maze)
	
	print("Saving Image ...")
	im = im.convert('RGB')
	impixels = im.load()
	length = len(path)
	
	for i in range(0,length-1):
		a = path[i]
		b = path[i+1]
		
		r = int((i / length) * 255)
		#print(r)
		px = (255-r,0,r)
		if a[0] == b[0]:
			for x in range(min(a[1],b[1]), max(a[1],b[1])):
				impixels[x,a[0]] = px
		elif a[1] == b[1]:
			for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
				impixels[a[1],y] = px

	im.save("ans.png")
	im.show()
		

main()
