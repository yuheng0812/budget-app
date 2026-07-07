expenses = []

def add_expense():
    name = input("請輸入項目名稱:")
    money = input("請輸入金額:")
    category = input("請輸入類別:")
    date = input("請輸入日期:")
    expense = {
        "name": name,
        "money": money,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    print(f"✅ 已新增:{expense['name']} / {expense['money']}元 / {expense['category']} / {expense['date']}")

def view_expenses():
    if len(expenses) == 0:
        print("目前沒有任何紀錄")
    else:
        print("=== 所有支出紀錄 ===")
        for i, expense in enumerate(expenses):
            print(f"{i+1}. {expense['name']} / {expense['money']}元 / {expense['category']} / {expense['date']}")

def show_total():
    total = 0
    for expense in expenses:
        total += int(expense['money'])
    print(f"總共花了:{total}元")

def save_expenses():
    with open("budget.csv","w") as file:
        for expense in expenses:
            file.write(f"{expense['name']},{expense['money']},{expense['category']},{expense['date']}\n")

def load_expenses():
    try:
        with open("budget.csv","r") as file:
            for line in file:
                data = line.strip().split(",")
                expense = {
                    "name": data[0],
                    "money": data[1],
                    "category": data[2],
                    "date": data[3]
                }
                expenses.append(expense)
    except FileNotFoundError:
        pass

def main():
    while True:
        print(f"=== 記帳程式 ===")
        print(f"1. 新增支出")
        print(f"2. 查看紀錄")
        print(f"3. 顯示總花費")
        print(f"4. 離開")
        choice = input("請選擇功能:")

        if choice == "1":
            add_expense()
            print("-" * 30)

        elif choice == "2":
            view_expenses()
            print("-" * 30)

        elif choice == "3":
            show_total()
            print("-" * 30)

        elif choice == "4":
            save_expenses()
            print("-" * 30)
            break

        else:
            print(f"輸入錯誤，請重新輸入 1 / 2 / 3 / 4")
            print("-" * 30)

load_expenses()
main()