# Intellectual Property Registry

A blockchain-based intellectual property registration and verification system built on the **Stellar blockchain** using Soroban smart contracts.

---

## 🧠 Overview

This system enables creators to **register and verify intellectual property** on the Stellar blockchain. Each registration is permanently recorded on-chain via a Soroban smart contract, providing an immutable, timestamped proof of ownership. A clean web interface allows users to register new IP entries and search existing records by ID.

---

## 🏗️ Architecture

### Technology Stack

| Layer | Technology |
|---|---|
| Blockchain | Stellar Testnet + Soroban Smart Contracts (Rust) |
| Backend | Python + Flask |
| Frontend | HTML + CSS + Vanilla JS (Jinja2 templates) |
| Wallet | Freighter Wallet |

### System Components

- **Smart Contract (Soroban)** — Stores IP records on-chain. Handles creation and lookup of registered properties.
- **Backend (Flask)** — Routes for registration, search, and wallet validation. Invokes the Stellar CLI to interact with the deployed contract.
- **Frontend (Jinja2 Templates)** — Server-rendered pages for registering IP, searching records, and viewing results.

---

## 📁 Project Structure

```
blockchain/hello-world/
├── src/                        # Soroban smart contract source (Rust)
├── target/                     # Compiled contract artifacts
├── Cargo.lock
├── Cargo.toml
├── static/
│   ├── style.css               # Global styles
│   └── wallet.js               # Freighter wallet integration
├── templates/
│   ├── index.html              # Home page
│   ├── register.html           # IP registration form
│   ├── search.html             # Search by property ID
│   └── dashboard.html          # Registered properties dashboard
├── app.py                      # Flask application & route logic
└── requirements.txt            # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Rust + Cargo
- [Stellar CLI](https://developers.stellar.org/docs/tools/developer-tools/stellar-cli)
- [Freighter Wallet](https://freighter.app/) browser extension
- A funded Stellar testnet account

### Installation

**1. Clone the repository**

```bash
git clone <your-repo-url>
cd blockchain/hello-world
```

**2. Install Python dependencies**

```bash
pip install -r requirements.txt
```

**3. Build the smart contract**

```bash
stellar contract build
```

**4. Deploy the smart contract to testnet**

```bash
stellar contract deploy \
  --wasm target/wasm32-unknown-unknown/release/hello_world.wasm \
  --network testnet
```

Copy the returned `CONTRACT_ID` for the next step.

**5. Configure environment variables**

Create a `.env` file in the project root:

```env
CONTRACT_ID=<your_deployed_contract_id>
SOURCE_KEY=<your_stellar_secret_key>
NETWORK=testnet
```

**6. Run the application**

```bash
python app.py
```

Access at: `http://localhost:5000`

---

## 📋 Features

### ✅ IP Registration
- Submit a title, description, and Freighter public wallet address
- Wallet address is validated before submission
- Duplicate title detection prevents redundant registrations
- Invokes the Soroban contract `create` function on Stellar testnet
- Returns a unique **Registry ID** upon success

### ✅ IP Search
- Look up any registered property by its numeric Registry ID
- Queries the on-chain record and displays full details

### ✅ Dashboard
- View all registered intellectual property entries

### ✅ Wallet Validation
- Validates Freighter public wallet address format before any on-chain interaction

---

## 🔗 Routes

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | Home page |
| `GET` | `/register` | Registration form |
| `POST` | `/register_ip` | Submit IP to blockchain |
| `GET` | `/search` | Search form |
| `POST` | `/search` | Query IP by ID |
| `GET` | `/dashboard` | View all registrations |

---

## 🔐 Smart Contract Functions

```rust
// Register a new intellectual property record
pub fn create(
    env: Env,
    title: String,
    description: String,
    owner: String,
) -> u64  // Returns registry ID

// Retrieve an IP record by ID
pub fn get(
    env: Env,
    id: u64,
) -> IPRecord
```

---

## 📊 Data Stored On-Chain

Each registered record stores the following on the Stellar blockchain:

- Registry ID (auto-incremented)
- Title
- Description
- Owner wallet address (Freighter public key)
- Timestamp

---

## 🛠️ Development Notes

The Flask backend invokes the Stellar CLI directly using `subprocess` to interact with the deployed Soroban contract:

```python
cmd = [
    "stellar", "contract", "invoke",
    "--id", CONTRACT_ID,
    "--source", SOURCE_KEY,
    "--network", "testnet",
    "--", "create",
    "--title", title,
    "--description", description,
    "--owner", wallet
]
```

---

## 📝 License

This project is developed for academic and demonstration purposes on the Stellar testnet.

---

## 👥 Contributors
Department: Computer Science (IoT and Cybersecurity including Blockchain)
Institution: Dayananda Sagar College of Engineering, Bangalore

https://stellar.expert/explorer/testnet/contract/CC7LJ7NVULQ5S43MCA664GMB7LFRT6EVDIOIGP5AQ7B4SA3252K4MZ2X

<img width="1913" height="636" alt="image" src="https://github.com/user-attachments/assets/b35d68e2-c079-4d49-a535-61df5e134e77" />


<img width="1883" height="885" alt="image" src="https://github.com/user-attachments/assets/88367011-86ec-4e4f-bb79-3a33557398f5" />





<img width="1916" height="904" alt="image" src="https://github.com/user-attachments/assets/97b0c70c-6320-4aef-a307-f7f0f6039864" />

<img width="1919" height="899" alt="image" src="https://github.com/user-attachments/assets/057bc66a-4285-4712-81c9-89ce263df29b" />

<img width="1919" height="904" alt="image" src="https://github.com/user-attachments/assets/71c05add-a397-4472-ba45-64d0b44bae3c" />


<img width="1919" height="894" alt="image" src="https://github.com/user-attachments/assets/f01fb7c5-5a12-4951-a364-60ff8ff11e37" />


<img width="1893" height="905" alt="image" src="https://github.com/user-attachments/assets/66389223-49da-4039-86b5-fb45659d05dd" />



Built with ❤️ using **Stellar Blockchain Technology**
