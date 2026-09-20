# WireGuard VPN Infrastructure

API FastAPI qui génère des clés WireGuard et des fichiers de configuration client, associée à un serveur VPN WireGuard sous Ubuntu (WSL) et à un client Windows.

Projet personnel réalisé pour comprendre le fonctionnement d'un VPN de bout en bout : cryptographie à clés publiques, tunnel chiffré, adressage réseau et automatisation côté backend.

**Stack :** Python · FastAPI · PyNaCl · WireGuard · Ubuntu (WSL) · Windows

---

## Ce que fait le projet

- Génère des paires de clés WireGuard (Curve25519) avec PyNaCl, encodées en base64 au format attendu par WireGuard
- Génère automatiquement le fichier `.conf` d'un client (interface, pair, DNS, keepalive)
- Expose ces fonctions via une API REST, avec un endpoint pour télécharger le fichier `client.conf`
- Établit un tunnel chiffré entre un client Windows et un serveur WireGuard sous Ubuntu, vérifié par un handshake réussi

## Architecture

```text
Client Windows (WireGuard)
        │
        │  tunnel chiffré (UDP 51820)
        ▼
Ubuntu / WSL ── serveur WireGuard (interface wg0)

API FastAPI ──► génère les clés et le fichier client.conf
```

## Structure du projet

```text
.
├── backend/
│   ├── main.py                    # API FastAPI (routes)
│   └── utils/
│       ├── wireguard.py           # génération des clés publique/privée
│       └── config_generator.py    # génération du fichier .conf client
├── .gitignore                     # exclut venv, clés (*.key) et configs générées
└── README.md
```

## Endpoints de l'API

| Méthode | Route | Description |
|---|---|---|
| GET | `/` | Vérifie que l'API fonctionne |
| GET | `/generate-keys` | Génère une paire de clés WireGuard |
| GET | `/generate-config` | Génère une configuration client (retournée en JSON) |
| GET | `/download-config` | Génère et télécharge le fichier `client.conf` |

Exemple de configuration générée :

```ini
[Interface]
PrivateKey = <clé privée du client>
Address = 10.0.0.2/32
DNS = 1.1.1.1

[Peer]
PublicKey = <clé publique du serveur>
Endpoint = <ip-du-serveur>:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

## Captures d'écran

**API FastAPI en cours d'exécution**

<img width="768" height="287" alt="API FastAPI lancée avec uvicorn" src="https://github.com/user-attachments/assets/fc24482d-c4ca-422b-8044-6f9276df1eb1" />

**Génération de la configuration VPN**

<img width="639" height="393" alt="Réponse de l'endpoint /generate-config" src="https://github.com/user-attachments/assets/2c08b377-7529-4adc-b881-c9deeed9fbb1" />

**Client WireGuard Windows connecté**

<img width="980" height="771" alt="Client WireGuard actif sous Windows" src="https://github.com/user-attachments/assets/c942a6c0-501a-40c4-9b6a-d51535bb2692" />

**Handshake WireGuard réussi (`sudo wg`)**

<img width="556" height="153" alt="Sortie de sudo wg avec latest handshake" src="https://github.com/user-attachments/assets/e11c99b7-7143-4456-a034-e21e62b35e8c" />

## Installation

```bash
git clone https://github.com/tanim-veer/wireguard-vpn-infrastructure.git
cd wireguard-vpn-infrastructure/backend
python -m venv venv
venv\Scripts\activate        # Linux/macOS : source venv/bin/activate
pip install fastapi uvicorn pynacl
mkdir configs                # dossier de sortie des fichiers .conf
uvicorn main:app --reload
```

L'API est ensuite disponible sur `http://127.0.0.1:8000`, avec la documentation interactive sur `/docs`.

## Limites actuelles

Ce projet est une preuve de concept, pas une solution prête pour la production :

- La clé publique du serveur (`SERVER_PUBLIC_KEY`), l'adresse IP du client et l'endpoint du serveur sont des valeurs codées en dur dans `main.py` et à remplacer
- Une nouvelle paire de clés est générée à chaque requête, et la clé privée est renvoyée par l'API : il n'y a pas d'authentification
- Le serveur n'est pas encore configuré pour router tout le trafic Internet (NAT et IP forwarding)

## Pistes d'amélioration

- Ajouter une authentification à l'API
- Enregistrer les pairs et attribuer automatiquement les adresses IP
- Configurer le NAT et le routage complet du trafic
- Générer un QR code pour les clients mobiles
- Conteneuriser avec Docker et déployer sur un VPS

## Ce que j'ai appris

- Fonctionnement de WireGuard : clés, pairs, `AllowedIPs`, handshake
- Développement d'une API REST avec FastAPI
- Bases de l'administration Linux et du réseau (interfaces, adressage, tunnels)
- Bonnes pratiques de sécurité : exclusion des clés et des configurations du dépôt Git

## Auteur

Tanim Veer, étudiant en BUT Informatique (parcours Data & IA)

[GitHub](https://github.com/tanim-veer) · [Portfolio](https://tanim-veer.fr)
