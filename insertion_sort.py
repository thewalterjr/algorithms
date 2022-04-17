def insertion_sort(arr):
  for index in range(1, len(arr)):
    j = index
    while arr[j-1] > arr[j] and j > 0:
      aux = arr[j-1]
      arr[j-1] = arr[j]
      arr[j] = aux

      j -= 1
      

arr = [2, 8, 7, 5, 6, 1, 4, 3]
insertion_sort(arr)
print(arr)
