class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output=[]
        table = {}
       
        for num in nums:
            if num not in table.keys():
                #hashed_num = hash(num)
                table[num] = 1
                #print(table[hashed_num], hashed_num)
            
            elif num in table.keys():
                #hashed_num = hash(num)
                table[num] += 1
                #print(table[hashed_num], hashed_num)
        
        #k-frequent
        val_list = list(table.items())
        val_list.sort(reverse=True,key=lambda x: x[1])
        print(val_list)
        for i in range(k):
            output.append(val_list[i][0])
        return output
        












        '''
        num_count = []
        num_ids = []
        for num in nums:
            if num not in num_ids:
                num_ids.append(num)
                num_count.append(0)     #initialize count
            elif num in num_ids:
                num_index = num_ids.index(num)
                num_count[num_index] += 1
        
        #k-frequent
        if len(num_ids) == 0:   #edge cases
            return 0
        elif len(num_ids) == 1: #edge case
            return num_ids[0]
        else:
        '''
