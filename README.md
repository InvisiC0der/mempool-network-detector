# Bitcoin Mempool & Network Anomaly Detector 

### Real-Time Intrusion Detection System (IDS) for Bitcoin

**Author:** Durga Prasath  
**Domain:** Network Forensics & Blockchain Security

---

##  Project Overview
The Bitcoin Mempool is a "waiting room" for unconfirmed transactions. However, it is often used as a vector for network attacks. **Dust Attacks** (tiny transactions) are used to deanonymize users, while **Spam Waves** (low-fee flooding) are used to congest the network (DoS).

I built this **Mempool Sentinel** to act as a security monitor. It connects to the live Bitcoin network, scans every new transaction, and logs potential threats based on heuristic analysis (Fee Rats, Dust Limits, and Whale Movements).

##  Key Features
* **Live Threat Detection:** Connects to `mempool.space` API to fetch real-time data every 10 seconds.
* **Dust Attack Identification:** Flags transactions under **546 Satoshis** (the standard dust limit) used for tracking surveillance.
* **Forensic Logging:** Automatically saves all flagged threats to a local `threat_log.txt` file for security review.
* **Visual Dashboard:** A color-coded terminal interface (Green/Red/Cyan) to visualize network health instantly.

## Technical Stack
* **Language:** Python 3.x
* **Networking:** `requests` (REST API Integration)
* **Forensics:** File I/O for persistent threat logging
* **OS Integration:** `os` module for cross-platform terminal management

## How to Run
1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/mempool-spam-detector.git](https://github.com/YOUR_USERNAME/mempool-spam-detector.git)
    cd mempool-spam-detector
    ```

2.  **Install dependencies**
    ```bash
    pip install requests
    ```

3.  **Start the Sentinel**
    ```bash
    python mempool_scanner_v2.py
    ```

## 📸 Sample Log Output (`threat_log.txt`)
```text
[2026-02-14 10:15:20]  [DUST ATTACK] Value: 546 sats | TX: a1b2c3...
[2026-02-14 10:15:22]  [WHALE ALERT] Moved 50.00 BTC | TX: d4e5f6...
