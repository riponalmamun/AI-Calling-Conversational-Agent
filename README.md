# 🤖 AI Calling Conversational Agent

<div align="center">

[![Python](https://img.shields.io/badge/python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/riponalmamun/AI-Calling-Conversational-Agent?style=for-the-badge&logo=github)](https://github.com/riponalmamun/AI-Calling-Conversational-Agent/stargazers)

**An intelligent voice-based assistant that seamlessly integrates AI-powered conversations with real-time call handling**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Documentation](#-api-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

**AI Calling Conversational Agent** is a sophisticated voice assistant platform built with modern Python technologies. It combines the power of advanced language models with real-time telecommunications to deliver natural, intelligent voice interactions. Whether you're building a customer support system, virtual receptionist, or interactive voice response solution, this platform provides the foundation you need.

### Why Choose This Project?

- **Scalable Architecture**: Built on FastAPI for high-performance, production-ready deployments
- **AI-Powered Intelligence**: Leverage state-of-the-art language models for natural conversations
- **Real-Time Processing**: Handle voice calls with minimal latency
- **Developer-Friendly**: Clean, modular codebase with comprehensive documentation
- **Extensible Design**: Easy to customize and integrate with existing systems

---

## ✨ Features

### Core Capabilities

- 📞 **Real-Time Voice Call Management** - Initiate, manage, and terminate voice calls programmatically
- 🧠 **AI-Driven Conversations** - Natural language understanding and context-aware responses
- ⚡ **High-Performance API** - FastAPI backend optimized for speed and reliability
- 🔧 **Modular Architecture** - Service-based design for easy maintenance and expansion
- 📊 **Conversation Analytics** - Track and analyze interaction patterns
- 🔐 **Secure by Design** - Built-in security best practices

### Technical Highlights

- Asynchronous request handling for optimal performance
- Structured logging for debugging and monitoring
- Environment-based configuration management
- RESTful API design with OpenAPI documentation
- Comprehensive error handling and validation

---

## 🏗️ Project Structure

```
AI-Calling-Conversational-Agent/
│
├── 📄 main.py                    # FastAPI application entry point
├── 📄 requirements.txt           # Python dependencies
│
├── 📁 config/
│   └── settings.py               # Configuration management
│
├── 📁 models/
│   └── conversation.py           # Data models and schemas
│
├── 📁 services/
│   ├── ai_service.py             # AI response generation
│   └── call_service.py           # Call handling logic
│
├── 📁 .venv/                     # Virtual environment (not tracked)
└── 📄 .gitignore                 # Git ignore rules
```

---

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Virtual environment tool (venv)

### Step-by-Step Setup

1. **Clone the Repository**

```bash
git clone https://github.com/riponalmamun/AI-Calling-Conversational-Agent.git
cd AI-Calling-Conversational-Agent
```

2. **Create Virtual Environment**

```bash
python -m venv .venv
```

3. **Activate Virtual Environment**

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.\.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

4. **Install Dependencies**

```bash
pip install -r requirements.txt
```

5. **Configure Environment Variables**

Create a `.env` file in the root directory:

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG_MODE=True

# AI Service Configuration
AI_MODEL=gpt-4
AI_API_KEY=your_api_key_here

# Call Service Configuration
CALL_PROVIDER=twilio
CALL_API_KEY=your_call_api_key
```

---

## 💻 Usage

### Running the Application

Start the FastAPI server with auto-reload for development:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

For production deployment:

```bash
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
```

### Accessing the API

Once the server is running, you can:

- **Interactive API Docs**: http://127.0.0.1:8000/docs (Swagger UI)
- **Alternative Docs**: http://127.0.0.1:8000/redoc (ReDoc)
- **OpenAPI Schema**: http://127.0.0.1:8000/openapi.json

### Quick Start Example

```python
import requests

# Initiate a call
response = requests.post(
    "http://127.0.0.1:8000/api/v1/call/initiate",
    json={
        "phone_number": "+1234567890",
        "greeting": "Hello! How can I assist you today?"
    }
)

print(response.json())
```

---

## 📚 API Documentation

### Key Endpoints

#### **POST** `/api/v1/call/initiate`
Initiate a new AI-powered call

**Request Body:**
```json
{
  "phone_number": "+1234567890",
  "greeting": "Hello! How can I help?",
  "context": {}
}
```

**Response:**
```json
{
  "call_id": "abc123",
  "status": "initiated",
  "timestamp": "2024-12-09T10:30:00Z"
}
```

#### **GET** `/api/v1/conversation/{conversation_id}`
Retrieve conversation history

#### **POST** `/api/v1/message/send`
Send a message within an active conversation

For complete API documentation, visit the `/docs` endpoint after starting the server.

---

## 🛠️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `API_HOST` | Server host address | `0.0.0.0` |
| `API_PORT` | Server port | `8000` |
| `DEBUG_MODE` | Enable debug logging | `False` |
| `AI_MODEL` | AI model identifier | `gpt-4` |
| `AI_API_KEY` | AI service API key | Required |
| `CALL_PROVIDER` | Call service provider | `twilio` |

### Customizing Services

To integrate your own AI or call service:

1. Create a new service class in the `services/` directory
2. Implement the required interface methods
3. Update configuration in `config/settings.py`
4. Register the service in `main.py`

---

## 🧪 Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest --cov=. --cov-report=html
```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Contribution Workflow

1. **Fork the Repository**
   ```bash
   git fork https://github.com/riponalmamun/AI-Calling-Conversational-Agent.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Write clean, documented code
   - Follow PEP 8 style guidelines
   - Add tests for new features

4. **Commit Your Changes**
   ```bash
   git commit -m "feat: add amazing feature"
   ```
   
   Use conventional commits:
   - `feat:` New features
   - `fix:` Bug fixes
   - `docs:` Documentation updates
   - `refactor:` Code refactoring
   - `test:` Test additions/updates

5. **Push to Your Fork**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Describe your changes clearly
   - Reference any related issues
   - Wait for review and feedback

### Development Guidelines

- Write clear commit messages
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting
- Follow the existing code style

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Md. Ripon Al Mamun

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🌟 Roadmap

- [ ] Multi-language support
- [ ] WebSocket support for real-time updates
- [ ] Advanced analytics dashboard
- [ ] Voice emotion detection
- [ ] Call recording and transcription
- [ ] Integration with popular CRM systems
- [ ] Docker containerization
- [ ] Kubernetes deployment configs

---

## 📞 Contact & Support

**Md. Ripon Al Mamun**

- 🐙 GitHub: [@riponalmamun](https://github.com/riponalmamun)
- 📧 Email: riponalmamunrasel@gmail.com
- 💼 LinkedIn: [Md. Ripon Al Mamun](https://www.linkedin.com/in/mdriponalmamun/)

### Getting Help

- 📖 Check the [Documentation](https://github.com/riponalmamun/AI-Calling-Conversational-Agent/wiki)
- 🐛 Report bugs via [GitHub Issues](https://github.com/riponalmamun/AI-Calling-Conversational-Agent/issues)
- ⭐ Star the project if you find it useful!

---

## 🙏 Acknowledgments

- FastAPI framework and community
- OpenAI for language model capabilities
- Twilio for telecommunications infrastructure
- All contributors who help improve this project

---

<div align="center">

**Made with ❤️ by [Ripon Al Mamun](https://github.com/riponalmamun)**

If this project helps you, please consider giving it a ⭐!

[⬆ Back to Top](#-ai-calling-conversational-agent)

</div>
