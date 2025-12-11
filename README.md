# Telegram Bot with Free VPN Configs

Get free VLESS, VMess, Trojan, and Shadowsocks VPN configs via Telegram.

## 🚀 Setup

### Using uv (recommended)
```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and run
git clone https://github.com/chuhan3131/free-vpn-tg-bot.git
cd free-vpn-tg-bot
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your BOT_TOKEN

# Run
python bot.py
```

### Using pip
```bash
pip install -r requirements.txt
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
