import streamlit as st

st.set_page_config(layout="wide")

# Retrieve solution option from session state ("ILA" or "Gen AI")
selected_solution = st.session_state.selected_solution
# user_inputs_sa = st.session_state.user_inputs_sa 

# Initialize session state
# if 'selected_solution' not in st.session_state:
#     st.session_state.selected_solution = "ILA"
# if 'user_inputs_sa' not in st.session_state:
#      st.session_state.user_inputs_sa = {}
# if 'selected_options' not in st.session_state:
#     st.session_state.selected_options = {}
if 'selected_solutions_aspect' not in st.session_state:
    st.session_state.selected_solutions_aspect = {}


# Retrieve client name from session state
client_name = st.session_state.client_name

solution_aspects_ILA = {
    "Business Objectives":'ILA_sa_bo', 
    "Cloud Posture":'ILA_sa_cp',
    "Systems":'ILA_sa_sy',
    "Licenses":'ILA_sa_l',
    "Storage":'ILA_sa_st',
    "Networking":'ILA_sa_n',
    "Integration":'ILA_sa_i' ,
    "Reliability":'ILA_sa_rel' ,
    "Disaster Recovery":'ILA_sa_dr' ,
    "Team Capability & Structure":'ILA_sa_tcs' ,
    "Security & Access Control":'ILA_sa_sac' ,
    "Data Cataloguing":'ILA_sa_dc' ,
    "Master Data":'ILA_sa_md' ,
    "Data Quality":'ILA_sa_dq' ,
    "Data Movement":'ILA_sa_dm' ,
    "Data Literacy":'ILA_sa_dl' ,
    "Reporting":'ILA_sa_rep' ,
    "Data Sharing":'ILA_sa_ds'  

}

solution_aspects_Gen_AI = {
    "AI Advisory":'Gen_AI_sa_aia', 
    "Prebuilt AI Solution":'Gen_AI_sa_pais', 
    "AI Launch Hub POC Accelerator":'Gen_AI_sa_', 
    "AI Ops":'Gen_AI_sa_"aio', 
    "AI Policy Formulation":'Gen_AI_sa_aipf', 
}

# List to store user inputs for ILA solution aspects
user_inputs_ILA_sa = []
# List to store user inputs for Gen AI solution aspects
user_inputs_Gen_AI_sa = []

# If "ILA" is selected, show the "Solution Aspects - ILA" page
if st.session_state.selected_solution == "ILA":
    st.header(f"Solution Aspects - {selected_solution} for *{client_name}*")
    for challenge_sa, variable_name_sa in solution_aspects_ILA.items():
        # Get the corresponding user input from session state
        user_input = st.session_state.selected_solutions_aspect.get(f"{variable_name_sa}_input", "")
        user_input = st.text_area(f"Enter details for {challenge_sa}: ", value=user_input, key=f"{variable_name_sa}_input", placeholder="Enter text here")
         # Only append if user_input is not blank
        if user_input.strip():
            user_inputs_ILA_sa.append(f"{challenge_sa} : {user_input}")
        # Store the user input in session state
        st.session_state.selected_solutions_aspect[f"{variable_name_sa}_input"] = user_input
        st.session_state.user_inputs_ILA_sa = user_inputs_ILA_sa

    # If "Gen AI" is selected, show the "Solution Aspects" page                
else:
    if st.session_state.selected_solution == "Gen AI":
       
        st.header(f"Solution Aspects - {selected_solution} for *{client_name}*")
        for challenge_sa, variable_name_sa in solution_aspects_Gen_AI.items():
            # Get the corresponding user input from session state
            user_input = st.session_state.selected_solutions_aspect.get(f"{variable_name_sa}_input", "")
            user_input = st.text_area(f"Enter details for {challenge_sa}: ", value=user_input, key=f"{variable_name_sa}_input", placeholder="Enter text here")
            # Only append if user_input is not blank
            if user_input.strip():
                user_inputs_Gen_AI_sa.append(f"{challenge_sa} : {user_input}")
            # Store the user input in session state
            st.session_state.selected_solutions_aspect[f"{variable_name_sa}_input"] = user_input
            st.session_state.user_inputs_Gen_AI_sa = user_inputs_Gen_AI_sa
                


if st.button("Proceed to **Overview Summary**"):
    st.switch_page("pages/4_Overview_Summary.py")