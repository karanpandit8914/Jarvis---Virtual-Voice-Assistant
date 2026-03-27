# 🤖 JARVIS - AI Voice Assistant (Python)

> A smart voice-controlled virtual assistant built using Python, inspired by JARVIS from Iron Man.  
> It can perform tasks like opening websites, playing music, fetching news, and answering queries using AI.

---

## 🚀 Features

- 🎤 Voice Recognition (Speech-to-Text)
- 🔊 Text-to-Speech Response (Realistic Voice)
- 🌐 Open Websites (Google, YouTube, LinkedIn, etc.)
- 🎵 Play Music from Library
- 📰 Fetch Latest News Headlines
- 🤖 AI-powered responses using OpenAI
- ⚡ Wake word detection ("Jarvis")

---

## 🛠️ Tech Stack

- **Python**
- `speech_recognition`
- `pyttsx3`
- `gTTS`
- `pygame`
- `requests`
- `OpenAI API`
- `webbrowser`

---

## 📂 Project Structure

```
📁 Jarvis-AI
│── main.py
│── musicLibrary.py
│── README.md
│── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

Then say:

👉 **"Jarvis"** to activate  
👉 Give commands like:

- "Open Google"
- "Play song_name"
- "Open YouTube"
- "Give me news"

---

## 🔐 Important Note (Security)

⚠️ **Do NOT expose your API keys publicly**

- Remove your OpenAI API key from code
- Use `.env` file instead:

Example:

```bash
OPENAI_API_KEY=your_api_key_here
```

---

## 🧠 How It Works

1. Listens continuously for wake word **"Jarvis"**
2. Converts speech → text using Google Speech API
3. Processes command:
   - Predefined tasks (open sites, music, news)
   - AI response via OpenAI
4. Converts response → speech

---

## 💡 Future Improvements

- GUI Interface (Tkinter / Web App)
- Better wake word detection
- Offline mode
- Custom voice options
- Task automation (emails, reminders)

---

## 👨‍💻 Author

**Karan Pandit**   
* 💼 LinkedIn: https://www.linkedin.com/in/karan-pandit-55962a361
* 👉 Follow me on LinkedIn for more projects and updates!

---

## ⭐ Support

If you like this project:

👉 Star ⭐ the repository  
👉 Follow for more projects  

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💬 Inspiration

Inspired by **JARVIS from Iron Man** 🦾

---

## 🔥 Setup Tip

Generate requirements file:

```bash
pip freeze > requirements.txt
```
