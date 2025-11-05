numbers = [2,2,3,4,5]

def remove_smallest(numbers):
    new = []
    if len(numbers) == 0:
        return new
    else:
        for i in numbers: # new list
            new.append(i)
        for i in new:   # remove the min for the new list
            if i == min(new):
                new.remove(i)
                return new

print(remove_smallest(numbers))