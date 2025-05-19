def multiples(inputs):
    divisors = range(1, 10) 
    result = {}
    for d in divisors:
        count = 0
        for n in inputs:
            if n%d == 0:
                count+= 1
        result[d]=count

    return result

inputs = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = multiples(inputs)
print(output)
