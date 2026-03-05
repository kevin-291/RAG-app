# Simple RAG API with FastAPI and Groq

This project is a lightweight Retrieval-Augmented Generation (RAG) API built with FastAPI. It uses LangChain and ChromaDB to chunk and index local text documents, and the Groq API (`llama-3.3-70b-versatile`) to generate context-aware answers to user queries.

## Prerequisites

* **Python 3.10+** installed on your system.
* A **Groq API Key** (Get one at [console.groq.com](https://console.groq.com/)).

## Installation

1.  **Install uv** (if not already installed):

-   Windows - Open PowerShell in administrator mode and run:
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

-   macOS/Linux
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Clone the repository** and navigate to the project directory:
    ```bash
    git clone <repository-url>
    cd RAG-app
    ```

3.  **Install dependencies**:
    ```bash
    uv sync
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the project root and add your Groq API key:
    ```env
    GROQ_API_KEY = "your_groq_api_key_here"
    ```

## Running the Application

Start the FastAPI server using `uv`:

```bash
uv run main.py
```

The API will be available at `http://localhost:8000`.

## Testing with Example Script

In a separate terminal, run the included `usage.py` script to test the API:

```bash
uv run usage.py
```


