lst = []
with open("raw-data.txt") as f:
  for line in f:
    lst.append(str(line).strip())


lst_name = lst[::2]
lst_country = lst[1::2] 

print(lst_name)
print(lst_country)

