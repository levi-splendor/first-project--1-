import streamlit as st
number=st.number_input("enter number")
while number<=30:
    if(number%3==0 and number%5==0):
        st.write("fizz_buzz")
        st.write(number)
    elif (number%3==0):
        st.write("fizz")
        st.write(number)
    elif(number%5==0):
        st.write("buzz")
        st.write(number)

    number+=1