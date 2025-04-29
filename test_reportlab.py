from reportlab.pdfgen import canvas

c = canvas.Canvas("test_output.pdf")
c.drawString(100, 750, "Hello, ReportLab!")
c.save()
# This script creates a simple PDF file named "test_output.pdf" with the text "Hello, ReportLab!" at coordinates (100, 750).
