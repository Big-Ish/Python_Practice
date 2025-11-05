geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
birds = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

def goose_filter(birds):
    filtered = []
    for b in birds:
        if b not in geese:
            filtered.append(b)
    return filtered

print(goose_filter(birds))
print(birds)