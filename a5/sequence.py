# Array printing utility function. Feel free to use.
def printArr(arr, k):
  for i in range(k):
    print(str(arr[i]) + " "),
  print

def printSeqUtil(n, k, len1, arr):
## Your code - begin

#arr stores a part of sequence which is to be printed
#when the length of sequence is equal to k then that means that the sequence is now complete so we then print it.
    if (len1 == k): # it is a base condition to finally end the recursion
        printArr(arr, k);
        return;#as the sequence is now completed and printed we return to calling function or callee

# if len1 == 0 this means that there is no previous element in arr hence put "1".
# if len1 != 0, then start from the value which is greater than the value of previous element by 1.
    i = 1
    if(len1 != 0):
        i=arr[len1 - 1] + 1;

# if index is 0 then length of the sequence is 1
# when index is 1 that means that the length of the sequence is 2
# so len1 helps us to keep a track of index over which elements are to be inserted
    len1 += 1;

# Assigning or replacing numbers that are greater than the element before at new position.
    while (i <= n):# i(i.e. the number which is to be assigned) cannot be greater than n
        arr[len1 - 1] = i;
        printSeqUtil(n, k, len1, arr);
        i += 1;

## Your code - end

def printSeq(n, k):
    arr = [0] * k
    len1 = 0
    printSeqUtil(n, k, len1, arr)

if __name__ == "__main__":
  n = input("Enter n: ")
  k = input("Enter k: ")
  printSeq(n, k)
