n = int(input())

arr = list(map(int, (input().rstrip().split())  ))
arr = sorted(arr);
sock_set = set();

offset = 1;
arr_len = len(arr);
count = 0
i = 0;
while(i < n):
  arr.append(0);
  if arr[i] == arr[i + 1]:
    count = count + 1; 
    i = i + 2;
  else: 
    i = i + 1;


print(count)