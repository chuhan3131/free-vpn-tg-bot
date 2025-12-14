# 🌐 **Telegram VPN Bot**

Get **free VLESS, VMess, Trojan, and Shadowsocks VPN configs** instantly via Telegram.

<img width="524" height="655" alt="изображение" src="https://github.com/user-attachments/assets/43314f2c-18c9-4227-a65f-d0c6d25134e2" />


**💬 Live Bot:** [t.me/chfreevpn_bot](https://t.me/chfreevpn_bot)

---

## 🚀 **Setup**

### 1️⃣ Using `pip` (Simple)

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your BOT_TOKEN
python main.py
```

### 2️⃣ Using `uv` (Faster)

```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

cp .env.example .env
# Edit .env with your BOT_TOKEN
python main.py
```

---

## 📋 **Commands**

| Command   | Description               |
| --------- | ------------------------- |
| `/start`  | Show bot info             |
| `/vpn`    | Get a VPN key             |
| `/donate` | Support the project       |
| `/api`    | Examples of using the API |

---

## 📁 **Project Files**

| File / Folder      | Purpose                        |
| ------------------ | ------------------------------ |
| `main.py`          | Main bot code                  |
| `config.py`        | Bot configuration              |
| `.env.example`     | Example env file               |
| `requirements.txt` | Python dependencies            |
| `keys_counter.txt` | Counter for VPN keys           |
| `handlers/`        | Bot command and event handlers |
| `utils/`           | Utility functions              |

---

## ⭐ **Support & Community**

If you like this project, give it a ⭐!

* **Telegram DM:** [t.me/glattstyle](https://t.me/glattstyle)
* **Telegram Blog:** [t.me/chuhandev](https://t.me/chuhandev)
* **Telegram Chat:** [t.me/chuhanchat](https://t.me/chuhanchat)
