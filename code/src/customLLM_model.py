import PyPDF2
import chromadb
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()





# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="./vector_db")
collection = chroma_client.get_or_create_collection(name="rules")

def store_text_in_vector_db(text, metadata):
    collection.add(
        ids=[metadata["id"]],
        documents=[text],
        metadatas=[metadata]
    )



pdf_file = "data/US_Auto_Loan.pdf"
pdf_text = extract_text_from_pdf(pdf_file)
print("Extracted PDF text:", pdf_text[:4096]) 


store_text_in_vector_db(pdf_text, {"id": "rule_001"})



def load_excel(excel_path):
    df = pd.read_excel(excel_path)
    return df

# Load existing rule data

df_rules = load_excel("data/rules.xlsx")
print("Loaded audit rules:", df_rules.head())


def compare_rules(extracted_text, rule_text):
    prompt = f"""
    Given the extracted rule: {extracted_text}
    Compare it with the existing rule: {rule_text}
    Provide a response if they match or differ.
    """
    model_name = "meta-llama/Llama-2-7b-chat-hf"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cuda")
    # inputs = tokenizer(prompt, return_tensors="pt")
    # output = model.generate(**inputs, max_new_tokens=50)
    
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=4096).to("cuda")
    outputs = model.generate(**inputs,max_new_tokens=500)

    return tokenizer.decode(output[0], skip_special_tokens=True)

def validate_and_update_excel(input_excel, output_excel, extracted_text):
    df = pd.read_excel(input_excel)
    feedback_list = []

    for index, row in df.iterrows():
        rule_text = row["Rule_Text"]  # Assuming Excel has a column named "Rule_Text"
        feedback = compare_rules(extracted_text, rule_text[:100])  # Compare first 1000 characters
        feedback_list.append(feedback)

    df["Validation_Feedback"] = feedback_list  # Add new column
    df.to_excel(output_excel, index=False)  # Save updated Excel file

# Run validation
#validate_and_update_excel("data/rules.xlsx", "validated_rules.xlsx", pdf_text)