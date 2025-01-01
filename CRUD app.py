import streamlit as st
import mysql.connector as ms

mydb = ms.connect(
    host="localhost",
    user="root",
    password="Password123",
    database="app_data"
)

my_cursor = mydb.cursor()
print("Connection established")

# create streamlit app
def main():
    st.title("Record Creation");
    # Display options
    option = st.sidebar.selectbox("Select an operation", ("Create", "View", "Update", "Delete"))
    # Perform selected operations
    if option == "Create":
        st.subheader("Create a Record")
        name = st.text_input("Enter your name")
        email = st.text_input("Enter your email address")
        if st.button("Create"):
            sql = "insert into users(name, email) values(%s,%s)"
            val = (name, email)
            my_cursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully")

    elif option == "View":
        st.subheader("View Records")
        my_cursor.execute("select * from users")
        result = my_cursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Update":
        st.subheader("Update a Record")
        id = st.number_input("Enter ID", min_value=1)
        name = st.text_input("Enter new name")
        email = st.text_input("Enter new email")
        if st.button("Update"):
            sql = "update users set name=%s, email=%s where id =%s"
            val = (name, email, id)
            my_cursor.execute(sql, val)
            mydb.commit()
            st.success("Record updated successfully")



    elif option == "Delete":
        st.subheader("Delete a Record")
        id = st.number_input("Enter ID", min_value=1)
        if st.button("Delete"):
            sql = "delete from users where id = %s"
            val = (id,)
            my_cursor.execute(sql, val)
            mydb.commit()
            st.success("Record deleted successfully")


if __name__ == "__main__":
    main()




