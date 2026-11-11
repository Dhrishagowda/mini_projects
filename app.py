
import streamlit as st

# Store expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.title("💰 My Expense Tracker")

st.write("Welcome to my Expense Tracker!")
# Dashboard

st.header("Dashboard")

total = 0

for expense in st.session_state.expenses:
    total += expense["amount"]

expense_count = len(st.session_state.expenses)

categories_count = len(set(
    expense["category"]
    for expense in st.session_state.expenses
))

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Expenses", f"₹{total:.2f}")

with col2:
    st.metric("Number of Expenses", expense_count)

with col3:
    st.metric("Categories Used", categories_count)

st.divider()

st.header("Add a New Expense")

expense_name = st.text_input("Expense Name")

amount = st.number_input(
    "Amount",
    min_value=0.0,
    step=1.0
)

category = st.selectbox(
    "Select Category",
    ["Food", "Travel", "Shopping", "Education", "Other"]
)

if st.button("Add Expense"):

    if expense_name.strip() == "":
        st.warning("Please enter an expense name!")

    elif amount <= 0:
        st.warning("Please enter a valid amount!")

    else:
        expense = {
            "name": expense_name,
            "amount": amount,
            "category": category
        }

        st.session_state.expenses.append(expense)

        st.success("Expense added successfully!")

# Display expenses
st.header("Your Expenses")

for expense in st.session_state.expenses:
    st.write(
        expense["name"],
        expense["amount"],
        expense["category"]
    )

# Calculate total expenses

st.header("Total Expenses")

total = 0

for expense in st.session_state.expenses:
    total = total + expense["amount"]

st.metric("Total Amount Spent", f"₹{total:.2f}")
# Category-wise Summary

st.header("Category-wise Summary")

summary = {}

for expense in st.session_state.expenses:

    category = expense["category"]
    amount = expense["amount"]

    if category in summary:
        summary[category] += amount
    else:
        summary[category] = amount

for category, total in summary.items():
    st.write(category, ":", f"₹{total:.2f}")
# Delete Expense

st.header("Delete an Expense")

if len(st.session_state.expenses) == 0:

    st.info("No expenses available to delete!")

else:

    selected_index = st.selectbox(
        "Select expense to delete",
        range(len(st.session_state.expenses)),
        format_func=lambda i: (
            f"{i+1}. "
            f"{st.session_state.expenses[i]['name']} - "
            f"₹{st.session_state.expenses[i]['amount']}"
        )
    )

    if st.button("Delete Expense"):

        st.session_state.expenses.pop(selected_index)

        st.success("Expense deleted successfully!")

        st.rerun()
# Edit Expense

st.header("Edit an Expense")

if len(st.session_state.expenses) == 0:

    st.info("No expenses available to edit!")

else:

    selected_index = st.selectbox(
        "Select expense to edit",
        range(len(st.session_state.expenses)),
        format_func=lambda i: (
            f"{i+1}. {st.session_state.expenses[i]['name']} - "
            f"₹{st.session_state.expenses[i]['amount']}"
        ),
        key="edit_select"
    )

    selected_expense = st.session_state.expenses[selected_index]

    new_name = st.text_input(
        "New Expense Name",
        value=selected_expense["name"]
    )

    new_amount = st.number_input(
        "New Amount",
        min_value=0.0,
        value=float(selected_expense["amount"]),
        step=1.0,
        key="edit_amount"
    )

    new_category = st.selectbox(
        "New Category",
        ["Food", "Travel", "Shopping", "Education", "Other"],
        index=["Food", "Travel", "Shopping", "Education", "Other"].index(
            selected_expense["category"]
        ),
        key="edit_category"
    )

    if st.button("Update Expense"):

        if new_name.strip() == "" or new_amount <= 0:
            st.warning("Enter valid expense details!")

        else:
            selected_expense["name"] = new_name
            selected_expense["amount"] = new_amount
            selected_expense["category"] = new_category

            st.success("Expense updated successfully!")

            st.rerun()
# Search by Category

st.header("Search Expenses by Category")

search_category = st.selectbox(
    "Choose category to search",
    ["Food", "Travel", "Shopping", "Education", "Other"],
    key="search_category"
)

if st.button("Search"):

    found = False

    for expense in st.session_state.expenses:

        if expense["category"].lower() == search_category.lower():

            st.write("Name:", expense["name"])
            st.write("Category:", expense["category"])
            st.write("Amount: ₹", expense["amount"])

            st.divider()

            found = True

    if not found:
        st.info("No expenses found in this category!")
# Search by Category

st.header("Search Expenses by Category")

search_category = st.selectbox(
    "Choose category to search",
    ["Food", "Travel", "Shopping", "Education", "Other"],
    key="search_category"
)

if st.button("Search"):

    found = False

    for expense in st.session_state.expenses:

        if expense["category"].lower() == search_category.lower():

            st.write("Name:", expense["name"])
            st.write("Category:", expense["category"])
            st.write("Amount: ₹", expense["amount"])

            st.divider()

            found = True

    if not found:
        st.info("No expenses found in this category!")
# Expense Visualization

st.header("Expense Visualization")

chart_summary = {}

for expense in st.session_state.expenses:

    category = expense["category"]
    amount = expense["amount"]

    if category in chart_summary:
        chart_summary[category] += amount
    else:
        chart_summary[category] = amount

if chart_summary:

    chart_data = {
        "Category": list(chart_summary.keys()),
        "Amount": list(chart_summary.values())
    }

    st.bar_chart(
        chart_data,
        x="Category",
        y="Amount"
    )

else:
    st.info("Add expenses to view your chart!")