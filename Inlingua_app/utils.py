from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class Student:
    def __init__(self, Student_Name, Student_ID, Language_Name, Level_and_Hour, Amount_Paide):
        self.Student_Name = Student_Name
        self.Student_ID = Student_ID
        self.Language_Name = Language_Name
        self.Level_and_Hour = Level_and_Hour
        self.Amount_Paide = Amount_Paide

def generate_student_invoice(student):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Title
    p.setFont("Helvetica-Bold", 24)
    p.drawString(200, 750, "INVOICE")

    # Company Info
    p.setFont("Helvetica", 12)
    p.drawString(50, 700, "Zylker Electronics Hub")
    p.drawString(50, 685, "1481 Northern Street")
    p.drawString(50, 670, "Greater South Avenue")
    p.drawString(50, 655, "New York, New York 10001")
    p.drawString(50, 640, "USA")

    # Invoice Info
    p.drawString(400, 700, "Invoice No: INV-000031")
    p.drawString(400, 685, "Invoice Date: 18 May 2023")
    p.drawString(400, 670, "Due Date: 18 May 2023")

    # Bill To
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, 600, "Bill To:")
    p.setFont("Helvetica", 12)
    p.drawString(50, 585, student.Student_Name)
    p.drawString(50, 570, "1234 Hillside Lake Road")
    p.drawString(50, 555, "Needham, 02792 Maine")

    # Ship To
    p.setFont("Helvetica-Bold", 12)
    p.drawString(400, 600, "Ship To:")
    p.setFont("Helvetica", 12)
    p.drawString(400, 585, student.Student_Name)
    p.drawString(400, 570, "1234 Hillside Lake Road")
    p.drawString(400, 555, "Needham, 02792 Maine")

    # Table Header
    p.drawString(50, 510, "Item & Description")
    p.drawString(300, 510, "Qty")
    p.drawString(350, 510, "Rate")
    p.drawString(400, 510, "Amount")

    # Table Content
    items = [
        ("Camera", "1.00", "$899.00", "$899.00"),
        ("Fitness Tracker", "1.00", "$129.00", "$129.00"),
        ("Laptop", "1.00", "$999.00", "$999.00")
    ]
    
    y = 490
    for item, qty, rate, amount in items:
        p.drawString(50, y, item)
        p.drawString(300, y, qty)
        p.drawString(350, y, rate)
        p.drawString(400, y, amount)
        y -= 20

    # Total
    p.drawString(400, y - 20, "Sub Total: $2027.00")
    p.drawString(400, y - 40, "Tax Rate: 5.00%")
    p.drawString(400, y - 60, "Total: $2128.35")
    p.drawString(400, y - 80, "Balance Due: $2128.35")

    # Footer
    p.setFont("Helvetica", 10)
    p.drawString(200, 100, "Thanks for your business.")
    p.drawString(50, 85, "Terms & Conditions: Full payment is due upon receipt of this invoice. Late payments may incur additional charges or interest as per the applicable laws.")

    # Save the PDF
    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer

# Example usage
student = Student("Ms. Mary D. Dunton", "12345", "English", "Level 1 - 20 hours", "500.00")
buffer = generate_student_invoice(student)

# Save the buffer to a file for testing
with open("student_invoice.pdf", "wb") as f:
    f.write(buffer.read())


def send_welcome_email(to_email, name, pdf_buffer):
    subject = "Welcome to Inlingua"
    body = render_to_string('email/welcome_email.html', {'name': name})
    email = EmailMessage(
        subject,
        body,
        'vignesh@revaadigital.com',
        [to_email],
    )
    email.content_subtype = "html"  # Main content is now text/html
    email.attach('invoice.pdf', pdf_buffer.getvalue(), 'application/pdf')
    email.send()
