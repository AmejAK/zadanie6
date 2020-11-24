import copy
di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
di_kopia = copy.deepcopy(di)
print(di)
print(di_kopia)
di['four'][0] = 'cztery'
print(di)
print(di_kopia)