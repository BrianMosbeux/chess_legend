#compute the number of wheat grain on each square of the board using for loop
x = 1
total = 1
for i in range(1,65):
    print(f"{i}a casilla = {x:,} granos de arroz")
    x += x
    total += x

total = total-x
print(f"TOTAL ARROZ = {total:,}")

print(x**(1/64))
print(f"{2**64:,}")
grain_per_kg = 30000
print(f"{total/(grain_per_kg*1000):,} T")

#compute the number of wheat grain on each square of the board using regression
def chess_story(x):
    if x == 1:
        return 1
    else:
        return 2 * chess_story(x-1)

print(f"board = {chess_story(64):,}")
