pattern_size = int(input("Enter the size of the pattern:"))
i=0
while i< pattern_size+1:
  j=0
  while j< pattern_size+1:
    print("*", end="")
    j +=1
  print()
  i +=1
