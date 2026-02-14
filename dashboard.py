import streamlit as st
import requests
import pandas as pd
import time
import plotly.express as px

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Bitcoin Threat Intel",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS to make it look "Hacker-like" (Dark Mode)
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #00FF00;
    }
    .metric-card {
        background-color: #262730;
        border: 1px solid #4B4B4B;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# API FUNCTIONS
# ---------------------------------------------------------
def get_mempool_data():
    """Fetches the latest unconfirmed transactions"""
    try:
        # Get recent transactions
        tx_resp = requests.get("https://mempool.space/api/mempool/recent")
        # Get network stats (block height, etc.)
        block_resp = requests.get("https://mempool.space/api/blocks/tip/height")
        
        if tx_resp.status_code == 200:
            return tx_resp.json(), block_resp.text
    except:
        return [], "Error"
    return [], "Error"

# ---------------------------------------------------------
# MAIN DASHBOARD UI
# ---------------------------------------------------------
st.title("🛡️ Bitcoin Network Threat Monitor")
st.markdown("### Real-Time Forensic Analysis of Mempool Traffic")

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Scanner Settings")
    dust_limit = st.slider("Dust Threshold (Sats)", 0, 1000, 546)
    whale_limit = st.slider("Whale Threshold (BTC)", 1, 100, 10)
    refresh_rate = st.selectbox("Refresh Rate", [5, 10, 30])
    st.info("Status: 🟢 Connected to Mainnet")

# Placeholders for live updates
kpi1, kpi2, kpi3 = st.columns(3)
chart_col, log_col = st.columns([2, 1])

# ---------------------------------------------------------
# THE LIVE LOOP
# ---------------------------------------------------------
# Create a placeholder container that we can overwrite
placeholder = st.empty()

while True:
    txs, block_height = get_mempool_data()
    
    if not txs:
        time.sleep(2)
        continue

    # Process Data
    df = pd.DataFrame(txs)
    df['value_btc'] = df['value'] / 100_000_000
    
    # 1. Calculate Metrics
    dust_txs = df[df['value'] <= dust_limit]
    whale_txs = df[df['value_btc'] >= whale_limit]
    avg_fee = df['fee'].mean()
    
    # 2. Update UI inside the placeholder
    with placeholder.container():
        # KPI ROW
        k1, k2, k3, k4 = st.columns(4)
        k1.metric(label="🧱 Current Block", value=block_height)
        k2.metric(label="📉 Traffic Load", value=f"{len(txs)} txs")
        k3.metric(label="🌪️ Dust Attacks", value=len(dust_txs), delta_color="inverse")
        k4.metric(label="🐳 Whale Moves", value=len(whale_txs))

        # ALERT BANNER
        if len(dust_txs) > 0:
            st.error(f"🚨 SECURITY ALERT: {len(dust_txs)} Dusting Transactions Detected! Possible Surveillance Attempt.")
        else:
            st.success("✅ Network Traffic Normal. No active threats detected.")

        # VISUALIZATION ROW
        c1, c2 = st.columns([2, 1])
        
        with c1:
            st.subheader("Transaction Value Distribution")
            # Create a scatter plot: Value vs Fee
            fig = px.scatter(
                df, 
                x="value", 
                y="fee", 
                size="vsize", 
                color="value", 
                title="Mempool Traffic Fingerprint",
                log_x=True, log_y=True
            )
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.subheader("⚠️ Threat Log")
            if not dust_txs.empty:
                st.dataframe(dust_txs[['txid', 'value', 'fee']].head(10), hide_index=True)
            else:
                st.write("No anomalies in this batch.")

    # Pause before next update
    time.sleep(refresh_rate)