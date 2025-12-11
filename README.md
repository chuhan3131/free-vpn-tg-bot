# Telegram Bot with Free VPN Configs

### Get free VLESS, VMess, Trojan, and Shadowsocks VPN configs via Telegram.
![Bot Screenshot](https://github.com/user-attachments/assets/64636758-3533-4927-bf7c-21df32bb5576)

**Live bot:** [t.me/chfreevpn_bot](https://t.me/chfreevpn_bot)
## 🚀 Setup

### Option 1: Using pip (simple)
```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your BOT_TOKEN
python bot.py
```

### Option 2: Using uv (faster)
```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

cp .env.example .env
# Edit .env with your BOT_TOKEN
python bot.py
```


## 📋 Commands

- `/start` - Show bot info
- `/vpn` - Get VPN key
- `/donate` - Support the project

## 📁 Files

- `bot.py` - Main bot code
- `.env` - Configuration (create from `.env.example`)
- `requirements.txt` - Dependencies

---

## ⭐ If you like this project, give it a star!
- **Telegram DM:** [t.me/glattstyle](https://t.me/glattstyle)
- **Telegram Blog:** [t.me/chuhandev](https://t.me/chuhandev)  
- **Telegram Chat:** [t.me/chuhanchat](https://t.me/chuhanchat)
