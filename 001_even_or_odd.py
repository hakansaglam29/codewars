def even_or_odd(number):
    if number % 2 == 1:
        return "Odd"
    else:
        return "Even"
print(even_or_odd(int(input("Please enter a number: "))))

# def even_or_odd(number):
#   return ["Even", "Odd"][number % 2] 