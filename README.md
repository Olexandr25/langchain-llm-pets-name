# Pet Name Generator with Langchain and Streamlit

This project uses Langchain and Streamlit to generate names for pets based on their type and color. The app also describes the pet's personality and generates a cool tagline.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.9+
- Virtual environment (recommended `venv`)
- OpenAI API Key

# Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

## 2.Create and activate a virtual environment

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

### For Windows

```bash
.venv\Scripts\activate
```

### For MacOS/Linux

```bash
source .venv/bin/activate
```

## 3. Install dependencies

After activating the virtual environment, install all required packages:

```bash
pip install -r requirements.txt
```

## 4. Create .env file

Create a .env file in the root directory of the project and add your OpenAI API key:

```bash
OPENAI_API_KEY="your_openai_key"
```

## 5. Run the app

To launch the application, use the following Streamlit command:

```bash
streamlit run main.py
```
