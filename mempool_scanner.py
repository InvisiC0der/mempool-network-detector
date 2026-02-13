import requests
import time
import datetime
import os

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
DUST_THRESHOLD = 546       # satoshis (Tracking attacks)
WHALE_THRESHOLD = 10       # BTC (Market manipulation)
SPAM_FEE_RATE = 2.0        # sats/vByte (Low fee = potential spam congestion)

# Terminal Colors for "Hacker" Aesthetic
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def log_threat(message):
    """Saves alerts to a file for forensic analysis"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("threat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def fetch_mempool_recent():
    try:
        response = requests.get("https://mempool.space/api/mempool/recent")
        if response.status_code == 200:
            return response.json()
    except:
        return []
    return []

def scan_network():
    # Clear screen for a dashboard look
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Colors.CYAN + "="*70)
    print(f"🛡️  BITCOIN MEMPOOL SENTINEL - ACTIVE MONITORING")
    print(f"📡 CONNECTED TO: Mainnet (Mempool.space API)")
    print("="*70 + Colors.RESET)
    
    while True:
        txs = fetch_mempool_recent()
        if not txs:
            print(Colors.YELLOW + "⚠️  Connection lost. Retrying..." + Colors.RESET)
            time.sleep(5)
            continue
            
        print(f"\n🔄 Scanning batch of {len(txs)} transactions at {datetime.datetime.now().strftime('%H:%M:%S')}...")
        
        threats_found = 0
        
        for tx in txs:
            txid = tx['txid']
            value = tx['value'] 
            size = tx['vsize']
            # Calculate Fee Rate (Satoshis per Byte)
            fee = tx['fee']
            fee_rate = fee / size if size > 0 else 0
            
            # --- DETECTION LOGIC ---
            
            # 1. DUST ATTACK (Privacy Threat)
            if value <= DUST_THRESHOLD:
                msg = f"🔴 [DUST ATTACK] Value: {value} sats | TX: {txid[:8]}..."
                print(Colors.RED + msg + Colors.RESET)
                log_threat(msg)
                threats_found += 1

            # 2. WHALE MOVEMENT (Volatility Threat)
            elif value > (WHALE_THRESHOLD * 100000000):
                btc_val = value / 100000000
                msg = f"🐳 [WHALE ALERT] Moved {btc_val:.2f} BTC | TX: {txid[:8]}..."
                print(Colors.CYAN + msg + Colors.RESET)
                log_threat(msg)
                threats_found += 1
                
            # 3. SPAM/CONGESTION (DoS Threat)
            # Low fee transactions flooding the mempool
            elif fee_rate < SPAM_FEE_RATE:
                # We don't print every spam tx (too noisy), just count them
                pass 

        # --- DASHBOARD SUMMARY ---
        if threats_found == 0:
            print(Colors.GREEN + "✅  Network Status: NORMAL (No immediate threats)" + Colors.RESET)
        else:
            print(Colors.YELLOW + f"⚠️  WARNING: {threats_found} potential threats flagged in this block." + Colors.RESET)
            
        print("-" * 70)
        time.sleep(8) # Wait for new data

if __name__ == "__main__":
    scan_network()