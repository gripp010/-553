import random
again="да"
while again=="да":
    
    health=100
    location="start"
    mana=0
    max_mana=0
    mag=False
    while health>0 and location!="dead":
        if mag:
            print(f"\nЗдоровье:{health} Мана:{mana}/{max_mana}")
        else:    
            print(f"\nЗдоровье:{health}")
            if location=="start":
                action=input("Вы стоите перед замком: (зайти/пройти мимо)")
                if action=="зайти":
                    location="castle"    
                elif action=="пройти мимо":
                    location="city"
            elif location=="castle":
                print("Вы ходите по замку ")
                room=input("Слышны звуки из комнаты: (зайти/уйти)")
                if room=="зайти":
                    potion=input("Там сидит старик и предлогает зелье: (взять/отказать)")
                    if potion=="взять":
                        print(f"Вы отравились (-20HP) ")
                        health-=20
                    elif potion=="отказать":
                        print("Вы вернулись в замок")
                elif room=="уйти":
                    location=="start"    
            elif location=="city":
                magic=input("познакомиться с магом: (да/нет)")    
                if magic=="да":
                    print("Вы дошли до деревни")
                    if not mag:
                        mane=input("Маг хочет научить вас магии: (да/нет)")
                        if mane=="да":
                            max_mana=random.randint(50, 150)
                            mana=max_mana
                            mag=True
                            print(f"Вы научились магии")
                        else:
                            print("Вы отказались")
                    else:
                        print("Вы уже обучены магии")        
                elif magic=="нет":
                    print("Вас убили разбойники") 
                    health=0           
    if health<=0:
        print("Игра окончена вы погибли")    
    again=input("Вы хоте пройти игру еще раз?(да/нет) ")                            

                        
            
                

    