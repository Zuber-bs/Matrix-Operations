matrix1 = [[1, 2, 3],
           [4, 3, 7],]

matrix2 = [[6, 8], 
           [3, 2],
           [4, 6]]

def addMatrix():
  result = []
  for i in range(2):
    for j in range(3):
      result.append(matrix1[i][j] + matrix2[i][j])
  return result

def subtractMatrix():
  result = []
  for i in range(2):
    for j in range(3):
      result.append(matrix1[i][j] - matrix2[i][j])
  return result

def multiplyMatrix():
  result = []
  for i in range(2):
    for j in range(3):
      row1 = matrix1[0][j]
      row2 = matrix1[1][j]

  for i in range(3):
    column1 = matrix2[i][0]
    column2 = matrix2[i][1]

  result.append(row1*column1)
  result.append(row2*column2)

  return result


# print(addMatrix())
# print(subtractMatrix())
print(multiplyMatrix())
