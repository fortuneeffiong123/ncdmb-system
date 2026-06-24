# NCDMB Equipment Monitoring System

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge\&logo=amazonaws)](http://ec2-13-60-28-201.eu-north-1.compute.amazonaws.com/)
[![AWS EC2](https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge\&logo=amazonaws\&logoColor=white)](https://aws.amazon.com/ec2/)
[![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge\&logo=flask)](https://flask.palletsprojects.com/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-499848?style=for-the-badge\&logo=gunicorn\&logoColor=white)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-009639?style=for-the-badge\&logo=nginx\&logoColor=white)](https://nginx.org/)
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://python.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)](https://ubuntu.com/)
[![REST API](https://img.shields.io/badge/API-REST-blue?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)]()
[![Industry](https://img.shields.io/badge/Industry-Oil%20%26%20Gas-red?style=for-the-badge)]()

![GitHub Repo Size](https://img.shields.io/github/repo-size/fortuneeffiong123/ncdmb-system-repo?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/fortuneeffiong123/ncdmb-system-repo?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/fortuneeffiong123/ncdmb-system-repo?style=for-the-badge)
![GitHub Issues](https://img.shields.io/github/issues/fortuneeffiong123/ncdmb-system-repo?style=for-the-badge)
![GitHub Last Commit](https://img.shields.io/github/last-commit/fortuneeffiong123/ncdmb-system-repo?style=for-the-badge)
![GitHub Commit Activity](https://img.shields.io/github/commit-activity/m/fortuneeffiong123/ncdmb-system-repo?style=for-the-badge)
![GitHub Contributors](https://img.shields.io/github/contributors/fortuneeffiong123/ncdmb-system-repo?style=for-the-badge)

> A cloud-based Oil & Gas Equipment Monitoring System that provides real-time equipment visibility, status tracking, and maintenance recommendations for critical field assets across onshore and offshore operations.

---

## 🚀 Live Demo

### Application URL

http://ec2-13-60-28-201.eu-north-1.compute.amazonaws.com/

> Note: This deployment currently runs on HTTP for demonstration purposes.

---

## 📋 Project Overview

The NCDMB Equipment Monitoring System is designed to monitor operational equipment used in the Oil & Gas industry. The platform enables operators, engineers, and maintenance teams to track equipment status and receive maintenance recommendations from a centralized dashboard.

The solution helps reduce downtime, improve operational efficiency, and support proactive maintenance planning.

---

## 🎯 Project Objectives

* Monitor critical Oil & Gas equipment.
* Display operational status in real time.
* Generate maintenance recommendations.
* Improve equipment reliability.
* Reduce operational downtime.
* Support digital transformation initiatives.
* Provide centralized visibility across multiple locations.

---

## ✨ Key Features

### Equipment Monitoring

* Real-time equipment status tracking
* Active, Warning, and Inactive indicators
* Maintenance recommendation engine

### Dashboard Analytics

* Equipment inventory overview
* Status distribution
* Equipment location tracking

### Asset Management

* Equipment categorization
* Site-based monitoring
* Recommendation tracking

### Cloud Deployment

* AWS EC2 hosting
* Nginx reverse proxy
* Gunicorn application server
* Systemd service management

---

## 🛢️ Equipment Covered

| Equipment      | Type                      | Location              |
| -------------- | ------------------------- | --------------------- |
| Wellhead       | Production Equipment      | Onshore Fields        |
| Christmas Tree | Flow Control Equipment    | Offshore Platforms    |
| Drilling Rig   | Drilling Equipment        | Exploration Sites     |
| Mud Pump       | Pumping Equipment         | Drilling Operations   |
| Pipeline       | Transportation Equipment  | Pipeline Corridors    |
| Storage Tank   | Storage Equipment         | Tank Farms            |
| Separator      | Processing Equipment      | Processing Facilities |
| Gas Compressor | Compression Equipment     | Gas Plants            |
| Heat Exchanger | Thermal Equipment         | Refineries            |
| Control Valve  | Instrumentation Equipment | Processing Plants     |

---

## 📊 Equipment Status Classification

| Status      | Description                     |
| ----------- | ------------------------------- |
| 🟢 Active   | Equipment operating normally    |
| 🟡 Warning  | Maintenance required soon       |
| 🔴 Inactive | Equipment unavailable or faulty |

---

## 🏗️ System Architecture

```text
Browser
   │
   ▼
Nginx Reverse Proxy
   │
   ▼
Gunicorn Server
   │
   ▼
Flask Backend
   │
   ▼
Equipment Data Layer
```

### Deployment Flow

1. User accesses application.
2. Nginx receives request.
3. Request forwarded to Gunicorn.
4. Gunicorn executes Flask application.
5. Equipment data returned to dashboard.

---

## 🛠️ Technology Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Frontend         | HTML5, CSS3, JavaScript |
| Backend          | Python Flask            |
| API              | RESTful API             |
| Web Server       | Nginx                   |
| WSGI Server      | Gunicorn                |
| Service Manager  | systemd                 |
| Cloud Platform   | AWS EC2                 |
| Operating System | Ubuntu Linux            |

---

## 🔒 Security & Reliability

* Reverse proxy protection via Nginx
* Gunicorn worker process isolation
* Automatic restart using systemd
* Linux-based deployment environment
* Production-ready architecture
* Fault-tolerant service management

---

## 📡 API Documentation

### Get All Equipment

```http
GET /equipment
```

### Sample Response

```json
[
  {
    "id": 1,
    "name": "Storage Tank",
    "type": "Storage Equipment",
    "location": "Tank Farm",
    "status": "warning",
    "recommendation": "Inspect corrosion and monitor liquid levels."
  }
]
```

---

## ⚙️ Local Installation

### Clone Repository

```bash
git clone https://github.com/fortuneeffiong123/ncdmb-system-repo.git
cd ncdmb-system-repo
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will be available at:

```text
http://127.0.0.1:5000
```

---

## ☁️ AWS Deployment

### Production Components

* AWS EC2 Instance
* Ubuntu Server
* Nginx
* Gunicorn
* Flask
* systemd

### Deployment Benefits

* High Availability
* Automatic Recovery
* Scalable Architecture
* Cloud Accessibility

---

## 📂 Project Structure

```text
ncdmb-system-repo/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│
└── README.md
```

---

## 🗺️ Future Enhancements

* MariaDB Integration
* User Authentication
* Equipment Image Upload
* AWS RDS Integration
* CloudWatch Monitoring
* Predictive Maintenance Analytics
* Machine Learning Recommendations
* Role-Based Access Control
* Equipment History Tracking

---

## 📈 Benefits

* Reduced equipment downtime
* Improved maintenance planning
* Better operational visibility
* Increased asset utilization
* Enhanced decision making
* Centralized equipment management

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit changes.
4. Push branch.
5. Submit a Pull Request.

---

## 📄 License

Licensed under the MIT License.

---

## 👨‍💻 Author

**Fortune Effiong**

GitHub:
https://github.com/fortuneeffiong123

Repository:
https://github.com/fortuneeffiong123/ncdmb-system-repo

---

### ⭐ If you find this project useful, consider giving it a star on GitHub.
