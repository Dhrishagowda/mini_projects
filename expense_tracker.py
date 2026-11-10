expenses=[] 
def add_expense():
    print('adding expenses')

    expense_name=input('enter the expense name:')
    amount=float(input('enter the amount:'))
    category=input('enter the category:')

    expense={
        "name":expense_name,
        "amount":amount,
        "category":category
    }

    expenses.append(expense)
    print('expense added successfully!')

def view_expense():
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

def calc_tot_expenses():
     print('calculating total')
     total=0
     for expense in expenses:
           total=total+ expense["amount"]
     print('total amount:',total)

def category_wise():
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

def delete():
   print('----YOUR EXPENSES----')
   if len(expenses)==0:
      print('no expenses added yet')
   else:
        for i, expense in enumerate(expenses, start=1):
            print(i, expense["name"], '- Rs', expense["amount"])
        number=int(input('enter the expense to be deleted:'))
        if 1 <= number <= len(expenses):
               expenses.pop(number-1)
               print('expense deleted succesfully')
        else:
                print('invalid expense number')

    

def by_category():
     category=input('enter category to search')
     found=False
     for expense in expenses:
        if expense["category"].lower()==category.lower():
          print('name:', expense["name"])
          print('category:', expense["category"])
          print('amount : Rs',expense["amount"])
          found=True
     if found==False:
         print('no expenses found in the category')

def edit():
    print('-----edit expenses-----')
    if len(expenses)==0:
      print('no expenses available to edit')
    else:
        for i, expense in enumerate(expenses, start=1):
            print(i, expense["name"], '- Rs', expense["amount"])
        number=int(input('enter the expense number to edit:'))
        if 1 <= number <= len(expenses):
          selected_expense = expenses[number-1]
    
          new_name = input('enter new expense name:')
          new_amount = float(input('enter new amount:'))
          new_category = input('enter new category:')
    
          selected_expense["name"] = new_name
          selected_expense["amount"] = new_amount
          selected_expense["category"] = new_category
    
          print('expense updated successfully!')
        else:
            print('invalid expense number')
               
while True:
  print('1. add expense')
  print('2. view expenses')
  print('3. calculate total expenses')
  print('4. category wise summary')
  print('5. delete an expense')
  print('6. exit')
  print('7. search by category')
  print('8. edit an expense')
  try :
    choice=int(input('enter your choice'))
  except ValueError:
    print('invalid input! enter number')
    continue
  if choice==1:
    add_expense()
    
  elif choice==2:
    view_expense()

  elif choice==3:
    calc_tot_expenses()

  elif choice==4:
     category_wise()

  elif choice==5:
     delete()
  elif choice==6:
    print('thankyou for using the tracker')
    break

  elif choice==7:
    by_category()

  elif choice==8:
     edit()
           
  else: print('invalid choice')

