from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import datetime as dt

class Student:
    def __init__(self, Student_Name, Student_ID, Language_Name, Level_and_Hour, Amount_Paide, Student_Mail_Id, Student_Phone_No, Balance_Amount, Payment_Type, Transaction_ID):
        self.Student_Name = Student_Name
        self.Student_ID = Student_ID
        self.Language_Name = Language_Name
        self.Level_and_Hour = Level_and_Hour
        self.Amount_Paide = Amount_Paide
        self.Student_Mail_Id = Student_Mail_Id
        self.Student_Phone_No = Student_Phone_No
        self.Balance_Amount = Balance_Amount
        self.Payment_Type = Payment_Type
        self.Transaction_ID = Transaction_ID

def generate_student_invoice(student, employee, new_receipt):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    line_height = 17  # Adjust this value to control line height

    # # Add the background image
    # watermark_path = "static/img/imgs/employees.png"  # Path to your watermark logo
    # watermark = ImageReader(watermark_path)
    # p.drawImage(watermark, 0, 0, width=letter[0], height=letter[1], mask='auto')  # Cover the entire page

    # Title
    p.setFont("Helvetica-Bold", 24)
    p.drawString(200, 750, "Payment Receipt")

    # Add the company logo
    logo_path = "static/img/imgs/receipt_logo.png"  # Path to your logo
    logo = ImageReader(logo_path)
    p.drawImage(logo, 50, 660, width=200, height=50)  # Adjust the width, height, and position as needed

    # Company Info
    p.setFont("Helvetica", 12)
    y = 640
    p.drawString(50, y, "AMG Towers, 28, Lawyer")
    y -= line_height
    p.drawString(50, y, "Jagannathan Street, Guindy")
    y -= line_height
    p.drawString(50, y, "Chennai- 600016")
    y -= line_height
    p.drawString(50, y, "Tamil Nadu")
    y -= line_height
    p.drawString(50, y, "--------------------------------------------------------------------------------------------------------------------------------")

    # Invoice Info
    y = 640
    p.drawString(400, y, f"S.No : {new_receipt.payment_number}")
    y -= line_height
    p.drawString(400, y, f"Date : {dt.datetime.now().date()}")
    y -= line_height
    p.drawString(400, y, f"Time : {dt.datetime.now().time().strftime('%H:%M:%S')}")

    # Bill To 
    y = 555
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Bill To:")
    p.setFont("Helvetica", 12)
    y -= line_height
    p.drawString(50, y, employee.name)
    y -= line_height
    p.drawString(50, y, f"91 {employee.phone}")
    y -= line_height
    p.drawString(50, y, employee.email)

    # Ship To
    y = 555
    p.setFont("Helvetica-Bold", 12)
    p.drawString(400, y, "Ship To:")
    p.setFont("Helvetica", 12)
    y -= line_height
    p.drawString(400, y, student.Student_Name)
    y -= line_height
    p.drawString(400, y, f"91 {student.Student_Phone_No}")
    y -= line_height
    p.drawString(400, y, student.Student_Mail_Id)
    y -= line_height
    p.drawString(50, y, "--------------------------------------------------------------------------------------------------------------------------------")

    # Table Header
    y = 470
    line_height = 20
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Payment Details:")
    p.setFont("Helvetica", 12)
    y -= line_height
    p.drawString(50, y, "For the Payment of")
    y -= line_height
    p.drawString(50, y, "Paid")
    y -= line_height
    p.drawString(50, y, "Balance")
    y -= line_height
    p.drawString(50, y, "Payment Type")
    y -= line_height
    p.drawString(50, y, "Paid By")
    y -= line_height
    p.drawString(50, y, "Transaction ID")

    # Table Content
    y = 450
    p.setFont("Helvetica", 12)
    p.drawString(200, y, f"{student.Language_Name} - {student.Level_and_Hour}")
    y -= line_height
    p.drawString(200, y, f"Rs . {student.Amount_Paide}")
    y -= line_height
    p.drawString(200, y, f"Rs . {student.Balance_Amount}")
    y -= line_height
    p.drawString(200, y, f"{student.Payment_Type} Payment")
    y -= line_height
    p.drawString(200, y, "Online Payment")
    y -= line_height
    p.drawString(200, y, f"{student.Transaction_ID}")

    # Ship To
    y = 300
    p.setFont("Helvetica-Bold", 12)
    p.drawString(400, y, "Received By:")
    p.setFont("Helvetica", 12)
    y -= line_height
    p.drawString(400, y, "K.Ramya")

    # Save the PDF
    p.showPage()
    p.save()

    buffer.seek(0)
    new_receipt.payment_receipt.save(f"payment_receipt_{new_receipt.payment_number}.pdf", buffer)
    return buffer

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
    email.attach('Payment_receipt.pdf', pdf_buffer.getvalue(), 'application/pdf')
    email.send()
