# 🤖 Enhanced Q&A Chatbot with Groq

A simple and interactive Q&A chatbot built using **Streamlit**, **LangChain**, and **Groq LLMs**. Users can provide their Groq API key, select a model, customize generation parameters, and ask questions through a clean web interface.

---

## 🚀 Features

* Interactive Streamlit web interface
* Integration with Groq LLMs using LangChain
* Support for multiple Groq models:

  * llama-3.3-70b-versatile
  * llama-3.1-8b-instant
  * qwen/qwen3-32b
* Adjustable temperature and max token settings
* LangSmith tracing support
* Secure API key input through the sidebar

---

## 📂 Project Structure

```text
.
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create and Activate a Virtual Environment

Using Conda:

```bash
conda create -p venv python=3.11 -y
conda activate ./venv
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```txt
langchain
langchain-community
langchain-groq
langchain-core
streamlit
python-dotenv
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

> Groq API Key is entered directly through the Streamlit sidebar during runtime.

---

## ▶️ Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## 🎯 How to Use

1. Launch the application.
2. Enter your Groq API key in the sidebar.
3. Select a Groq model.
4. Adjust:

   * Temperature
   * Maximum Tokens
5. Enter your question.
6. Click **Generate Response**.
7. View the AI-generated answer.

---

## ⚙️ Technologies Used

* Python
* Streamlit
* LangChain
* Groq API
* LangSmith
* Python Dotenv

---

## 📸 Application Workflow

1. User enters a query.
2. LangChain constructs a prompt.
3. Groq LLM processes the request.
4. Response is parsed using `StrOutputParser`.
5. Output is displayed in the Streamlit interface.

---

## 📈 Future Enhancements

* Chat history support
* Conversation memory
* File upload and document Q&A
* Retrieval-Augmented Generation (RAG)
* Authentication and user management
* Response streaming

---

## 👨‍💻 Author

**Bedant Behera**

Built using Streamlit, LangChain, and Groq to explore modern LLM-powered applications.
