expenses=[] 
while True:

  print('1. Add expenses')
  print('2. view expenses')
  print('3. calculate total expenses')
  print('5. exit')
  print('4. category wise summary')
  choice=int(input("enter your choice: "))
  if choice==1:
    print('adding expenses')
    expense_name=input('enter the expense name:')
    amount=float(input('enter the amount'))
    category=input('enter the category')
    expense= {
        "name":expense_name,
        "amount":amount,
        "category":category 
        }
      
    expenses.append(expense)
    print('expense added succesfully!')
  elif choice==2:
    print('viewing expenses')
    if len(expenses)==0:
       print('no expenses added yet')
    else:
       print('\n ---your expenses---')
    for expense in expenses:
        print('name :',expense["name"])
        print('amount : Rs',expense["amount"])
        print('category :' ,expense["category"])
        print('--------------')

  elif choice==3:
    print('calculating total')
    total=0
    for expense in expenses:
        total=total+ expense["amount"]
    print('total amount:',total)

  elif choice==4:
     summary = {}

     for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

     print("\n--- CATEGORY SUMMARY ---")
     for category, total in summary.items():
            print(category, ":", total)

  elif choice==5:
    print('thankyou for using the tracker!')
    exit()

  else: print('invalid choice')

