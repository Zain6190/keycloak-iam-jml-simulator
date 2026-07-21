# 🔐 Mini Identity Governance & Administration (IGA) Platform using Keycloak

A modular Python application that demonstrates **Identity Governance & Administration (IGA)** concepts by integrating with **Keycloak** through the **Admin REST API**.

This project simulates how enterprise IAM platforms such as **Fischer IAM**, **midPoint**, **SailPoint**, **Okta**, and **Microsoft Entra ID** manage digital identities while using **Keycloak as the Identity Provider (IdP)** for authentication and authorization.

---

# 📖 Project Overview

The goal of this project is to build a **Mini Identity Governance Platform** rather than simply interacting with Keycloak.

Instead of manually creating users from the Keycloak Admin Console, this application automates Identity Administration through a layered architecture and enterprise design principles.

The project currently supports complete User Lifecycle Management and is being extended toward:

- Identity Governance (IGA)
- RBAC
- Joiner • Mover • Leaver (JML)
- LDAP Integration
- Approval Workflows
- Reporting
- Identity Automation

---

# 🏗 Architecture

```
                    Users
                      │
                      ▼
           Mini IGA Platform (Python)
                      │
         Business Logic & Workflows
                      │
             Keycloak Admin REST API
                      │
                      ▼
                Keycloak Server
          (Authentication & Authorization)
                      │
                      ▼
          React Applications / APIs
```

Keycloak is used as the Identity Provider while this project provides the governance and administration layer.

---

# ✨ Features

## Authentication

- JWT Authentication
- OAuth2 Admin Login
- Keycloak Admin REST API
- Secure Token Management

---

## User Management

- List Users
- Create Users
- Search Users
- Update Users
- Disable Users
- Delete Users

---

## Identity Lifecycle

Current:

- Joiner (Provision User)

Upcoming:

- Mover
- Leaver

---

## Audit Logging

Every administrative action is logged.

Examples:

- Login
- Create User
- Search User
- Update User
- Disable User
- Delete User

---

## Enterprise Project Architecture

The project follows a layered architecture inspired by enterprise IAM products.

```
Presentation Layer
        │
        ▼
Menus
        │
        ▼
Operations
        │
        ▼
Services
        │
        ▼
REST API Client
        │
        ▼
Keycloak
```

This separation makes the project scalable and easy to maintain.

---

# 🗂 Project Structure

```
keycloak-iam-jml-simulator/

│
├── config/
│   ├── settings.py
│
├── core/
│   ├── auth.py
│   ├── api_client.py
│   ├── logger.py
│
├── menus/
│   ├── main_menu.py
│   ├── user_menu.py
│   ├── group_menu.py
│   ├── role_menu.py
│   └── jml_menu.py
│
├── operations/
│   ├── users/
│   │      ├── list_users.py
│   │      ├── create_user.py
│   │      ├── search_user.py
│   │      ├── update_user.py
│   │      ├── disable_user.py
│   │      └── delete_user.py
│   │
│   ├── groups/
│   ├── roles/
│   └── reports/
│
├── lifecycle/
│   ├── joiner.py
│   ├── mover.py
│   ├── leaver.py
│   └── simulator.py
│
├── services/
│   ├── users.py
│   ├── groups.py
│   ├── roles.py
│
├── utils/
│
├── logs/
│
├── README.md
├── requirements.txt
└── main.py
```

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3 |
| Authentication | Keycloak |
| Protocols | OAuth2, OpenID Connect (OIDC), JWT |
| API | Keycloak Admin REST API |
| Frontend | React (Authentication) |
| HTTP Client | Requests |
| Containerization | Docker |
| Operating System | Kali Linux |
| Virtualization | Oracle VirtualBox |
| Version Control | Git & GitHub |

---

# 🔐 Authentication Flow

```
Administrator

      │

      ▼

Python IAM Platform

      │

Authenticate

      │

      ▼

Keycloak

      │

Returns JWT Access Token

      │

      ▼

Admin REST API

      │

Manage Users
```

---

# 👤 User Management Workflow

```
Login

↓

Access Token

↓

User Service

↓

List Users

↓

Create User

↓

Search User

↓

Update User

↓

Disable User

↓

Delete User

↓

Audit Log
```

---

# 🔁 JML Lifecycle

### Joiner

```
New Employee

↓

Create User

↓

Assign Group

↓

Assign Role
```

---

### Mover (Upcoming)

```
Department Change

↓

Update Groups

↓

Update Roles
```

---

### Leaver (Upcoming)

```
Disable User

↓

Remove Access

↓

Delete User
```

---

# 🚀 Running the Project

## Clone Repository

```bash
git clone https://github.com/Zain6190/keycloak-iam-jml-simulator.git
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Configure

Update:

```
config/settings.py
```

Configure:

- Keycloak URL
- Realm
- Admin Username
- Admin Password

---

## Start Keycloak

Run Keycloak using Docker.

---

## Run Application

```bash
python main.py
```

---

# 📊 Current Progress

| Module | Status |
|----------|--------|
| JWT Authentication | ✅ |
| Admin REST API | ✅ |
| User CRUD | ✅ |
| Audit Logging | ✅ |
| Enterprise Architecture | ✅ |
| Menu System | ✅ |
| Operations Layer | ✅ |
| Services Layer | ✅ |
| Groups | 🚧 |
| Roles | 🚧 |
| RBAC | 🚧 |
| Joiner Workflow | 🚧 |
| Mover Workflow | 🚧 |
| Leaver Workflow | 🚧 |
| Reports | 🚧 |
| LDAP Integration | 🚧 |

---

# 🎯 Learning Objectives

This project explores:

- Identity & Access Management (IAM)
- Identity Governance & Administration (IGA)
- Keycloak Administration
- OAuth2
- OpenID Connect (OIDC)
- JWT Authentication
- REST API Integration
- Enterprise Software Architecture
- Service Layer Pattern
- Audit Logging
- User Lifecycle Management
- Role-Based Access Control (RBAC)
- Identity Automation

---

# 🚀 Roadmap

## Phase 1 ✅

- Authentication
- User CRUD
- Logging
- Modular Architecture

---

## Phase 2 (Current)

- Group Management
- RBAC
- User Membership

---

## Phase 3

- Role Management
- Client Roles
- Realm Roles

---

## Phase 4

- Joiner Workflow
- Mover Workflow
- Leaver Workflow

---

## Phase 5

- LDAP Integration
- Identity Synchronization

---

## Phase 6

- React Admin Dashboard
- Reporting Dashboard
- Approval Workflow
- Email Notifications

---

# 👨‍💻 Author

**Zain Ul Abideen**

BS Computer Science

Learning Enterprise Identity & Access Management

GitHub:
https://github.com/Zain6190

LinkedIn:
(Add your LinkedIn profile)

---

# 📜 License

This project is licensed under the MIT License.
