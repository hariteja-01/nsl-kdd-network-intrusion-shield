# AegisNet Shield: Distributed Network Intrusion Detection & Threat Intelligence System

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5.9-orange.svg)](https://spark.apache.org/)
[![Spark MLlib](https://img.shields.io/badge/Engine-Spark%20MLlib-red.svg)](https://spark.apache.org/mllib/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Production-FF4B4B.svg)](https://nsl-kdd-network-intrusion-shield.streamlit.app/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)

An enterprise-grade, distributed Network Intrusion Detection System (NIDS) and Security Operations Center (SOC) telemetry simulator built on **Apache Spark 3.5.9 MLlib**. 

The system processes large-scale network traffic, engineer 121-dimensional normalized feature vectors, and classifies connections in real time into **Benign Normal Traffic** or **Adversarial Network Attacks** with up to **99.71% accuracy** and 5-fold cross-validated stability.

---

## 🌐 Live Interactive Platform
Access the production dashboard: **[nsl-kdd-network-intrusion-shield.streamlit.app](https://nsl-kdd-network-intrusion-shield.streamlit.app/)**

---

## 🚀 Key Highlights & Empirical Performance

- **Distributed Big Data Engine**: Implemented using Apache Spark 3.5.9 (PySpark) with Spark RDDs, DataFrames, Spark SQL, and Spark MLlib.
- **Enterprise Benchmark Dataset**: Rigorously evaluated on **148,517 network connections** from the UNB NSL-KDD benchmark (125,973 training records + 22,544 held-out novel attack test records).
- **Leakage-Free 121-Dimensional Pipeline**: Categorical encoders (`StringIndexer` + `OneHotEncoder`) and `MinMaxScaler` fitted exclusively on training splits to prevent test leakage.
- **Multi-Model Benchmark Suite**:
  - **Random Forest**: 99.71% Accuracy | 0.9971 F1 | 5-Fold CV: 99.62% (Delta: 0.0009)
  - **Decision Tree**: 99.61% Accuracy | 0.9961 F1 | 5-Fold CV: 99.65% (Delta: 0.0004)
  - **Support Vector Machine (LinearSVC)**: 97.42% Accuracy | 0.9742 F1 | 5-Fold CV: 97.39% (Delta: 0.0003)
  - **Logistic Regression**: 97.32% Accuracy | 0.9731 F1 | 5-Fold CV: 97.35% (Delta: 0.0004)
  - **Naive Bayes**: 92.71% Accuracy | 0.9266 F1 | 5-Fold CV: 92.43% (Delta: 0.0028)
- **Unsupervised Anomaly Clustering**: K-Means ($k=2$, Silhouette 0.5512) proves that normal and attack traffic naturally form distinct geometric partitions with 99.3% attack purity in Cluster 0 without label supervision.
- **Multivariate Linear Regression**: Predicts host service patterns (`dst_host_srv_count`) from host traffic signals with $R^2 = 0.8438$, RMSE = 43.72, and MAE = 23.65.
- **Novel Attack Generalization Assessment**: Evaluated against 22,544 unseen zero-day attacks on the official KDDTest+ partition (77.1% - 79.8%), demonstrating why continuous retraining is vital for production intrusion defense.

---

## 📊 Empirical Classification Results (Hold-Out Test: 25,257 Records)

| Rank | Model Architecture | Accuracy | F1-Score | Precision | Recall | 5-Fold CV Accuracy | CV Delta | True Negative | False Positive | False Negative | True Positive |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 🥇 | **Random Forest** (60 trees, depth 12) | **99.71%** | **0.9971** | **0.9971** | **0.9971** | **99.62%** | **+0.0009** | **13,481** | **13** | **61** | **11,702** |
| 🥈 | **Decision Tree** (depth 10) | **99.61%** | **0.9961** | **0.9961** | **0.9961** | **99.65%** | **-0.0004** | **13,452** | **42** | **57** | **11,706** |
| 🥉 | **LinearSVC** (maxIter 50) | **97.42%** | **0.9742** | **0.9743** | **0.9742** | **97.39%** | **+0.0003** | **13,242** | **252** | **399** | **11,364** |
| 4 | **Logistic Regression** (L-BFGS) | **97.32%** | **0.9731** | **0.9732** | **0.9732** | **97.35%** | **-0.0004** | **13,228** | **266** | **412** | **11,351** |
| 5 | **Naive Bayes** (Multinomial) | **92.71%** | **0.9266** | **0.9309** | **0.9271** | **92.43%** | **+0.0028** | **13,203** | **291** | **1,551** | **10,212** |

---

## 🏗️ End-to-End System Pipeline

```
Raw Network Flows (148,517 NSL-KDD Records, 43 Features)
    │
    ▼
[Distributed Ingestion]: sc.textFile() RDD Partitions
    │
    ▼
[Structured DataFrame]: spark.read.csv(inferSchema=True, header=True)
    │
    ▼
[Exploratory Spark SQL]: Temporary Views, Aggregation, and Wildcard Traffic Filters
    │
    ▼
[Binary Target Mapping]: 23 granular attack classes mapped to 0.0 (Normal) vs 1.0 (Attack)
    │
    ▼
[Feature Engineering]: StringIndexer + OneHotEncoder on [protocol_type, service, flag]
    │
    ▼
[Vector Assembly]: VectorAssembler combining 38 numeric + 3 OHE vectors = 121 dimensions
    │
    ▼
[Feature Scaling]: MinMaxScaler fit strictly on training set (100,716 records)
    │
    ▼
[Model Training & Cross-Validation]: Parallel Spark MLlib execution (5 Classifiers, 5-Fold CV)
    │
    ▼
[Production Presentation]: 21st.dev-Inspired Streamlit SOC Telemetry Dashboard
```

---

## 🛠️ Technology Stack

- **Big Data & Analytics Engine**: Apache Spark 3.5.9 (PySpark), Spark SQL, Spark MLlib
- **Runtime Environment**: Java 8 (Adoptium OpenJDK 1.8.0_504), Python 3.10 / 3.13
- **Frontend & Visualization**: Streamlit, Plotly Express, Plotly Graph Objects
- **Data Science Tooling**: Pandas, NumPy, Matplotlib, Seaborn

---

## 💻 Local Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hariteja-01/nsl-kdd-network-intrusion-shield.git
   cd nsl-kdd-network-intrusion-shield
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Dashboard**:
   ```bash
   streamlit run app.py
   ```
   Open your browser at `http://localhost:8501`.

---

## 🔒 Security & Defense Applications

- **Real-Time Anomaly Scoring**: Evaluates TCP, UDP, and ICMP connection signatures against trained distributed decision boundaries.
- **Automated Incident Response Playbooks**: Provides actionable remediation advice (eBPF firewall rules, SYN flood rate-limiting, SIEM escalation).
- **Adversarial Drift Tracking**: Highlights detection degradation under novel unseen zero-day attacks to trigger automated retraining workflows.

---

## 📄 License
This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
