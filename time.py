from PIL import Image, ImageDraw, ImageFont

# Define the size of the image and create a blank image
width, height = 1920, 1080
background_color = (255, 255, 255)  # White background
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Define fonts
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust the font path if needed
font_size_title = 40
font_size_text = 30
font_title = ImageFont.truetype(font_path, font_size_title)
font_text = ImageFont.truetype(font_path, font_size_text)

# Define timetable content
timetable = [
    ("Monday to Friday", [
        ("5:30 PM - 6:00 PM", "Break / Dinner"),
        ("6:00 PM - 8:00 PM", "Aptitude Practice"),
        ("8:00 PM - 9:00 PM", "OS / CN (Alternate Days)"),
        ("9:00 PM - 10:00 PM", "SQL")
    ]),
    ("Saturday", [
        ("9:00 AM - 11:00 AM", "Full-Length Mock Aptitude Test"),
        ("11:00 AM - 12:00 PM", "Review Mock Test Results"),
        ("12:00 PM - 1:00 PM", "Break / Lunch"),
        ("1:00 PM - 3:00 PM", "DBMS Theory and Practice"),
        ("3:00 PM - 4:00 PM", "OS Revision"),
        ("4:00 PM - 5:00 PM", "CN Revision"),
        ("5:00 PM - 6:00 PM", "Break / Relax"),
        ("6:00 PM - 8:00 PM", "DSA Practice"),
        ("8:00 PM - 9:00 PM", "Dinner"),
        ("9:00 PM - 10:00 PM", "Practice SQL Queries")
    ]),
    ("Sunday", [
        ("10:00 AM - 12:00 PM", "Mock Interviews / Aptitude Test Practice"),
        ("12:00 PM - 1:00 PM", "Break / Lunch"),
        ("1:00 PM - 3:00 PM", "Review Mistakes from Mock Tests"),
        ("3:00 PM - 5:00 PM", "Subject Revision"),
        ("5:00 PM - 6:00 PM", "Break / Relax"),
        ("6:00 PM - 8:00 PM", "DSA Practice"),
        ("8:00 PM - 9:00 PM", "Dinner"),
        ("9:00 PM - 10:00 PM", "Relax / Light Reading")
    ])
]

# Draw the timetable on the image
x, y = 50, 50
padding = 20
for title, items in timetable:
    draw.text((x, y), title, fill="black", font=font_title)
    y += font_size_title + padding
    for time, task in items:
        draw.text((x, y), f"{time}: {task}", fill="black", font=font_text)
        y += font_size_text + padding
    y += padding  # Add extra space between sections

# Save the image
image.save("timetable.png")
