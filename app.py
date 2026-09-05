import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Mohamed Hussein | AI Student",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# SETTINGS
# =========================

GITHUB = "https://github.com/Mohamed-Hussain-AlSahabi"
LINKEDIN = "https://www.linkedin.com/in/mohamed-alsahabi-25601a292"
EMAIL = "mohamedalsahabi@gmail.com"

# =========================
# CSS
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    box-sizing: border-box;
    font-family: Inter, sans-serif;
}

html {
    scroll-behavior: smooth;
}

.stApp {
    background:
    radial-gradient(circle at 10% 5%, rgba(34,211,238,.10), transparent 25%),
    radial-gradient(circle at 90% 10%, rgba(168,85,247,.12), transparent 28%),
    #050816;
    color: #f8fafc;
}

.block-container {
    max-width: 1200px;
    padding: 1rem 2rem 4rem;
}

#MainMenu,
header,
footer {
    visibility: hidden;
}

/* NAV */

.nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;

    padding: 13px 18px;
    margin-bottom: 25px;

    border: 1px solid rgba(148,163,184,.15);
    border-radius: 18px;

    background: rgba(5,8,22,.80);
    backdrop-filter: blur(18px);
}

.logo {
    font-size: 20px;
    font-weight: 800;
    white-space: nowrap;
}

.logo span {
    color: #22d3ee;
}

.navlinks {
    display: flex;
    gap: 18px;
}

.navlinks a {
    color: #cbd5e1 !important;
    text-decoration: none;
    font-size: 13px;
}

.navlinks a:hover {
    color: #22d3ee !important;
}

/* BUTTON */

.btn {
    display: inline-block;
    padding: 11px 17px;
    border-radius: 11px;

    color: white !important;
    text-decoration: none !important;

    font-size: 13px;
    font-weight: 700;

    background: linear-gradient(90deg,#0891b2,#7c3aed);
    border: 1px solid rgba(34,211,238,.4);
}

.btn2 {
    background: rgba(15,23,42,.8);
    border-color: #334155;
}

/* HERO */

.hero {
    padding: 45px;
    min-height: 500px;

    border-radius: 28px;
    border: 1px solid rgba(148,163,184,.14);

    background: linear-gradient(
        135deg,
        rgba(12,20,38,.95),
        rgba(7,12,27,.85)
    );
}

.eyebrow {
    display: inline-block;

    padding: 7px 12px;

    border-radius: 999px;

    color: #67e8f9;
    background: rgba(34,211,238,.07);

    border: 1px solid rgba(34,211,238,.35);

    font-size: 11px;
    font-weight: 800;
}

.hero h1 {
    font-size: clamp(38px, 6vw, 68px);
    line-height: 1.05;

    margin: 18px 0 12px;

    letter-spacing: -3px;
}

.gradient {
    background: linear-gradient(
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
    font-size: 18px;
    font-weight: 500;
}

.hero p {
    max-width: 700px;

    color: #94a3b8;

    line-height: 1.8;
    font-size: 14px;
}

/* PROFILE */

.profile-box {
    display: flex;
    justify-content: center;
    align-items: center;

    padding: 35px 0 20px;
}

.profile-border {
    width: min(300px, 70vw);
    aspect-ratio: 1;

    padding: 7px;

    border-radius: 50%;

    background: linear-gradient(
        135deg,
        #22d3ee,
        #7c3aed,
        #ec4899
    );

    box-shadow: 0 0 60px rgba(34,211,238,.18);
}

.profile {
    width: 100%;
    height: 100%;

    object-fit: cover;

    border-radius: 50%;
    border: 6px solid #07101f;

    display: block;
}

/* STATS */

.stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.stat {
    padding: 15px 8px;

    text-align: center;

    border-radius: 15px;

    background: rgba(15,23,42,.65);
    border: 1px solid rgba(148,163,184,.14);
}

.stat b {
    display: block;
    font-size: 21px;
}

.stat span {
    color: #94a3b8;
    font-size: 10px;
}

/* SECTIONS */

.section {
    margin: 55px 0 20px;
}

.section h2 {
    margin: 0;
    font-size: 29px;
}

.section p {
    color: #94a3b8;
}

/* CARD */

.card {
    height: 100%;

    padding: 24px;

    border-radius: 20px;

    background: rgba(12,20,38,.78);
    border: 1px solid rgba(148,163,184,.14);
}

.card h3 {
    margin-top: 0;
}

.card p,
.card li {
    color: #94a3b8;
    line-height: 1.7;
}

/* SKILLS */

.skill {
    display: inline-block;

    padding: 7px 10px;
    margin: 4px 3px 0 0;

    border-radius: 9px;

    background: #0b1325;
    border: 1px solid #263653;

    color: #dbeafe;

    font-size: 11px;
}

.barline {
    margin: 15px 0;
}

.barhead {
    display: flex;
    justify-content: space-between;

    color: #cbd5e1;

    font-size: 13px;
}

.bar {
    height: 7px;
    margin-top: 7px;

    background: #172033;

    border-radius: 10px;
    overflow: hidden;
}

.fill {
    height: 100%;

    border-radius: 10px;

    background: linear-gradient(
        90deg,
        #06b6d4,
        #8b5cf6
    );
}

/* KNOWLEDGE */

.know {
    height: 100%;

    padding: 21px;

    border-radius: 18px;

    background: linear-gradient(
        145deg,
        #0b1325,
        #0a1020
    );

    border: 1px solid rgba(148,163,184,.14);
}

.know .icon {
    font-size: 27px;
}

.know h3 {
    margin: 9px 0;
}

.know li {
    color: #94a3b8;
    margin: 5px 0;
    font-size: 13px;
}

/* PROJECT */

.project {
    height: 100%;

    padding: 23px;

    border-radius: 20px;

    background: linear-gradient(
        145deg,
        rgba(15,23,42,.9),
        rgba(8,14,28,.9)
    );

    border: 1px solid rgba(148,163,184,.14);
}

.project-number {
    color: #64748b;
    font-size: 11px;
}

.project p {
    color: #94a3b8;
    line-height: 1.7;
}

/* CONTACT */

.contact {
    padding: 35px;

    border-radius: 23px;

    background: linear-gradient(
        135deg,
        rgba(34,211,238,.07),
        rgba(124,58,237,.08)
    );

    border: 1px solid rgba(34,211,238,.20);
}

.contact a {
    color: #67e8f9 !important;
    text-decoration: none;
}

/* MOBILE */

@media (max-width: 800px) {

    .block-container {
        padding: .7rem .8rem 3rem;
    }

    .nav {
        flex-direction: column;
        text-align: center;
        padding: 15px;
    }

    .navlinks {
        display: none;
    }

    .nav .btn {
        width: 100%;
        text-align: center;
    }

    .hero {
        padding: 25px 19px;
        min-height: auto;
        border-radius: 22px;
    }

    .hero h1 {
        font-size: clamp(34px, 10vw, 47px);
        letter-spacing: -2px;
    }

    .hero h3 {
        font-size: 15px;
        line-height: 1.5;
    }

    .hero p {
        font-size: 13px;
        line-height: 1.75;
    }

    .hero .btn {
        display: block;
        width: 100%;
        text-align: center;
        margin-top: 10px;
    }

    .profile-box {
        padding-top: 25px;
    }

    .profile-border {
        width: min(220px, 62vw);
    }

    .stats {
        gap: 6px;
    }

    .stat {
        padding: 11px 4px;
    }

    .stat b {
        font-size: 18px;
    }

    .stat span {
        font-size: 9px;
    }

    .section {
        margin-top: 42px;
    }

    .section h2 {
        font-size: 23px;
    }

    .card,
    .know,
    .project {
        margin-bottom: 12px;
    }

    .contact {
        padding: 23px 18px;
        overflow-wrap: anywhere;
    }

    .contact h2 {
        font-size: 21px;
    }
}

/* VERY SMALL PHONES */

@media (max-width: 430px) {

    .hero h1 {
        font-size: 33px;
    }

    .profile-border {
        width: 185px;
    }

    .stats {
        grid-template-columns: 1fr 1fr;
    }

    .stat:last-child {
        grid-column: 1 / -1;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================
# NAVIGATION
# =========================

st.markdown(
    f"""
    <div class="nav">

        <div class="logo">
            <span>MH</span> Mohamed Hussein
        </div>

        <div class="navlinks">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>

        <a class="btn" href="CV.pdf" target="_blank">
            ⬇ Download CV
        </a>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# HERO
# =========================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

left, right = st.columns(
    [1.35, 1],
    gap="large"
)

with left:

    st.markdown(
        """
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

            <a class="btn" href="#projects">
                View My Work →
            </a>

            <a class="btn btn2" href="#contact">
                Let's Talk
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )


with right:

    photo = Path("profile.jpg")

    if photo.exists():

        image_data = base64.b64encode(
            photo.read_bytes()
        ).decode()

        st.markdown(
            f"""
            <div class="profile-box">

                <div class="profile-border">

                    <img
                        class="profile"
                        src="data:image/jpeg;base64,{image_data}"
                    >

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "profile.jpg was not found."
        )

    st.markdown(
        """
        <div class="stats">

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
        """,
        unsafe_allow_html=True
    )


# =========================
# ABOUT
# =========================

st.markdown(
    """
    <div id="about" class="section">

        <h2>👨‍💻 About Me</h2>

        <p>
            Building my path from programming fundamentals
            to intelligent software.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

a1, a2 = st.columns(2, gap="large")

with a1:

    st.markdown(
        """
        <div class="card">

            <h3>Who I Am</h3>

            <p>
                My name is <b>Mohamed Hussein Amin Hussein</b>.
                I am an Artificial Intelligence student interested
                in software development and intelligent systems.
            </p>

            <p>
                I have studied C++, Python, OOP, databases,
                data structures, machine learning,
                operating systems, networking and software engineering.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with a2:

    st.markdown(
        """
        <div class="card">

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
        """,
        unsafe_allow_html=True
    )


# =========================
# SKILLS
# =========================

st.markdown(
    """
    <div id="skills" class="section">

        <h2>⚡ Skills & Expertise</h2>

        <p>
            My current technical toolkit.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

skills_left = [
    ("C++ / OOP", 90),
    ("Python / OOP", 90),
    ("Data Structures", 85),
    ("Database", 80),
    ("Machine Learning", 75)
]

skills_right = [
    ("Operating Systems", 80),
    ("Software Engineering", 85),
    ("Advanced Software Engineering", 75),
    ("Computer Networks", 80),
    ("Web Development", 85)
]

s1, s2 = st.columns(2, gap="large")

for column, skills in [
    (s1, skills_left),
    (s2, skills_right)
]:

    with column:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        for name, percent in skills:

            st.markdown(
                f"""
                <div class="barline">

                    <div class="barhead">
                        <span>{name}</span>
                        <span>{percent}%</span>
                    </div>

                    <div class="bar">

                        <div
                            class="fill"
                            style="width:{percent}%">
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


# =========================
# KNOWLEDGE
# =========================

st.markdown(
    """
    <div class="section">

        <h2>🧠 What I Know</h2>

    </div>
    """,
    unsafe_allow_html=True
)

knowledge = [
    ("💻", "Programming", "C++", "Python", "OOP Concepts"),
    ("📊", "Data & Algorithms", "Data Structures", "Algorithms", "Problem Solving"),
    ("🗄️", "Databases", "Database Design", "SQL", "Data Management"),
    ("🤖", "AI & ML", "Machine Learning", "Data Processing", "Model Building"),
    ("⚙️", "Systems", "Operating Systems", "Processes", "Memory Management"),
    ("🌐", "Networks", "Computer Networks", "Protocols", "Network Fundamentals")
]

knowledge_columns = st.columns(3)

for index, item in enumerate(knowledge):

    icon, title, one, two, three = item

    with knowledge_columns[index % 3]:

        st.markdown(
            f"""
            <div class="know">

                <div class="icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <ul>
                    <li>{one}</li>
                    <li>{two}</li>
                    <li>{three}</li>
                </ul>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# PROJECTS
# =========================

st.markdown(
    """
    <div id="projects" class="section">

        <h2>🚀 Featured Projects</h2>

        <p>
            Projects I can showcase and expand as my portfolio grows.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)

projects = [
    (
        "01",
        "🛒",
        "Supermarket Management System",
        "A software system concept for managing products and application data with a clean structure.",
        ["C++", "OOP", "Database"]
    ),
    (
        "02",
        "🤖",
        "Machine Learning Projects",
        "Machine-learning practice focused on data, models and intelligent problem solving using Python.",
        ["Python", "Machine Learning", "Data"]
    ),
    (
        "03",
        "🌐",
        "Personal Portfolio",
        "A modern personal website built to present my skills, projects and professional profile.",
        ["Streamlit", "HTML", "CSS", "JavaScript"]
    )
]

project_columns = st.columns(3)

for column, project in zip(project_columns, projects):

    number, icon, title, description, tags = project

    tags_html = ""

    for tag in tags:
        tags_html += f'<span class="skill">{tag}</span>'

    with column:

        st.markdown(
            f"""
            <div class="project">

                <div class="project-number">
                    PROJECT {number}
                </div>

                <div style="font-size:34px;margin-top:12px;">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {description}
                </p>

                {tags_html}

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# TECHNOLOGIES
# =========================

st.markdown(
    """
    <div class="section">

        <h2>🧰 Technologies</h2>

    </div>
    """,
    unsafe_allow_html=True
)

technologies = [
    "🐍 Python",
    "⚙️ C++",
    "🧠 Machine Learning",
    "🌊 Streamlit",
    "🌐 HTML",
    "🎨 CSS",
    "⚡ JavaScript",
    "🗄️ Database",
    "🌐 Networking",
    "🖥️ Operating Systems"
]

tech_html = ""

for technology in technologies:
    tech_html += f'<span class="skill">{technology}</span>'

st.markdown(
    f"""
    <div class="card" style="text-align:center;">
        {tech_html}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# CONTACT
# =========================

st.markdown(
    """
    <div id="contact" class="section">

        <h2>📩 Contact</h2>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="contact">

        <h2>
            Let's Build Something Great 🚀
        </h2>

        <p>
            Open to learning, collaboration, software projects
            and internship opportunities.
        </p>

        <p>
            📧
            <a href="mailto:{EMAIL}">
                {EMAIL}
            </a>
        </p>

        <p>
            💼
            <a href="{LINKEDIN}" target="_blank">
                LinkedIn Profile
            </a>
        </p>

        <p>
            💻
            <a href="{GITHUB}" target="_blank">
                GitHub Profile
            </a>
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# FOOTER
# =========================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#475569;
        margin-top:35px;
        font-size:12px;
    ">
        © 2026 Mohamed Hussein Amin Hussein
        · Artificial Intelligence Student
    </div>
    """,
    unsafe_allow_html=True
)
