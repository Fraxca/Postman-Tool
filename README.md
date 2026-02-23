# 📬 Postman Tool

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![API](https://img.shields.io/badge/Category-API-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A simple **Postman-like tool** developed in Python.  
It allows you to send HTTP requests, test APIs, and analyze responses directly from the terminal.

---

## 🚀 Features
- 🌐 Send GET, POST, PUT, DELETE requests  
- 📦 Handle headers, parameters, and body payloads  
- 📊 Display response status, headers, and content  
- 🖥️ Simple command-line interface  
- 🔑 How to Use API Keys
- Some APIs require authentication via API keys or tokens.
- Here’s how to set them up:
- Obtain your API key from the service provider (e.g., OpenWeatherMap, GitHub API, etc.).
- In the project folder, create a file named .env.
- Add your key like this:
- API_KEY=your_api_key_here
- Save the file.
- The tool will automatically load your API key when sending requests.
- 🖥️ Usage
- Run main.py
- Choose the request type (GET, POST, etc.)
- Enter the URL and optional headers/body
- The tool will display the response details
