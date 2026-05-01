class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output=[]
        table = {}
       
        for num in nums:
            if num not in table.keys():
                table[num] = 1
            
            elif num in table.keys():
                table[num] += 1
        
        #k-frequent
        val_list = list(table.items())
        val_list.sort(reverse=True,key=lambda x: x[1])
        print(val_list)
        for i in range(k):
            output.append(val_list[i][0])
        return output
