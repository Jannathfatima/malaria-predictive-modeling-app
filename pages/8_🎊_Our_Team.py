import streamlit as st
from page_utils import font_modifier, display_image

display_image.display_image('https://cdn-images-1.medium.com/max/800/0*vBDO0wwrvAIS5e1D.png')

st.header("Meet the Team :TADA:")
# Define team members with their roles
team_members = {
    "Project Manager": ["Daikukai Bindah"],
    "ML Engineer": ["Aditya Sharma", "Dinesh Kumar M", "Muhtasim Ibteda Shochcho", "N Priyanka", "Sahar Nikoo", "AYALURI SRI KAUSHIK"],
    "Researcher": ["Ahmed Daker", "Fauzia Khan Mohamed Abdulla", "Jannath Fatima Mohammed", "Paulo Nascimento", "Shanawaz Anwar"],
    "Data Collector": ["Arnav Kumar", "Bartequa Blackmon", "Elias Dzobo", "Fathima Shanavas", "Friday Emmanuel James", "Hareesh Haridas", "Jayashree Subramanian", "Mansi Upadhyay", "Peter Mahuthu", "Poornachander Pothana", "Rishab Bandodkar", "Sahil Bhandari", "Tejansh Sachdeva", "Tinotenda Mangarai", "Trishika Boyila"],
    "Lead Data Analyst": ["Ekeke Chidiebere Chiwuikem"],
    "Data Analyst": ["Dorothea Paulssen", "Linda Oraegbunam", "Raul Catacora", "Rohit Bhalode", "Satvik Rajesh"],
    "Data Visualization Developer": ["Maria Loureiro"],
    "Model Deployment Engineer": ["Lanz Vincent T. Vencer", "Varshitha M"],
    "Data Scientist": ["Ndong Henry Ndang", "Sindhusha Nannapaneni"],
    "Senior Research Fellow": ["Oscar Daniel Murgueytio Panana"],
    "Lead ML Engineer": ["Thomas James"]
}

# Function to display team members
def display_team(role, members):
    st.subheader(role)
    for member in members:
        st.write(member)

# Streamlit app
def main():
    st.title("Team Page")

    for role, members in team_members.items():
        display_team(role, members)

if __name__ == "__main__":
    main()
