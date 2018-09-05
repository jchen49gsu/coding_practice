class Solution(object):
	def roverMove(self,size,cmds):
		start = [0,0]

		for cmd in cmds:
			if cmd == 'RIGHT' and start[1] <size-1:
				start[1]+=1
				print start
			elif cmd == "LEFT" and start[1] >0:
				start[1]-=1
				print start
			elif cmd == "UP" and start[0] >0:
				start[0]-=1
				print start
			elif cmd == "DOWN" and start[0] < size-1:
				start[0]+=1
				print start
		print start
		return start[1] + start[0] * size
		

s = Solution()
cmds1 = "RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"
cmds2 = "RIGHT", "UP", "DOWN", "LEFT", "LEFT", "DOWN", "DOWN"
print s.roverMove(4,cmds1)
print s.roverMove(4,cmds2)
