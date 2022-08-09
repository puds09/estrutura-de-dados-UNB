# I won't use this variable, but i need to create it because was ordered
n = int(input())
clothes = input().split()

# duplicated = [clothe for i, clothe in enumerate(clothes) if i != clothes.index(clothe)]
duplicated = []
# just another way to do the same as older commit
for i, clothe in enumerate(clothes):
    if(i != clothes.index(clothe)): duplicated.append(clothe)
print(len(duplicated))