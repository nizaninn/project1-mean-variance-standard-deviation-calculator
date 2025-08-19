import numpy as np

def calculate(lst):
 if len(lst) !=9:
  raise ValueError("The list must contain 9 items")

 arr=np.array(lst).reshape(3, 3)

 def get_stats(func):
        return [func(arr, axis=0).tolist(), func(arr, axis=1).tolist(), func(arr).item()]

 return {
 'mean': get_stats(np.mean),
 'variance': get_stats(np.var),
 'standard deviation': get_stats(np.std),
 'max': get_stats(np.max),
 'min': get_stats(np.min),
 'sum': get_stats(np.sum)
}