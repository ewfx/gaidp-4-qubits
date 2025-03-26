from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

from customLLM_model import extract_text_from_pdf, store_text_in_vector_db, validate_and_update_excel

app = Flask(__name__)

# Swagger UI Configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    pdf_file = request.files["file"]
    pdf_text = extract_text_from_pdf(pdf_file)
    
    # Store extracted data in VectorDB
    store_text_in_vector_db(pdf_text, {"id": "uploaded_rule"})
    
    return jsonify({"message": "PDF processed successfully", "extracted_text": pdf_text})

@app.route("/validate_rules", methods=["POST"])
def validate_rules():
    input_excel = request.form.get("input_excel")
    output_excel = request.form.get("output_excel")
    
    pdf_text = extract_text_from_pdf("artifacts/demo/US_Auto_Loan.pdf")  # Assume sample.pdf is uploaded
    validate_and_update_excel(input_excel, output_excel, pdf_text)
    
    return jsonify({"message": "Rules validated successfully", "output_file": output_excel})

if __name__ == "__main__":
    app.run(debug=True)
