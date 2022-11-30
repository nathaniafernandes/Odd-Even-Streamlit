import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome All"

def main():
  st.title("Subtraction")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Subtraction of 2 numbers using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num = st.number_input("Number")
  if (num%2 ==0):
    result= "Even"
  else:
    result= "Odd"
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("Nathania Fernandes")
      st.text("21f1000454")

if __name__=='__main__':
  main()
