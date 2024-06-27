from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Define a function to create a single PDF file with technical drawings
def create_pdf(file_path, applicant_name, project_description, project_address, project_type, estimated_cost, drawing_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)

    c.drawString(100, height - 100, f"Applicant Name: {applicant_name}")
    c.drawString(100, height - 130, f"Project Description: {project_description}")
    c.drawString(100, height - 160, f"Project Address: {project_address}")
    c.drawString(100, height - 190, f"Project Type: {project_type}")
    c.drawString(100, height - 220, f"Estimated Cost: ${estimated_cost}")

    # Add technical drawing
    if os.path.exists(drawing_path):
        c.drawImage(drawing_path, 100, height - 500, width=400, height=300)
    else:
        c.drawString(100, height - 500, "Technical Drawing: Not Available")
        print(f"Debug: Technical drawing file not found at {drawing_path}")

    c.save()

# Check and create the technical drawings directory if necessary
technical_drawings_dir = "technical_drawings"
if not os.path.exists(technical_drawings_dir):
    os.makedirs(technical_drawings_dir)
    print(f"Directory '{technical_drawings_dir}' was missing and has been created.")

# Define sample data
sample_data = [
    {"applicant_name": "Alice", "project_description": "New construction of a 2-story house", "project_address": "123 Main St", "project_type": "Residential", "estimated_cost": 250000, "drawing_path": "technical_drawings/drawing1.jpg"},
    {"applicant_name": "Bob", "project_description": "Renovation of kitchen and bathrooms", "project_address": "456 Elm St", "project_type": "Residential", "estimated_cost": 75000, "drawing_path": "technical_drawings/drawing2.png"},
    {"applicant_name": "Charlie", "project_description": "Demolition of old structure and new construction", "project_address": "789 Maple Ave", "project_type": "Residential", "estimated_cost": 300000, "drawing_path": "technical_drawings/drawing3.png"},
    {"applicant_name": "David", "project_description": "New construction of a commercial building", "project_address": "101 Oak St", "project_type": "Commercial", "estimated_cost": 500000, "drawing_path": "technical_drawings/drawing4.png"},
]

# Create PDFs directory if it doesn't exist
pdf_directory = "building_permit_applications"
if not os.path.exists(pdf_directory):
    os.makedirs(pdf_directory)
    print(f"Directory '{pdf_directory}' was missing and has been created.")

# Create PDFs
for i, data in enumerate(sample_data):
    file_path = f"{pdf_directory}/application_{i+1}.pdf"
    create_pdf(file_path, **data)

print("PDF files with technical drawings have been created in the 'building_permit_applications' directory.")
