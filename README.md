# WireGuard VPN Infrastructure

A self-hosted VPN infrastructure built with WireGuard, FastAPI, and Ubuntu Linux.

This project demonstrates the implementation of a secure VPN architecture with automated client configuration generation, Linux networking, WireGuard tunnel management, and backend API development.

---

# Features

* Secure WireGuard VPN server setup
* Automated VPN client configuration generation
* Public/private key cryptography management
* FastAPI backend API
* Windows ↔ Linux encrypted VPN tunnels
* Linux networking and tunnel provisioning
* Downloadable `.conf` client files
* Modular Python backend structure

---

# Technologies Used

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| Python             | Backend development            |
| FastAPI            | REST API                       |
| WireGuard          | VPN tunneling                  |
| Ubuntu Linux (WSL) | VPN server environment         |
| Windows            | VPN client                     |
| Networking         | Routing & tunnel configuration |
| Cryptography       | Secure peer authentication     |

---

# Project Architecture

```text
Windows Client
       ↓
WireGuard Tunnel
       ↓
Ubuntu Linux (WSL)
       ↓
WireGuard Server (wg0)
```

---

# Backend Structure

```text
vpn-project/
│
├── backend/
│   ├── main.py
│   ├── utils/
│   │   ├── wireguard.py
│   │   └── config_generator.py
│   ├── configs/
│   └── venv/
│
├── README.md
└── .gitignore
```

---

# API Endpoints

| Endpoint           | Description                |
| ------------------ | -------------------------- |
| `/`                | API status                 |
| `/generate-keys`   | Generate WireGuard keys    |
| `/generate-config` | Generate VPN configuration |
| `/download-config` | Download `.conf` VPN file  |

---

# Example WireGuard Configuration

```ini
[Interface]
PrivateKey = CLIENT_PRIVATE_KEY
Address = 10.0.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = SERVER_PUBLIC_KEY
Endpoint = 127.0.0.1:51820
AllowedIPs = 10.0.0.0/24
PersistentKeepalive = 25
```

---

# Security

This project uses:

* Public/private key cryptography
* Secure encrypted WireGuard tunnels
* Peer-based authentication
* Isolated VPN IP addressing
* `.gitignore` protection for sensitive files and keys

Sensitive files such as private keys and generated VPN configurations are excluded from version control.

---

# Screenshots

## Recommended Screenshots

Add screenshots for:

1. FastAPI running locally
2. `/generate-config` API response
3. WireGuard Windows client connected
4. `sudo wg` output showing successful handshake
5. VSCode project structure
6. Ubuntu terminal running WireGuard server

---

# Future Improvements

* Full internet routing through VPN
* NAT & IP forwarding
* Web dashboard for VPN management
* User authentication system
* Docker deployment
* Cloud VPS deployment
* QR code generation for mobile clients
* Automated peer provisioning

---

# Learning Outcomes

This project helped develop skills in:

* Backend API development
* Linux system administration
* Networking fundamentals
* VPN architecture
* Cryptography concepts
* DevOps workflows
* Git & GitHub version control
* Secure infrastructure deployment

---

# Installation

## Clone repository

```bash
git clone https://github.com/tanim-veer/wireguard-vpn-infrastructure.git
```

## Start backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn pynacl
uvicorn main:app --reload
```

---

# Author

Tanim Veer

GitHub: [https://github.com/tanim-veer](https://github.com/tanim-veer)
