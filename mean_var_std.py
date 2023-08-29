import numpy as np

def calculate(list):
    matrix = np.array(list).reshape(3,3)
    
    mean = []
    variance = []
    standard_deviation = []
    minimum = []
    maximum = []
    list_sum = []

    for ax in range(2):
        avg, var, stdev, minim, maxim, sum_list = matrix.mean(axis=ax).tolist(), matrix.var(axis=ax).tolist(), matrix.std(axis=ax).tolist(), matrix.min(axis=ax).tolist(), matrix.max(axis=ax).tolist(), matrix.sum(axis=ax).tolist()
        mean.append(avg)
        variance.append(var)
        standard_deviation.append(stdev)
        minimum.append(minim)
        maximum.append(maxim)
        list_sum.append(sum_list)

    mean.append(np.mean(list))
    variance.append(np.var(list))
    standard_deviation.append(np.std(list))
    minimum.append(min(list))
    maximum.append(max(list))
    list_sum.append(sum(list))

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': maximum,
        'min': minimum,
        'sum': list_sum
    }

    return calculations

print(calculate([2,6,2,8,4,0,1,5,7]))