import streamlit as st
# from session_state import session_state

# Initiate client name
client_name = st.text_input("Enter client name:", placeholder="Please enter client name here", value=st.session_state.get("client_name", ""))

# Store client's name in session state
st.session_state.client_name = client_name

# Initiate solution option
selected_solution = st.selectbox("Enter client name:", ["ILA", "Gen AI"],placeholder="Choose an option")

# Store solution option in session state
st.session_state.selected_solution = selected_solution

if st.button("Proceed to **Key Challenges**"):
    st.switch_page("pages/2_Key_Challenges.py")