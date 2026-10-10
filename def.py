def menu():
    print("\n1-Продолжить.")
    print("2-Выйти из игры.")
def HP(health):
    print("Ваше здоровье:",health)
def damage(health,damage):
    print("Ты получаешь урон",damage,"!")
    return health-damage
def heal(health, amount):
    print("Ты восстанавливаешь", amount,"здоровья.")
    return health+amount
health=100
print("Ты заходишь в темное подземлье...")
while True:
    HP(health)
    menu()
    choice= input("Твой выбор: ").lower().strip
    if choice=="Выход":
        print("Ты решил покинуть подземелье.")
        break
    if choice=="1":
        health

    

