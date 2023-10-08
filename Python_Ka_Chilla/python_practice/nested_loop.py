#nested loops

colors = ['red', 'green','blue']
items = ['book', 'pen', 'copy']

for color in colors:
    for item in items:
        #  print(color, item)
         print( item, color)


# i = 0
# while i <= 5:
#      j = 101
#      while j <= 105:
#         #  print(i, j)
#          print(j, i)
         
#          j += 1
#      i += 1


i = 1

while i< 4:
     for j in range(3):
            print(i, j)
     i += 1

# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# 3 0

#while loop inside for loop

# for i in range(4):
#      while i < 4:
#           print(i)
#           i += 1
