# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---


## 🎯 Introduction
To achieve this, we'll build a Gen-AI-based rule profiling model using Hugging Face's LLAMA LLM, process input PDFs, extract and transform data, store it in a Vector Database, compare the extracted rules with an Excel sheet, and update the Excel sheet with validation feedback.

   - We will build an LLM-based ruling profiling model that:
   - Extracts data from a PDF file.
   - Encrypts or transforms the data using LLAMA (Hugging Face).
   - Stores the transformed data in a Vector Database (ChromaDB).
   - Loads an Excel file and compares it with extracted rules.
   - Validates the rules and updates the Excel file with feedback.
   - Exposes the process as a Flask API using Swagger UI.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Flow Diagram with Arch Folder](link-to-image)

*Figure: Flow diagram showcasing the architecture folder integration.*

Explanation of the Flowchart:
1.	Start: The process begins with input PDFs and an Excel sheet containing rules.
2.	Process PDF?: The system checks if there are more PDFs to process.
3.	Extract Text from PDF (pypdf): If there are PDFs, the text is extracted using pypdf.
4.	Extract Rules using LLAMA (langchain, transformers, torch): The extracted text is passed to the Llama 2 model (managed by LangChain, Transformers, and PyTorch) to extract rules.
5.	Transform & Format Rules: The extracted rules are formatted and cleaned.
6.	Generate Rule Embeddings (sentence-transformers): The rules are converted into vector embeddings using sentence-transformers.
7.	Store Rules & Embeddings in ChromaDB: The rules and embeddings are stored in the ChromaDB vector database.
8.	Load Excel Sheet (pandas): If there are no more PDFs to process, the Excel sheet is loaded using pandas.
9.	Compare Rules?: The system checks if rules from the excel sheet need to be compared.
10.	Retrieve Similar Rules from ChromaDB: Similar rules are retrieved from ChromaDB based on the Excel sheet rules.
11.	Compare Excel Rules with Retrieved Rules: The retrieved rules are compared with the rules from the Excel sheet.
12.	Generate Validation Feedback: Validation feedback is generated based on the comparison.
13.	Update Excel Sheet with Feedback (openpyxl): The Excel sheet is updated with the validation feedback using openpyxl.
14.	End: The process ends.


## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

## 🛠️ How We Built It
Briefly outline the technologies, frameworks, and tools used in development.

## 🚧 Challenges We Faced
Describe the major technical or non-technical challenges your team encountered.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Install dependencies  
   ```sh
    pip install -r requirements.txt (for Python)
   ```
     
3. Run the project  
   ```sh
   python code/src/main.py
   ```
4. Swagger UI at 
   ```sh
    http://127.0.0.1:5000/swagger/
   ```
## 🏗️ Tech Stack
- 🔹 Frontend: React / Vue / Angular
- 🔹 Backend: Node.js / FastAPI / Django
- 🔹 Database: PostgreSQL / Firebase
- 🔹 Other: OpenAI API / Twilio / Stripe

## 👥 Team
- **Your Name** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)