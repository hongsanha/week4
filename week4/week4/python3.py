empty_list=[]
while True:
    answer=input("Enter anything: ")
    if answer == "q":
        break
    else:
        empty_list.append(answer)
print(empty_list)