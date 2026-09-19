class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l=0
        r=len(numbers)-1

        while l<r:
            Cursum=numbers[l]+numbers[r]

            if Cursum > target: 
                r-=1
            elif Cursum < target:
                l+=1
            else:
                return [l+1,r+1]  
        return []       