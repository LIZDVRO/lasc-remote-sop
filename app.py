import streamlit as st

st.set_page_config(
    page_title="Remote Appearance SOP | Manock Law",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 820px; }
        h1, h2, h3 { font-weight: 400 !important; letter-spacing: -0.02em; }
        h1 { border-bottom: 2px solid #1f2937; padding-bottom: 10px; margin-bottom: 20px; }
        h2 { border-bottom: 1px solid #e5e7eb; padding-bottom: 5px; margin-top: 30px; }
        .stTabs [data-baseweb="tab-list"] { gap: 24px; }
        .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: transparent; border-radius: 0px; border-bottom: 2px solid transparent; padding-top: 10px; padding-bottom: 10px; }
        .stTabs [aria-selected="true"] { border-bottom: 2px solid #1f2937 !important; color: #1f2937 !important; }
        .streamlit-expanderHeader { font-weight: 500; color: #1f2937; border-bottom: 1px solid #e5e7eb; padding-left: 0px !important; background-color: transparent !important; }
        [data-testid="stExpander"] { border: none !important; box-shadow: none !important; background-color: transparent !important; }
        #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Select Court")
    court = st.radio("Which courthouse?", [
        "Los Angeles (Stanley Mosk)",
        "Fresno County",
        "Tulare County",
        "Kings County",
        "Madera County",
        "Sacramento County"
    ], label_visibility="collapsed")
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
        st.markdown("Most civil hearings are eligible for remote appearance, **except:** Trials and Prove-Ups (except Small Claims), Settlement Conferences, Final Status Conferences (in-person strongly encouraged), and Appeals. *Always verify with the assigned department's [courtroom information page](https://www.lacourt.ca.gov/courtroominformation/).*")
        st.markdown("## Procedure A: Advance Scheduling")
        st.markdown("*Use when the hearing is more than one day away (up to 30 days in advance).*")
        st.markdown("""
        1. Go to [my.lacourt.org/laccwelcome](https://my.lacourt.org/laccwelcome).
        2. **Sign in** with your Court ID (or create one).
        3. Click **Schedule**, enter the **Case Number**, click **Lookup Case**.
        4. Select role: **Attorney**. Enter attendee info (name, email, Bar number).
        5. Select the party you represent and the hearing event.
        6. Review and click **Schedule**. Print/save confirmation.
        """)
        st.markdown("## Procedure B: Same-Day Check-In")
        st.markdown("*Use on the actual morning of the hearing.*")
        st.markdown("""
        1. Go to [lacc.lacourt.org](https://lacc.lacourt.org). Select **Civil**. Click **I Agree**.
        2. Search by **Case Number**, click **Select**.
        3. Enter email, select your name and party, click **Check-In**.
        4. Click **JOIN** to enter the Teams lobby.
        """)
        st.markdown("## Joining via Microsoft Teams")
        st.markdown("Choose **Continue on this browser** or **Join on the Teams app**. Enter your name, turn camera OFF, mute mic, click **Join now**. Wait in lobby. Use **Raise Hand** to be recognized.")
        st.markdown("## Presenting Evidence")
        st.markdown("Deliver **physical copies** to the courtroom before the hearing. The court may use Teams **screen-share**. For Small Claims: use the [Digital Evidence System](https://www.lacourt.ca.gov/digitalevidence/).")
    with tab2:
        st.markdown("## Hearing Day Pre-Flight Checklist")
        st.checkbox("Confirmed department eligibility for remote appearance", key="la_ck1")
        st.checkbox("Verified case number and hearing time", key="la_ck2")
        st.checkbox("Signed into LACourtConnect", key="la_ck3")
        st.checkbox("Physical exhibits delivered to courtroom (if applicable)", key="la_ck4")
        st.checkbox("Headset connected and tested", key="la_ck5")
        st.checkbox("Teams camera OFF and mic MUTED before joining lobby", key="la_ck6")
        st.checkbox("Background is neutral and lighting is adequate", key="la_ck7")
        st.success("Once all boxes are checked, click **JOIN** in LACourtConnect!")
    with tab3:
        st.markdown("## Frequently Asked Questions")
        with st.expander("Is there a fee to use LACourtConnect?"):
            st.write("No. LACourtConnect is completely free.")
        with st.expander("Can we use CourtCall for LASC hearings?"):
            st.write("No. LASC transitioned entirely to LACourtConnect in 2025.")
        with st.expander("What hearings are NOT eligible?"):
            st.write("Trials/Prove-Ups (except Small Claims), Settlement Conferences, Final Status Conferences, and Appeals.")
        with st.expander("My hearing isn't showing up. What do I do?"):
            st.write("Same-Day Check-in only shows today's hearings. Use Advance Scheduling for future dates. Call LACC Help Desk at **(213) 830-0400**.")
        with st.expander("Can I appear by phone only?"):
            st.write("Yes, but not recommended. Judicial officers strongly prefer camera-on.")
        with st.expander("Who do I contact for help?"):
            st.write("**LACC Help Desk:** (213) 830-0400 (7:30 AM - 5:30 PM, court days)")

# ═══════════════════════════════════════════════
#  FRESNO COUNTY SUPERIOR COURT
# ═══════════════════════════════════════════════
elif court == "Fresno County":
    st.title("Fresno County Superior Court")
    st.markdown("**Remote Appearance SOP**")
    st.markdown("*Platforms: [CourtCall](https://courtcall.com) (~$72) | [Zoom](https://zoom.us) (Free, select depts)*")
    st.error("**⚠️ STOP - Check Your Department First!**\n\n**If your hearing is a CMC in Department 97E, you do NOT need to file RA-010/RA-020 forms.** Skip the procedure below and go directly to [CourtCall.com](https://courtcall.com) or call (888) 882-6878. Schedule at least 2 court days before (~$72). *Per Local Rule 2.2.4.*")
    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])
    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Remote Appearance Info](https://www.fresno.courts.ca.gov/divisions/civil/remote-appearance-information)")
            st.markdown("- [CourtCall Scheduling](https://courtcall.com)")
        with col2:
            st.markdown("- [RA-010 Form](https://www.fresno.courts.ca.gov/system/files/forms-and-filings/ra-010-notice-remote-appearance.pdf)")
            st.markdown("- [RA-020 Form](https://www.fresno.courts.ca.gov/system/files/forms-and-filings/ra-020-order-regarding-remote-appearance.pdf)")
        st.warning("**Fresno requires advance filing of RA-010 + RA-020 forms and court approval (except Dept. 97E CMCs).**")
        st.info("**CourtCall:** (888) 882-6878 | **Civil Zoom:** (559) 457-1810 | **Probate Zoom:** (559) 457-1760")
        st.markdown("## Step 1: File RA-010 + RA-020")
        st.markdown("File both forms with the court. E-file RA-010 as 'NOTICE OF REMOTE APPEARANCE' (separate document). Include email or SASE.")
        st.markdown("## Step 2: Filing Deadlines")
        st.markdown("### Evidentiary Hearings")
        st.markdown("| Scenario | File By | Opposition By |\n|---|---|---|\n| >15 court days out | 10 court days before | 5 court days before |\n| Within 15 days (moving) | With moving papers | 12:00 PM day before |\n| Within 15 days (non-moving) | 2:00 PM day before | 12:00 PM day before |")
        st.markdown("### Non-Evidentiary Hearings")
        st.markdown("| Scenario | File By |\n|---|---|\n| >3 court days out | 2 court days before |\n| Within 3 days (moving) | With moving papers |\n| Within 3 days (non-moving) | 2:00 PM day before |")
        st.markdown("## Step 3: Serve opposing counsel on same deadlines.")
        st.markdown("## Step 4: Wait for court's ruling by email/SASE.")
        st.markdown("## Step 5A: CourtCall (~$72, audio) - schedule 2+ court days prior at [CourtCall.com](https://courtcall.com) or (888) 882-6878.")
        st.markdown("## Step 5B: Zoom (free, video) - court emails Meeting ID/Password. Join with camera ON, mic MUTED.")
        st.markdown("## Tentative Rulings")
        st.markdown("Posted by **2:00 PM** the court day before. To contest: notify clerk AND all parties by **4:00 PM**. If no contest, tentative becomes the order.")
    with tab2:
        st.markdown("## Pre-Hearing Checklist")
        st.checkbox("Confirmed department (97E CMC? Skip to CourtCall)", key="fr_ck0")
        st.checkbox("RA-010 and RA-020 filed with court", key="fr_ck1")
        st.checkbox("Served on all parties", key="fr_ck2")
        st.checkbox("Court order GRANTING remote appearance received", key="fr_ck3")
        st.checkbox("CourtCall scheduled OR Zoom details received", key="fr_ck4")
        st.checkbox("Checked tentative ruling (posted by 2:00 PM day before)", key="fr_ck5")
        st.checkbox("Headset connected and tested", key="fr_ck6")
        st.success("Ready to appear!")
    with tab3:
        st.markdown("## FAQ")
        with st.expander("CMC in Dept. 97E - do we file RA forms?"):
            st.write("**No.** Contact CourtCall directly. Per Local Rule 2.2.4.")
        with st.expander("Fees?"):
            st.write("CourtCall: ~$72. Zoom: Free.")
        with st.expander("Same-day check-in like LA?"):
            st.write("No. Fresno requires advance RA form filing and court approval.")
        with st.expander("Who do I contact?"):
            st.write("**CourtCall:** (888) 882-6878 | **Civil Zoom:** (559) 457-1810 | **Probate Zoom:** (559) 457-1760")

# ═══════════════════════════════════════════════
#  TULARE COUNTY SUPERIOR COURT
# ═══════════════════════════════════════════════
elif court == "Tulare County":
    st.title("Tulare County Superior Court")
    st.markdown("**Remote Appearance SOP (Civil Only)**")
    st.markdown("*Platforms: [Zoom](https://zoom.us) (Free) | [CourtCall](https://courtcall.com) (~$72)*")
    st.success("**💡 TIP:** Email **RemoteHearings@tulare.courts.ca.gov** to join the weekly Zoom distribution list - no individual requests needed!")
    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])
    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Request Remote Hearing](https://www.tulare.courts.ca.gov/online-services/request-remote-hearings)")
            st.markdown("- [CourtCall](https://courtcall.com)")
        with col2:
            st.markdown("- [Tentative Rulings](https://www.tulare.courts.ca.gov/general-information/tentative-rulings)")
            st.markdown("- [Judicial Assignments](https://www.tulare.courts.ca.gov/general-information/judicial-assignments)")
        st.info("**Remote Hearing Help:** (559) 738-2330 | **CourtCall:** (888) 882-6878 | **Visalia Clerk:** (559) 730-5000 | **Porterville Clerk:** (559) 782-3700")
        st.markdown("## Civil Departments")
        st.markdown("| Dept | Judge | Plaintiffs |\n|---|---|---|\n| 1 | Hon. David Mathias | A, B, C, S |\n| 2 | Hon. Bret Hillman | D-L, R |\n| 7 | Hon. Nathan Ide | M-Z (excl. R, S) |\n| 19 (Porterville) | Hon. Russell Burke | All South County |")
        st.markdown("## Eligibility")
        st.markdown("**Eligible:** CMCs, Law & Motion, Demurrers, Summary Judgments, OSC, Fee Waivers, Minor's Compromise, Prove-Ups, Name Changes, Ex Parte.")
        st.markdown("**NOT eligible (in-person):** Settlement Conferences, Trial Readiness, Trials/Contested/Evidentiary, Creditor Exams, Restraining Orders, UD Trials.")
        st.markdown("## Option A: Zoom via Court Web Form (Free)")
        st.markdown("1. Submit the [online form](https://www.tulare.courts.ca.gov/online-services/request-remote-hearings) (no more than **1 week** in advance).\n2. Court responds within **24 hours** by email with Zoom credentials.\n3. Give notice per **CRC 3.672** and **CCP 367.75**.\n4. Naming convention: **J. Doe Retained Counsel**")
        st.markdown("## Option B: CourtCall (~$72)")
        st.markdown("Per Local Rule 108. Schedule **5+ court days** prior at [CourtCall.com](https://courtcall.com) or (888) 882-6878.")
        st.markdown("## Tentative Rulings")
        st.markdown("Posted by **3:00 PM** day before at [Tentative Rulings page](https://www.tulare.courts.ca.gov/general-information/tentative-rulings). Contest by **4:00 PM** via fax (559-733-6774), email (research_attorney@tulare.courts.ca.gov), or phone (559-730-5010).")
        st.markdown("## Courtesy Copies (Local Rule 703)")
        st.markdown("Email law & motion docs to **research_attorney@tulare.courts.ca.gov** (.doc/.docx/.pdf).")
    with tab2:
        st.markdown("## Pre-Hearing Checklist")
        st.checkbox("Hearing type is eligible for remote", key="tu_ck1")
        st.checkbox("Online form submitted (Zoom) OR CourtCall scheduled (5+ days)", key="tu_ck2")
        st.checkbox("Court confirmation email received", key="tu_ck3")
        st.checkbox("Notice given to all parties (CRC 3.672 / CCP 367.75)", key="tu_ck4")
        st.checkbox("Checked tentative ruling (by 3:00 PM day before)", key="tu_ck5")
        st.checkbox("Courtesy copies emailed to research attorney", key="tu_ck6")
        st.checkbox("Zoom display name: J. Doe Retained Counsel", key="tu_ck7")
        st.success("Ready to appear!")
    with tab3:
        st.markdown("## FAQ")
        with st.expander("Do I need RA-010/RA-020 forms like Fresno?"):
            st.write("**No.** Just submit the online form and give notice per CRC 3.672 / CCP 367.75.")
        with st.expander("Weekly distribution list?"):
            st.write("Email **RemoteHearings@tulare.courts.ca.gov** to be added.")
        with st.expander("Timing?"):
            st.write("**Zoom:** No more than 1 week in advance; court responds within 24 hours. **CourtCall:** 5+ court days prior.")
        with st.expander("Tentative rulings?"):
            st.write("Posted by 3:00 PM day before. Contest by 4:00 PM via fax/email/phone.")
        with st.expander("Contacts?"):
            st.write("**Remote Hearing Help:** (559) 738-2330 | **CourtCall:** (888) 882-6878 | **Visalia Clerk:** (559) 730-5000 | **Porterville Clerk:** (559) 782-3700")
# ═══════════════════════════════════════════════
#  KINGS COUNTY SUPERIOR COURT
# ═══════════════════════════════════════════════
elif court == "Kings County":
    st.title("Kings County Superior Court")
    st.markdown("**Remote Appearance SOP (Civil Only)**")
    st.markdown("*Platform: [CourtCall](https://courtcall.com) (~$72/appearance) | Audio only*")

    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])

    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Court Calls Info](https://www.kings.courts.ca.gov/general-information/court-calls)")
            st.markdown("- [CourtCall Scheduling](https://courtcall.com)")
        with col2:
            st.markdown("- [Tentative Rulings](https://kingscourtscagov.sharepoint.com/:f:/s/KingsCourtPublicAccess/EnaOoFqXlW9DhVCjZYXubMoBQgQxHSzy33GZfFhBV1N4FQ?e=cG393e)")
            st.markdown("- [Local Rules (PDF)](https://www.kings.courts.ca.gov/system/files/local-rules/kingscountylocalrules_01-01-26_final_updated-1.pdf)")
        st.info("**CourtCall:** (888) 882-6878 | **Court Clerk:** (559) 582-1010")

        st.warning("**Kings County uses CourtCall ONLY for telephonic remote appearances.** There is no Zoom-based web form option. All remote appearances require prior court approval.")

        st.markdown("## Eligibility (per Local Rule 305)")
        st.markdown("**Eligible (with court approval):** Case Management Conferences, Civil Law and Motion hearings, Probate hearings.")
        st.markdown("**NOT eligible (in-person required):** Readiness Conferences, Settlement Conferences, Trial Calls, Evidentiary Hearings, Trials.")

        st.markdown("## CourtCall Departments (Civil)")
        st.markdown("""
        | Dept | Judge |
        |---|---|
        | 1 | Hon. Jennifer Giuliani |
        | 2 | Hon. Robert Shane Burns |
        | 3 | Hon. Kendra Weber |
        | 4 | Comr. Mark Skinner |
        | 5 | Hon. Rise A. Donlon |
        | 6 | Hon. Marianne Gilbert |
        | 7 | Hon. Melissa R. D'Morias |
        | 8 | Hon. Kathy Ciuffini |
        | 9 | Presiding Judge |
        | 10 | Hon. Michael J. Reinhart |
        """)

        st.markdown("## Procedure")
        st.markdown("""
        1. Contact CourtCall at **(888) 882-6878** or schedule online at [CourtCall.com](https://courtcall.com).
        2. Provide: hearing date/time, department number, calendar type, case name/number, and your info.
        3. Pay the fee (~$72; Visa/MC/Amex/Discover).
        4. Receive confirmation with check-in time.
        5. On hearing day, call in **at least 5 minutes** before your scheduled time.
        6. First counsel requesting telephonic appearance pays conference call costs.
        """)

        st.markdown("## Tentative Rulings (Local Rule 313)")
        st.markdown("Tentative rulings are posted on the court's [SharePoint site](https://kingscourtscagov.sharepoint.com/:f:/s/KingsCourtPublicAccess/EnaOoFqXlW9DhVCjZYXubMoBQgQxHSzy33GZfFhBV1N4FQ?e=cG393e). Per CRC 3.1308, rulings are available by **3:00 PM** the court day before the hearing. To contest, notify the court and all parties by **4:00 PM**.")

    with tab2:
        st.markdown("## Pre-Hearing Checklist")
        st.checkbox("Confirmed hearing type is eligible (CMC, Law & Motion, or Probate)", key="ki_ck1")
        st.checkbox("CourtCall scheduled with case info and department number", key="ki_ck2")
        st.checkbox("CourtCall fee paid (~$72)", key="ki_ck3")
        st.checkbox("CourtCall confirmation received", key="ki_ck4")
        st.checkbox("Checked tentative ruling (by 3:00 PM day before)", key="ki_ck5")
        st.checkbox("Ready to call in 5 minutes before scheduled time", key="ki_ck6")
        st.success("Ready to appear!")

    with tab3:
        st.markdown("## FAQ")
        with st.expander("Can I appear by Zoom in Kings County?"):
            st.write("Kings County does not offer a Zoom-based remote appearance option for civil hearings. CourtCall (telephonic, ~$72) is the only remote appearance platform.")
        with st.expander("What hearings can I attend remotely?"):
            st.write("Case Management Conferences, Civil Law & Motion, and Probate hearings (with prior court approval). Readiness Conferences, Settlement Conferences, and Trials require in-person attendance.")
        with st.expander("Who pays for the CourtCall conference call?"):
            st.write("Per the court's policy, the first counsel requesting a telephonic appearance pays the costs of any conference calls.")
        with st.expander("Where are tentative rulings posted?"):
            st.write("On the court's SharePoint site. Access via the link on the [court homepage](https://www.kings.courts.ca.gov) under 'Tentative Rulings.'")
        with st.expander("Contacts?"):
            st.write("**CourtCall:** (888) 882-6878 | **Court Clerk:** (559) 582-1010")
# ═══════════════════════════════════════════════
#  MADERA COUNTY SUPERIOR COURT
# ═══════════════════════════════════════════════
elif court == "Madera County":
    st.title("Madera County Superior Court")
    st.markdown("**Remote Appearance SOP (Civil Only)**")
    st.markdown("*Platforms: [Zoom](https://zoom.us) (Free, via Google Form) | [CourtCall](https://courtcall.com) (~$72)*")

    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])

    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Zoom Appearance Request Form](https://forms.gle/FrzfvqjSYH1xWU5U7)")
            st.markdown("- [CourtCall Scheduling](https://courtcall.com)")
            st.markdown("- [Remote Appearance Info](https://www.madera.courts.ca.gov/general-information/covid-19-information/remote-video-appearances)")
        with col2:
            st.markdown("- [RA-010 Form](https://www.madera.courts.ca.gov/system/files/ra-010.pdf)")
            st.markdown("- [RA-020 Form](https://www.madera.courts.ca.gov/system/files/forms-and-filings/order-regarding-remote-appearance-ra-020-1-1-2022.pdf)")
            st.markdown("- [Local Rules (PDF)](https://www.madera.courts.ca.gov/system/files/local-rules/final-local-rules-eff-jan-1-2026.pdf)")
        st.info("**Court Clerk:** (559) 675-7721 | **CourtCall:** (888) 882-6878")

        st.markdown("## Overview")
        st.markdown("Madera uses **Zoom** as its preferred remote appearance platform. Requests are submitted via a **Google Form**. For civil proceedings, RA-010 and related forms may also need to be filed per **CRC 3.672** and **CCP 367.75**. CourtCall is available as an alternative in select departments per Local Rule 2.7.")

        st.markdown("## Civil Departments (Probate-Civil Division)")
        st.markdown("""
        | Dept | Judge | Notes |
        |---|---|---|
        | 37 | Hon. Miguel Valdovinos | CourtCall available |
        | 40 | Hon. D. Lynn Collet | CourtCall available |
        | 44 | Hon. Eric J. LiCalsi | CourtCall available |
        | 17 | Hon. Michael J. Jurkovich | Supervising Civil Judge; CourtCall available |
        | 21 | Hon. James E. Oakley | CourtCall available |
        """)
        st.markdown("*All departments located at 200 South G Street, Madera, CA 93637.*")

        st.markdown("## Option A: Zoom via Google Form (Free)")
        st.markdown("""
        1. Fill out the [Zoom Appearance Request Form](https://forms.gle/FrzfvqjSYH1xWU5U7).
        2. For civil cases, also file **RA-010** (Notice of Remote Appearance) per CRC 3.672.
        3. Serve RA-010 on all parties per CCP 367.75.
        4. Court provides Zoom credentials by email.
        5. On hearing day, join Zoom. **Display your full first and last name.**
        """)

        st.markdown("## Option B: CourtCall (~$72)")
        st.markdown("Per Local Rule 2.7. Contact CourtCall at **(888) 882-6878** or [CourtCall.com](https://courtcall.com). Available in Depts 17, 21, 37, 40, and 44.")

        st.markdown("## RA Forms (per CRC 3.672)")
        st.markdown("""
        | Form | Purpose |
        |---|---|
        | [RA-010](https://www.madera.courts.ca.gov/system/files/ra-010.pdf) | Notice of Remote Appearance |
        | [RA-015](https://www.madera.courts.ca.gov/system/files/ra-015.pdf) | Opposition to Remote Proceeding |
        | [RA-020](https://www.madera.courts.ca.gov/system/files/forms-and-filings/order-regarding-remote-appearance-ra-020-1-1-2022.pdf) | Order Regarding Remote Appearance |
        | [RA-025](https://www.madera.courts.ca.gov/system/files/ra-025.pdf) | Request to Appear Remotely |
        | [RA-030](https://www.madera.courts.ca.gov/system/files/ra-030.pdf) | Order on Request to Appear Remotely |
        """)

        st.markdown("## Tentative Rulings (Local Rule 3.3.6)")
        st.markdown("Per CRC 3.1308, tentative rulings are available by **3:00 PM** the court day before the hearing. To contest, notify the court and all parties by **4:00 PM**.")

    with tab2:
        st.markdown("## Pre-Hearing Checklist")
        st.checkbox("Submitted Zoom Appearance Request Form (Google Form)", key="ma_ck1")
        st.checkbox("Filed RA-010 with the court (if required by CRC 3.672)", key="ma_ck2")
        st.checkbox("Served RA-010 on all parties per CCP 367.75", key="ma_ck3")
        st.checkbox("Received Zoom credentials from court OR CourtCall confirmation", key="ma_ck4")
        st.checkbox("Checked tentative ruling (by 3:00 PM day before)", key="ma_ck5")
        st.checkbox("Zoom display name shows full first and last name", key="ma_ck6")
        st.success("Ready to appear!")

    with tab3:
        st.markdown("## FAQ")
        with st.expander("What platform does Madera use?"):
            st.write("**Zoom** is the preferred platform (free). Requests are submitted via a Google Form. CourtCall (~$72, audio only) is also available in select departments per Local Rule 2.7.")
        with st.expander("Do I need to file RA-010 forms?"):
            st.write("For civil proceedings governed by CRC 3.672, yes - file RA-010 and serve it on all parties. Also fill out the Google Form for the Zoom link.")
        with st.expander("Where is the courthouse?"):
            st.write("200 South G Street, Madera, CA 93637.")
        with st.expander("Naming convention for Zoom?"):
            st.write("The court requires participants to **fully display their first and last names** when appearing remotely.")
        with st.expander("Contacts?"):
            st.write("**Court Clerk:** (559) 675-7721 | **CourtCall:** (888) 882-6878")
# ═══════════════════════════════════════════════
#  SACRAMENTO COUNTY SUPERIOR COURT
# ═══════════════════════════════════════════════
elif court == "Sacramento County":
    st.title("Sacramento County Superior Court")
    st.markdown("**Remote Appearance SOP (Civil Only)**")
    st.markdown("*Platform: [ZoomGov](https://zoomgov.com) (Free) | No CourtCall*")

    st.success("**💡 Sacramento PRESUMES remote appearance for all non-evidentiary civil hearings.** No prior approval needed - just give notice per CCP 367.75. Zoom links are published in each tentative ruling.")

    tab1, tab2, tab3 = st.tabs(["📋 SOP & Workflows", "✅ Checklist", "❓ FAQ"])

    with tab1:
        st.markdown("## Important Links")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- [Civil Motions Info](https://www.saccourt.ca.gov/civil/motions-hearings-general.aspx)")
            st.markdown("- [Zoom Links by Department (PDF)](https://www.saccourt.ca.gov/civil/docs/civil-court-zoom-links.pdf)")
            st.markdown("- [Case Portal (Tentative Rulings)](https://prod-portal-sacramento-ca.journaltech.com/public-portal/)")
        with col2:
            st.markdown("- [Public Notice - Remote Procedures](https://www.saccourt.ca.gov/civil/docs/pn-civil-remote-and-in-person-proceedings-effective-monday-january-3-2022.pdf)")
            st.markdown("- [Local Rules](https://www.saccourt.ca.gov/local-rules/local-rules.aspx)")
            st.markdown("- [Presiding Judge Info](https://www.saccourt.ca.gov/civil/presiding-judge-info.aspx)")
        st.info("**Tentative Ruling Phone:** (916) 874-7848 or (916) 874-7858 | **L&M Oral Argument Line:** (916) 874-2615 | **CMC Oral Argument Line:** (916) 874-5463 | **Toll-Free Zoom Phone:** (833) 568-8864 | **Civil Self-Help:** (916) 874-1421")

        st.markdown("## Two Tracks: Non-Evidentiary vs. Evidentiary")

        st.markdown("### Non-Evidentiary Hearings (Presumed Remote)")
        st.markdown("""
        The court **presumes** all parties appear remotely. No prior approval or RA-010 filing needed. Just give notice per CCP 367.75.

        **Hearing types:**
        Civil Jury Trial Assignment, Short Cause Trial Assignment, Case Management, Complex Civil Case Management, Civil Law & Motion, Presiding Judge L&M, Writ of Mandate, Minor's Compromise, Fee Waivers.

        **How to appear:**
        1. Check the **tentative ruling** (posted by 2:00 PM day before) - the Zoom link is in the ruling.
        2. Or use the [Zoom Links PDF](https://www.saccourt.ca.gov/civil/docs/civil-court-zoom-links.pdf) for your department.
        3. Join via ZoomGov with video/audio. Phone-in via **(833) 568-8864** + Meeting ID.
        """)

        st.markdown("### Evidentiary Hearings (RA-010 Required)")
        st.markdown("""
        **Hearing types:** Civil Jury Trials, Civil Short Cause Trials, Order of Examination (OX) Hearings, Civil Harassment Hearings/Trials.

        **How to request:**
        1. File **RA-010** (Notice of Remote Appearance) in the noticed/assigned trial department.
        2. Serve opposing parties per CCP 367.75.
        3. If previously filed, provide endorsed copies to the department.
        4. Opposition may file RA-015.
        """)

        st.markdown("## Civil Home Court Departments")
        st.markdown("""
        | Dept | Judge |
        |---|---|
        | 3A | Judge Jennifer K. Rockwell |
        | 3B | Judge Stephen P. Acquisto |
        | 8A | Judge Jill H. Talley |
        | 8B | Judge Lauri A. Damrell |
        | 8C | Judge Richard C. Miadich |
        | 8D | Judge Julie G. Yap |
        | 10A | Judge George Acero |
        | 10B | Judge Steven M. Gevercer |
        | 10C | Judge Augustin Jimenez |
        | 11B | Judge Thadd Blizzard |
        | 12B | Judge Ernest Sawtelle |
        | 13A | Judge James P. Arguelles |
        | 14A | Judge Julie Weng-Gutierrez |
        | 15A | Judge Donald J. Currier |
        | 16B | Judge Shelleyanne W.L. Chang |
        | 16C | Judge Christopher E. Krueger |
        | 16D | Judge Richard K. Sueyoshi |
        | 17A | Judge Lawrence G. Brown |
        """)

        st.markdown("## Tentative Rulings (Local Rule 1.06)")
        st.markdown("""
        Posted by **2:00 PM** one court day before the hearing.

        **To access:** Search your case on the [public portal](https://prod-portal-sacramento-ca.journaltech.com/public-portal/) or call **(916) 874-7848** / **(916) 874-7858**.

        **If you AGREE:** Do nothing. If no one contests by 4:00 PM, the tentative becomes the order.

        **If you DISAGREE:** Call the appropriate line by **4:00 PM** and notify the other party:
        - **Law & Motion:** (916) 874-2615
        - **CMC:** (916) 874-5463

        **If ruling says "APPEARANCE REQUIRED":** Attend the hearing (may appear via Zoom).
        """)

    with tab2:
        st.markdown("## Pre-Hearing Checklist")
        st.markdown("### Non-Evidentiary Hearings")
        st.checkbox("Gave notice to all parties per CCP 367.75", key="sac_ck1")
        st.checkbox("Checked tentative ruling (by 2:00 PM day before)", key="sac_ck2")
        st.checkbox("Located Zoom link (in tentative ruling or Zoom Links PDF)", key="sac_ck3")
        st.checkbox("ZoomGov app installed or browser ready", key="sac_ck4")
        st.checkbox("If contesting tentative: called oral argument line by 4:00 PM AND notified other party", key="sac_ck5")
        st.markdown("### Evidentiary Hearings")
        st.checkbox("Filed RA-010 in noticed/assigned department", key="sac_ck6")
        st.checkbox("Served RA-010 on all parties per CCP 367.75", key="sac_ck7")
        st.checkbox("Provided endorsed copies to department (if previously filed)", key="sac_ck8")
        st.success("Ready to appear!")

    with tab3:
        st.markdown("## FAQ")
        with st.expander("Do I need prior approval for non-evidentiary hearings?"):
            st.write("**No.** Sacramento presumes remote appearance for all non-evidentiary civil hearings. Just give notice per CCP 367.75. The Zoom link is in the tentative ruling.")
        with st.expander("Is CourtCall available in Sacramento?"):
            st.write("**No.** Sacramento is not on the CourtCall participating courts list. The court uses ZoomGov exclusively (free).")
        with st.expander("Where do I find the Zoom link?"):
            st.write("In the tentative ruling for your case (posted on the public portal by 2:00 PM day before). Or use the [Zoom Links PDF](https://www.saccourt.ca.gov/civil/docs/civil-court-zoom-links.pdf) which lists permanent links for each department.")
        with st.expander("When are RA-010 forms required?"):
            st.write("Only for **evidentiary** hearings: Jury Trials, Short Cause Trials, Order of Examination (OX), and Civil Harassment Hearings/Trials.")
        with st.expander("Can I call in by phone only?"):
            st.write("Yes. The toll-free number for all departments is **(833) 568-8864**. You will need the Meeting ID for your department (see the Zoom Links PDF).")
        with st.expander("Tentative ruling process?"):
            st.write("Posted by 2:00 PM day before. If you disagree, call the oral argument line by 4:00 PM (Law & Motion: 916-874-2615 / CMC: 916-874-5463) AND notify the other party. If no one contests, the tentative becomes the order.")
        with st.expander("Contacts?"):
            st.write("**Tentative Ruling Phone:** (916) 874-7848 or (916) 874-7858 | **L&M Oral Argument:** (916) 874-2615 | **CMC Oral Argument:** (916) 874-5463 | **Zoom Toll-Free:** (833) 568-8864 | **Civil Self-Help:** (916) 874-1421")