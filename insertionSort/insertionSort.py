from typing import List
class InsertionSort:
    def sort(self, arr:List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key = arr[i]
            j= i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = key
                
            
        return arr
        


if __name__ == "__main__":
    a = InsertionSort().sort([11, 500, 9,6,8,5,3,1,2,4,7])
    print(a)