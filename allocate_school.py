class Solution:
	def allocate_school(sel,schoolSeatsArray,studentScoreArray,studentSchoolPreArray):

		studentScoreSortedArray = [[i,studentScoreArray[i]] for i in xrange(len(studentScoreArray))]
		studentScoreSortedArray.sort(key=lambda x:x[1], reverse = True)

		numOfStudent = 0
		numOfSeat=0

		for student_id, student_score in studentScoreSortedArray:
			allocated = False
			for school_id in studentSchoolPreArray[student_id]:
				if schoolSeatsArray[school_id] > 0:
					schoolSeatsArray[school_id] -=1
					allocated = True
					break
			if not allocated:
				numOfStudent+=1


		numOfSeat = sum(schoolSeatsArray)
		return [numOfSeat,numOfStudent]







s = Solution()
schoolSeatsArray = [1,3,1,2]
studentScoreArray = [990,780,830,860,920]
studentSchoolPreArray =[[3,2,1],[3,0,0],[2,0,1],[0,1,3],[0,2,3]]
print s.allocate_school(schoolSeatsArray,studentScoreArray,studentSchoolPreArray)
