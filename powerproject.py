v = float(input("what is the voltage? "))
i = float(input("what is the current? "))
p = round(v * i, 2)
if p >= 5000:
    print(f"Danger! High power!: ")
else:
    print("power is", p, "watts")