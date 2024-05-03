import streamlit as st 
import csv 
import datetime
st.set_page_config(layout="wide")
def main():

    # Retrieve client's name from session state
    client_name = st.session_state.client_name

    # Retrieve selected solution from session state
    selected_solution = st.session_state.selected_solution

    if selected_solution == "ILA":
    # Retrieve user inputs from session state
        user_inputs_ILA_sa = st.session_state.user_inputs_ILA_sa
    elif selected_solution == "Gen AI":
    # Retrieve user inputs from session state
        user_inputs_Gen_AI_sa = st.session_state.user_inputs_Gen_AI_sa
    
    st.title(f"Overview Summary for *{client_name}*")
 
    # Retrieve captured data from session state
    high_importance_oc = st.session_state.get("high_importance_oc", [])
    moderate_importance_oc = st.session_state.get("moderate_importance_oc", [])
    low_importance_oc = st.session_state.get("low_importance_oc", [])

    high_importance_md = st.session_state.get("high_importance_md", [])
    moderate_importance_md = st.session_state.get("moderate_importance_md", [])
    low_importance_md = st.session_state.get("low_importance_md", [])

    high_importance_mdp = st.session_state.get("high_importance_mdp", [])
    moderate_importance_mdp = st.session_state.get("moderate_importance_mdp", [])
    low_importance_mdp = st.session_state.get("low_importance_mdp", [])

    # user_inputs_sa = st.session_state.user_inputs_sa
    user_inputs_ILA_sa = st.session_state.get("user_inputs_ILA_sa",[])
    user_inputs_Gen_AI_sa = st.session_state.get("user_inputs_Gen_AI_sa",[])

    st.subheader("Key Challenges - Overall Challenges :")

    st.markdown("**High Importance:**")
    for input in high_importance_oc:
        st.write(input)

    st.markdown("**Moderate Importance:**")
    for input in moderate_importance_oc:
        st.write(input)

    st.markdown("**Low Importance:**")
    for input in low_importance_oc:
        st.write(input)

    st.subheader("Key Challenges - Master Data :")
    st.markdown("**High Importance:**")
    for input in high_importance_md:
        st.write(input)

    st.markdown("**Moderate Importance:**")
    for input in moderate_importance_md:
        st.write(input)

    st.markdown("**Low Importance:**")
    for input in low_importance_md:
        st.write(input)

    st.subheader("Key Challenges - MDP :")
    st.markdown("**High Importance:**")
    for input in high_importance_mdp:
        st.write(input)

    st.markdown("**Moderate Importance:**")
    for input in moderate_importance_mdp:
        st.write(input)

    st.markdown("**Low Importance:**")
    for input in low_importance_mdp:
        st.write(input)
    
    if selected_solution =="ILA":
        st.subheader("**Solution Acpects** :")
        for input in user_inputs_ILA_sa:
            st.write(input)
    elif selected_solution == "Gen AI":
        st.subheader("**Solution Acpects** :")
        for input in user_inputs_Gen_AI_sa:
            st.write(input)       

    if selected_solution == "ILA":
        # Export to CSV when the submit button is clicked
        if st.button("Export to CSV"):
            data = [
                ("Client Name", client_name),
                ("Selected Solution", selected_solution),
                ("Key Challenges - Overall Challenges (High Importance)", "\n".join(high_importance_oc)),
                ("Key Challenges - Overall Challenges (Moderate Importance)", "\n".join(moderate_importance_oc)),
                ("Key Challenges - Overall Challenges (Low Importance)", "\n".join(low_importance_oc)),
                ("Key Challenges - Master Data (High Importance)", "\n".join(high_importance_md)),
                ("Key Challenges - Master Data (Moderate Importance)", "\n".join(moderate_importance_md)),
                ("Key Challenges - Master Data (Low Importance)", "\n".join(low_importance_md)),
                ("Key Challenges - MDP (High Importance)", "\n".join(high_importance_mdp)),
                ("Key Challenges - MDP (Moderate Importance)", "\n".join(moderate_importance_mdp)),
                ("Key Challenges - MDP (Low Importance)", "\n".join(low_importance_mdp)),
                ("Solution Aspects", "\n".join(user_inputs_ILA_sa))
        ]
        # Export data to CSV
            export_to_csv(data)
    elif selected_solution == "Gen AI":
       if st.button("Export to CSV"):
        data = [
                    ("Client Name", client_name),
                    ("Selected Solution", selected_solution),
                    ("Key Challenges - Overall Challenges (High Importance)", "\n".join(high_importance_oc)),
                    ("Key Challenges - Overall Challenges (Moderate Importance)", "\n".join(moderate_importance_oc)),
                    ("Key Challenges - Overall Challenges (Low Importance)", "\n".join(low_importance_oc)),
                    ("Key Challenges - Master Data (High Importance)", "\n".join(high_importance_md)),
                    ("Key Challenges - Master Data (Moderate Importance)", "\n".join(moderate_importance_md)),
                    ("Key Challenges - Master Data (Low Importance)", "\n".join(low_importance_md)),
                    ("Key Challenges - MDP (High Importance)", "\n".join(high_importance_mdp)),
                    ("Key Challenges - MDP (Moderate Importance)", "\n".join(moderate_importance_mdp)),
                    ("Key Challenges - MDP (Low Importance)", "\n".join(low_importance_mdp)),
                    ("Solution Aspects", "\n".join(user_inputs_Gen_AI_sa))
            ]
            # Export data to CSV
        export_to_csv(data) 
def export_to_csv(data):
    # Define CSV file path
    client_name = st.session_state.client_name
    Year = datetime.datetime.now().strftime("%Y")
    Hour = datetime.datetime.now().strftime("%H")
    Minutes = datetime.datetime.now().strftime("%M")
    Seconds = datetime.datetime.now().strftime("%S")
    csv_file_path = (f"Overview_Summary_{client_name}_{Year}{Hour}{Minutes}{Seconds}.csv")

    # Write data to CSV file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    st.success(f"Data exported to CSV file: {csv_file_path}")

if __name__ == "__main__":
    main()
