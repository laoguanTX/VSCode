def fahrenheit_to_celsius(f):
    return 5 * (f - 32) / 9

def print_temperature_table(lower, upper):
    if lower > upper or lower < 0 or upper > 100:
        print("Invalid.")
        return
    
    print("fahr celsius")
    for f in range(lower, upper + 1, 2):
        c = fahrenheit_to_celsius(f)
        print(f"{f:d} {c:6.1f}")


try:
    lower, upper = map(int, input().split())
    print_temperature_table(lower, upper)
except ValueError:
    print("Invalid.")