import streamlit as st
checkbox=st.checkbox("check here to register")
st.error("check first")
if not checkbox:
  st.write("check the box first")
elif checkbox:
 with st.form("enter info"):
  name=st.text_input("name")
  email=st.text_input("email")
  number=st.number_input("number")

  button=st.form_submit_button("submit")
  if button:
   (name, email, number)
   st.write("you've submitted ")
                            

 

