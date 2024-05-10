import streamlit as st
from page_utils import font_modifier, display_image

display_image.display_image('https://cdn-images-1.medium.com/max/800/0*vBDO0wwrvAIS5e1D.png')

st.header("Meet the Team :tada:")

def team_page():
    st.title("Our Team")

    team_members = [
        ("Aditya Sharma", "ML Engineer"),
        ("Ahmed Daker", "Researcher"),
        ("Arnav Kumar", "Data Collector"),
        ("Bartequa Blackmon", "Data Collector"),
        ("Ekeke Chidiebere Chiwuikem", "Lead Data Analyst"),
        ("Dinesh Kumar M", "ML Engineer"),
        ("Dorothea Paulssen", "Data Analyst"),
        ("Elias Dzobo", "Data Collector"),
        ("Fathima Shanavas", "Data Collector"),
        ("Fauzia Khan Mohamed Abdulla", "Researcher"),
        ("Friday Emmanuel James", "Data Collector"),
        ("Hareesh Haridas", "Data Collector"),
        ("Jannath fatima Mohammed", "Researcher"),
        ("Jayashree Subramanian", "Data Collector"),
        ("Lanz Vincent T. Vencer", "Model Deployment Engineer"),
        ("Linda Oraegbunam", "Data Analyst"),
        ("Mansi upadhyay", "Data Collector"),
        ("Maria Loureiro", "Data Visualization Developer"),
        ("Muhtasim Ibteda Shochcho", "ML Engineer"),
        ("N Priyanka", "ML Engineer"),
        ("Ndong Henry Ndang", "Data scientist"),
        ("Oscar Daniel Murgueytio Panana", "Senior Research Fellow"),
        ("Paulo Nascimento", "Researcher"),
        ("Peter Mahuthu", "Data Collector"),
        ("Poornachander Pothana", "Data Collector"),
        ("Raul Catacora", "Data Analyst"),
        ("Rishab Bandodkar", "Data Collector"),
        ("Rohit Bhalode", "Data Analyst"),
        ("Sahar Nikoo", "ML Engineer"),
        ("Sahil bhandari", "Data Collector"),
        ("Satvik Rajesh", "Data Analyst"),
        ("Shanawaz Anwar", "Researcher"),
        ("Sindhusha Nannapaneni", "Data scientist"),
        ("AYALURI SRI KAUSHIK", "ML Engineer"),
        ("Tejansh Sachdeva", "Data Collector"),
        ("Thomas James", "Lead ML Engineer"),
        ("Tinotenda Mangarai", "Data Collector"),
        ("Trishika Boyila", "Data Collector"),
        ("Varshitha M", "Model Deployment Engineer"),
        ("Vivien Siew", "Data Scientist"),
        ("Daikukai Bindah", "Project Manager")
    ]

    roles = {}
    project_manager = None
    for name, role in team_members:
        if role == "Project Manager":
            project_manager = name
        else:
            if role not in roles:
                roles[role] = []
            roles[role].append(name)

    if project_manager:
        st.header("Project Manager")
        st.write(f"- {project_manager}")

    st.write("Meet our incredible team!")

    for role, members in roles.items():
        st.header(role)
        for member in members:
            st.write(f"- {member}")

team_page()
