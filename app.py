import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="LASC Remote Appearance SOP",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. MINIMALIST CUSTOM CSS
# This removes the default Streamlit UI clutter and gives it the sleek, clean look you prefer.
st.markdown("""
    <style>
        /* Main container styling */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 800px;
        }
        
        /* Typography & Underlines */
        h1, h2, h3 {
            font-weight: 400 !important;
            letter-spacing: -0.02em;
        }
        h1 {
            border-bottom: 2px solid #1f2937;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        h2 {
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 5px;
            margin-top: 30px;
        }
        
        /* Clean up Streamlit Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 0px;
            border-bottom: 2px solid transparent;
            padding-top: 10px;
            padding-bottom: 10px;
        }
        .stTabs [aria-selected="true"] {
            border-bottom: 2px solid #1f2937 !important;
            color: #1f2937 !important;
        }
        
        /* Dynamic FAQ Expanders - Sleek without bubbles */
        .streamlit-expanderHeader {
            font-weight: 500;
            color: #1f2937;
            border-bottom: 1px solid #e5e7eb;
            padding-left: 0px !important;
            background-color: transparent !important;
        }
        [data-testid="stExpander"] {
            border: none !important;
            box-shadow: none !important;
            background-color: transparent !important;
        }
        
        /* Hide default Streamlit menu and footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. HEADER
st.title("Los Angeles Superior Court")
st.markdown("**Remote Appearance SOP & Guide** | Manock Law")
st.markdown("*Use this interactive guide to schedule and check into LASC remote hearings via LACourtConnect.*")

# 4. TAB LAYOUT
tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Interactive Checklist", "❓ Dynamic FAQ"])

# ----------------- TAB 1: SOP -----------------
with tab1:
    st.markdown("## 1. Important Links")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- [Advance Scheduling Portal](https://my.lacourt.org/laccwelcome)")
        st.markdown("- [Same-Day Check-In](https://lacc.lacourt.org)")
    with col2:
        st.markdown("- [Check Dept. Eligibility](https://www.lacourt.ca.gov/courtroominformation/)")
        st.markdown("- [LACC Terms of Use](https://lacc.lacourt.org/termsofuse)")
    
    st.info("**LACC Help Desk:** (213) 830-0400 | Available 7:30 AM - 5:30 PM (court days)")

    st.markdown("## 2. Procedure A: Advance Scheduling")
    st.markdown("*Use this method when the hearing is more than one day away (up to 30 days in advance).*")
    st.markdown("""
    1. Go to [my.lacourt.org/laccwelcome](https://my.lacourt.org/laccwelcome).
    2. **Sign in** with Court ID (requires email and password).
    3. Click **Schedule**.
    4. Enter the **Case Number** and click **Lookup Case**.
    5. Verify case info and click **Proceed to Step 2**.
    6. Select role: **Attorney** (or Party/Witness).
    7. Enter attendee info (name, email, State Bar number).
    8. Select the party you represent.
    9. Select the applicable hearing event from the list.
    10. Click **Proceed to Step 4**, review, and click **Schedule**.
    """)

    st.markdown("## 3. Procedure B: Same-Day Check-In")
    st.markdown("*Use this method on the actual morning of the hearing.*")
    st.markdown("""
    1. Go to [lacc.lacourt.org](https://lacc.lacourt.org).
    2. Select Litigation Type: **Civil**.
    3. Click "I Agree" on the Restriction Policy.
    4. Search by **Case Number** and click **Select** next to the case.
    5. Enter your **Email Address** (tracks all checked-in hearings).
    6. Select your name from the party list, and the party you represent.
    7. Click **Check-In**.
    8. When ready to enter the courtroom, click the **JOIN** button.
    """)

    st.markdown("## 4. Courtroom Etiquette")
    st.markdown("""
    - **Enter Muted / Camera Off:** Join the Teams lobby with mic and camera off.
    - **Raise Hand:** Use the Teams 'Raise Hand' feature to be recognized.
    - **Headset Recommended:** Use a headset to prevent audio feedback.
    - **No Recording:** Photographing or recording the hearing is strictly prohibited by CRC 1.150.
    """)

# ----------------- TAB 2: INTERACTIVE CHECKLIST -----------------
with tab2:
    st.markdown("## Hearing Day Pre-Flight Checklist")
    st.markdown("Use this checklist to ensure everything is ready before joining the virtual courtroom.")
    
    st.checkbox("Checked department eligibility to confirm remote appearance is allowed")
    st.checkbox("Verified case number and hearing time")
    st.checkbox("Signed into LACourtConnect via Same-Day Check-in")
    st.checkbox("Physical exhibits/documents delivered to the courtroom (if applicable)")
    st.checkbox("Headset connected and tested")
    st.checkbox("Microsoft Teams camera turned OFF before joining lobby")
    st.checkbox("Microsoft Teams microphone MUTED before joining lobby")
    st.checkbox("Background is neutral and lighting is adequate")
    
    st.success("Once all boxes are checked, you are ready to click **JOIN** in LACourtConnect!")

# ----------------- TAB 3: DYNAMIC FAQ -----------------
with tab3:
    st.markdown("## Frequently Asked Questions")
    
    with st.expander("Is there a fee to use LACourtConnect?"):
        st.write("No. LACourtConnect (LACC) is a free service provided by the Los Angeles Superior Court.")
        
    with st.expander("Can we use CourtCall for Stanley Mosk cases?"):
        st.write("No. LASC transitioned entirely away from CourtCall and Webex in 2025. LACourtConnect is the exclusive platform for remote appearances in LA County.")
        
    with st.expander("What types of hearings are NOT eligible for remote appearance?"):
        st.write("""
        Generally, the following require IN-PERSON appearances:
        - Trials and Prove-Ups (Except Small Claims)
        - Settlement Conferences 
        - Final Status Conferences (Usually strongly encouraged in-person)
        *Always verify with the specific department's courtroom information page.*
        """)
        
    with st.expander("My hearing isn't showing up when I search. What do I do?"):
        st.write("""
        - If using **Same-Day Check-in**, only today's hearings will appear. If the hearing is tomorrow, use the Advance Scheduling portal.
        - Verify the case number is typed correctly without spaces.
        - Try searching by Court Calendar (Courthouse + Department) instead of case number.
        - Call the LACC Help Desk at (213) 830-0400.
        """)
        
    with st.expander("What if I have multiple hearings at the same time?"):
        st.write("Once you check in to your first hearing on the Same-Day portal, LACC will auto-populate other cases where you are the attorney of record. You can check into all of them. If times overlap, join the first one and ask the clerk/judge for 'priority/first call', then jump to your second hearing.")
        
    with st.expander("How do I present evidence remotely?"):
        st.write("For general civil cases, you must deliver physical copies of your exhibits to the courtroom before the hearing date. During the hearing, the court may use the Teams screen-share function to display evidence.")
