
# 🏥 Health Information System API

A simple, well-documented health information system for managing clients and health programs — built with Flask. 

---

## 🚀 Features

- Create health programs (e.g., TB, Malaria, HIV)
- Register new clients
- Enroll clients in one or more programs
- Search for clients
- View full client profiles including enrolled programs
- REST API access to client profiles

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Data Storage**: In-memory (dictionary-based for demo)
- **API Tooling**: JSON responses, Flask routes
- **Environment**: Virtualenv + VS Code

---

## 🔧 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/Agostinejohn/Health_Information_system.git
cd health-info-system

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

---

## 🔁 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/programs` | Create a new health program |
| POST | `/clients` | Register a new client |
| POST | `/clients/<client_id>/enroll` | Enroll client in programs |
| GET | `/clients?name=John` | Search clients by name |
| GET | `/clients/<client_id>` | View client profile |

---

## 📈 Example API Usage

**Register a new client**:
```json
POST /clients
{
  "name": "John Maubi",
  "age": 32
}
```

**Enroll a client**:
```json
POST /clients/<client_id>/enroll
{
  "program_ids": ["program_id_1", "program_id_2"]
}
```

---

## 🔐 Security Considerations

Although this application uses in-memory storage and is designed as a demonstration, the following security principles were considered and would be enforced in a production environment:

- **Input Validation**: User input is sanitized to prevent injection attacks.
- **UUID Usage**: Secure identifiers for clients and programs.
- **RESTful Design**: Minimal route exposure and clean endpoint structure.
- **Limited Data Exposure**: Only necessary data is shared via APIs.
- **Future Scope**: Authentication (JWT), HTTPS enforcement, CORS policies, rate-limiting, and logging.

---

## 🧠 System Design Overview

The system is structured into clearly defined components:

- **Data Layer**: In-memory dictionaries simulate storage.
- **Service Layer**: Core logic separated into reusable functions.
- **API Layer**: Flask routes expose functionality via RESTful endpoints.
- **Future Scalability**: Easy to migrate to real databases (MongoDB, SQLite).

---

## 🧪 Prototype Demonstration

You can view a demonstration of the API in action via:

This link:

https://github.com/Agostinejohn/Health_Information_system/blob/main/Health_Infor_System_API_Testing.pdf

---

## 🧪 Testing 

Unit tests were considered using `unittest` or `pytest` for:

- Client registration logic
- Program enrollment
- API response status codes

Testing can be integrated for enhanced reliability.

---

## 🗂 Git Hygiene

The project uses a `.gitignore` file to exclude:

- `venv/` (virtual environment)
- `__pycache__/` (Python compiled cache)
- `.env` (future use for secrets or configs)

This ensures the repository remains clean and secure.



