i = list("_________")
print("---------")
print(f"| {i[0]} {i[1]} {i[2]} |")
print(f"| {i[3]} {i[4]} {i[5]} |")
print(f"| {i[6]} {i[7]} {i[8]} |")
print("---------")
m = 0
while m < 9:
    k = input("Enter coordinates:").split()
    if k[0].isnumeric():
        coordinates = 8 + int(k[0]) - 3 * int(k[1])
        if coordinates >= 0 and coordinates <= 8:
            if i[coordinates] == "_":
                if m % 2 == 0:
                    i[coordinates]  = "X"
                    print("---------")
                    print(f"| {i[0]} {i[1]} {i[2]} |")
                    print(f"| {i[3]} {i[4]} {i[5]} |")
                    print(f"| {i[6]} {i[7]} {i[8]} |")
                    print("---------")
                    m += 1
                else:
                    i[coordinates] = "O"
                    print("---------")
                    print(f"| {i[0]} {i[1]} {i[2]} |")
                    print(f"| {i[3]} {i[4]} {i[5]} |")
                    print(f"| {i[6]} {i[7]} {i[8]} |")
                    print("---------")
                    m += 1
                if i[0] == i[1] == i[2] == "X" or i[3] == i[4] == i[5] == "X" or i[6] == i[7] == i[8] == "X":
                    print("X wins")
                    break
                elif i[0] == i[1] == i[2] == "O" or i[3] == i[4] == i[5] == "O" or i[6] == i[7] == i[8] == "O":
                    print("O wins")
                    break
                elif i[0] == i[4] == i[8] == "O" or i[6] == i[4] == i[2] == "O":
                    print("O wins")
                    break
                elif i[0] == i[4] == i[8] == "X" or i[6] == i[4] == i[2] == "X":
                    print("X wins")
                    break
                elif i[0] == i[3] == i[6] == "X" or i[1] == i[4] == i[7] == "X" or i[2] == i[5] == i[8] == "X":
                    print("X wins")
                    break
                elif i[0] == i[3] == i[6] == "O" or i[1] == i[4] == i[7] == "O" or i[2] == i[5] == i[8] == "O":
                    print("O wins")
                    break
                elif "_" not in i:
                    print("Draw")
                    break
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
