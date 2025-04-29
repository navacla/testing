from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Define your chapter data here
chapters = [
    (
        "Synchronicity",
        "🌌",
        "Synchronicity is when two souls meet at the right energetic frequency.",
    ),
    (
        "Unhealed Wounds",
        "🩹",
        "We attract partners who mirror our unresolved emotional wounds.",
    ),
]

# Create a new PDF
pdf_path = "jung_summary.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)

width, height = A4
y = height - 100

# Set fonts and colors
c.setFont("Helvetica-Bold", 16)
c.drawString(50, y, "Carl Jung: Soul, Love & Healing — Summary")
y -= 40

c.setFont("Helvetica", 12)

# Loop through chapters
for title, emoji, body in chapters:
    if y < 150:
        c.showPage()
        y = height - 100
        c.setFont("Helvetica", 12)
    c.drawString(50, y, f"{emoji} {title}")
    y -= 20
    c.drawString(70, y, body)
    y -= 40

c.save()
print("PDF created:", pdf_path)
# This script creates a PDF summary of Carl Jung's concepts related to soul, love, and healing.

# It includes chapter titles, emojis, and brief descriptions.
