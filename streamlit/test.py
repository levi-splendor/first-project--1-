import streamlit as st

button=st.button("get started")
if button:
    st.text
    secretNumber=7
    st.secretNumber=secretNumber
st.guess=None
guess= st.number_input("enter the number")
while (guess !=secretNumber):
    guess= st.number_input("enter the number")
    if(guess<secretNumber):
        st.write("too low")
    elif (guess>secretNumber):
        st.write("too high")
    else:
        st.write("you guessed it right")
        break
print("congrats")
   


   