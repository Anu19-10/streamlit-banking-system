import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Banking System")

menu = [
    "Create Account",
    "Deposit",
    "Withdraw",
    "Check Details",
    "Update Details",
    "Delete Account"
]

choice = st.sidebar.selectbox("Menu", menu)


# CREATE ACCOUNT
if choice == "Create Account":

    st.subheader("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create"):

        result = bank.create_account(name, age, email, int(pin))

        if isinstance(result, dict):

            st.success("Account Created")

            st.write("Account Number:", result["account_no"])

        else:
            st.error(result)


# DEPOSIT
elif choice == "Deposit":

    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):

        result = bank.deposit(acc, int(pin), amount)
        st.success(result)


# WITHDRAW
elif choice == "Withdraw":

    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):

        result = bank.withdraw(acc, int(pin), amount)
        st.success(result)


# DETAILS
elif choice == "Check Details":

    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Check"):

        user = bank.get_details(acc, int(pin))

        if user:
            st.write(user)
        else:
            st.error("Account not found")


# UPDATE
elif choice == "Update Details":

    st.subheader("Update Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    field = st.selectbox("Field", ["name", "email", "pin"])
    value = st.text_input("New Value")

    if st.button("Update"):

        result = bank.update_details(acc, int(pin), field, value)
        st.success(result)


# DELETE
elif choice == "Delete Account":

    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):

        result = bank.delete_account(acc, int(pin))
        st.warning(result)