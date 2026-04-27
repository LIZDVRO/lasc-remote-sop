import streamlit as st

# ─────────────────────────────────────────────
# 1. PAGE CONFIGURATION
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Remote Appearance SOP | Manock Law",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# 2. MINIMALIST CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 820px;
        }
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
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# 3. SIDEBAR - COURT SELECTOR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Select Court")
    court = st.radio(
        "Which courthouse?",
        ["Los Angeles (Stanley Mosk)", "Fresno County", "Tulare County"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("**Manock Law**")
    st.markdown("*Remote Appearance Guide*")
    st.markdown("*Last Updated: April 27, 2026*")


# ═══════════════════════════════════════════════
#  LOS ANGELES SUPERIOR COURT
# ═══════════════════════════════════════════════
if court == "Los Angeles (Stanley Mosk)":

    st.title("Los Angeles Superior Court")
    st.markdown("**Stanley Mosk Courthouse - Remote Appearance SOP**")
    st.markdown("*Platform: [LACourtConnect](https://www.lacourt.ca.gov/laccwelcome) (Free) | Video: Microsoft Teams*")

    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])

    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Advance Scheduling Portal](https://my.lacourt.org/laccwelcome)")
            st.markdown("- [Same-Day Check-In](https://lacc.lacourt.org)")
        with col2:
            st.markdown("- [Check Dept. Eligibility](https://www.lacourt.ca.gov/courtroominformation/)")
            st.markdown("- [LACC Terms of Use](https://lacc.lacourt.org/termsofuse)")
        st.info("**LACC Help Desk:** (213) 830-0400 | 7:30 AM - 5:30 PM (court days)")

        st.markdown("## Eligibility")
        st.markdown("""
        Most civil hearings are eligible for remote appearance, **except:**
        - Trials and Prove-Ups (except Small Claims)
        - Settlement Conferences
        - Final Status Conferences (in-person strongly encouraged)
        - Appeals (generally)

        *Always verify with the assigned department's [courtroom information page](https://www.lacourt.ca.gov/courtroominformation/).*
        """)

        st.markdown("## Procedure A: Advance Scheduling")
        st.markdown("*Use when the hearing is more than one day away (up to 30 days in advance).*")
        st.markdown("""
        1. Go to [my.lacourt.org/laccwelcome](https://my.lacourt.org/laccwelcome).
        2. **Sign in** with your Court ID (or create one).
        3. Click **Schedule**.
        4. Enter the **Case Number** and click **Lookup Case**.
        5. Verify case info and click **Proceed to Step 2**.
        6. Select role: **Attorney** (or Party/Witness).
        7. Enter attendee info (name, email, State Bar number).
        8. Select the party you represent.
        9. Select the hearing event from the list.
        10. Click **Proceed to Step 4**, review, and click **Schedule**.
        11. Print or save the confirmation page.
        """)

        st.markdown("## Procedure B: Same-Day Check-In")
        st.markdown("*Use on the actual morning of the hearing.*")
        st.markdown("""
        1. Go to [lacc.lacourt.org](https://lacc.lacourt.org).
        2. Select Litigation Type: **Civil**.
        3. Click **I Agree** on the Restriction Policy.
        4. Search by **Case Number** and click **Select**.
        5. Enter your **Email Address**.
        6. Select your name and the party you represent.
        7. Click **Check-In**.
        8. When ready, click the **JOIN** button to enter the Teams lobby.
        """)

        st.markdown("## Joining via Microsoft Teams")
        st.markdown("""
        1. After clicking JOIN, choose **Continue on this browser** or **Join on the Teams app**.
        2. Enter your name (browser only).
        3. Turn camera **OFF** and **mute** your microphone.
        4. Click **Join now** and wait in the lobby until admitted.
        5. Use the **Raise Hand** feature to be recognized by the court.
        """)

        st.markdown("## Courtroom Etiquette")
        st.markdown("""
        - Enter muted with camera off; turn camera on once admitted.
        - Use a **headset with microphone** for optimal audio.
        - Ensure proper lighting; use a neutral background.
        - Dress professionally (at minimum from the waist up).
        - Do not appear from a vehicle, while walking, or in a public space.
        - **Recording, photographing, or broadcasting is strictly prohibited** (CRC 1.150 / LASC Local Rule 2.17).
        """)

        st.markdown("## Presenting Evidence")
        st.markdown("""
        - Deliver **physical copies** of all exhibits to the courtroom before the hearing.
        - The court may use Teams **screen-share** to display evidence during the hearing.
        - For Small Claims: use the [Digital Evidence System](https://www.lacourt.ca.gov/digitalevidence/) (Chrome/Edge only).
        """)

    with tab2:
        st.markdown("## Hearing Day Pre-Flight Checklist")
        st.checkbox("Confirmed department eligibility for remote appearance", key="la_ck1")
        st.checkbox("Verified case number and hearing time", key="la_ck2")
        st.checkbox("Signed into LACourtConnect (Same-Day Check-In or Advance Scheduling)", key="la_ck3")
        st.checkbox("Physical exhibits delivered to courtroom (if applicable)", key="la_ck4")
        st.checkbox("Headset connected and tested", key="la_ck5")
        st.checkbox("Microsoft Teams camera OFF before joining lobby", key="la_ck6")
        st.checkbox("Microsoft Teams microphone MUTED before joining lobby", key="la_ck7")
        st.checkbox("Background is neutral and lighting is adequate", key="la_ck8")
        st.success("Once all boxes are checked, click **JOIN** in LACourtConnect!")

    with tab3:
        st.markdown("## Frequently Asked Questions")

        with st.expander("Is there a fee to use LACourtConnect?"):
            st.write("No. LACourtConnect is completely free.")
        with st.expander("Can we use CourtCall for LASC hearings?"):
            st.write("No. LASC transitioned entirely to LACourtConnect in 2025. CourtCall is not available for any LA County Superior Court locations.")
        with st.expander("What hearings are NOT eligible for remote appearance?"):
            st.write("Trials and Prove-Ups (except Small Claims), Settlement Conferences, Final Status Conferences (strongly encouraged in-person), and Appeals. Always verify with the specific department's courtroom information page.")
        with st.expander("My hearing isn't showing up when I search. What do I do?"):
            st.write("**Same-Day Check-in** only shows today's hearings. Use Advance Scheduling for future dates. Verify the case number is typed correctly. Try searching by Court Calendar (Courthouse + Department) instead. Call the LACC Help Desk at **(213) 830-0400**.")
        with st.expander("Can I appear by phone only (audio, no video)?"):
            st.write("Yes, but it is not recommended. Dial in using the phone number and Conference ID from the LACC meeting details. Judicial officers strongly prefer camera-on appearances.")
        with st.expander("What if I have multiple hearings the same day?"):
            st.write("After checking in to your first hearing, LACC auto-populates other cases where you are attorney of record. Check into all of them and manage from 'My Checked-in Hearings.' If times overlap, request priority/first call on one, then jump to the next.")
        with st.expander("Do I need to notify opposing counsel?"):
            st.write("No prior notice or court approval is required for most departments. However, it is good practice to inform opposing counsel.")
        with st.expander("How do I present evidence during a remote hearing?"):
            st.write("Deliver physical copies of exhibits to the courtroom before the hearing. The court may use Teams screen-sharing during the hearing.")
        with st.expander("Can witnesses appear remotely?"):
            st.write("Yes. Witnesses check in via LACC by selecting 'Other' on the check-in page and entering their name and role.")
        with st.expander("Who do I contact for technical help?"):
            st.write("**LACC Help Desk:** (213) 830-0400 (7:30 AM - 5:30 PM, court days)")


# ═══════════════════════════════════════════════
#  FRESNO COUNTY SUPERIOR COURT
# ═══════════════════════════════════════════════
elif court == "Fresno County":

    st.title("Fresno County Superior Court")
    st.markdown("**Remote Appearance SOP**")
    st.markdown("*Platforms: [CourtCall](https://courtcall.com) (~$72/appearance) | [Zoom](https://zoom.us) (Free, select departments)*")

    st.error("""
    **⚠️ STOP - Check Your Department First!**

    **If your hearing is a Case Management Conference (CMC) in Department 97E,
    you do NOT need to file RA-010/RA-020 forms.**

    Skip the entire form-filing procedure below and go directly to CourtCall:
    - **Online:** [CourtCall.com](https://courtcall.com)
    - **Phone:** (888) 882-6878
    - Schedule at least **2 court days** before the hearing (~$72 fee).

    *Per Local Rule 2.2.4. For all other departments and hearing types, continue with the full procedure below.*
    """)

    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])

    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Remote Appearance Info](https://www.fresno.courts.ca.gov/divisions/civil/remote-appearance-information)")
            st.markdown("- [CourtCall Scheduling](https://courtcall.com)")
        with col2:
            st.markdown("- [RA-010 Form (Notice)](https://www.fresno.courts.ca.gov/system/files/forms-and-filings/ra-010-notice-remote-appearance.pdf)")
            st.markdown("- [RA-020 Form (Order)](https://www.fresno.courts.ca.gov/system/files/forms-and-filings/ra-020-order-regarding-remote-appearance.pdf)")
        st.warning("**Unlike LA County, Fresno requires advance filing of RA-010 + RA-020 forms and court approval before any remote appearance (except Dept. 97E CMCs).**")
        st.info("""
        **CourtCall:** (888) 882-6878
        **Civil Zoom Coordinator:** (559) 457-1810 / civilzoomcoordinator@fresno.courts.ca.gov
        **Probate Zoom Coordinator:** (559) 457-1760 / probatezoomcoordinator@fresno.courts.ca.gov
        """)

        st.markdown("## Eligibility")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Evidentiary Hearings:**
            - Civil harassment hearings
            - Trials / Prove-ups
            - Orders to Show Cause
            - Motions / Ex Parte
            - Writs
            - Name/Gender Change Petitions
            """)
        with col2:
            st.markdown("""
            **Non-Evidentiary Hearings:**
            - Case Management Conferences
            - Case Status Conferences
            - Pre-Trial Discovery Conferences
            - Dismissal Hearings
            - Judgment Status Hearings
            """)

        st.markdown("## Step 1: File Required Forms")
        st.markdown("""
        1. **RA-010** - Notice of Remote Appearance
        2. **RA-020** - Proposed Order Regarding Remote Appearance

        **E-filing:** Use document names "NOTICE OF REMOTE APPEARANCE" and "PROPOSED ORDER." RA-010 must be e-filed as a **separate document**. Include email or SASE for court's ruling.
        """)

        st.markdown("## Step 2: Meet the Filing Deadlines")
        st.markdown("### Evidentiary Hearings")
        st.markdown("""
        | Scenario | File RA-010 By | Opposition (RA-015) By |
        |---|---|---|
        | Hearing > 15 court days away | 10 court days before | 5 court days before |
        | Within 15 days (moving party) | With moving papers | 12:00 PM day before |
        | Within 15 days (non-moving) | 2:00 PM day before | 12:00 PM day before |
        """)
        st.markdown("### Non-Evidentiary Hearings")
        st.markdown("""
        | Scenario | File RA-010 By |
        |---|---|
        | Hearing > 3 court days away | 2 court days before |
        | Within 3 days (moving party) | With moving papers |
        | Within 3 days (non-moving) | 2:00 PM day before |
        """)

        st.markdown("## Step 3: Serve Opposing Counsel")
        st.markdown("Serve copies of RA-010 and RA-020 on all parties per the same deadlines above.")
        st.markdown("## Step 4: Wait for Court Ruling")
        st.markdown("The court will email (or mail to your SASE) an order granting or denying the request.")

        st.markdown("## Step 5A: Appear via CourtCall")
        st.markdown("*Most Civil Unlimited departments. Audio only.*")
        st.markdown("""
        1. Go to [CourtCall.com](https://courtcall.com) or call **(888) 882-6878**.
        2. Schedule at least **2 court days** before the hearing.
        3. Pay the fee (~$72; Visa/MC/Amex/Discover).
        4. Receive Confirmation with check-in time.
        5. On hearing day, call in at the specified time.
        """)

        st.markdown("## Step 5B: Appear via Zoom")
        st.markdown("*Civil Limited, Probate, and select departments.*")
        st.markdown("""
        1. Court provides **Meeting ID** and **Password** via email.
        2. Download [Zoom](https://zoom.us/download).
        3. On hearing day, join with **camera ON** and **mic MUTED**.
        4. Wait in the waiting room until admitted.
        5. Use **Raise Hand** to be recognized.
        """)

        st.markdown("## Tentative Rulings (Civil Unlimited Law & Motion)")
        st.markdown("""
        - Posted by **2:00 PM** the court day before hearing.
        - To contest: notify clerk AND all parties by **4:00 PM** the day before.
        - If no contest, the tentative becomes the order.
        """)

        st.markdown("## Courtroom Etiquette")
        st.markdown("""
        - Dress professionally. Appear from an **indoor, quiet location**.
        - Camera must show clear video with adequate lighting.
        - Use a headset. Speak at a measured pace.
        - **Recording is strictly prohibited** (CRC 1.150).
        """)

    with tab2:
        st.markdown("## Pre-Hearing Checklist")
        st.markdown("### Filing & Approval")
        st.checkbox("Confirmed department (check if Dept. 97E CMC - if so, skip to CourtCall)", key="fr_ck0")
        st.checkbox("RA-010 filed with the court", key="fr_ck1")
        st.checkbox("RA-020 filed with the court", key="fr_ck2")
        st.checkbox("RA-010 and RA-020 served on all parties", key="fr_ck3")
        st.checkbox("Court order GRANTING remote appearance received", key="fr_ck4")
        st.markdown("### Platform Setup")
        st.checkbox("CourtCall scheduled (2+ court days prior) OR Zoom details received", key="fr_ck5")
        st.checkbox("CourtCall fee paid (~$72) (if applicable)", key="fr_ck6")
        st.checkbox("Zoom app downloaded and tested (if applicable)", key="fr_ck7")
        st.markdown("### Day-Of Preparation")
        st.checkbox("Physical exhibits delivered to courtroom (if applicable)", key="fr_ck8")
        st.checkbox("Headset connected and tested", key="fr_ck9")
        st.checkbox("Quiet, indoor location with neutral background", key="fr_ck10")
        st.checkbox("Checked tentative ruling (posted by 2:00 PM day before)", key="fr_ck11")
        st.success("Once all applicable boxes are checked, you are ready to appear!")

    with tab3:
        st.markdown("## Frequently Asked Questions")
        with st.expander("Our hearing is a CMC in Dept. 97E. Do we still need to file RA forms?"):
            st.write("**No.** Per Local Rule 2.2.4, CMCs in Dept. 97E do NOT require filing RA-010/RA-020 forms. Contact CourtCall directly at [CourtCall.com](https://courtcall.com) or (888) 882-6878. Schedule at least 2 court days prior (~$72 fee).")
        with st.expander("Is there a fee for remote appearances in Fresno?"):
            st.write("**CourtCall:** ~$72/appearance. **Zoom:** No fee.")
        with st.expander("Can I just check in same-day like LA County?"):
            st.write("No. Fresno requires advance filing of RA-010/RA-020 forms and court approval.")
        with st.expander("What if the court denies my request?"):
            st.write("You must appear in person. The judge has full discretion to deny or revoke remote appearance.")
        with st.expander("Which departments use Zoom vs. CourtCall?"):
            st.write("**CourtCall (audio only):** Most Civil Unlimited. **Zoom (video + audio):** Civil Limited, Probate. Contact Civil Zoom Coordinator at (559) 457-1810 if unsure.")
        with st.expander("What are the filing deadlines?"):
            st.write("**Evidentiary:** >15 days out = 10 court days before; within 15 days (moving) = with papers; (non-moving) = 2:00 PM day before. **Non-evidentiary:** >3 days out = 2 court days before; within 3 days (moving) = with papers; (non-moving) = 2:00 PM day before.")
        with st.expander("How do tentative rulings work?"):
            st.write("Posted by 2:00 PM the court day before. Contest by 4:00 PM via clerk + all parties. If no contest, tentative becomes the order.")
        with st.expander("Who do I contact for help?"):
            st.write("**CourtCall:** (888) 882-6878. **Civil Zoom:** (559) 457-1810. **Probate Zoom:** (559) 457-1760. **Civil Clerk:** (559) 457-1900.")


# ═══════════════════════════════════════════════
#  TULARE COUNTY SUPERIOR COURT
# ═══════════════════════════════════════════════
elif court == "Tulare County":

    st.title("Tulare County Superior Court")
    st.markdown("**Remote Appearance SOP (Civil Only)**")
    st.markdown("*Platforms: [Zoom](https://zoom.us) (Free, via court web form) | [CourtCall](https://courtcall.com) (~$72/appearance)*")

    st.success("""
    **💡 TIP: Get on the Weekly Zoom Distribution List!**

    Email **RemoteHearings@tulare.courts.ca.gov** to be added to the weekly distribution list.
    This eliminates the need to submit individual requests for each hearing.
    """)

    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])

    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Request Remote Hearing (Form)](https://www.tulare.courts.ca.gov/online-services/request-remote-hearings)")
            st.markdown("- [CourtCall Scheduling](https://courtcall.com)")
            st.markdown("- [Zoom Download](https://zoom.us/download)")
        with col2:
            st.markdown("- [Tentative Rulings](https://www.tulare.courts.ca.gov/general-information/tentative-rulings)")
            st.markdown("- [Judicial Assignments](https://www.tulare.courts.ca.gov/general-information/judicial-assignments)")
            st.markdown("- [Local Rules (PDF)](https://www.tulare.courts.ca.gov/system/files/local-rules/local-rules_effective-1-1-2026_final.pdf)")
        st.info("""
        **Remote Hearing Assistance:** (559) 738-2330
        **CourtCall:** (888) 882-6878
        **Visalia Civil Clerk:** (559) 730-5000
        **Porterville Civil Clerk:** (559) 782-3700
        **Research Attorney:** research_attorney@tulare.courts.ca.gov
        """)

        st.markdown("## Civil Department Assignments")
        st.markdown("*Effective May 4, 2026*")
        st.markdown("""
        **Visalia (North County):**

        | Dept | Judge | Plaintiffs (by last name) |
        |---|---|---|
        | 1 | Hon. David Mathias | A, B, C, S |
        | 2 | Hon. Bret Hillman | D, E, F, G, H, I, J, K, L, R |
        | 7 | Hon. Nathan Ide | M, N, O, P, Q, T, U, V, W, X, Y, Z |

        **Porterville (South County):**

        | Dept | Judge | Assignment |
        |---|---|---|
        | 19 | Hon. Russell Burke | All South County civil |
        """)

        st.markdown("## Eligibility")
        st.markdown("""
        **Eligible (at judge's discretion):** CMCs, Law & Motion, Demurrers, Summary Judgments, OSC hearings, Fee Waivers, Minor's Compromise, Prove-Ups, Name Changes, Ex Parte hearings, and all other non-evidentiary civil matters.

        **NOT eligible (in-person required):**
        - Settlement Conferences
        - Trial Readiness Conferences
        - Trials / Contested / Evidentiary Hearings
        - Creditor Examinations / Orders of Examination
        - Restraining Orders (CH, WV, EA, GV)
        - Unlawful Detainer Trials
        """)

        st.markdown("## Option A: Zoom via Court Web Form (Free)")
        st.markdown("""
        1. Go to the [Request Remote Hearing form](https://www.tulare.courts.ca.gov/online-services/request-remote-hearings).
        2. Complete the form: your name, firm, email, phone, address, case number, case name, hearing date, and department.
        3. Submit the form. The court responds within **24 hours** by email.
        4. Give notice to the court and all parties per **CRC 3.672** and **CCP 367.75**.
        5. Once approved, the court emails you a **Zoom Meeting ID and Password**.
        6. On hearing day, join Zoom with the provided credentials.
        7. Use naming convention: **"J. Doe Retained Counsel"**

        **Timing:** Request no more than **1 week** in advance.
        """)

        st.markdown("## Option B: CourtCall (~$72)")
        st.markdown("*Per Local Rule 108. Audio only.*")
        st.markdown("""
        1. Contact CourtCall at **(888) 882-6878** or [CourtCall.com](https://courtcall.com).
        2. Schedule **no later than 5 court days** before the hearing.
        3. Pay the fee (~$72; Visa/MC/Amex/Discover).
        4. Receive Confirmation with check-in time.
        5. On hearing day, call in at the specified time.
        """)

        st.markdown("## Tentative Rulings (Civil Law & Motion)")
        st.markdown("""
        Per Local Rule 701, tentative rulings are posted by **3:00 PM** the court day before the hearing at the [Tentative Rulings page](https://www.tulare.courts.ca.gov/general-information/tentative-rulings).

        **To contest:** Notify the court AND all parties by **4:00 PM** via:
        - **Fax:** (559) 733-6774
        - **Email:** research_attorney@tulare.courts.ca.gov
        - **Phone:** (559) 730-5010

        If no party contests, the tentative becomes the order of the court.

        **No tentative rulings issued for:** Writs of Attachment/Possession, Claims of Exemption, Motions to Tax Costs After Trial, Motions for New Trial, or Motions to Continue Trial.
        """)

        st.markdown("## Courtesy Copies (Local Rule 703)")
        st.markdown("""
        A courtesy copy of **all law and motion documents** must be emailed to the research attorney upon filing:
        **research_attorney@tulare.courts.ca.gov** (.doc, .docx, or .pdf only)
        """)

        st.markdown("## Courtroom Etiquette")
        st.markdown("""
        - Dress in a soft solid color; solid ties over patterned.
        - Look directly at the **webcam**, not the screen.
        - Position camera at **eye level** or slightly above.
        - Use a solid neutral wall or virtual background.
        - Light should face you (not behind you).
        - Speak one at a time; pause for audio/video lag.
        - **Mute when not speaking.**
        - **Recording is strictly prohibited** without express prior consent.
        """)

    with tab2:
        st.markdown("## Pre-Hearing Checklist")
        st.markdown("### Request & Approval")
        st.checkbox("Confirmed hearing type is eligible for remote appearance", key="tu_ck1")
        st.checkbox("Submitted online request form (Zoom) OR scheduled CourtCall (5+ court days prior)", key="tu_ck2")
        st.checkbox("Received court confirmation email (Zoom link or CourtCall confirmation)", key="tu_ck3")
        st.checkbox("Gave notice to all parties per CRC 3.672 and CCP 367.75", key="tu_ck4")
        st.markdown("### Day-Before Preparation")
        st.checkbox("Checked tentative ruling (posted by 3:00 PM day before)", key="tu_ck5")
        st.checkbox("Emailed courtesy copies of law & motion docs to research_attorney@tulare.courts.ca.gov", key="tu_ck6")
        st.markdown("### Day-Of Preparation")
        st.checkbox("Physical exhibits delivered to courtroom (if applicable)", key="tu_ck7")
        st.checkbox("Zoom app installed and tested", key="tu_ck8")
        st.checkbox("Headset connected and tested", key="tu_ck9")
        st.checkbox("Quiet, indoor location with neutral background and front-facing light", key="tu_ck10")
        st.checkbox("Zoom display name set to: J. Doe Retained Counsel", key="tu_ck11")
        st.success("Once all applicable boxes are checked, you are ready to appear!")

    with tab3:
        st.markdown("## Frequently Asked Questions")

        with st.expander("Do I need to file RA-010/RA-020 forms like Fresno?"):
            st.write("**No.** Tulare does not require Judicial Council forms. Just submit the online request form on the court's website and give notice per CRC 3.672 and CCP 367.75.")

        with st.expander("Is there a free option for remote appearances?"):
            st.write("**Yes.** The court's Zoom-based system is completely free. Submit a request via the online form at tulare.courts.ca.gov/online-services/request-remote-hearings. CourtCall is the paid alternative (~$72).")

        with st.expander("How far in advance should I request a remote hearing?"):
            st.write("**Zoom:** No more than 1 week in advance. Court responds within 24 hours. Requests within 24 hours of the hearing are accommodated on a best-effort basis. **CourtCall:** No later than 5 court days prior per Local Rule 108.")

        with st.expander("Can our firm get on a weekly Zoom distribution list?"):
            st.write("**Yes.** Email **RemoteHearings@tulare.courts.ca.gov** to be added. This eliminates the need to submit individual requests for each hearing.")

        with st.expander("What hearings require in-person appearance?"):
            st.write("Settlement Conferences, Trial Readiness Conferences, Trials/Contested/Evidentiary Hearings, Creditor Examinations/Orders of Examination, Restraining Orders (CH, WV, EA, GV), and Unlawful Detainer Trials.")

        with st.expander("Which departments handle our civil cases?"):
            st.write("**Visalia:** Dept 1 (Judge Mathias, plaintiffs A/B/C/S), Dept 2 (Judge Hillman, plaintiffs D-L/R), Dept 7 (Judge Ide, plaintiffs M-Z). **Porterville:** Dept 19 (Judge Burke, all South County civil).")

        with st.expander("How do tentative rulings work in Tulare?"):
            st.write("Posted by **3:00 PM** the court day before the hearing at tulare.courts.ca.gov/general-information/tentative-rulings. To contest, notify the court AND all parties by **4:00 PM** via fax (559-733-6774), email (research_attorney@tulare.courts.ca.gov), or phone (559-730-5010). If no one contests, the tentative becomes the order.")

        with st.expander("Do I need to send courtesy copies of law & motion docs?"):
            st.write("**Yes.** Per Local Rule 703, email courtesy copies to **research_attorney@tulare.courts.ca.gov** in .doc, .docx, or .pdf format upon filing.")

        with st.expander("What naming convention should I use in Zoom?"):
            st.write("For private retained counsel: **J. Doe Retained Counsel** (first initial, last name, then 'Retained Counsel').")

        with st.expander("Who do I contact for help?"):
            st.write("""
            - **Remote Hearing Assistance:** (559) 738-2330
            - **CourtCall:** (888) 882-6878 / CourtCall.com
            - **Visalia Civil Clerk:** (559) 730-5000
            - **Porterville Civil Clerk:** (559) 782-3700
            - **Research Attorney:** research_attorney@tulare.courts.ca.gov
            """)