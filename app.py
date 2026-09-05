import base64
from pathlib import Path
import streamlit as st

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

# تحضير الصورة برمجيًا بأمان
photo = Path("profile.jpg")
img_base64 = ""
if photo.exists():
    img_base64 = base64.b64encode(photo.read_bytes()).decode()

st.markdown(
    f"""
<style>  
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');  
  
:root {{  
    --bg: #050816;  
    --panel: rgba(12, 20, 38, .78);  
    --line: rgba(148,163,184,.14);  
    --text: #f8fafc;  
    --muted: #94a3b8;  
    --cyan: #22d3ee;  
    --purple: #a855f7;  
}}  
  
* {{ font-family: Inter, sans-serif; box-sizing: border-box; }}  
html {{ scroll-behavior: smooth; }}  
.stApp {{  
    background:  
      radial-gradient(circle at 8% 5%, rgba(34,211,238,.09), transparent 25%),  
      radial-gradient(circle at 90% 12%, rgba(168,85,247,.10), transparent 28%),  
      #050816;  
    color: var(--text);  
}}  
.block-container {{ max-width: 1240px; padding: 1.2rem 2rem 4rem; }}  
  
#MainMenu, footer, header {{ visibility: hidden; }}  
  
/* Navigation */  
.nav {{  
    position: sticky; top: 10px; z-index: 50;  
    display: flex; align-items: center; justify-content: space-between;  
    padding: 12px 18px; margin-bottom: 25px;  
    border: 1px solid var(--line); border-radius: 18px;  
    background: rgba(5,8,22,.85); backdrop-filter: blur(18px);  
    flex-wrap: wrap; gap: 10px;
}}  
.logo {{ font-size: 20px; font-weight: 800; }}  
.logo span {{ color: var(--cyan); }}  
.navlinks a {{  
    color: #cbd5e1 !important; text-decoration: none; margin: 0 10px;  
    font-size: 13px;  
}}  
.navlinks a:hover {{ color: var(--cyan) !important; }}  
  
.btn {{  
    display: inline-block; padding: 11px 17px; border-radius: 11px;  
    text-decoration: none !important; font-weight: 700; font-size: 13px;  
    color: white !important; border: 1px solid rgba(34,211,238,.45);  
    background: linear-gradient(90deg,#0891b2,#7c3aed);  
    box-shadow: 0 8px 30px rgba(34,211,238,.12);  
    margin-top: 5px;
}}  
.btn2 {{  
    background: rgba(15,23,42,.8);  
    border-color: #334155;  
}}  
  
/* Hero Section */  
.hero {{  
    position: relative; overflow: hidden;  
    border: 1px solid var(--line); border-radius: 30px;  
    padding: 40px; min-height: auto;  
    background: linear-gradient(135deg,rgba(12,20,38,.92),rgba(7,12,27,.80));  
}}  
.eyebrow {{  
    display: inline-block; padding: 7px 12px; border-radius: 999px;  
    border: 1px solid rgba(34,211,238,.35);  
    color: #67e8f9; background: rgba(34,211,238,.07);  
    font-size: 12px; font-weight: 800; letter-spacing: .5px;  
}}  
.hero h1 {{  
    font-size: clamp(30px, 5vw, 60px); line-height: 1.1;  
    margin: 18px 0 12px; letter-spacing: -1.5px;  
}}  
.gradient {{  
    background: linear-gradient(90deg,#22d3ee,#818cf8,#c084fc);  
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;  
}}  
.hero h3 {{ color: #cbd5e1; font-size: 18px; font-weight: 500; }}  
.hero p {{ color: var(--muted); line-height: 1.7; max-width: 700px; }}  
  
.profile-wrap {{  
    width: 250px; height: 250px; margin: 20px auto;  
    padding: 6px; border-radius: 50%;  
    background: linear-gradient(135deg,#22d3ee,#7c3aed,#ec4899,#22d3ee);  
    box-shadow: 0 0 45px rgba(34,211,238,.16);  
}}  
.profile {{  
    width: 100%; height: 100%; object-fit: cover;  
    border-radius: 50%; border: 5px solid #07101f;  
}}  
.statrow {{ display: flex; gap: 10px; margin-top: 20px; flex-wrap: wrap; }}  
.stat {{  
    flex: 1; min-width: 90px; padding: 12px; border-radius: 16px;  
    border: 1px solid var(--line); background: rgba(15,23,42,.6);  
    text-align: center;
}}  
.stat b {{ display: block; font-size: 20px; }}  
.stat span {{ color: var(--muted); font-size: 11px; }}  
  
/* Sections & Cards */  
.section {{ margin: 45px 0 20px; }}  
.section h2 {{ font-size: 26px; margin: 0; }}  
.section p {{ color: var(--muted); margin-top: 5px; }}  
  
.panel {{  
    padding: 22px; border-radius: 20px;  
    background: var(--panel); border: 1px solid var(--line);  
    margin-bottom: 15px;
}}  
.panel h3 {{ margin-top: 0; }}  
.panel p, .panel li {{ color: var(--muted); line-height: 1.6; }}  
  
.skill {{  
    margin: 4px 3px; display: inline-block;  
    padding: 6px 12px; border-radius: 10px;  
    background: #0b1325; border: 1px solid #263653;  
    color: #dbeafe; font-size: 12px;  
}}  
  
.barline {{ margin: 14px 0; }}  
.barhead {{ display: flex; justify-content: space-between; color: #cbd5e1; font-size: 13px; }}  
.bar {{ height: 7px; margin-top: 6px; border-radius: 10px; background: #172033; overflow: hidden; }}  
.fill {{ height: 100%; border-radius: 10px; background: linear-gradient(90deg,#06b6d4,#8b5cf6); }}  
  
.know {{  
    padding: 20px; border-radius: 18px; margin-bottom: 15px;
    background: linear-gradient(145deg,#0b1325,#0a1020);  
    border: 1px solid var(--line);  
}}  
.know .icon {{ font-size: 26px; }}  
.know h3 {{ margin: 8px 0; font-size: 18px; }}  
.know ul {{ padding-left: 18px; margin-bottom: 0; }}  
.know li {{ color: var(--muted); margin: 4px 0; font-size: 13px; }}  
  
.project {{  
    padding: 22px; border-radius: 20px; margin-bottom: 15px;
    background: linear-gradient(145deg,rgba(15,23,42,.9),rgba(8,14,28,.9));  
    border: 1px solid var(--line);  
}}  
.project .number {{ color: #64748b; font-size: 12px; }}  
.project h3 {{ color: #e2e8f0; font-size: 18px; margin: 8px 0; }}  
.project p {{ color: var(--muted); line-height: 1.6; font-size: 13px; }}  
  
.contact {{  
    padding: 30px 20px; border-radius: 22px; text-align: center;
    border: 1px solid rgba(34,211,238,.20);  
    background: linear-gradient(135deg,rgba(34,211,238,.07),rgba(124,58,237,.08));  
}}  
.contact a {{ color: #67e8f9 !important; text-decoration: none; word-break: break-all; }}  
  
/* Mobile Responsive Media Query */  
@media(max-width: 768px) {{  
    .block-container {{ padding: 0.8rem 0.8rem 2rem !important; }}  
    .navlinks {{ display: none; }}  
    .nav {{ justify-content: center; text-align: center; }}  
    .hero {{ padding: 22px 16px; text-align: center; }}  
    .hero p {{ margin: 0 auto 15px; }}  
    .profile-wrap {{ width: 180px; height: 180px; margin-top: 15px; }}  
    .statrow {{ justify-content: center; }}  
    .stat {{ min-width: 45%; }}  
}}  
</style>  
""",
    unsafe_allow_html=True,
)

# Navbar
st.markdown(
    f"""
<div class="nav">  
  <div class="logo"><span>MH</span> &nbsp; Mohamed Hussein</div>  
  <div class="navlinks">  
    <a href="#home">Home</a>  
    <a href="#about">About</a>  
    <a href="#skills">Skills</a>  
    <a href="#projects">Projects</a>  
    <a href="#contact">Contact</a>  
  </div>  
  <a class="btn" href="{CV_FILE}" target="_blank">⬇ Download CV</a>  
</div>  
""",
    unsafe_allow_html=True,
)

# Hero Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
c1, c2 = st.columns([1.35, 1], gap="medium")

with c1:
    st.markdown(
        """
    <div class="hero">
        <span class="eyebrow">ARTIFICIAL INTELLIGENCE STUDENT</span>
        <h1>Mohamed Hussein<br><span class="gradient">Amin Hussein</span></h1>
        <h3>AI Student · Software Engineer · Developer</h3>
        <p>
        Passionate about programming, Artificial Intelligence, Machine Learning 
        and building practical software. I enjoy learning modern technologies 
        and turning ideas into clean, useful applications.
        </p>
        <p>
        Currently developing my skills across software engineering, data, 
        systems, networking and web development.
        </p>
        <a class="btn" href="#projects">View My Work →</a>
        <a class="btn btn2" href="#contact">Let's Talk</a>
    </div>
    """,
        unsafe_allow_html=True,
    )

with c2:
    if img_base64:
        st.markdown(
            f'<div class="profile-wrap"><img class="profile" src="data:image/jpeg;base64,{img_base64}"></div>',
            unsafe_allow_html=True,
        )
    st.markdown(
        """
    <div class="statrow">
        <div class="stat"><b>15+</b><span>Projects</span></div>
        <div class="stat"><b>10+</b><span>Core Skills</span></div>
        <div class="stat"><b>AI</b><span>Study Focus</span></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# About Section
st.markdown(
    '<div id="about" class="section"><h2>👨‍💻 About Me</h2><p>Building my path from programming fundamentals to intelligent software.</p></div>',
    unsafe_allow_html=True,
)
a1, a2 = st.columns(2, gap="medium")
with a1:
    st.markdown(
        """
    <div class="panel">
        <h3>Who I Am</h3>
        <p>
        My name is <b>Mohamed Hussein Amin Hussein</b>. I am an Artificial 
        Intelligence student interested in software development and intelligent systems.
        </p>
        <p>
        I have studied C++, Python, OOP, databases, data structures, 
        machine learning, operating systems, networking and software engineering.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
with a2:
    st.markdown(
        """
    <div class="panel">
        <h3>My Direction</h3>
        <p>
        I am working toward becoming a strong software engineer with an AI background, 
        combining programming, problem solving, data and modern application development.
        </p>
        <p><b>Focus:</b> Software Engineering · AI/ML · Python · C++ · Web Applications</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Skills Section
st.markdown(
    '<div id="skills" class="section"><h2>⚡ Skills & Expertise</h2><p>My current technical toolkit.</p></div>',
    unsafe_allow_html=True,
)
s1, s2 = st.columns(2, gap="medium")
left_skills = [
    ("C++ / OOP", 90),
    ("Python / OOP", 90),
    ("Data Structures", 85),
    ("Database", 80),
    ("Machine Learning", 75),
]
right_skills = [
    ("Operating Systems", 80),
    ("Software Engineering", 85),
    ("Advanced Software Engineering", 75),
    ("Computer Networks", 80),
    ("Web Development", 85),
]

for col, group in [(s1, left_skills), (s2, right_skills)]:
    with col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        for name, pct in group:
            st.markdown(
                f"""
            <div class="barline">
                <div class="barhead"><span>{name}</span><span>{pct}%</span></div>
                <div class="bar"><div class="fill" style="width:{pct}%"></div></div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

# Knowledge Section
st.markdown(
    '<div class="section"><h2>🧠 What I Know</h2></div>', unsafe_allow_html=True
)
knowledge = [
    ("💻", "Programming", "C++", "Python", "OOP Concepts"),
    ("📊", "Data & Algorithms", "Data Structures", "Algorithms", "Problem Solving"),
    ("🗄️", "Databases", "Database Design", "SQL", "Data Management"),
    ("🤖", "AI & ML", "Machine Learning", "Data Processing", "Model Building"),
    ("⚙️", "Systems", "Operating Systems", "Processes", "Memory Management"),
    ("🌐", "Networks", "Computer Networks", "Protocols", "Network Fundamentals"),
]
cols = st.columns(3)
for i, item in enumerate(knowledge):
    with cols[i % 3]:
        st.markdown(
            f"""
        <div class="know">
            <div class="icon">{item[0]}</div>
            <h3>{item[1]}</h3>
            <ul><li>{item[2]}</li><li>{item[3]}</li><li>{item[4]}</li></ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Projects Section
st.markdown(
    '<div id="projects" class="section"><h2>🚀 Featured Projects</h2><p>Projects I can showcase and expand as my portfolio grows.</p></div>',
    unsafe_allow_html=True,
)
projects = [
    (
        "01",
        "🛒",
        "Supermarket Management System",
        "A software system concept for managing products and application data with a clean structure.",
        ["C++", "OOP", "Database"],
    ),
    (
        "02",
        "🤖",
        "Machine Learning Projects",
        "Machine-learning practice focused on data, models and intelligent problem solving using Python.",
        ["Python", "Machine Learning", "Data"],
    ),
    (
        "03",
        "🌐",
        "Personal Portfolio",
        "A modern personal website built to present my skills, projects and professional profile.",
        ["Streamlit", "HTML", "CSS", "JavaScript"],
    ),
]
cols = st.columns(3)
for col, (num, icon, title, desc, tags) in zip(cols, projects):
    with col:
        st.markdown(
            f"""
        <div class="project">
            <div class="number">PROJECT {num}</div>
            <div style="font-size:32px;margin-top:8px">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
            {''.join(f'<span class="skill">{x}</span>' for x in tags)}
        </div>
        """,
            unsafe_allow_html=True,
        )

# Tech Stack Section
st.markdown(
    '<div class="section"><h2>🧰 Technologies</h2></div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="panel" style="text-align:center">  
    <span class="skill">🐍 Python</span>  
    <span class="skill">⚙️ C++</span>  
    <span class="skill">🧠 Machine Learning</span>  
    <span class="skill">🌊 Streamlit</span>  
    <span class="skill">🌐 HTML</span>  
    <span class="skill">🎨 CSS</span>  
    <span class="skill">⚡ JavaScript</span>  
    <span class="skill">🗄️ Database</span>  
    <span class="skill">🌐 Networking</span>  
    <span class="skill">🖥️ Operating Systems</span>  
</div>  
""",
    unsafe_allow_html=True,
)

# Contact Section
st.markdown(
    '<div id="contact" class="section"><h2>📩 Contact</h2></div>',
    unsafe_allow_html=True,
)
st.markdown(
    f"""
<div class="contact">  
  <h2>Let's Build Something Great 🚀</h2>  
  <p style="color:#94a3b8">  
    Open to learning, collaboration, software projects and internship opportunities.  
  </p>  
  <p>📧 <a href="mailto:{EMAIL}">{EMAIL}</a></p>  
  <p>💼 <a href="{LINKEDIN}" target="_blank">LinkedIn Profile</a></p>  
  <p>💻 <a href="{GITHUB}" target="_blank">GitHub Profile</a></p>  
</div>  
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div style="text-align:center;color:#475569;margin-top:35px">  
© 2026 Mohamed Hussein Amin Hussein · Artificial Intelligence Student  
</div>  
""",
    unsafe_allow_html=True,
)
