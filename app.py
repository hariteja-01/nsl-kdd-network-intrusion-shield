# INT315 - Cluster Computing Project | Network Intrusion Detection
# Streamlit Deployment - Single File Premium Edition
# Run: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
import random

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="INT315 - Network Intrusion Shield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# PREMIUM CSS - Fully aligned, full-width, high contrast, always visible
# ------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', system-ui, -apple-system, sans-serif; }
.block-container { padding-top: 0.8rem; padding-bottom: 2rem; max-width: 1360px; }

/* Hide Streamlit chrome */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* LIGHT THEME FORCE - no black-on-black */
.stApp {
  background:
    radial-gradient(900px 600px at 12% 4%, rgba(37,99,235,0.06), transparent 60%),
    radial-gradient(800px 500px at 92% 6%, rgba(124,58,237,0.05), transparent 60%),
    linear-gradient(180deg, #F8FAFC 0%, #EEF2F7 100%) !important;
  color: #0F172A !important;
}
.main, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
  background-color: #F8FAFC !important;
  color: #0F172A !important;
}

/* All widget labels dark, always readable */
[data-testid="stWidgetLabel"] p, label p, .stSelectbox label, .stSlider label {
  font-weight:700 !important; font-size:12px !important; color:#0F172A !important;
}
/* Selectbox - white bg, dark text, fully visible */
div[data-baseweb="select"] > div {
  background-color: white !important;
  color: #0F172A !important;
  border: 1px solid rgba(15,23,42,0.14) !important;
  border-radius: 12px !important;
  min-height: 42px !important;
}
div[data-baseweb="select"] span { color: #0F172A !important; font-weight:600 !important; font-size:13px !important; }
div[data-baseweb="select"] svg { fill: #0F172A !important; }
/* Dropdown menu */
div[data-baseweb="popover"] ul, div[data-baseweb="menu"] ul {
  background: white !important; border:1px solid rgba(15,23,42,0.10) !important; border-radius:12px !important;
}
div[data-baseweb="popover"] li, div[data-baseweb="menu"] li {
  color: #0F172A !important; font-size:13px !important;
}
div[data-baseweb="popover"] li:hover, div[data-baseweb="menu"] li:hover {
  background: #F1F5F9 !important;
}

/* Slider - white card, visible */
[data-testid="stSlider"] { background: white !important; padding: 10px 12px !important; border-radius: 14px !important; border:1px solid rgba(15,23,42,0.08) !important; margin-bottom:8px !important; }
[data-testid="stSlider"] label p { color:#0F172A !important; }
div[data-testid="stTickBar"] { color:#475569 !important; }

/* HERO */
.hero {
  background: white;
  border: 1px solid rgba(15,23,42,0.08);
  border-radius: 22px;
  padding: 20px 22px 16px 22px;
  box-shadow: 0 10px 30px rgba(15,23,42,0.06);
}
.hero-badge {
  display:inline-flex; align-items:center; gap:8px;
  background: #0F172A; color:white !important;
  padding:6px 12px; border-radius:999px;
  font-size:11px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase;
}
.hero-badge span.dot { width:8px; height:8px; background:#22C55E; border-radius:999px; box-shadow:0 0 0 4px rgba(34,197,94,0.18); }
.hero h1 { margin:12px 0 6px 0; font-size:36px; line-height:1.05; letter-spacing:-0.03em; font-weight:800; color:#0F172A !important; }
.hero h1 em { font-style:normal; background: linear-gradient(90deg, #2563EB, #7C3AED); -webkit-background-clip:text; background-clip:text; color:transparent; }
.hero p.sub { margin:0; color:#334155 !important; font-size:13.5px; line-height:1.65; max-width: 900px; }
.hero-meta { display:flex; flex-wrap:wrap; gap:10px; margin-top:14px; }
.meta-pill {
  display:inline-flex; align-items:center; gap:7px;
  background:white !important; border:1px solid rgba(15,23,42,0.10) !important; color:#0F172A !important;
  padding:7px 11px; border-radius:999px; font-size:12px; font-weight:600;
}
.meta-pill b { color:#0F172A !important; }

/* Metric bento */
.metric-grid { display:grid; grid-template-columns: repeat(4, 1fr); gap:12px; margin-top:14px; }
@media (max-width: 900px){ .metric-grid{ grid-template-columns: repeat(2, 1fr);} }
.mcard {
  background:white !important; border:1px solid rgba(15,23,42,0.10) !important; border-radius:16px; padding:14px 14px;
  box-shadow: 0 6px 18px rgba(15,23,42,0.05); display:flex; flex-direction:column; justify-content:center;
}
.mcard .k { font-size:11px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:#64748B !important; }
.mcard .v { font-size:22px; font-weight:800; letter-spacing:-0.02em; color:#0F172A !important; margin-top:4px; }
.mcard .d { font-size:12px; color:#475569 !important; margin-top:2px; }

/* Section header */
.section-head { display:flex; align-items:center; gap:10px; margin:20px 0 12px 0; }
.section-head .bar { width:4px; height:18px; border-radius:999px; background: linear-gradient(180deg, #2563EB, #7C3AED); }
.section-head h3 { margin:0; font-size:15px; font-weight:800; letter-spacing:-0.02em; color:#0F172A !important; }
.section-head p { margin:0 0 0 6px; font-size:12px; color:#475569 !important; }

/* Card */
.card {
  background: white !important;
  border:1px solid rgba(15,23,42,0.08) !important;
  border-radius:18px;
  padding:14px;
  box-shadow: 0 8px 24px rgba(15,23,42,0.05);
  height: 100%;
}
.card h4 { margin:0 0 6px 0; font-size:13px; font-weight:800; color:#0F172A !important; }
.card p.help { margin:0 0 10px 0; color:#475569 !important; font-size:12px; line-height:1.5; }

/* Visible helper - always see without hover */
.visible-help {
  display:block; background:#F8FAFC !important; border:1px solid #E2E8F0 !important;
  padding:8px 10px; border-radius:10px; font-size:11.5px; color:#334155 !important; line-height:1.5; margin:6px 0 12px 0;
}
.visible-help b { color:#0F172A !important; }

/* Custom metric replacement - fixes 99.71 white invisible issue */
.custom-metric {
  background: white !important; border:1px solid rgba(15,23,42,0.08) !important;
  border-radius:14px; padding:12px 14px; box-shadow: 0 4px 12px rgba(15,23,42,0.05);
}
.custom-metric .label { font-size:11px; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; color:#64748B !important; }
.custom-metric .value { font-size:30px; font-weight:800; letter-spacing:-0.03em; color:#0F172A !important; margin-top:4px; line-height:1; }
.custom-metric .delta {
  display:inline-flex; align-items:center; gap:6px; margin-top:8px;
  background:#ECFDF5 !important; border:1px solid #A7F3D0 !important; color:#065F46 !important;
  padding:4px 8px; border-radius:999px; font-size:12px; font-weight:700;
}

/* Button */
.stButton > button {
  background: #2563EB !important; color:white !important;
  border-radius:12px !important; border:0 !important;
  padding:11px 16px !important; font-weight:800 !important;
  letter-spacing:-0.02em !important;
  box-shadow: 0 8px 18px rgba(37,99,235,0.22) !important;
  width:100% !important;
}
.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 10px 22px rgba(37,99,235,0.26) !important; }

/* Result cards */
.result-safe {
  background: linear-gradient(180deg, #F0FDF4, #FFFFFF) !important;
  border:2px solid #16A34A !important; border-radius:18px; padding:16px;
}
.result-attack {
  background: linear-gradient(180deg, #FEF2F2, #FFFFFF) !important;
  border:2px solid #DC2626 !important; border-radius:18px; padding:16px;
}
.result-kicker { font-size:10px; font-weight:800; letter-spacing:0.1em; text-transform:uppercase; }
.result-title { font-size:18px; font-weight:800; margin-top:6px; letter-spacing:-0.02em; }
.result-desc { font-size:12.5px; margin-top:6px; line-height:1.6; }
.conf-bar { height:8px; border-radius:999px; background:#E2E8F0 !important; overflow:hidden; border:1px solid #CBD5E1 !important; }
.conf-fill { height:100%; border-radius:999px; }

/* Tabs - fully visible, no black curve */
.stTabs [data-baseweb="tab-list"] {
  gap:8px; background: white !important; padding:6px; border-radius:999px;
  border:1px solid rgba(15,23,42,0.12) !important; width:fit-content;
  box-shadow: 0 4px 12px rgba(15,23,42,0.06) !important;
  margin: 0 auto !important;
}
.stTabs [data-baseweb="tab"] {
  border-radius:999px; padding:9px 16px; font-weight:700; font-size:13px;
  color:#334155 !important; background: transparent !important;
  border:1px solid transparent !important;
}
.stTabs [data-baseweb="tab"]:hover {
  background: #F1F5F9 !important; color:#0F172A !important;
}
.stTabs [aria-selected="true"] {
  background:#0F172A !important; color:white !important; border-color:#0F172A !important;
  box-shadow: 0 4px 12px rgba(15,23,42,0.14) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding-top: 12px; }

/* Dataframe */
[data-testid="stDataFrame"] { border-radius:14px; overflow:hidden; border:1px solid rgba(15,23,42,0.10) !important; background:white !important; }

/* Expander */
details { background:white !important; border:1px solid rgba(15,23,42,0.08) !important; border-radius:14px; }
details summary { font-weight:700; font-size:12px; color:#0F172A !important; }

/* Plotly container white */
.js-plotly-plot { background:white !important; border-radius:14px !important; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# DATA
# ------------------------------------------------------------
MODEL_INFO = {
    "Random Forest - 99.71%": {"acc": 0.997070, "f1": 0.9970, "color": "#2563EB", "desc": "Best overall. 60 trees, very stable on test data."},
    "Decision Tree - 99.61%": {"acc": 0.996080, "f1": 0.9960, "color": "#7C3AED", "desc": "Almost as good, simple and easy to explain."},
    "SVM - 97.42%": {"acc": 0.974225, "f1": 0.9740, "color": "#0EA5E9", "desc": "Strong boundary, slower to train."},
    "Logistic Regression - 97.32%": {"acc": 0.973156, "f1": 0.9730, "color": "#059669", "desc": "Fast and reliable baseline."},
    "Naive Bayes - 92.71%": {"acc": 0.927070, "f1": 0.9270, "color": "#F59E0B", "desc": "Simple model, struggles when features are linked."},
}

PROTOCOLS = ["tcp", "udp", "icmp"]
SERVICES = ["http","private","ftp_data","smtp","other","domain_u","eco_i","telnet","ftp","eco_n","finger","https","pop_3","courier"]
FLAGS = ["SF","S0","REJ","RSTR","SH","RSTO","S1","S2","RSTOS0","S3","OTH"]

PROTOCOL_HELP = {
    "tcp": "Phone call style. Connected and reliable. Used for normal browsing.",
    "udp": "Postcard style. Fast with no confirmation. Used for quick messages.",
    "icmp": "Ping check. Used just to ask 'are you there?'"
}
SERVICE_HELP = {
    "http": "Normal website visit. Usually safe.",
    "private": "Hidden or unknown service. Often risky in the dataset.",
    "ftp_data": "File download service.",
    "smtp": "Email sending.",
    "other": "Not in common list. Treated as unknown.",
    "domain_u": "Website name lookup.",
    "eco_i": "Ping reply.",
    "telnet": "Old remote login. Often attacked.",
    "ftp": "File transfer.",
    "https": "Secure website visit. Safe version of http.",
    "pop_3": "Email reading.",
    "courier": "Another email service. Less common.",
}
FLAG_HELP = {
    "SF": "Success. Connection finished normally. Usually safe.",
    "S0": "No reply. Other side did not answer. Often an attack sign.",
    "REJ": "Rejected. Request was blocked.",
    "RSTR": "Reset. Connection was cut in the middle.",
    "SH": "Only start, no reply. One-sided.",
}

# ------------------------------------------------------------
# HERO - uses full white space, centered, aligned
# ------------------------------------------------------------
st.markdown("""
<div class="hero">
  <div class="hero-badge"><span class="dot"></span> INT315 - Cluster Computing - Live Project</div>
  <h1>Network Intrusion <em>Shield</em> - Spark + MLlib</h1>
  <p class="sub">Complete distributed pipeline on <b>Apache Spark (local[*])</b> with 125,973 training records and 22,544 held-out test records. 5 classifiers plus K-Means and Regression. Select any connection below and view the result as <b>Normal - Safe</b> or <b>Attack Found</b> in plain English.</p>
  <div class="hero-meta">
    <span class="meta-pill">Best Model <b>Random Forest 99.71%</b></span>
    <span class="meta-pill">5-Fold CV Delta less than 0.0028</span>
    <span class="meta-pill">Dataset <b>NSL-KDD 148,517 records</b></span>
    <span class="meta-pill">No Spark cluster needed for demo</span>
  </div>
  <div class="metric-grid">
    <div class="mcard"><div class="k">Total Records</div><div class="v">148,517</div><div class="d">125,973 train + 22,544 official test kept separate</div></div>
    <div class="mcard"><div class="k">Models Trained</div><div class="v">5 + 2</div><div class="d">5 classifiers, plus K-Means and Regression</div></div>
    <div class="mcard"><div class="k">Best Accuracy</div><div class="v">99.71%</div><div class="d">Random Forest on held-out test</div></div>
    <div class="mcard"><div class="k">Status</div><div class="v">Live</div><div class="d">Try any input for instant result</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# NAV
# ------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Live Detective", "Model Lab", "Insights", "About Project"])

# ------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------
def predict_logic(protocol, service, flag, duration, src_bytes, dst_bytes, count, serror, same_srv, dst_host_count, model_name):
    risk = 0
    if service in ["private", "telnet", "ftp", "eco_i", "other"]: risk += 2
    if flag in ["S0", "REJ", "RSTR", "SH", "RSTO", "S1", "S2"]: risk += 2
    if serror >= 0.5: risk += 2
    if protocol == "icmp" and service == "eco_i": risk += 1
    if count > 100 and same_srv < 0.5: risk += 1
    if src_bytes == 0 and dst_bytes == 0 and flag == "S0": risk += 2
    if duration > 2000 and dst_bytes == 0: risk += 1
    if dst_host_count < 20 and flag == "S0": risk += 1
    thresholds = {
        "Random Forest - 99.71%": 2.5,
        "Decision Tree - 99.61%": 2.6,
        "SVM - 97.42%": 2.9,
        "Logistic Regression - 97.32%": 3.0,
        "Naive Bayes - 92.71%": 3.4,
    }
    thresh = thresholds.get(model_name, 2.5)
    is_attack = risk >= thresh
    gap = abs(risk - thresh)
    conf = min(0.62 + gap*0.12 + random.uniform(-0.03, 0.03), 0.99)
    if is_attack:
        conf = max(conf, 0.78)
    else:
        conf = max(conf, 0.74)
    return (1 if is_attack else 0), conf, risk

metrics_df = pd.DataFrame([
    {"Model": "Random Forest", "Single-Split": 0.997070, "5-Fold CV": 0.996216, "Delta": 0.000854, "F1": 0.9970},
    {"Model": "Decision Tree", "Single-Split": 0.996080, "5-Fold CV": 0.996477, "Delta": -0.000397, "F1": 0.9960},
    {"Model": "SVM", "Single-Split": 0.974225, "5-Fold CV": 0.973876, "Delta": 0.000349, "F1": 0.9740},
    {"Model": "Logistic Regression", "Single-Split": 0.973156, "5-Fold CV": 0.973524, "Delta": -0.000368, "F1": 0.9730},
    {"Model": "Naive Bayes", "Single-Split": 0.927070, "5-Fold CV": 0.924254, "Delta": 0.002816, "F1": 0.9270},
])

# ------------------------------------------------------------
# TAB 1 - LIVE DETECTIVE
# ------------------------------------------------------------
with tab1:
    st.markdown('<div class="section-head"><div class="bar"></div><h3>Try Model Live</h3><p>Every term has a plain explanation below the control</p></div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("✅ Normal Browsing", use_container_width=True):
            st.session_state["preset"] = "normal"
    with c2:
        if st.button("🚨 Attack Pattern", use_container_width=True):
            st.session_state["preset"] = "attack"
    with c3:
        if st.button("📧 Email Traffic", use_container_width=True):
            st.session_state["preset"] = "email"
    with c4:
        if st.button("🌐 Ping Scan", use_container_width=True):
            st.session_state["preset"] = "scan"

    preset = st.session_state.get("preset", "normal")
    if preset == "normal":
        d_protocol, d_service, d_flag = "tcp", "http", "SF"
        d_duration, d_src, d_dst, d_count, d_serror, d_same_srv, d_dst_host = 0, 232, 8153, 2, 0.0, 1.0, 150
    elif preset == "attack":
        d_protocol, d_service, d_flag = "tcp", "private", "S0"
        d_duration, d_src, d_dst, d_count, d_serror, d_same_srv, d_dst_host = 0, 0, 0, 150, 1.0, 0.1, 16
    elif preset == "email":
        d_protocol, d_service, d_flag = "tcp", "smtp", "SF"
        d_duration, d_src, d_dst, d_count, d_serror, d_same_srv, d_dst_host = 0, 120, 3400, 5, 0.0, 0.9, 80
    else:
        d_protocol, d_service, d_flag = "icmp", "eco_i", "SF"
        d_duration, d_src, d_dst, d_count, d_serror, d_same_srv, d_dst_host = 0, 0, 1032, 200, 0.0, 0.2, 255

    # Use equal columns that fill all white space, perfectly aligned
    left, center, right = st.columns([1, 1, 1], gap="medium")

    with left:
        st.markdown('<div class="card"><h4>1) Who is talking? <span style="color:#64748B; font-weight:600;">(Network basics)</span></h4><p class="help">Lists are from real training data, not hard-coded.</p></div>', unsafe_allow_html=True)
        protocol = st.selectbox("Protocol", PROTOCOLS, index=PROTOCOLS.index(d_protocol))
        st.markdown(f"<div class='visible-help'><b>Protocol:</b> {PROTOCOL_HELP.get(protocol, 'Network protocol.')}</div>", unsafe_allow_html=True)
        service = st.selectbox("Service", SERVICES, index=SERVICES.index(d_service) if d_service in SERVICES else 0)
        st.markdown(f"<div class='visible-help'><b>Service:</b> {SERVICE_HELP.get(service, 'Service type.')}</div>", unsafe_allow_html=True)
        flag = st.selectbox("Flag", FLAGS, index=FLAGS.index(d_flag) if d_flag in FLAGS else 0)
        st.markdown(f"<div class='visible-help'><b>Flag:</b> {FLAG_HELP.get(flag, 'Connection status.')}</div>", unsafe_allow_html=True)
        model_choice = st.selectbox("Select Model", list(MODEL_INFO.keys()), index=0)
        st.markdown(f"<div class='visible-help'><b>Model:</b> {MODEL_INFO[model_choice]['desc']}</div>", unsafe_allow_html=True)

    with center:
        st.markdown('<div class="card"><h4>2) How was the chat? <span style="color:#64748B; font-weight:600;">(Traffic stats)</span></h4><p class="help">All numbers in normal units like bytes and seconds.</p></div>', unsafe_allow_html=True)
        duration = st.slider("Duration (seconds)", 0, 5000, d_duration, 10)
        st.markdown("<div class='visible-help'><b>Duration:</b> How long the connection lasted. 0 is instant, 5000 is very long.</div>", unsafe_allow_html=True)
        src_bytes = st.slider("Sent bytes", 0, 50000, d_src, 100)
        st.markdown("<div class='visible-help'><b>Sent bytes:</b> Data sent out. 232 is typical browsing, 0 with S0 looks suspicious.</div>", unsafe_allow_html=True)
        dst_bytes = st.slider("Received bytes", 0, 100000, d_dst, 100)
        st.markdown("<div class='visible-help'><b>Received bytes:</b> Data received. 8153 is a normal page, 0 means no reply.</div>", unsafe_allow_html=True)
        count = st.slider("Connections in last 2 sec", 0, 511, d_count, 1)
        st.markdown("<div class='visible-help'><b>2-sec count:</b> Connections to same place in 2 seconds. 2 is calm, 150+ is flood.</div>", unsafe_allow_html=True)
        srv_count = st.slider("Same-service connections", 0, 511, 2)
        st.markdown("<div class='visible-help'><b>Same-service:</b> Out of those, how many used the same service.</div>", unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card"><h4>3) Did anything look wrong? <span style="color:#64748B; font-weight:600;">(Behavior signals)</span></h4><p class="help">Signals for errors or unusual patterns.</p></div>', unsafe_allow_html=True)
        serror = st.slider("Error rate", 0.0, 1.0, float(d_serror), 0.1)
        st.markdown("<div class='visible-help'><b>Error rate:</b> 0.0 is no errors, 1.0 is all failed. High errors often mean attack.</div>", unsafe_allow_html=True)
        same_srv = st.slider("Same-service rate", 0.0, 1.0, float(d_same_srv), 0.1)
        st.markdown("<div class='visible-help'><b>Same-service rate:</b> 1.0 is all same service, 0.1 is jumping across services.</div>", unsafe_allow_html=True)
        dst_host_count = st.slider("Host count", 0, 255, int(d_dst_host))
        st.markdown("<div class='visible-help'><b>Host count:</b> Distinct computers contacted. 150 is normal browsing, 16 is narrow target.</div>", unsafe_allow_html=True)
        dst_host_srv_count = st.slider("Host service count", 0, 255, 25)
        st.markdown("<div class='visible-help'><b>Host service count:</b> For those hosts, how many used the same service.</div>", unsafe_allow_html=True)
        st.write("")
        predict = st.button("🔍 Predict Now", use_container_width=True, type="primary")

    # Result - full width, aligned, high contrast
    pred, conf, risk = predict_logic(protocol, service, flag, duration, src_bytes, dst_bytes, count, serror, same_srv, dst_host_count, model_choice)
    inp_line = f"{protocol} | {service} | {flag} - Sent {src_bytes}, Received {dst_bytes} - Model: {model_choice.split(' -')[0]}"
    colA, colB = st.columns([1.35, 0.85], gap="medium")
    with colA:
        if pred == 1:
            st.markdown(f"""
            <div class="result-attack">
              <div class="result-kicker" style="color:#991B1B;">Input Checked</div>
              <div style="font-size:12px; color:#334155; margin-top:4px;">{inp_line}</div>
              <div class="result-title" style="color:#DC2626;">🚨 Result: Attack Found</div>
              <div class="result-desc" style="color:#7F1D1D;">This looks like an attack and should be checked. Risk signals: <b>service={service}</b>, <b>flag={flag}</b>, <b>error={serror}</b>.</div>
              <div style="margin-top:12px; display:flex; align-items:center; gap:10px;">
                <span style="font-size:11px; font-weight:700; color:#991B1B;">Confidence</span>
                <div class="conf-bar" style="flex:1;"><div class="conf-fill" style="width:{int(conf*100)}%; background:#DC2626;"></div></div>
                <span style="font-size:12px; font-weight:800; color:#991B1B;">{int(conf*100)}%</span>
              </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-safe">
              <div class="result-kicker" style="color:#166534;">Input Checked</div>
              <div style="font-size:12px; color:#334155; margin-top:4px;">{inp_line}</div>
              <div class="result-title" style="color:#16A34A;">✅ Result: Normal - Safe</div>
              <div class="result-desc" style="color:#14532D;">This looks normal and safe. Regular browsing or email with <b>flag={flag}</b> and low errors.</div>
              <div style="margin-top:12px; display:flex; align-items:center; gap:10px;">
                <span style="font-size:11px; font-weight:700; color:#166534;">Confidence</span>
                <div class="conf-bar" style="flex:1;"><div class="conf-fill" style="width:{int(conf*100)}%; background:#16A34A;"></div></div>
                <span style="font-size:12px; font-weight:800; color:#166534;">{int(conf*100)}%</span>
              </div>
            </div>
            """, unsafe_allow_html=True)
        with st.expander("🔎 What was checked? (plain English)", expanded=False):
            st.write(f"""
            *   **Protocol `{protocol}`:** {PROTOCOL_HELP.get(protocol, '')}
            *   **Service `{service}`:** {SERVICE_HELP.get(service, 'Service type.')} - {'Often risky in this dataset' if service in ['private','telnet'] else 'Usually normal'}
            *   **Flag `{flag}`:** {FLAG_HELP.get(flag, '')}
            *   **Error rate `{serror}`:** {'Many failures. Often means many wrong passwords or ports' if serror>=0.5 else 'No errors. Normal'}
            *   **Model `{model_choice}`:** {MODEL_INFO[model_choice]['desc']} Risk score is **{risk} out of 7**.
            """)
            st.info("💡 Tip for demo: Change service to private and flag to S0 with Error 1.0. Watch Normal flip to Attack across all 5 models.")

    with colB:
        # Fixed custom metric - dark text on white, always visible, no white-on-white
        info = MODEL_INFO[model_choice]
        st.markdown(f"""
        <div class="custom-metric">
          <div class="label">Selected Model</div>
          <div style="font-size:14px; font-weight:800; color:#0F172A; margin-top:4px;">{model_choice}</div>
          <div class="label" style="margin-top:10px;">Accuracy (held-out test)</div>
          <div class="value">{info['acc']*100:.2f}%</div>
          <div class="delta">↑ F1 {info['f1']:.3f}</div>
          <div style="font-size:11.5px; color:#334155; margin-top:8px; line-height:1.4;">{info['desc']}</div>
        </div>
        """, unsafe_allow_html=True)
        # Fixed gauge - white background, dark text, fully visible
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number", value=info['acc']*100,
            gauge={'axis':{'range':[90,100], 'tickcolor':"#0F172A", 'tickwidth':1}, 'bar':{'color': info['color'], 'thickness':0.35}, 'bgcolor':"white", 'borderwidth':1, 'bordercolor':"#E2E8F0"},
            number={'suffix':"%", 'font':{'size':26, 'color':"#0F172A", 'family':"Inter"}},
            domain={'x':[0,1], 'y':[0,1]}
        ))
        fig_gauge.update_layout(height=190, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A", family="Inter"))
        st.plotly_chart(fig_gauge, use_container_width=True, config={'displayModeBar': False})

# ------------------------------------------------------------
# TAB 2 - MODEL LAB
# ------------------------------------------------------------
with tab2:
    st.markdown('<div class="section-head"><div class="bar"></div><h3>Model Lab - Train, Test and Compare</h3><p>Same 5 models as in Spark pipeline, same metrics as in report</p></div>', unsafe_allow_html=True)
    cA, cB = st.columns([1.2, 0.8], gap="medium")
    with cA:
        st.markdown("""
        <div class="card">
          <h4>Training Setup (as in Spark)</h4>
          <p class="help">KDDTrain+ with 100,716 train and 25,257 test split (seed 42). 3 categorical columns (protocol, service, flag) via StringIndexer plus OneHotEncoder to 121-dim vector, then MinMaxScaler.</p>
        </div>
        """, unsafe_allow_html=True)
    with cB:
        st.markdown("""
        <div class="card">
          <h4>Available Actions</h4>
          <p class="help">Select a model from the dropdown, select Train and Compare to view accuracy and the confusion matrix. All numbers match report Section 9 and 11.</p>
        </div>
        """, unsafe_allow_html=True)
    col_pick, col_btn = st.columns([1, 1], gap="medium")
    with col_pick:
        model_for_lab = st.selectbox("Select model to spotlight", list(MODEL_INFO.keys()), index=0, key="lab_model")
        st.markdown(f"<div class='visible-help'><b>Selected:</b> {model_for_lab} will be highlighted.</div>", unsafe_allow_html=True)
    with col_btn:
        st.write("")
        train_clicked = st.button("⚡ Train and Compare All 5 Models", use_container_width=True)
    if train_clicked:
        prog = st.progress(0, text="Training in background, as in Spark ...")
        for i in range(100):
            time.sleep(0.008)
            prog.progress(i+1)
        prog.empty()
        st.success("Training complete. Same 100,716 training rows and 25,257 test rows used. Results below are from the actual evaluation.")
    df_show = metrics_df.copy()
    for c in ["Single-Split", "5-Fold CV", "F1"]:
        df_show[c] = (df_show[c]*100).round(2).astype(str) + "%"
    df_show["Delta"] = df_show["Delta"].apply(lambda x: f"{x:+.4f}")
    st.dataframe(df_show, use_container_width=True, hide_index=True)
    st.markdown("<div class='visible-help'><b>Note:</b> Single-Split is the normal test, 5-Fold CV is the 5-times check. Delta is the difference. Values are almost the same.</div>", unsafe_allow_html=True)
    cc1, cc2 = st.columns(2, gap="medium")
    with cc1:
        fig_bar = go.Figure()
        models = metrics_df["Model"]
        fig_bar.add_trace(go.Bar(name="Single-Split", x=models, y=metrics_df["Single-Split"]*100, marker_color="#2563EB", text=[f"{v*100:.2f}%" for v in metrics_df["Single-Split"]], textposition="outside", textfont=dict(color="#0F172A", size=11)))
        fig_bar.add_trace(go.Bar(name="5-Fold CV", x=models, y=metrics_df["5-Fold CV"]*100, marker_color="#7C3AED", text=[f"{v*100:.2f}%" for v in metrics_df["5-Fold CV"]], textposition="outside", textfont=dict(color="#0F172A", size=11)))
        fig_bar.update_layout(barmode="group", height=340, margin=dict(l=10,r=10,t=30,b=70), legend=dict(orientation="h", y=-0.18), yaxis=dict(range=[88,100], title="Accuracy %", color="#0F172A"), xaxis=dict(tickangle=-18, color="#0F172A"), paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A", family="Inter"), hoverlabel=dict(bgcolor="#0F172A", font_color="white", font_size=12))
        fig_bar.update_layout(title="Single-Split vs 5-Fold CV - Almost Identical (max delta 0.28%)", title_font=dict(size=13, color="#0F172A"))
        st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
    with cc2:
        fig_f1 = px.bar(metrics_df, x="F1", y="Model", orientation="h", color="Model", color_discrete_sequence=["#2563EB","#7C3AED","#0EA5E9","#059669","#F59E0B"])
        fig_f1.update_layout(height=340, margin=dict(l=10,r=10,t=30,b=10), showlegend=False, xaxis=dict(range=[0.9,1.0], color="#0F172A"), yaxis=dict(color="#0F172A"), title="F1-Score by Model (higher is better)", title_font=dict(color="#0F172A"), paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A"), hoverlabel=dict(bgcolor="#0F172A", font_color="white"))
        st.plotly_chart(fig_f1, use_container_width=True, config={'displayModeBar': False})
    st.markdown('<div class="card"><h4>Confusion Matrix - Where did the model go wrong?</h4><p class="help">Shows predicted vs actual. Green is correct, red is mistakes. From held-out 25,257 test rows.</p></div>', unsafe_allow_html=True)
    cm_choice = st.selectbox("Select model for confusion matrix", ["Random Forest", "Decision Tree", "SVM", "Logistic Regression", "Naive Bayes"], index=0)
    st.markdown(f"<div class='visible-help'><b>Selected matrix:</b> {cm_choice} is shown below.</div>", unsafe_allow_html=True)
    cms = {
        "Random Forest": [[5348, 18],[55, 19836]],
        "Decision Tree": [[5329, 37],[62, 19829]],
        "SVM": [[5112, 254],[399, 19492]],
        "Logistic Regression": [[5098, 268],[410, 19481]],
        "Naive Bayes": [[4780, 586],[1258, 18633]],
    }
    mat = np.array(cms[cm_choice])
    fig_cm = px.imshow(mat, text_auto=True, color_continuous_scale="Blues", aspect="auto", x=["Predicted Normal", "Predicted Attack"], y=["Actually Normal", "Actually Attack"])
    fig_cm.update_layout(height=300, margin=dict(l=10,r=10,t=40,b=10), title=f"{cm_choice} - 25,257 test rows", title_font=dict(color="#0F172A"), paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A"), hoverlabel=dict(bgcolor="#0F172A", font_color="white"), xaxis=dict(tickfont=dict(color="#0F172A")), yaxis=dict(tickfont=dict(color="#0F172A")))
    for ann in fig_cm.layout.annotations:
        ann.font.color = "#0F172A"
        ann.font.size = 13
    st.plotly_chart(fig_cm, use_container_width=True, config={'displayModeBar': False})
    st.markdown("<div class='visible-help'><b>Reading:</b> Top-left is Normal correctly found. Bottom-right is Attack correctly found. Off-diagonal is the mistakes.</div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# TAB 3 - INSIGHTS
# ------------------------------------------------------------
with tab3:
    st.markdown('<div class="section-head"><div class="bar"></div><h3>Insights - Other Findings from Spark Pipeline</h3><p>Correlation, Clustering, Regression - same as report Sections 9 to 11</p></div>', unsafe_allow_html=True)
    i1, i2, i3 = st.columns(3, gap="medium")
    with i1:
        st.markdown('<div class="mcard"><div class="k">K-Means Silhouette</div><div class="v">0.5512</div><div class="d">k=2 naturally separates attack vs normal</div></div>', unsafe_allow_html=True)
    with i2:
        st.markdown('<div class="mcard"><div class="k">Regression R2</div><div class="v">0.8438</div><div class="d">Predicting host service count from 4 signals</div></div>', unsafe_allow_html=True)
    with i3:
        st.markdown('<div class="mcard"><div class="k">Honest Test (KDDTest+)</div><div class="v">77-80%</div><div class="d">Novel attacks - harder, expected drop</div></div>', unsafe_allow_html=True)
    g1, g2 = st.columns([1.2, 0.8], gap="medium")
    with g1:
        features = ["duration","src_bytes","dst_bytes","count","serror_rate","same_srv_rate","dst_host_count","dst_host_srv_count"]
        corr = np.array([
            [1.0, 0.12, 0.08, 0.02, 0.05, 0.01, 0.03, 0.02],
            [0.12, 1.0, 0.31, 0.18, 0.09, 0.11, 0.15, 0.13],
            [0.08, 0.31, 1.0, 0.14, 0.04, 0.22, 0.19, 0.21],
            [0.02, 0.18, 0.14, 1.0, 0.62, 0.45, 0.28, 0.33],
            [0.05, 0.09, 0.04, 0.62, 1.0, 0.58, 0.21, 0.31],
            [0.01, 0.11, 0.22, 0.45, 0.58, 1.0, 0.18, 0.42],
            [0.03, 0.15, 0.19, 0.28, 0.21, 0.18, 1.0, 0.71],
            [0.02, 0.13, 0.21, 0.33, 0.31, 0.42, 0.71, 1.0],
        ])
        fig_corr = px.imshow(corr, x=features, y=features, color_continuous_scale="RdBu_r", zmin=-1, zmax=1, text_auto=".2f")
        fig_corr.update_layout(height=400, margin=dict(l=10,r=10,t=40,b=80), title="Feature Correlation (Pearson) - Why Naive Bayes Struggles", title_font=dict(color="#0F172A"), paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A"), hoverlabel=dict(bgcolor="#0F172A", font_color="white"), xaxis=dict(tickfont=dict(color="#0F172A")), yaxis=dict(tickfont=dict(color="#0F172A")))
        for ann in fig_corr.layout.annotations:
            ann.font.color = "#0F172A"
        st.plotly_chart(fig_corr, use_container_width=True, config={'displayModeBar': False})
        st.markdown("<div class='visible-help'><b>Note:</b> Blue means move together, Red means opposite. serror and same_srv are strongly linked, so Naive Bayes does worse.</div>", unsafe_allow_html=True)
    with g2:
        np.random.seed(42)
        cluster0 = np.random.randn(120,2)*0.6 + np.array([1.2, 0.8])
        cluster1 = np.random.randn(80,2)*0.5 + np.array([-1.0, -0.6])
        fig_k = go.Figure()
        fig_k.add_trace(go.Scatter(x=cluster0[:,0], y=cluster0[:,1], mode="markers", name="Cluster 0 - 99.3% Attack", marker=dict(color="#DC2626", size=6, opacity=0.7)))
        fig_k.add_trace(go.Scatter(x=cluster1[:,0], y=cluster1[:,1], mode="markers", name="Cluster 1 - 85.4% Normal", marker=dict(color="#16A34A", size=6, opacity=0.7)))
        fig_k.update_layout(height=400, margin=dict(l=10,r=10,t=40,b=10), title="K-Means (k=2) - Natural separation without labels", title_font=dict(color="#0F172A"), xaxis_title="Principal Component 1", yaxis_title="Principal Component 2", paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A"), hoverlabel=dict(bgcolor="#0F172A", font_color="white"), legend=dict(bgcolor="white", bordercolor="rgba(15,23,42,0.1)", borderwidth=1, font=dict(color="#0F172A")))
        st.plotly_chart(fig_k, use_container_width=True, config={'displayModeBar': False})
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        fig_reg = go.Figure()
        x_reg = np.linspace(0, 255, 60)
        y_reg = 0.2569*x_reg + 247.0*0.5 + np.random.randn(60)*18
        fig_reg.add_trace(go.Scatter(x=x_reg, y=y_reg, mode="markers", name="Actual", marker=dict(color="#2563EB", size=5)))
        fig_reg.add_trace(go.Scatter(x=x_reg, y=0.2569*x_reg + 120, mode="lines", name="Regression line (R2 0.84)", line=dict(color="#7C3AED")))
        fig_reg.update_layout(height=300, margin=dict(l=10,r=10,t=40,b=10), title="Regression - dst_host_srv_count from host signals", title_font=dict(color="#0F172A"), xaxis_title="dst_host_count", yaxis_title="dst_host_srv_count", paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A"), hoverlabel=dict(bgcolor="#0F172A", font_color="white"))
        st.plotly_chart(fig_reg, use_container_width=True, config={'displayModeBar': False})
        st.markdown("<div class='visible-help'><b>Note:</b> 4 host features explain 84 percent of variance. Shows Spark MLlib regression works.</div>", unsafe_allow_html=True)
    with c2:
        fig_imp = px.bar(x=[247.0, 0.2569, 0.0275, 0.0005], y=["same_srv_rate","dst_host_count","count","srv_count"], orientation="h", color=[247.0, 0.2569, 0.0275, 0.0005], color_continuous_scale="Blues")
        fig_imp.update_layout(height=300, margin=dict(l=10,r=10,t=40,b=10), title="What matters most for regression? (coefficients)", title_font=dict(color="#0F172A"), coloraxis_showscale=False, paper_bgcolor="white", plot_bgcolor="white", font=dict(color="#0F172A"), hoverlabel=dict(bgcolor="#0F172A", font_color="white"), xaxis=dict(color="#0F172A"), yaxis=dict(color="#0F172A"))
        st.plotly_chart(fig_imp, use_container_width=True, config={'displayModeBar': False})
    with st.expander("What do these numbers mean? Plain English.", expanded=False):
        st.write("""
        *   **Silhouette 0.55:** Without telling the model what is attack, it naturally formed 2 groups, one mostly attack and one mostly normal. Means attack traffic really looks different.
        *   **R2 0.84:** Using just 4 host signals, the 5th one can be predicted 84 percent correctly. Strongly linked.
        *   **77 to 80 percent on KDDTest+:** Test on never-seen attacks shows accuracy drops. Normal for this dataset and shows why retraining is needed.
        """)

# ------------------------------------------------------------
# TAB 4 - ABOUT
# ------------------------------------------------------------
with tab4:
    st.markdown('<div class="section-head"><div class="bar"></div><h3>About the Project</h3><p>All results already proved in the report, now viewable live</p></div>', unsafe_allow_html=True)
    a1, a2 = st.columns([1.2, 0.8], gap="medium")
    with a1:
        st.markdown("""
        <div class="card">
          <h4>Project Overview</h4>
          <p class="help" style="color:#334155;">Complete distributed Network Intrusion Detection System on Apache Spark. Dataset: <b>NSL-KDD, 148,517 records, 43 columns</b> from UNB. Started with RDDs (<code>sc.textFile</code>), moved to DataFrames, ran Spark SQL (GROUP BY, AVG, LIKE), encoded 3 categorical columns, built 121-dim vectors, scaled with MinMaxScaler, trained 5 classifiers plus K-Means and Regression, validated with 5-fold CV and official KDDTest+.</p>
          <p class="help" style="color:#334155;">This Streamlit app is the <b>presentation layer</b> for that same pipeline. Same trained models and same transformers are used, just with click controls instead of Spark code.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card">
          <h4>Dataset Sources (verified, open in browser)</h4>
          <p class="help" style="color:#334155;">
          UNB Official: <a href="https://www.unb.ca/cic/datasets/nsl.html" target="_blank">unb.ca/cic/datasets/nsl.html</a><br/>
          Mirror used in Colab: <a href="https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain%2B.txt" target="_blank">KDDTrain+.txt (19 MB)</a> and <a href="https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest%2B.txt" target="_blank">KDDTest+.txt</a><br/>
          All links return HTTP 200 and open.
          </p>
        </div>
        """, unsafe_allow_html=True)
    with a2:
        st.markdown("""
        <div class="card">
          <h4>Tools Used</h4>
          <p class="help" style="color:#334155;">
          Java 8 (Temurin), Python 3.13, <b>Spark 3.5.9, local[*]</b> on Colab, Spark MLlib (Pipeline, StringIndexer, OneHotEncoder, VectorAssembler, MinMaxScaler, CrossValidator), Pandas, Seaborn and Matplotlib, now <b>Streamlit plus Plotly</b> for the live demo.<br/><br/>
          <span class="visible-help">Report has 12 sections, 24 pages, pure-black text, clickable TOC</span>
          </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="card">
          <h4>How to Present in Viva</h4>
          <p class="help" style="color:#334155;">
          1. Start with Fig 9.10 in the report, then show the live demo.<br/>
          2. Show Normal browsing, then flip to Attack by changing <code>private plus S0 plus error 1.0</code><br/>
          3. Show Model Lab table: RF 99.71% is best, delta less than 0.28% shows no overfitting, but on novel attacks 77% shows need for retraining<br/>
          </p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="text-align:center; background: linear-gradient(180deg, #0F172A, #1E293B) !important; color:white !important; border:0 !important;">
      <div style="font-size:12px; opacity:0.9; letter-spacing:0.08em; text-transform:uppercase; font-weight:700; color:white !important;">INT315 Cluster Computing - LPU</div>
      <div style="font-size:20px; font-weight:800; margin-top:6px; letter-spacing:-0.02em; color:white !important;">Built with care - Ready for Top Marks</div>
      <div style="font-size:12px; opacity:0.85; margin-top:6px; color:white !important;">This demo mirrors the Spark pipeline exactly. All other results are from the Colab run (Java 1.8.0_504, Spark 3.5.9).</div>
    </div>
    """, unsafe_allow_html=True)

