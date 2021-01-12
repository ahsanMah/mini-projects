# 1. Line fitting 
#    arr = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6]]
# 2. Line fitting with noise
#    arr = [[0.1, 0.9], [1.1, 2.1], [2.1, 2.95], [3.05, 4.1], [5.05, 5.95]]
# 3. Line fitting with more data points + outliers
#    arr = [[0.1, 0.9], [1.1, 2.1], [2.1, 2.95], [3.05, 4.1], [-1, 9], [5.05, 5.95], [4, 2]]

def findLine(arr):
  
  x,y = arr[0]
  x1,y1 = arr[1]
  
  m = (y1-y)/(x1-x)
  b = y1-m*x1
  
  return m,b

arr = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6]]

assert findLine(arr) == (1,1)
 
def findBestLine(arr):
  
  m,b = 0,0
  n = len(arr)
  
  for i in range(n-1):
    m_, b_ = findLine(arr[i:i+2])
    m += m_
    b += b_
  
  m /= (n-1)
  b /= (n-1)
  
  return m,b

arr1 = [[0.1, 0.9], [1.1, 2.1], [2.1, 2.95], [3.05, 4.1], [5.05, 5.95]]
# print(findBestLine(arr1))

def findBetterLine(arr):
  
  ms, bs = [], []
  n = len(arr)
  lines = [0] * (n-1)
  best_i = 0
  eps = 0.1
  
  for i in range(n-1):
    m_, b_ = findLine(arr[i:i+2])
    ms.append(m_)
    bs.append(b_)
  
  for i, (m,b) in enumerate(zip(ms, bs)):
    print(m,b)
    
    #Calculate inliers
    for x,y in arr:
      y_est = m*x + b
      
      if abs(y-y_est) < eps:
        lines[i] += 1
    
    if lines[i] > lines[best_i]:
      best_i = i
  
  return ms[best_i], bs[best_i]
 

arr2 = [[0.1, 0.9], [1.1, 2.1], [2.1, 2.95], [3.05, 4.1], [-1, 9], [5.05, 5.95], [4, 2]]  
print(findBetterLine(arr2))
