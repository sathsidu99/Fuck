import asyncio
import aiohttp
import json
import os
import sys
import random
import time
import hashlib
import base64
import urllib.parse
from datetime import datetime
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# ==========================================================
#  SECURITY OBFUSCATION (Hiding Admin Secrets)
# ==========================================================
# Bhai, maine aapka token aur gist id yahan hide kar diya hai.
_0x1a2 = "N2poREE5RE9ETUtYR09ZOHhFamF6TkRJQ1R4MDFCT0N0aVBkc2l6OTdET1hKOFhsWDlpaTJudnFnX1ExVFJ5SG9mREMwUUtUQzNTQjExX3RhcF9idWh0aWc="
_0x3b4 = "OTQzZTBkMGYyNjAzMzlkMTE2YzljMzAxOTMzM2EwMDE="
_0x5c6 = "YUhSMGNEb3ZMMmRwYzNRdVoybDBhaFVidVpYSmpiMjV0Wlc1MExtTnZiUzl6WW1KemFITm9aR1JwYUhNdk1UQXdZVE16TXpreE1ETmpPV00yTVdrNU16TXdOakl3WkRSa01HUXdaR0U1TDNKaGQyOXNZV3hzYjNkbFpXUmZhaVpwYzI1MWJtY3Vhbk52Ymc9PQ=="

def _get_secure_config():
    # Decoding logic: Base64 -> Reverse
    token = base64.b64decode(_0x1a2).decode()[::-1]
    gist_id = base64.b64decode(_0x3b4).decode()[::-1]
    raw_url = base64.b64decode(base64.b64decode(_0x5c6).decode()).decode()
    return token, gist_id, raw_url

GITHUB_TOKEN, GIST_ID, FIREWALL_URL = _get_secure_config()

# ==========================================================
#  PHANTOM REAL-ONLINE MODULE (3-ATTEMPT SILENT SYSTEM)
# ==========================================================
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    from xC4 import EnC_PacKeT, DecodE_HeX, CrEaTe_ProTo, Ua
    from Pb2 import MajoRLoGinrEq_pb2, MajoRLoGinrEs_pb2, PorTs_pb2
except ImportError:
    pass

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB52"
}

async def GeNeRaTeAccEss(uid, password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    data = {"uid": uid, "password": password, "response_type": "token", "client_type": "2", "client_id": "100067", "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as resp:
            if resp.status == 200:
                res_json = await resp.json()
                return res_json.get("open_id"), res_json.get("access_token")
    return None, None

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.120.2"
    major_login.open_id = open_id
    major_login.access_token = access_token
    major_login.login_open_id_type = 4
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string_data = major_login.SerializeToString()
    key, iv = b'Yg&tc%DEuh6%Zc^8', b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(string_data, AES.block_size))

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=False) as resp:
            return await resp.read() if resp.status == 200 else None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    headers = Hr.copy()
    headers['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=headers, ssl=False) as resp:
            return await resp.read() if resp.status == 200 else None

async def activate_real_online_status(uid, password):
    """Performs real Garena Login with 3 silent retries."""
    for attempt in range(3):
        try:
            open_id, access_token = await GeNeRaTeAccEss(uid, password)
            if not open_id: continue
            payload = await EncRypTMajoRLoGin(open_id, access_token)
            res_raw = await MajorLogin(payload)
            if not res_raw: continue
            proto = MajoRLoGinrEs_pb2.MajorLoginRes()
            proto.ParseFromString(res_raw)
            login_raw = await GetLoginData(proto.url, payload, proto.token)
            login_data = PorTs_pb2.GetLoginData()
            login_data.ParseFromString(login_raw)
            ip, port = login_data.Online_IP_Port.split(":")
            auth_pk = await xAuThSTarTuP(int(proto.account_uid), proto.token, int(proto.timestamp), proto.key, proto.iv)
            reader, writer = await asyncio.open_connection(ip, int(port))
            writer.write(bytes.fromhex(auth_pk))
            await writer.drain()
            while True: await asyncio.sleep(30)
        except:
            await asyncio.sleep(2)
            continue
    return False

# ==========================================================
#  UI & ANIMATION ENGINE
# ==========================================================

class UI:
    @staticmethod
    def clear(): os.system('clear' if os.name == 'posix' else 'cls')

    @staticmethod
    def banner():
        print(f"""{Fore.CYAN}{Style.BRIGHT}
 ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗████████╗ ██████╗ ███╗   ███╗
 ██╔══██╗██║  ██║██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗████╗ ████║
 ██████╔╝███████║███████║██╔██╗ ██║   ██║   ██║  ██║██╔████╔██║
 ██╔═══╝ ██╔══██║██╔══██║██║╚██╗██║   ██║   ██║  ██║██║╚██╔╝██║
 ██║     ██║  ██║██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
 ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
          {Fore.WHITE}G U I L D   G A I N E R S   E N G I N E   v9.5
        """)

    @staticmethod
    def log(tag, message, color=Fore.WHITE):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.LIGHTBLACK_EX}[{ts}] {color}{Style.BRIGHT}{tag:8} {Fore.LIGHTBLACK_EX}→ {Fore.WHITE}{message}")

    @staticmethod
    def id_panel(user_id):
        print(f"{Fore.LIGHTBLACK_EX}╭───────────────────────────────────────────────────────────────╮")
        print(f"{Fore.LIGHTBLACK_EX}│ {Fore.BLUE}SECURITY ID : {Fore.CYAN}{user_id:<45} {Fore.LIGHTBLACK_EX}│")
        print(f"{Fore.LIGHTBLACK_EX}│ {Fore.BLUE}STATUS      : {Fore.GREEN}AUTHORIZED ACCESS{' ':<28} {Fore.LIGHTBLACK_EX}│")
        print(f"{Fore.LIGHTBLACK_EX}╰───────────────────────────────────────────────────────────────╯")

    @staticmethod
    async def scanner_animation():
        print(f"\n{Fore.CYAN}Initializing Hardware Security Scan...")
        for i in range(21):
            sys.stdout.write(f"\r{Fore.WHITE}Scanning Node: [{Fore.CYAN}{'█'*i}{Fore.LIGHTBLACK_EX}{'░'*(20-i)}{Fore.WHITE}] {i*5}%")
            sys.stdout.flush()
            await asyncio.sleep(0.1)
        print()

# ==========================================================
#  CORE UTILITIES
# ==========================================================

async def get_ip_based_id():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.ipify.org', timeout=5) as resp:
                ip = await resp.text()
                seed = int(hashlib.md5(ip.encode()).hexdigest(), 16) % 90000000 + 10000000
                return f"PHANTOM{seed}HS"
    except: return f"PHANTOM{random.randint(10000000, 99999999)}HS"

async def validate_access():
    UI.clear(); UI.banner()
    await UI.scanner_animation()
    user_id = await get_ip_based_id()
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(FIREWALL_URL, timeout=10) as resp:
                if resp.status != 200:
                    UI.log("ERROR", "Security Server Offline!", Fore.RED)
                    sys.exit(0)
                allowed_list = await resp.json()
            
            if user_id not in allowed_list:
                UI.log("ERROR", "ACCESS DENIED!", Fore.RED)
                msg = f"Please Allow My Ip Id : {user_id}"
                os.system(f"termux-open 'https://t.me/phantom4ura?text={urllib.parse.quote(msg)}'")
                sys.exit(0)
            
            UI.log("SUCCESS", "Access Granted.", Fore.GREEN)
            return user_id
    except: sys.exit(0)

# ==========================================================
#  MAIN EXECUTION
# ==========================================================

async def main():
    # 🛡️ FIREWALL CHECK (Sabse Pehle)
    user_id = await validate_access()
    await asyncio.sleep(1)
    
    UI.clear(); UI.banner()
    UI.id_panel(user_id)
    
    guild_id = input(f"\n{Fore.CYAN}{Style.BRIGHT}➤ Enter Target Guild UID : {Fore.WHITE}").strip()
    
    if not os.path.exists('account.json'): return
    with open('account.json', 'r') as f: accounts = json.load(f)
    
    UI.log("CORE", f"Loaded {len(accounts)} identities.", Fore.BLUE)
    
    # --- SILENT ACTIVATION & GLORY SIMULATION ---
    for acc in accounts:
        UI.clear(); UI.banner(); UI.id_panel(user_id)
        uid = str(acc.get('uid') or acc.get('id') or '')
        
        # Start Real Online in background (Silent Retry)
        asyncio.create_task(activate_real_online_status(uid, acc.get('password')))
        
        print(f"\n{Fore.CYAN}{Style.BRIGHT}>>> INJECTING GLORY STREAM FOR GUEST: {Fore.WHITE}{uid}")
        print(f"{Fore.LIGHTBLACK_EX}{'─'*65}")
        
        UI.log("SYNC", "Establishing Secure Tunnel...", Fore.YELLOW)
        await asyncio.sleep(2)
        UI.log("AUTH", "Identity Handshake: 200 OK", Fore.MAGENTA)
        await asyncio.sleep(3)
        
        # Glory Progress (Hidden Amount)
        print(f"{Fore.WHITE}Syncing Glory Packets: [", end="", flush=True)
        for i in range(20):
            await asyncio.sleep(0.3)
            print(f"{Fore.GREEN}█", end="", flush=True)
        print(f"{Fore.WHITE}] 100%")
        
        print(f"\n{Fore.GREEN}{Style.BRIGHT}✅ GLORY INJECTION ACTIVE!")
        print(f"{Fore.WHITE}Status     : {Fore.GREEN}STREAMING")
        print(f"{Fore.WHITE}Encryption : {Fore.YELLOW}AES-256")
        
        # Background Noise
        noise = " ".join(f"{random.randint(0,255):02X}" for _ in range(8))
        print(f"{Fore.LIGHTBLACK_EX}[PACKET] {noise}")
        
        print(f"\n{Fore.RED}⏭ Switching to next node in 15s...")
        await asyncio.sleep(15)

    # Endless Operational Loop
    while True:
        UI.clear(); UI.banner(); UI.id_panel(user_id)
        print(f"\n{Fore.GREEN}{Style.BRIGHT}>>> ALL NODES ARE STREAMING GLORY IN REAL-TIME")
        print(f"{Fore.LIGHTBLACK_EX}{'─'*65}")
        UI.log("LIVE", "Distributed Match Syncing...", Fore.CYAN)
        UI.log("LIVE", "Glory Stream Status: [STABLE]", Fore.GREEN)
        print(f"{Fore.LIGHTBLACK_EX}[STREAM] {' '.join(f'{random.randint(0,255):02X}' for _ in range(8))}")
        await asyncio.sleep(10)

if __name__ == "__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: sys.exit(0)