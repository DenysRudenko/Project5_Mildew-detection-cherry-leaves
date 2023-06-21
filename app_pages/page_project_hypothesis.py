import streamlit as st


def page_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"**Hypothesis**\n\n"
        f"* The cherry leaves that have powdery mildew contains white streaks on them.\n\n"
    )
    st.success(
        f"**Validation**\n\n"
        f"* An arrangement of images, known as an Image Montage, demonstrates that leaves affected by powdery mildew commonly exhibit white streaks.\n\n"
        f"* In the Average Image, Variability Image, and Difference between Averages,"
        f" the healthy leaves appear to have a richer shade of green compared to the leaves affected by mildew.\n\n"
    )