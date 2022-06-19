import streamlit as st

def landing_page():
    # title, header, caption content
    st.image("./logo.png")
    st.title("Using a Voter Profile Simulator to Develop Students Understand Voting Behavior")
    st.subheader("Brian P Zoellner, Richard Chant, Andreas Ink")
    st.caption(
        """
    This project was created to design and examine a voter profile simulator to integrate into a secondary social studies curriculum to utilize aspects of computer science principles through skills like formulating problems, examining and organizing data, and developing explanatory models to explain and understand data. In high school school civics and U.S. government classes and secondary social studies methods courses, we used exit poll data and voting choices emanating from presidential elections to allow students to examine historical voter demographic data (e.g., race, gender, SES, age) to make predictions about voting preferences using a computer simulator. In Phase 1 of our project, we tested the simulator with students to refine it for improved clarity and visual appeal and to fully develop lesson materials that support student challenges when learning about demographics and voting behavior.
                    """
    )

if 'score' not in st.session_state:
    st.session_state['score'] = 0
if __name__ == "__main__":
    landing_page()

    # https://github.com/le-n-qui/redistricting_sesame_street/blob/main/code_final/simulation.py