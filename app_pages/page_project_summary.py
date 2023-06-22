import streamlit as st


def page_summary_body():
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is a common fungal infection that impacts various types of plants. Numerous fungi "
        f"species belonging to the Erysiphales order are responsible for causing powdery mildew. This disease is relatively easy to recognize "
        f"due to its distinct symptoms. Affected plants exhibit noticeable white powdery patches on their leaves and stems."
        f"While the lower leaves are particularly susceptible, the mildew can manifest on any above-ground "
        f"portion of the plant. *[Source](https://en.wikipedia.org/wiki/Powdery_mildew)*" 
        )

    st.info(f"The machine learning feature on this platform has the capability to rapidly and accurately "
            f"identify cherry leaves that are infected with mildew, with an accuracy rate exceeding 97%. "
            f"Consequently, this eliminates the need for manual and time-consuming identification of mildew on cherry leaves. \n\n" 
    )
    if st.checkbox("Problem Statement"):
        st.info(
            f"* Farmy & Foods is currently facing a challenge with their cherry plantation crop, as they are " 
            f"experiencing an issue with powdery mildew affecting their cherry trees. At present, the "
            f"method employed involves manually inspecting each cherry tree to determine if it is affected by powdery mildew."
            f"\nAn employee dedicates approximately 30 minutes per tree, collecting leaf samples and visually" 
            f"confirming whether the tree is healthy or infected. In cases where powdery mildew is detected,"
            f"the employee administers a specific compound to eliminate the fungus, which takes about 1 minute."
            f"Given that the company has numerous cherry trees situated across multiple farms throughout the country," 
            f"this manual inspection process is not feasible on a large scale due to the significant time investment it requires."
            f"\n\n"
            f"**Project Dataset**\n"
            f"* The available dataset taken from the client's crop field contains 4208 images "
            f"of healthy and powdery mildew cherry leaves"
        )

    st.write("#### Business Requirement")
    st.success(
        f"The project has 2 business requirements:\n\n"
        f"The client is interested in:\n\n "
        f"* conducting a study to visually differentiate a cherry leaf "
        f"that is healthy and that contains powdery mildew\n"
        f"* predicting if a cherry leaf is healthy or contains powdery mildew."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/DenysRudenko/Project5_Mildew-detection-cherry-leaves/blob/main/README.md).")
    
    st.write(
        f"* To download the example Cherry-Leaves dataset, please follow the link"
        f"[Cherry-Leaves Dataset](https://www.kaggle.com/codeinstitute/cherry-leaves).")