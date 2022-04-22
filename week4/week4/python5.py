import random
import time

def recommend_menu():
    print("5개의 메뉴를 추천해 주세요! 5개가 입력되면 오늘의 메뉴를 추천해 드려요.")
    print("동일한 메뉴는 안 돼요!")
    menu_count=0
    menu_list=[]
    while True:
        menu=input("메뉴 추가: ")
        if menu in menu_list:
            print("이미 있는 메뉴에요! 다른 메뉴를 선택해주세요!")
            print(f"현재 메뉴 수 = {len(menu_list)}")

        else:
            menu_list.append(menu)
            menu_count+=1
            print(f"현재 메뉴 수 = {len(menu_list)}")
            print("\n")
        if menu_count==5:
            break
    for i in range(3):
        print(3-i)
        time.sleep(1)
    print("\n")
    print(menu_list)
    print("과연 오늘의 메뉴는?")
    print("\n")

    for i in range(3):
        print(3-i)
        time.sleep(1)
    print("\n")
    choice=random.choice(menu_list)
    print(f"오늘의 메뉴는 {menu_list.index(choice)+1}번째 메뉴, {choice}입니다.)")        
    
recommend_menu()