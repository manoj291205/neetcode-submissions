class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        for i in nums:
            count[i]=count.get(i,0)+1

        sorted_count=sorted(count.items(),key=lambda x:x[1],reverse=True)

        res=[]

        for i,freq in sorted_count[:k]:
            res.append(i)

        return res

        