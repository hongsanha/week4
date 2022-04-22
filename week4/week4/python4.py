dic={}
while True:
    fruit_name=input("Enter a fruit type (q to quit): ")
    if fruit_name=="q":
        break
    fruit_weight=input("Enter the weight in kg: ")
    dic[fruit_name]=fruit_weight
print(dic)