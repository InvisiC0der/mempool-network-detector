# Bitcoin Network Threat Monitor 

### Real-Time Threat Intelligence Dashboard for the Bitcoin Mempool

**Author:** Durga Prasath  
**Domain:** Network Security & Blockchain Forensics  


---

##  Project Overview
The Bitcoin Mempool is a chaotic environment often used as a vector for network attacks. **Dust Attacks** (tiny transactions) are used to deanonymize users, while **Spam Waves** (low-fee flooding) are used to congest the network (DoS).

I built this **Threat Monitor Dashboard** to visualize these anomalies in real-time. Unlike simple scripts, this tool provides a **Security Operations Center (SOC)** style interface, allowing analysts to spot attack patterns visually using interactive scatter plots and live metrics.

##  Key Features
* **Live Security Dashboard:** A "Matrix-style" dark mode interface built with **Streamlit** for real-time monitoring.
* **Interactive Threat Analysis:** Adjustable sliders to filter "Dust" (tracking attacks) and "Whale" (market manipulation) transactions on the fly.
* **Traffic Fingerprinting:** A dynamic **Bubble Chart** (Scatter Plot) that correlates Transaction Fee vs. Size to identify spam botnets.
* **Forensic Alerts:** Instant visual banners (Red/Green) when heuristic thresholds are breached.
* **Resilient API Handling:** Implements geometric backoff to handle rate limits from the Mempool.space API.

##  Technical Stack
* **Language:** Python 3.x
* **Frontend/UI:** `streamlit` (Web Dashboard)
* **Data Processing:** `pandas` (DataFrames for traffic analysis)
* **Visualization:** `plotly` (Interactive charts)
* **Networking:** `requests` (REST API Integration)

##  How to Run Locally
1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/mempool-network-detector.git](https://github.com/YOUR_USERNAME/mempool-network-detector.git)
    cd mempool-network-detector
    ```

2.  **Install dependencies**
    ```bash
    pip install streamlit pandas plotly requests
    ```

3.  **Launch the Dashboard**
    ```bash
    streamlit run dashboard.py
    ```
    *(This will automatically open the tool in your web browser)*

##  Dashboard Preview
**Security Status: Normal**  *Green banners indicate healthy network traffic.*

**Security Status: Attack Detected**  *Red alerts trigger immediately when Dust transactions spike above the threshold.*

---
*Disclaimer: This tool is designed for educational network analysis and monitoring.*
