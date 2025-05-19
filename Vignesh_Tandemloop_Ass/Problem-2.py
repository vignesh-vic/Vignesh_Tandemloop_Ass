def generate_series(a):
    result = []
    for i in range(0,a):
        odd_number = 2 * i + 1
        result.append(odd_number)
    print(",".join(map(str,result)))


a = int(input("enter number "))
generate_series(a)
