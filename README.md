NCDMB Equipment Monitoring System

Show Image
Show Image
Show Image
Show Image
Show Image


A real-time equipment monitoring and inspection-recommendation system for oil & gas infrastructure — tracking flow control units, wellheads, drilling rigs, pumps, pipelines, and storage tanks across onshore and offshore sites.




🚀 Live Demo

Click below to view the live application:

👉 http://ec2-13-60-28-201.eu-north-1.compute.amazonaws.com/


⚠️ Note: This demo runs over HTTP in a development/demo environment. Your browser may show a "Not Secure" warning in the address bar — this is expected and does not affect functionality.




📋 Overview

The NCDMB Equipment Monitoring System provides a centralized dashboard for tracking the operational status of critical oil & gas equipment. It surfaces real-time status (active, warning, inactive) alongside maintenance recommendations for each asset — helping operations teams prioritize inspections and preventive maintenance across multiple site types.

Equipment Tracked


🛢️ Storage Tanks — liquid level monitoring & corrosion inspection
🌲 Christmas Trees — valve inspection & emergency shutdown testing
🔧 Wellheads — pressure monitoring & routine inspection
🏗️ Drilling Rigs — preventive maintenance scheduling
⚙️ Mud Pumps — pressure monitoring & seal replacement tracking
🛤️ Pipelines — leak detection & integrity testing



✨ Features


📊 Real-time equipment status dashboard (active / warning / inactive)
🔍 Maintenance recommendations per asset
🌍 Multi-site tracking (onshore, offshore, tank farms, pipeline corridors)
🔄 RESTful API for equipment data
🛡️ Production-grade deployment with auto-restart on failure



🛠️ Tech Stack

LayerTechnologyFrontendHTML5, CSS3, JavaScriptBackendPython, FlaskWSGI ServerGunicornProcess ManagementsystemdWeb Server / Reverse ProxyNginxHostingAWS EC2


🏗️ Architecture

Browser
   │
   ▼
Nginx (Reverse Proxy, Port 80)
   │
   ▼
Gunicorn (3 Workers, Port 5000)
   │
   ▼
Flask Application
   │
   ▼
Equipment Data

The application is deployed on an AWS EC2 instance running Ubuntu. Nginx handles incoming HTTP traffic and proxies requests to a Gunicorn-managed Flask backend. Systemd supervises the Gunicorn process, automatically restarting it on failure and on server reboot — ensuring high availability without manual intervention.


📡 API Reference

Get All Equipment

httpGET /equipment

Sample Response:

json[
  {
    "id": 1,
    "name": "Storage Tank",
    "type": "Storage Equipment",
    "location": "Tank Farm",
    "status": "warning",
    "recommendation": "Monitor liquid levels and inspect for corrosion."
  }
]


⚙️ Local Setup

Prerequisites


Python 3.12+
pip


Installation

bash# Clone the repository
git clone https://github.com/fortuneeffiong123/ncdmb-system-repo.git
cd ncdmb-system-repo/backend

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py

The API will be available at http://127.0.0.1:5000.

Production Run (Gunicorn)

bashgunicorn -w 3 -b 127.0.0.1:5000 app:app


📦 Deployment

This project is deployed on AWS EC2 with the following production setup:


Gunicorn runs the Flask app with multiple worker processes for concurrency and resilience.
systemd manages the Gunicorn process — automatically restarting it on crash and on server reboot.
Nginx acts as a reverse proxy, forwarding public traffic to the Gunicorn server running on 127.0.0.1:5000.



📂 Project Structure

ncdmb-system-repo/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── venv/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md


🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.


📄 License

This project is licensed under the MIT License.


👤 Author

Fortune Effiong
GitHub · Repository
