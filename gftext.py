print('女友問："想吃什麼?"')    
print() 
count = 0  
no = 0
while True:
    gf = input("火鍋要不要?\n").strip()  
    print() 
    if gf =="要" or "好" in gf or "可以"in gf:
        print("出發吃飯囉~")
        input("按 Enter 結束!")
        break
        
        
    elif "不要" in gf or "熱" in gf:   
        no += 1
        if not "不要" in gf or "熱" in gf: 
            count += 1 
            
        if no == 1:
            input("燒烤要不要?\n")
            no += 1
            
        if no == 2:
            print()
            input("鐵板燒要不要?\n")
            no += 1  
            
        if  no >=3:
            print()
            print("問了3次，什麼都不要，那去吃大便好了!^_^\n")
            print()  
            input("按 Enter 結束 ! 作者無法保證使用者人身安全，保重拉~")
            break
            
    else:
        count += 1  
        print(f"什麼意思?我是問妳要不要")
        if count >= 3:  
            print("問了3次已讀亂回，那去吃大便好了!^_^\n")
            print()  
            input("按 Enter 結束 ! 作者無法保證使用者人身安全，保重拉~")
            break