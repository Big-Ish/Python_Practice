row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("\nWhere do you want to put the treasure?\n")
coord = [*position]

if coord[1] == "1" and coord[0] == "1":
    row1 = ["X", "️⬜️", "️⬜️"]
if coord[1] == "1" and coord[0] == "2":
    row1 = ["⬜️", "X", "️⬜️"]
if coord[1] == "1" and coord[0] == "3":
    row1 = ["⬜️", "️⬜️", "X"]


if coord[1] == "2" and coord[0] == "1":
    row2 = ["X", "⬜️", "️⬜️"]
if coord[1] == "2" and coord[0] == "2":
    row2 = ["⬜️", "X", "️⬜️"]
if coord[1] == "2" and coord[0] == "3":
    row2 = ["⬜️", "⬜️", "X"]


if coord[1] == "3" and coord[0] == "1":
    row3 = ["X", "⬜️️", "⬜️️"]
if coord[1] == "3" and coord[0] == "2":
    row3 = ["⬜️️", "X", "⬜️️"]
if coord[1] == "3" and coord[0] == "3":
    row3 = ["⬜️️", "⬜️️", "X"]

print(f"{row1}\n{row2}\n{row3}")
