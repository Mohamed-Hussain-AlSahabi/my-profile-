import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Mohamed Hussein | AI & Software Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- EDIT THESE ----------
GITHUB = "https://github.com/Mohamed-Hussain-AlSahabi"
LINKEDIN = "https://www.linkedin.com/in/mohamed-alsahabi-25601a292"
EMAIL = "mohamedalsahabi@gmail.com"
CV_FILE = "CV.pdf"
# -------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #050816;
    --panel: rgba(12, 20, 38, .78);
    --line: rgba(148,163,184,.14);
    --text: #f8fafc;
    --muted: #94a3b8;
    --cyan: #22d3ee;
    --purple: #a855f7;
}

* {
    font-family: Inter, sans-serif;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    padding: 0;
}

.stApp {
    background:
      radial-gradient(circle at 8% 5%, rgba(34,211,238,.09), transparent 25%),
      radial-gradient(circle at 90% 12%, rgba(168,85,247,.10), transparent 28%),
      #050816;
    color: var(--text);
}

.block-container {
    max-width: 1240px;
    padding: 1.2rem 2rem 4rem;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}


/* =========================
   NAVBAR
========================= */

.nav {
    position: sticky;
    top: 10px;
    z-index: 50;

    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;

    padding: 12px 18px;
    margin-bottom: 25px;

    border: 1px solid var(--line);
    border-radius: 18px;

    background: rgba(5,8,22,.78);
    backdrop-filter: blur(18px);
}

.logo {
    font-size: 20px;
    font-weight: 800;
    white-space: nowrap;
}

.logo span {
    color: var(--cyan);
}

.navlinks {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}

.navlinks a {
    color: #cbd5e1 !important;
    text-decoration: none;
    margin: 0 9px;
    font-size: 13px;
}

.navlinks a:hover {
    color: var(--cyan) !important;
}


/* =========================
   BUTTONS
========================= */

.btn {
    display: inline-block;

    padding: 11px 17px;
    border-radius: 11px;

    text-decoration: none !important;
    font-weight: 700;
    font-size: 13px;

    color: white !important;

    border: 1px solid rgba(34,211,238,.45);

    background: linear-gradient(
        90deg,
        #0891b2,
        #7c3aed
    );

    box-shadow: 0 8px 30px rgba(34,211,238,.12);

    transition: .2s ease;
}

.btn:hover {
    transform: translateY(-2px);
}

.btn2 {
    background: rgba(15,23,42,.8);
    border-color: #334155;
}


/* =========================
   HERO
========================= */

.hero {
    position: relative;
    overflow: hidden;

    border: 1px solid var(--line);
    border-radius: 30px;

    padding: 48px;
    min-height: 540px;

    background:
        linear-gradient(
            135deg,
            rgba(12,20,38,.92),
            rgba(7,12,27,.80)
        );
}

.hero:before {
    content: "";

    position: absolute;

    width: 330px;
    height: 330px;

    border-radius: 50%;

    right: -130px;
    top: -140px;

    background: rgba(168,85,247,.13);

    filter: blur(8px);

    pointer-events: none;
}

.eyebrow {
    display: inline-block;

    padding: 7px 12px;

    border-radius: 999px;

    border: 1px solid rgba(34,211,238,.35);

    color: #67e8f9;

    background: rgba(34,211,238,.07);

    font-size: 12px;
    font-weight: 800;

    letter-spacing: .5px;
}

.hero h1 {
    font-size: clamp(40px, 6vw, 70px);

    line-height: 1.03;

    margin: 18px 0 12px;

    letter-spacing: -3px;
}

.gradient {
    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #818cf8,
            #c084fc
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero h3 {
    color: #cbd5e1;

    font-size: 19px;

    font-weight: 500;

    line-height: 1.5;
}

.hero p {
    color: var(--muted);

    line-height: 1.85;

    max-width: 700px;

    font-size: 15px;
}


/* =========================
   PROFILE IMAGE
========================= */

.profile-container {
    display: flex;

    justify-content: center;
    align-items: center;

    width: 100%;

    padding-top: 55px;
}

.profile-wrap {
    width: min(310px, 75vw);
    aspect-ratio: 1 / 1;

    padding: 7px;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #22d3ee,
            #7c3aed,
            #ec4899,
            #22d3ee
        );

    box-shadow:
        0 0 65px rgba(34,211,238,.16);
}

.profile {
    width: 100%;
    height: 100%;

    object-fit: cover;
    object-position: center center;

    border-radius: 50%;

    border: 7px solid #07101f;

    display: block;
}


/* =========================
   STATS
========================= */

.statrow {
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 10px;

    margin-top: 28px;
}

.stat {
    min-width: 0;

    padding: 16px;

    border-radius: 16px;

    border: 1px solid var(--line);

    background: rgba(15,23,42,.6);

    text-align: center;
}

.stat b {
    display: block;

    font-size: 22px;
}

.stat span {
    color: var(--muted);

    font-size: 11px;

    line-height: 1.4;
}


/* =========================
   SECTIONS
========================= */

.section {
    margin: 65px 0 22px;
}

.section h2 {
    font-size: 30px;

    margin: 0;
}

.section p {
    color: var(--muted);

    margin-top: 7px;
}


/* =========================
   PANELS
========================= */

.panel {
    padding: 26px;

    border-radius: 22px;

    background: var(--panel);

    border: 1px solid var(--line);

    height: 100%;
}

.panel h3 {
    margin-top: 0;
}

.panel p,
.panel li {
    color: var(--muted);

    line-height: 1.75;
}


/* =========================
   SKILLS
========================= */

.skill {
    margin: 6px 5px 0 0;

    display: inline-block;

    padding: 8px 12px;

    border-radius: 10px;

    background: #0b1325;

    border: 1px solid #263653;

    color: #dbeafe;

    font-size: 12px;
}

.barline {
    margin: 16px 0;
}

.barhead {
    display: flex;

    justify-content: space-between;

    gap: 10px;

    color: #cbd5e1;

    font-size: 13px;
}

.bar {
    height: 7px;

    margin-top: 7px;

    border-radius: 10px;

    background: #172033;

    overflow: hidden;
}

.fill {
    height: 100%;

    border-radius: 10px;

    background:
        linear-gradient(
            90deg,
            #06b6d4,
            #8b5cf6
        );
}


/* =========================
   KNOWLEDGE CARDS
========================= */

.know {
    padding: 22px;

    border-radius: 19px;

    height: 100%;

    background:
        linear-gradient(
            145deg,
            #0b1325,
            #0a1020
        );

    border: 1px solid var(--line);
}

.know .icon {
    font-size: 28px;
}

.know h3 {
    margin: 10px 0;
}

.know ul {
    padding-left: 18px;

    margin-bottom: 0;
}

.know li {
    color: var(--muted);

    margin: 5px 0;

    font-size: 13px;
}


/* =========================
   PROJECTS
========================= */

.project {
    padding: 25px;

    border-radius: 21px;

    height: 100%;

    background:
        linear-gradient(
            145deg,
            rgba(15,23,42,.9),
            rgba(8,14,28,.9)
        );

    border: 1px solid var(--line);

    transition: .25s ease;
}

.project:hover {
    transform: translateY(-6px);

    border-color:
        rgba(34,211,238,.42);
}

.project .number {
    color: #64748b;

    font-size: 12px;
}

.project h3 {
    color: #e2e8f0;

    line-height: 1.4;
}

.project p {
    color: var(--muted);

    line-height: 1.7;
}


/* =========================
   CONTACT
========================= */

.contact {
    padding: 40px;

    border-radius: 25px;

    border: 1px solid rgba(34,211,238,.20);

    background:
        linear-gradient(
            135deg,
            rgba(34,211,238,.07),
            rgba(124,58,237,.08)
        );
}

.contact a {
    color: #67e8f9 !important;

    text-decoration: none;
}


/* =========================
   TABLET
========================= */

@media (max-width: 1000px) {

    .block-container {
        padding-left: 1.3rem;
        padding-right: 1.3rem;
    }

    .navlinks a {
        margin: 0 5px;
    }

    .hero {
        padding: 35px;
    }

    .hero h1 {
        font-size: clamp(38px, 7vw, 58px);
    }

    .profile-container {
        padding-top: 35px;
    }

}


/* =========================
   MOBILE
========================= */

@media (max-width: 800px) {

    .block-container {
        padding:
            .7rem
            .8rem
            3rem;
    }


    /* NAV */

    .nav {
        position: relative;

        flex-direction: column;

        text-align: center;

        padding: 14px;

        margin-bottom: 15px;
    }

    .logo {
        font-size: 18px;
    }

    .navlinks {
        display: none;
    }

    .nav .btn {
        width: 100%;

        text-align: center;

        padding: 12px;
    }


    /* HERO */

    .hero {
        padding: 27px 20px;

        min-height: auto;

        border-radius: 24px;

        text-align: left;
    }

    .hero h1 {
        font-size: clamp(
            35px,
            11vw,
            48px
        );

        letter-spacing: -2px;

        word-break: normal;
    }

    .hero h3 {
        font-size: 16px;
    }

    .hero p {
        font-size: 14px;

        line-height: 1.75;
    }

    .eyebrow {
        font-size: 10px;

        padding: 6px 10px;
    }


    /* HERO BUTTONS */

    .hero .btn {
        display: block;

        width: 100%;

        text-align: center;

        margin-top: 12px;

        padding: 13px 15px;
    }


    /* PROFILE */

    .profile-container {
        padding-top: 25px;

        padding-bottom: 5px;
    }

    .profile-wrap {
        width: min(
            230px,
            65vw
        );

        padding: 6px;
    }

    .profile {
        border-width: 5px;
    }


    /* STATS */

    .statrow {
        grid-template-columns:
            repeat(3, 1fr);

        gap: 7px;

        margin-top: 20px;
    }

    .stat {
        padding: 11px 5px;

        border-radius: 13px;
    }

    .stat b {
        font-size: 18px;
    }

    .stat span {
        font-size: 9px;
    }


    /* SECTIONS */

    .section {
        margin: 45px 0 18px;
    }

    .section h2 {
        font-size: 24px;
    }

    .section p {
        font-size: 13px;

        line-height: 1.6;
    }


    /* PANELS */

    .panel {
        padding: 20px;

        border-radius: 18px;
    }

    .panel p {
        font-size: 13px;
    }


    /* KNOW */

    .know {
        padding: 18px;

        border-radius: 17px;

        margin-bottom: 12px;
    }

    .know h3 {
        font-size: 17px;
    }


    /* PROJECTS */

    .project {
        padding: 20px;

        border-radius: 18px;

        margin-bottom: 12px;
    }

    .project h3 {
        font-size: 18px;
    }

    .project p {
        font-size: 13px;
    }


    /* CONTACT */

    .contact {
        padding: 25px 20px;

        border-radius: 20px;

        overflow-wrap: anywhere;
    }

    .contact h2 {
        font-size: 22px;
    }

    .contact p {
        font-size: 13px;
    }


    /* SKILLS */

    .skill {
        font-size: 11px;

        padding: 7px 9px;

        margin: 4px 3px 0 0;
    }

}


/* =========================
   SMALL PHONES
========================= */

@media (max-width: 430px) {

    .block-container {
        padding-left: .65rem;
        padding-right: .65rem;
    }

    .hero {
        padding: 23px 17px;
    }

    .hero h1 {
        font-size: 34px;

        line-height: 1.08;
    }

    .hero h3 {
        font-size: 15px;
    }

    .profile-wrap {
        width: 190px;
    }

    .statrow {
        grid-template-columns:
            1fr 1fr;
    }

    .stat:last-child {
        grid-column: 1 / -1;
    }

    .section h2 {
        font-size: 22px;
    }

    .panel {
        padding: 17px;
    }

    .contact {
        padding: 22px 17px;
    }

}


/* =========================
   TOUCH DEVICES
========================= */

@media (hover: none) {

    .project:hover {
        transform: none;

        border-color: var(--line);
    }

    .btn:hover {
        transform: none;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAV
# =========================================================

st.markdown(f"""
<div class="nav">

    <div class="logo">
        <span>MH</span> &nbsp; Mohamed Hussein
    </div>

    <div class="navlinks">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>

    <a class="btn"
       href="{CV_FILE}"
       target="_blank">
       ⬇ Download CV
    </a>

</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div id="home"></div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(
    [1.35, 1],
    gap="large"
)


with c1:

    st.markdown("""
    <div class="hero">

        <span class="eyebrow">
            ARTIFICIAL INTELLIGENCE STUDENT
        </span>

        <h1>
            Mohamed Hussein<br>
            <span class="gradient">
                Amin Hussein
            </span>
        </h1>

        <h3>
            AI Student · Software Engineer · Developer
        </h3>

        <p>
            Passionate about programming, Artificial Intelligence,
            Machine Learning and building practical software.
            I enjoy learning modern technologies and turning ideas
            into clean, useful applications.
        </p>

        <p>
            Currently developing my skills across software engineering,
            data, systems, networking and web development.
        </p>

        <a class="btn"
           href="#projects">
           View My Work →
        </a>

        &nbsp;

        <a class="btn btn2"
           href="#contact">
           Let's Talk
        </a>

    </div>
    """, unsafe_allow_html=True)


with c2:

    photo = Path("profile.jpg")

    if photo.exists():

        encoded_image = base64.b64encode(
            photo.read_bytes()
        ).decode()

        st.markdown(
            f"""
            <div class="profile-container">

                <div class="profile-wrap">

                    <img
                        class="profile"
                        src="data:image/jpeg;base64,{encoded_image}"
                    >

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="profile-container">

                <div class="profile-wrap"
                     style="
                     display:flex;
                     align-items:center;
                     justify-content:center;
                     color:white;
                     text-align:center;
                     ">

                    Add profile.jpg

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("""
    <div class="statrow">

        <div class="stat">
            <b>15+</b>
            <span>Projects & Practice</span>
        </div>

        <div class="stat">
            <b>10+</b>
            <span>Core Skills</span>
        </div>

        <div class="stat">
            <b>AI</b>
            <span>Study Focus</span>
        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ABOUT
# =========================================================

st.markdown("""
<div id="about"
     class="section">

    <h2>👨‍💻 About Me</h2>

    <p>
        Building my path from programming fundamentals
        to intelligent software.
    </p>

</div>
""", unsafe_allow_html=True)


a1, a2 = st.columns(
    2,
    gap="large"
)


with a1:

    st.markdown("""
    <div class="panel">

        <h3>Who I Am</h3>

        <p>
        My name is
        <b>Mohamed Hussein Amin Hussein</b>.
        I am an Artificial Intelligence student interested
        in software development and intelligent systems.
        </p>

        <p>
        I have studied C++, Python, OOP, databases,
        data structures, machine learning,
        operating systems, networking and software engineering.
        </p>

    </div>
    """, unsafe_allow_html=True)


with a2:

    st.markdown("""
    <div class="panel">

        <h3>My Direction</h3>

        <p>
        I am working toward becoming a strong software engineer
        with an AI background, combining programming,
        problem solving, data and modern application development.
        </p>

        <p>
        <b>Focus:</b>
        Software Engineering · AI/ML · Python · C++ · Web Applications
        </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# SKILLS
# =========================================================

st.markdown("""
<div id="skills"
     class="section">

    <h2>⚡ Skills & Expertise</h2>

    <p>
        My current technical toolkit.
    </p>

</div>
""", unsafe_allow_html=True)


s1, s2 = st.columns(
    2,
    gap="large"
)


left_skills = [
    ("C++ / OOP", 90),
    ("Python / OOP", 90),
    ("Data Structures", 85),
    ("Database", 80),
    ("Machine Learning", 75)
]

right_skills = [
    ("Operating Systems", 80),
    ("Software Engineering", 85),
    ("Advanced Software Engineering", 75),
    ("Computer Networks", 80),
    ("Web Development", 85)
]


for col, group in [
    (s1, left_skills),
    (s2, right_skills)
]:

    with col:

        st.markdown(
            '<div class="panel">',
            unsafe_allow_html=True
        )

        for name, pct in group:

            st.markdown(
                f"""
                <div class="barline">

                    <div class="barhead">
                        <span>{name}</span>
                        <span>{pct}%</span>
                    </div>

                    <div class="bar">

                        <div class="fill"
                             style="width:{pct}%">
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# =========================================================
# KNOWLEDGE
# =========================================================

st.markdown("""
<div class="section">

    <h2>🧠 What I Know</h2>

</div>
""", unsafe_allow_html=True)


knowledge = [

    (
        "💻",
        "Programming",
        "C++",
        "Python",
        "OOP Concepts"
    ),

    (
        "📊",
        "Data & Algorithms",
        "Data Structures",
        "Algorithms",
        "Problem Solving"
    ),

    (
        "🗄️",
        "Databases",
        "Database Design",
        "SQL",
        "Data Management"
    ),

    (
        "🤖",
        "AI & ML",
        "Machine Learning",
        "Data Processing",
        "Model Building"
    ),

    (
        "⚙️",
        "Systems",
        "Operating Systems",
        "Processes",
        "Memory Management"
    ),

    (
        "🌐",
        "Networks",
        "Computer Networks",
        "Protocols",
        "Network Fundamentals"
    )

]


cols = st.columns(3)


for i, item in enumerate(knowledge):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div 
