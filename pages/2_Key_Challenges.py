import streamlit as st
st.set_page_config(layout="wide")

# Retrieve solution option from session state
selected_solution = st.session_state.selected_solution

# Initialize session state
if 'selected_solution' not in st.session_state:
    st.session_state.selected_solution = "ILA"
if 'selected_options' not in st.session_state:
    st.session_state.selected_options = {}

# Retrieve client's name from session state
client_name = st.session_state.client_name
# Define a list of Key Challenges for ILA
key_challenges_ILA = {
    "Manual Reporting": 'ILA_kc_mr', 
    "Report Balancing & Conflicts": 'ILA_kc_rbc', 
    "Business trust": 'ILA_kc_bt', 
    "Cost": 'ILA_kc_c',
    "Change management and adoption": 'ILA_kc_cma', 
    "Information Silos": 'ILA_kc_is', 
    "Lack of Data Access": 'ILA_kc_lda',
    "Data Quality": 'ILA_kc_dq', 
    "Team capacity": 'ILA_kc_tc'
}


master_data_challenges_ILA = {
    "Master Data - Incomplete": 'ILA_kc_md_i', 
    "Master Data - Differences & multiple versions": 'ILA_kc_md_dmv',
    "Master Data - Local isolated data": 'ILA_kc_md_lid'
}

mdp_challenges_ILA = {
    "MDP - Technical complexity": 'ILA_kc_mdp_tc', 
    "MDP - Technical debt": 'ILA_kc_mdp_td',
    "MDP - Growing scale": 'ILA_kc_mdp_gs', 
    "MDP - Skills gaps": 'ILA_kc_mdp_sg', 
    "MDP - Governance overhead": 'ILA_kc_mdp_go'
}

key_challenges_Gen_AI = {
    "Lack of use cases":'GEN_AI_kc_luc',  
    "Variety of sources":'GEN_AI_kc_vs',  
    "Manual collection":'GEN_AI_kc_mc',  
    "Adoption":'GEN_AI_kc_a', 
    "Data Access":'GEN_AI_kc_da',
    "Data Quality":'GEN_AI_kc_dq', 
    "Cost":'GEN_AI_kc_c', 
    "Team capacity":'GEN_AI_kc_tc', 
    "Team capacity - Skills gaps":'GEN_AI_kc_tc_sg'
}

master_data_challenges_Gen_AI = {
    "Master Data - Incomplete":'GEN_AI_kc_md_i', 
    "Master Data - Differences & multiple versions":'GEN_AI_kc_md_dmv', 
    "Master Data - Local isolated data":'GEN_AI_kc_md_lid',
}

mdp_challenges_Gen_AI = {
    "MDP - Technical complexity":'GEN_AI_kc_mdp_tc', 
    "MDP - Technical debt":'GEN_AI_kc_mdp_td', 
    "MDP - Growing scale":'GEN_AI_kc_mdp_gs', 
    "MDP - Governance overhead":'GEN_AI_kc_mdp_go',
}

radio_options = ["None", "Low", "Moderate", "High"]

# List to store user inputs for Overall Challenges
user_inputs_oc = []
low_importance_oc = []
moderate_importance_oc = []
high_importance_oc = []

# List to store user inputs for Master Data
user_inputs_md = []
low_importance_md = []
moderate_importance_md = []
high_importance_md = []

# List to store user inputs for MDP
user_inputs_mdp = []
low_importance_mdp = []
moderate_importance_mdp = []
high_importance_mdp = []

# List to store user inputs for Solutions Aspects

    # If "ILA" is selected, show the "Key Challenges" page
if st.session_state.selected_solution == "ILA":
  
        st.title(f"Key Challenges - {selected_solution} for *{client_name}*")
        with st.expander("Overall Challenges"):
            # Display Radio buttons for each key challenge
            for challenge, variable_name in key_challenges_ILA.items():
                # Get the selected option from session state
                selected_option = st.session_state.selected_options.get(variable_name, radio_options[0])
                # Get the corresponding user input from session state
                user_input = st.session_state.selected_options.get(f"{variable_name}_input", "")

                # Create two columns
                col1, col2 = st.columns([1, 2])

                with col1:
                    # Display radio input on left
                    selected_option = st.radio(
                        f"Select level for {challenge}:", 
                        radio_options, 
                        index=radio_options.index(selected_option), 
                        key=f"{variable_name}", 
                        horizontal=True)

                with col2:
                    # Display text input boxes based on dropdown selection on right
                    if selected_option != "None":
                        user_input = st.text_area(f"Enter details for {challenge} ({selected_option}):", value=user_input, key=f"{variable_name}_input", placeholder="Enter details here")
                        user_inputs_oc.append(f"{challenge} importance: {selected_option} - {user_input}")
                    if selected_option == "Low":
                        low_importance_oc.append(f"{challenge}: {user_input}")
                    elif selected_option == "Moderate":
                        moderate_importance_oc.append(f"{challenge}: {user_input}")
                    elif selected_option == "High":
                        high_importance_oc.append(f"{challenge}: {user_input}")
                    else:
                        user_inputs_oc.append(f"{challenge} importance: {selected_option} - Not required")


                # Store the selected option and user input in session state
                st.session_state.selected_options[variable_name] = selected_option
                st.session_state.selected_options[f"{variable_name}_input"] = user_input
                st.session_state.high_importance_oc = high_importance_oc
                st.session_state.moderate_importance_oc = moderate_importance_oc
                st.session_state.low_importance_oc = low_importance_oc


        with st.expander("Master Data Challenges"):
            for challenge, variable_name in master_data_challenges_ILA.items():
                # Get the selected option from session state
                selected_option = st.session_state.selected_options.get(variable_name, radio_options[0])
                # Get the corresponding user input from session state
                user_input = st.session_state.selected_options.get(f"{variable_name}_input", "")
                
                # Create two columns
                col3, col4 = st.columns([1, 2])

                with col3:           
                    #for challenge, variable_name in master_data_challenges_ILA.items():
                    selected_option = st.radio(f"Select level for {challenge}:", radio_options, index=radio_options.index(selected_option), key=f"{variable_name}", horizontal=True)

                with col4:
                    # Display text input boxes based on dropdown selection on right
                    if selected_option != "None":
                        user_input = st.text_area(f"Enter details for {challenge} ({selected_option}):", value=user_input, key=f"{variable_name}_input", placeholder="Enter details here")
                        user_inputs_md.append(f"{challenge} importance: {selected_option} - {user_input}")
                        if selected_option == "Low":
                            low_importance_md.append(f"{challenge}: {user_input}")
                        elif selected_option == "Moderate":
                            moderate_importance_md.append(f"{challenge}: {user_input}")
                        elif selected_option == "High":
                            high_importance_md.append(f"{challenge}: {user_input}")
                        else:
                            user_inputs_md.append(f"{challenge} importance: {selected_option} - Not required")

                # Store the selected option and user input in session state
                st.session_state.selected_options[variable_name] = selected_option
                st.session_state.selected_options[f"{variable_name}_input"] = user_input
                st.session_state.high_importance_md = high_importance_md
                st.session_state.moderate_importance_md = moderate_importance_md
                st.session_state.low_importance_md = low_importance_md
    
        with st.expander("MDP Challenges"):
            for challenge, variable_name in mdp_challenges_ILA.items():

                # Get the selected option from session state
                selected_option = st.session_state.selected_options.get(variable_name, radio_options[0])
                # Get the corresponding user input from session state
                user_input = st.session_state.selected_options.get(f"{variable_name}_input", "")
                
                # Create two columns
                col5, col6 = st.columns([1, 2])
                with col5:           
                    #for challenge, variable_name in mdp_challenges_ILA.items():
                    selected_option = st.radio(f"Select level for {challenge}:", radio_options, index=radio_options.index(selected_option), key=f"{variable_name}", horizontal=True)

                with col6:
                # Display text input boxes based on dropdown selection on right
                    if selected_option != "None":
                        user_input = st.text_area(f"Enter details for {challenge} ({selected_option}):", value=user_input, key=f"{variable_name}_input", placeholder="Enter details here")
                        user_inputs_mdp.append(f"{challenge} importance: {selected_option} - {user_input}")
                        if selected_option == "Low":
                            low_importance_mdp.append(f"{challenge}: {user_input}")
                        elif selected_option == "Moderate":
                            moderate_importance_mdp.append(f"{challenge}: {user_input}")
                        elif selected_option == "High":
                            high_importance_mdp.append(f"{challenge}: {user_input}")
                        else:
                            user_inputs_mdp.append(f"{challenge} importance: {selected_option} - Not required")

                # Store the selected option and user input in session state
                st.session_state.selected_options[variable_name] = selected_option
                st.session_state.selected_options[f"{variable_name}_input"] = user_input
                st.session_state.high_importance_mdp = high_importance_mdp
                st.session_state.moderate_importance_mdp = moderate_importance_mdp
                st.session_state.low_importance_mdp = low_importance_mdp

else:
    
    # If "Gen AI" is selected, show the "Key Challenges" page
        if st.session_state.selected_solution == "Gen AI":
            st.title(f"Key Challenges - {selected_solution} for *{client_name}*")
        with st.expander("Overall Challenges"):
            # Display Radio buttons for each key challenge
            for challenge, variable_name in key_challenges_Gen_AI.items():
                # Get the selected option from session state
                selected_option = st.session_state.selected_options.get(variable_name, radio_options[0])
                # Get the corresponding user input from session state
                user_input = st.session_state.selected_options.get(f"{variable_name}_input", "")

                # Create two columns
                col1, col2 = st.columns([1, 2])

                with col1:
                    # Display radio input on left
                    selected_option = st.radio(
                        f"Select level for {challenge}:", 
                        radio_options, 
                        index=radio_options.index(selected_option), 
                        key=f"{variable_name}", 
                        horizontal=True)

                with col2:
                    # Display text input boxes based on dropdown selection on right
                    if selected_option != "None":
                        user_input = st.text_area(f"Enter details for {challenge} ({selected_option}):", value=user_input, key=f"{variable_name}_input", placeholder="Enter details here")
                        user_inputs_oc.append(f"{challenge} importance: {selected_option} - {user_input}")
                    if selected_option == "Low":
                        low_importance_oc.append(f"{challenge}: {user_input}")
                    elif selected_option == "Moderate":
                        moderate_importance_oc.append(f"{challenge}: {user_input}")
                    elif selected_option == "High":
                        high_importance_oc.append(f"{challenge}: {user_input}")
                    else:
                        user_inputs_oc.append(f"{challenge} importance: {selected_option} - Not required")


                # Store the selected option and user input in session state
                st.session_state.selected_options[variable_name] = selected_option
                st.session_state.selected_options[f"{variable_name}_input"] = user_input
                st.session_state.high_importance_oc = high_importance_oc
                st.session_state.moderate_importance_oc = moderate_importance_oc
                st.session_state.low_importance_oc = low_importance_oc


        with st.expander("Master Data Challenges"):
            for challenge, variable_name in master_data_challenges_Gen_AI.items():
                # Get the selected option from session state
                selected_option = st.session_state.selected_options.get(variable_name, radio_options[0])
                # Get the corresponding user input from session state
                user_input = st.session_state.selected_options.get(f"{variable_name}_input", "")
                
                # Create two columns
                col3, col4 = st.columns([1, 2])

                with col3:           
                    #for challenge, variable_name in master_data_challenges_ILA.items():
                    selected_option = st.radio(f"Select level for {challenge}:", radio_options, index=radio_options.index(selected_option), key=f"{variable_name}", horizontal=True)

                with col4:
                    # Display text input boxes based on dropdown selection on right
                    if selected_option != "None":
                        user_input = st.text_area(f"Enter details for {challenge} ({selected_option}):", value=user_input, key=f"{variable_name}_input", placeholder="Enter details here")
                        user_inputs_md.append(f"{challenge} importance: {selected_option} - {user_input}")
                        if selected_option == "Low":
                            low_importance_md.append(f"{challenge}: {user_input}")
                        elif selected_option == "Moderate":
                            moderate_importance_md.append(f"{challenge}: {user_input}")
                        elif selected_option == "High":
                            high_importance_md.append(f"{challenge}: {user_input}")
                        else:
                            user_inputs_md.append(f"{challenge} importance: {selected_option} - Not required")

                # Store the selected option and user input in session state
                st.session_state.selected_options[variable_name] = selected_option
                st.session_state.selected_options[f"{variable_name}_input"] = user_input
                st.session_state.high_importance_md = high_importance_md
                st.session_state.moderate_importance_md = moderate_importance_md
                st.session_state.low_importance_md = low_importance_md
    
        with st.expander("MDP Challenges"):
            for challenge, variable_name in mdp_challenges_Gen_AI.items():

                # Get the selected option from session state
                selected_option = st.session_state.selected_options.get(variable_name, radio_options[0])
                # Get the corresponding user input from session state
                user_input = st.session_state.selected_options.get(f"{variable_name}_input", "")
                
                # Create two columns
                col5, col6 = st.columns([1, 2])
                with col5:           
                    #for challenge, variable_name in mdp_challenges_ILA.items():
                    selected_option = st.radio(f"Select level for {challenge}:", radio_options, index=radio_options.index(selected_option), key=f"{variable_name}", horizontal=True)

                with col6:
                # Display text input boxes based on dropdown selection on right
                    if selected_option != "None":
                        user_input = st.text_area(f"Enter details for {challenge} ({selected_option}):", value=user_input, key=f"{variable_name}_input", placeholder="Enter details here")
                        user_inputs_mdp.append(f"{challenge} importance: {selected_option} - {user_input}")
                        if selected_option == "Low":
                            low_importance_mdp.append(f"{challenge}: {user_input}")
                        elif selected_option == "Moderate":
                            moderate_importance_mdp.append(f"{challenge}: {user_input}")
                        elif selected_option == "High":
                            high_importance_mdp.append(f"{challenge}: {user_input}")
                        else:
                            user_inputs_mdp.append(f"{challenge} importance: {selected_option} - Not required")

                # Store the selected option and user input in session state
                st.session_state.selected_options[variable_name] = selected_option
                st.session_state.selected_options[f"{variable_name}_input"] = user_input
                st.session_state.high_importance_mdp = high_importance_mdp
                st.session_state.moderate_importance_mdp = moderate_importance_mdp
                st.session_state.low_importance_mdp = low_importance_mdp
                   
if st.button(f"Proceed to **Solution Aspect - {selected_solution}**"):
    st.switch_page("pages/3_Solutions_Aspect.py")


