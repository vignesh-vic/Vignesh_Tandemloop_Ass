def generate_series(a):
    result = []
    r = a if a % 2 != 0 else a - 1

    for i in range(r):
        odd_number = 2 * i + 1
        result.append(odd_number)
    print(",".join(map(str,result)))


a = int(input("enter number "))
generate_series(a)
