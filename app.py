
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Mohamed Hussein | AI & Software Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- EDIT THESE ----------
GITHUB = "https://github.com/Mohamed-Hussain-AlSahabi"
LINKEDIN = "https://www.linkedin.com/in/mohamed-alsahabi-25601a292?utm_source=share_via&utm_content=profile&utm_medium=member_android"
EMAIL = "mohamedalsahabi@gmail.com"
CV_FILE = "CV.pdf"   # Put your CV.pdf beside app.py if you have one.
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

* { font-family: Inter, sans-serif; }
html { scroll-behavior: smooth; }
.stApp {
    background:
      radial-gradient(circle at 8% 5%, rgba(34,211,238,.09), transparent 25%),
      radial-gradient(circle at 90% 12%, rgba(168,85,247,.10), transparent 28%),
      #050816;
    color: var(--text);
}
.block-container { max-width: 1240px; padding: 1.2rem 2rem 4rem; }

#MainMenu, footer, header { visibility: hidden; }

/* top nav */
.nav {
    position: sticky; top: 10px; z-index: 50;
    display:flex; align-items:center; justify-content:space-between;
    padding: 12px 18px; margin-bottom: 25px;
    border:1px solid var(--line); border-radius:18px;
    background:rgba(5,8,22,.78); backdrop-filter: blur(18px);
}
.logo { font-size:20px; font-weight:800; }
.logo span { color:var(--cyan); }
.navlinks a {
    color:#cbd5e1 !important; text-decoration:none; margin:0 10px;
    font-size:13px;
}
.navlinks a:hover { color:var(--cyan) !important; }

.btn {
    display:inline-block; padding:11px 17px; border-radius:11px;
    text-decoration:none !important; font-weight:700; font-size:13px;
    color:white !important; border:1px solid rgba(34,211,238,.45);
    background:linear-gradient(90deg,#0891b2,#7c3aed);
    box-shadow:0 8px 30px rgba(34,211,238,.12);
}
.btn2 {
    background:rgba(15,23,42,.8);
    border-color:#334155;
}

/* hero */
.hero {
    position:relative; overflow:hidden;
    border:1px solid var(--line); border-radius:30px;
    padding:48px; min-height:540px;
    background:linear-gradient(135deg,rgba(12,20,38,.92),rgba(7,12,27,.80));
}
.hero:before {
    content:""; position:absolute; width:330px; height:330px;
    border-radius:50%; right:-130px; top:-140px;
    background:rgba(168,85,247,.13); filter:blur(8px);
}
.eyebrow {
    display:inline-block; padding:7px 12px; border-radius:999px;
    border:1px solid rgba(34,211,238,.35);
    color:#67e8f9; background:rgba(34,211,238,.07);
    font-size:12px; font-weight:800; letter-spacing:.5px;
}
.hero h1 {
    font-size:clamp(40px,6vw,70px); line-height:1.03;
    margin:18px 0 12px; letter-spacing:-3px;
}
.gradient {
    background:linear-gradient(90deg,#22d3ee,#818cf8,#c084fc);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.hero h3 { color:#cbd5e1; font-size:19px; font-weight:500; }
.hero p { color:var(--muted); line-height:1.85; max-width:700px; }

.profile-wrap {
    width:310px; height:310px; margin:auto;
    padding:7px; border-radius:50%;
    background:linear-gradient(135deg,#22d3ee,#7c3aed,#ec4899,#22d3ee);
    box-shadow:0 0 65px rgba(34,211,238,.16);
}
.profile {
    width:100%; height:100%; object-fit:cover;
    object-position:center 28%;
    border-radius:50%;
    border:7px solid #07101f;
}
.statrow { display:flex; gap:10px; margin-top:28px; }
.stat {
    flex:1; padding:16px; border-radius:16px;
    border:1px solid var(--line); background:rgba(15,23,42,.6);
}
.stat b { display:block; font-size:22px; }
.stat span { color:var(--muted); font-size:11px; }

/* sections */
.section { margin:65px 0 22px; }
.section h2 { font-size:30px; margin:0; }
.section p { color:var(--muted); margin-top:7px; }

.panel {
    padding:26px; border-radius:22px;
    background:var(--panel); border:1px solid var(--line);
    height:100%;
}
.panel h3 { margin-top:0; }
.panel p, .panel li { color:var(--muted); line-height:1.75; }

.skill {
    margin:6px 5px 0 0; display:inline-block;
    padding:8px 12px; border-radius:10px;
    background:#0b1325; border:1px solid #263653;
    color:#dbeafe; font-size:12px;
}

.barline { margin:16px 0; }
.barhead { display:flex; justify-content:space-between; color:#cbd5e1; font-size:13px; }
.bar {
    height:7px; margin-top:7px; border-radius:10px; background:#172033; overflow:hidden;
}
.fill {
    height:100%; border-radius:10px;
    background:linear-gradient(90deg,#06b6d4,#8b5cf6);
}

.know {
    padding:22px; border-radius:19px; height:100%;
    background:linear-gradient(145deg,#0b1325,#0a1020);
    border:1px solid var(--line);
}
.know .icon { font-size:28px; }
.know h3 { margin:10px 0; }
.know ul { padding-left:18px; margin-bottom:0; }
.know li { color:var(--muted); margin:5px 0; font-size:13px; }

.project {
    padding:25px; border-radius:21px; height:100%;
    background:linear-gradient(145deg,rgba(15,23,42,.9),rgba(8,14,28,.9));
    border:1px solid var(--line);
    transition:.25s ease;
}
.project:hover { transform:translateY(-6px); border-color:rgba(34,211,238,.42); }
.project .number { color:#64748b; font-size:12px; }
.project h3 { color:#e2e8f0; }
.project p { color:var(--muted); line-height:1.7; }

.contact {
    padding:40px; border-radius:25px;
    border:1px solid rgba(34,211,238,.20);
    background:linear-gradient(135deg,rgba(34,211,238,.07),rgba(124,58,237,.08));
}
.contact a { color:#67e8f9 !important; text-decoration:none; }

@media(max-width:800px) {
    .block-container { padding-left:1rem; padding-right:1rem; }
    .navlinks { display:none; }
    .hero { padding:28px 20px; }
    .profile-wrap { width:230px; height:230px; margin-top:25px; }
    .statrow { flex-wrap:wrap; }
    .stat { min-width:28%; }
}
</style>
""", unsafe_allow_html=True)

# NAV
st.markdown(f"""
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
""", unsafe_allow_html=True)

# HERO
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
c1, c2 = st.columns([1.35, 1], gap="large")
with c1:
    st.markdown("""
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
      &nbsp;
      <a class="btn btn2" href="#contact">Let's Talk</a>
    </div>
    """, unsafe_allow_html=True)
with c2:
    photo = Path("images/profile.jpg")
    st.markdown('<div style="height:55px"></div>', unsafe_allow_html=True)
    if photo.exists():
        st.markdown(
            f'<div class="profile-wrap"><img class="profile" src="data:image/jpeg;base64,{__import__("base64").b64encode(photo.read_bytes()).decode()}"></div>',
            unsafe_allow_html=True
        )
    st.markdown("""
    <div class="statrow">
      <div class="stat"><b>15+</b><span>Projects & Practice</span></div>
      <div class="stat"><b>10+</b><span>Core Skills</span></div>
      <div class="stat"><b>AI</b><span>Study Focus</span></div>
    </div>
    """, unsafe_allow_html=True)

# ABOUT
st.markdown('<div id="about" class="section"><h2>👨‍💻 About Me</h2><p>Building my path from programming fundamentals to intelligent software.</p></div>', unsafe_allow_html=True)
a1, a2 = st.columns(2, gap="large")
with a1:
    st.markdown("""
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
    """, unsafe_allow_html=True)
with a2:
    st.markdown("""
    <div class="panel">
      <h3>My Direction</h3>
      <p>
      I am working toward becoming a strong software engineer with an AI background,
      combining programming, problem solving, data and modern application development.
      </p>
      <p><b>Focus:</b> Software Engineering · AI/ML · Python · C++ · Web Applications</p>
    </div>
    """, unsafe_allow_html=True)

# SKILLS
st.markdown('<div id="skills" class="section"><h2>⚡ Skills & Expertise</h2><p>My current technical toolkit.</p></div>', unsafe_allow_html=True)
s1, s2 = st.columns(2, gap="large")
left_skills = [("C++ / OOP",90),("Python / OOP",90),("Data Structures",85),("Database",80),("Machine Learning",75)]
right_skills = [("Operating Systems",80),("Software Engineering",85),("Advanced Software Engineering",75),("Computer Networks",80),("Web Development",85)]
for col, group in [(s1,left_skills),(s2,right_skills)]:
    with col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        for name, pct in group:
            st.markdown(f"""
            <div class="barline">
              <div class="barhead"><span>{name}</span><span>{pct}%</span></div>
              <div class="bar"><div class="fill" style="width:{pct}%"></div></div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# KNOW
st.markdown('<div class="section"><h2>🧠 What I Know</h2></div>', unsafe_allow_html=True)
knowledge = [
    ("💻","Programming","C++","Python","OOP Concepts"),
    ("📊","Data & Algorithms","Data Structures","Algorithms","Problem Solving"),
    ("🗄️","Databases","Database Design","SQL","Data Management"),
    ("🤖","AI & ML","Machine Learning","Data Processing","Model Building"),
    ("⚙️","Systems","Operating Systems","Processes","Memory Management"),
    ("🌐","Networks","Computer Networks","Protocols","Network Fundamentals"),
]
cols = st.columns(3)
for i, item in enumerate(knowledge):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="know">
          <div class="icon">{item[0]}</div>
          <h3>{item[1]}</h3>
          <ul><li>{item[2]}</li><li>{item[3]}</li><li>{item[4]}</li></ul>
        </div>
        """, unsafe_allow_html=True)
    if i == 2:
        st.markdown("<br>", unsafe_allow_html=True)

# PROJECTS
st.markdown('<div id="projects" class="section"><h2>🚀 Featured Projects</h2><p>Projects I can showcase and expand as my portfolio grows.</p></div>', unsafe_allow_html=True)
projects = [
    ("01","🛒","Supermarket Management System",
     "A software system concept for managing products and application data with a clean structure.",
     ["C++","OOP","Database"]),
    ("02","🤖","Machine Learning Projects",
     "Machine-learning practice focused on data, models and intelligent problem solving using Python.",
     ["Python","Machine Learning","Data"]),
    ("03","🌐","Personal Portfolio",
     "A modern personal website built to present my skills, projects and professional profile.",
     ["Streamlit","HTML","CSS","JavaScript"]),
]
cols = st.columns(3)
for col, (num, icon, title, desc, tags) in zip(cols, projects):
    with col:
        st.markdown(f"""
        <div class="project">
          <div class="number">PROJECT {num}</div>
          <div style="font-size:35px;margin-top:12px">{icon}</div>
          <h3>{title}</h3>
          <p>{desc}</p>
          {''.join(f'<span class="skill">{x}</span>' for x in tags)}
        </div>
        """, unsafe_allow_html=True)

# STACK
st.markdown('<div class="section"><h2>🧰 Technologies</h2></div>', unsafe_allow_html=True)
st.markdown("""
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
""", unsafe_allow_html=True)

# CONTACT
st.markdown('<div id="contact" class="section"><h2>📩 Contact</h2></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="contact">
  <h2>Let's Build Something Great 🚀</h2>
  <p style="color:#94a3b8">
    Open to learning, collaboration, software projects and internship opportunities.
  </p>
  <p>📧 <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>💼 <a href="{LINKEDIN}" target="_blank">LinkedIn Profile</a></p>
  <p>💻 <a href="{GITHUB}" target="_blank">GitHub Profile</a></p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#475569;margin-top:35px">
© 2026 Mohamed Hussein Amin Hussein · Artificial Intelligence Student
</div>
""", unsafe_allow_html=True)
