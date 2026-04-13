from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

SET1 = [
    # --- Arithmetic Skills (Q1–13) ---
    ("1.", "What is 15 + 27?", ["A) 40", "B) 42", "C) 43", "D) 45"], "B"),
    ("2.", "What is 144 ÷ 12?", ["A) 10", "B) 11", "C) 12", "D) 13"], "C"),
    ("3.", "What is 23 × 4?", ["A) 88", "B) 90", "C) 92", "D) 94"], "C"),
    ("4.", "What is 256 − 89?", ["A) 167", "B) 168", "C) 177", "D) 178"], "A"),
    ("5.", "What is the LCM of 4 and 6?", ["A) 8", "B) 12", "C) 16", "D) 24"], "B"),
    ("6.", "What is the HCF of 12 and 18?", ["A) 3", "B) 4", "C) 6", "D) 9"], "C"),
    ("7.", "What is 3/4 + 1/4?", ["A) 4/8", "B) 1/2", "C) 1", "D) 3/8"], "C"),
    ("8.", "What is 5/6 − 1/3?", ["A) 1/2", "B) 4/6", "C) 1/3", "D) 2/3"], "A"),
    ("9.", "What is 2.5 × 4?", ["A) 8", "B) 9", "C) 10", "D) 11"], "C"),
    ("10.", "Which of the following is a prime number?", ["A) 15", "B) 21", "C) 29", "D) 33"], "C"),
    ("11.", "What is 0.75 expressed as a fraction?", ["A) 3/4", "B) 7/5", "C) 7/10", "D) 1/4"], "A"),
    ("12.", "What is 2³?", ["A) 6", "B) 8", "C) 9", "D) 12"], "B"),
    ("13.", "What is √81?", ["A) 7", "B) 8", "C) 9", "D) 10"], "C"),
    # --- Basic Algebra (Q14–26) ---
    ("14.", "If x + 5 = 12, then x = ?", ["A) 5", "B) 6", "C) 7", "D) 8"], "C"),
    ("15.", "If 3x = 18, then x = ?", ["A) 4", "B) 5", "C) 6", "D) 7"], "C"),
    ("16.", "Simplify: 3x + 2x", ["A) 5x", "B) 6x", "C) 5x²", "D) 6x²"], "A"),
    ("17.", "What is the value of 2x − 3 when x = 5?", ["A) 5", "B) 6", "C) 7", "D) 10"], "C"),
    ("18.", "Which is the coefficient in 7y?", ["A) y", "B) 7", "C) 7y", "D) None"], "B"),
    ("19.", "What is (x + 3)(x − 3)?", ["A) x² − 9", "B) x² + 9", "C) x² − 6x + 9", "D) x² + 6x − 9"], "A"),
    ("20.", "If 2x + 4 = 10, then x = ?", ["A) 2", "B) 3", "C) 4", "D) 5"], "B"),
    ("21.", "Expand: 2(x + 5)", ["A) 2x + 5", "B) 2x + 10", "C) x + 10", "D) 2x + 7"], "B"),
    ("22.", "What is x² when x = 3?", ["A) 6", "B) 8", "C) 9", "D) 12"], "C"),
    ("23.", "Simplify: 4x − x", ["A) 3", "B) 4x", "C) 3x", "D) 5x"], "C"),
    ("24.", "If y = 2x + 1 and x = 3, what is y?", ["A) 5", "B) 6", "C) 7", "D) 8"], "C"),
    ("25.", "What is the degree of x³ + x² + x?", ["A) 1", "B) 2", "C) 3", "D) 6"], "C"),
    ("26.", "Which expression equals 12 when x = 5?", ["A) 3x", "B) 2x + 2", "C) x + 7", "D) 4x − 8"], "D"),
    # --- Percentages (Q27–39) ---
    ("27.", "What is 20% of 200?", ["A) 30", "B) 40", "C) 50", "D) 60"], "B"),
    ("28.", "What is 15% of 80?", ["A) 10", "B) 12", "C) 14", "D) 15"], "B"),
    ("29.", "50 is what percent of 200?", ["A) 20%", "B) 25%", "C) 30%", "D) 40%"], "B"),
    ("30.", "A shirt costs $50 and is 10% off. What is the sale price?", ["A) $40", "B) $45", "C) $48", "D) $42"], "B"),
    ("31.", "What is 100% of 75?", ["A) 50", "B) 75", "C) 100", "D) 150"], "B"),
    ("32.", "Convert 0.45 to a percentage.", ["A) 4.5%", "B) 45%", "C) 450%", "D) 0.45%"], "B"),
    ("33.", "What percent of 60 is 12?", ["A) 15%", "B) 20%", "C) 25%", "D) 30%"], "B"),
    ("34.", "A price increased from $80 to $100. What is the percentage increase?", ["A) 15%", "B) 20%", "C) 25%", "D) 30%"], "C"),
    ("35.", "What is 5% of 1000?", ["A) 5", "B) 25", "C) 50", "D) 500"], "C"),
    ("36.", "Convert 3/4 to a percentage.", ["A) 34%", "B) 57%", "C) 75%", "D) 80%"], "C"),
    ("37.", "A student scored 45 out of 60. What is the percentage?", ["A) 70%", "B) 75%", "C) 80%", "D) 85%"], "B"),
    ("38.", "A population of 500 increases by 10%. What is the new population?", ["A) 510", "B) 540", "C) 550", "D) 600"], "C"),
    ("39.", "What is 30% of 90?", ["A) 25", "B) 27", "C) 30", "D) 33"], "B"),
    # --- Ratios & Proportion (Q40–50) ---
    ("40.", "Simplify the ratio 12:16.", ["A) 2:3", "B) 3:4", "C) 4:3", "D) 6:8"], "B"),
    ("41.", "Ratio of boys to girls is 3:2 and there are 15 boys. How many girls?", ["A) 8", "B) 10", "C) 12", "D) 15"], "B"),
    ("42.", "Which ratio is equal to 2:3?", ["A) 4:5", "B) 6:9", "C) 8:15", "D) 3:2"], "B"),
    ("43.", "If 5 pens cost $10, how much do 8 pens cost?", ["A) $14", "B) $16", "C) $18", "D) $20"], "B"),
    ("44.", "Simplify 25:75.", ["A) 1:2", "B) 1:3", "C) 2:5", "D) 3:1"], "B"),
    ("45.", "If a:b = 3:4 and b:c = 4:5, then a:c = ?", ["A) 3:4", "B) 3:5", "C) 4:5", "D) 5:3"], "B"),
    ("46.", "6 workers finish a task in 4 days. How many days will 8 workers take?", ["A) 2", "B) 3", "C) 4", "D) 6"], "B"),
    ("47.", "Find the 4th proportional to 3, 6, 9.", ["A) 12", "B) 15", "C) 18", "D) 27"], "C"),
    ("48.", "If x:y = 2:5, find x when y = 25.", ["A) 8", "B) 10", "C) 12", "D) 15"], "B"),
    ("49.", "The mean proportional between 4 and 16 is?", ["A) 6", "B) 8", "C) 10", "D) 12"], "B"),
    ("50.", "A recipe uses flour and sugar in ratio 3:1. If 12 cups of flour are used, how many cups of sugar are needed?", ["A) 3", "B) 4", "C) 5", "D) 6"], "B"),
]

SET2 = [
    # --- Simple Linear Equations (Q1–17) ---
    ("1.", "Solve: x + 7 = 15", ["A) 7", "B) 8", "C) 9", "D) 10"], "B"),
    ("2.", "Solve: 2x = 14", ["A) 5", "B) 6", "C) 7", "D) 8"], "C"),
    ("3.", "Solve: x − 4 = 9", ["A) 11", "B) 12", "C) 13", "D) 14"], "C"),
    ("4.", "Solve: 3x + 2 = 11", ["A) 2", "B) 3", "C) 4", "D) 5"], "B"),
    ("5.", "Solve: 5x − 5 = 20", ["A) 3", "B) 4", "C) 5", "D) 6"], "C"),
    ("6.", "Solve: x/4 = 5", ["A) 15", "B) 20", "C) 25", "D) 30"], "B"),
    ("7.", "Solve: 2x + 6 = 18", ["A) 4", "B) 5", "C) 6", "D) 7"], "C"),
    ("8.", "Solve: 7x = 49", ["A) 6", "B) 7", "C) 8", "D) 9"], "B"),
    ("9.", "Solve: x/3 + 2 = 5", ["A) 6", "B) 7", "C) 8", "D) 9"], "D"),
    ("10.", "Solve: 4x − 8 = 12", ["A) 4", "B) 5", "C) 6", "D) 7"], "B"),
    ("11.", "Solve: 2x + 3 = x + 7", ["A) 3", "B) 4", "C) 5", "D) 6"], "B"),
    ("12.", "Solve: 3(x + 2) = 18", ["A) 2", "B) 4", "C) 6", "D) 8"], "B"),
    ("13.", "Solve: 6x + 4 = 28", ["A) 3", "B) 4", "C) 5", "D) 6"], "B"),
    ("14.", "Solve: x + x + x = 21", ["A) 5", "B) 6", "C) 7", "D) 8"], "C"),
    ("15.", "Solve: 5x + 10 = 35", ["A) 3", "B) 4", "C) 5", "D) 6"], "C"),
    ("16.", "Solve: 2(x − 3) = 10", ["A) 6", "B) 7", "C) 8", "D) 9"], "C"),
    ("17.", "If 4x + 1 = 17, what is x?", ["A) 3", "B) 4", "C) 5", "D) 6"], "B"),
    # --- Basic Geometry (Q18–34) ---
    ("18.", "How many sides does a hexagon have?", ["A) 4", "B) 5", "C) 6", "D) 7"], "C"),
    ("19.", "What is the sum of angles in a triangle?", ["A) 90°", "B) 180°", "C) 270°", "D) 360°"], "B"),
    ("20.", "What type of angle is 90°?", ["A) Acute", "B) Right", "C) Obtuse", "D) Straight"], "B"),
    ("21.", "What is the sum of interior angles of a quadrilateral?", ["A) 180°", "B) 270°", "C) 360°", "D) 450°"], "C"),
    ("22.", "How many degrees are in a straight line?", ["A) 90°", "B) 180°", "C) 270°", "D) 360°"], "B"),
    ("23.", "An equilateral triangle has:", ["A) All sides different", "B) Two sides equal", "C) All sides equal", "D) No sides equal"], "C"),
    ("24.", "What is the radius if the diameter of a circle is 14 cm?", ["A) 5 cm", "B) 6 cm", "C) 7 cm", "D) 14 cm"], "C"),
    ("25.", "How many right angles does a rectangle have?", ["A) 1", "B) 2", "C) 3", "D) 4"], "D"),
    ("26.", "A polygon with 5 sides is called a?", ["A) Hexagon", "B) Heptagon", "C) Pentagon", "D) Octagon"], "C"),
    ("27.", "An angle less than 90° is called?", ["A) Right", "B) Acute", "C) Obtuse", "D) Reflex"], "B"),
    ("28.", "How many faces does a cube have?", ["A) 4", "B) 6", "C) 8", "D) 12"], "B"),
    ("29.", "What is the complement of a 35° angle?", ["A) 45°", "B) 55°", "C) 65°", "D) 145°"], "B"),
    ("30.", "Two lines that never meet are called?", ["A) Perpendicular", "B) Intersecting", "C) Parallel", "D) Diagonal"], "C"),
    ("31.", "A triangle with all sides of different lengths is called?", ["A) Equilateral", "B) Isosceles", "C) Scalene", "D) Right"], "C"),
    ("32.", "What is the supplement of a 60° angle?", ["A) 30°", "B) 90°", "C) 120°", "D) 150°"], "C"),
    ("33.", "How many vertices does a triangle have?", ["A) 1", "B) 2", "C) 3", "D) 4"], "C"),
    ("34.", "A full circle contains how many degrees?", ["A) 90°", "B) 180°", "C) 270°", "D) 360°"], "D"),
    # --- Basic Formulas of Geometry (Q35–50) ---
    ("35.", "What is the area of a rectangle with length 8 and width 5?", ["A) 13", "B) 26", "C) 40", "D) 80"], "C"),
    ("36.", "What is the perimeter of a square with side 6 cm?", ["A) 12 cm", "B) 24 cm", "C) 36 cm", "D) 48 cm"], "B"),
    ("37.", "What is the area of a square with side 7?", ["A) 14", "B) 28", "C) 49", "D) 56"], "C"),
    ("38.", "What is the perimeter of a rectangle with length 10 and width 4?", ["A) 14", "B) 28", "C) 40", "D) 56"], "B"),
    ("39.", "Area of a triangle with base 10 and height 6 is?", ["A) 16", "B) 30", "C) 60", "D) 80"], "B"),
    ("40.", "Using π ≈ 3.14, what is the circumference of a circle with radius 5?", ["A) 15.7", "B) 31.4", "C) 78.5", "D) 15.14"], "B"),
    ("41.", "Area of a circle with radius 7 (use π = 22/7) is?", ["A) 44", "B) 88", "C) 154", "D) 308"], "C"),
    ("42.", "What is the volume of a cube with side 4 cm?", ["A) 16 cm³", "B) 48 cm³", "C) 64 cm³", "D) 96 cm³"], "C"),
    ("43.", "Area of a parallelogram with base 9 and height 4 is?", ["A) 13", "B) 18", "C) 36", "D) 72"], "C"),
    ("44.", "Perimeter of a triangle with sides 5, 7, and 9 is?", ["A) 19", "B) 21", "C) 23", "D) 25"], "B"),
    ("45.", "The diagonal of a rectangle with length l and width w is?", ["A) l + w", "B) l × w", "C) √(l² + w²)", "D) 2(l + w)"], "C"),
    ("46.", "Surface area of a cube with side 3 cm is?", ["A) 27 cm²", "B) 36 cm²", "C) 54 cm²", "D) 81 cm²"], "C"),
    ("47.", "Volume of a cuboid with l=5, w=4, h=3 is?", ["A) 12", "B) 20", "C) 47", "D) 60"], "D"),
    ("48.", "Area of a trapezoid with parallel sides 6 and 10, height 4 is?", ["A) 16", "B) 32", "C) 64", "D) 80"], "B"),
    ("49.", "Which formula gives the circumference of a circle?", ["A) πr²", "B) 2πr", "C) πd²", "D) 2πr²"], "B"),
    ("50.", "The Pythagorean theorem states:", ["A) a + b = c", "B) a² + b² = c²", "C) a² − b² = c²", "D) a × b = c²"], "B"),
]

ANSWER_KEY_1 = [q[3] for q in SET1]
ANSWER_KEY_2 = [q[3] for q in SET2]


def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'Title', parent=styles['Title'],
        fontSize=16, textColor=colors.HexColor('#1a237e'),
        spaceAfter=4, alignment=TA_CENTER, fontName='Helvetica-Bold'
    )
    subtitle_style = ParagraphStyle(
        'Subtitle', parent=styles['Normal'],
        fontSize=11, textColor=colors.HexColor('#37474f'),
        spaceAfter=2, alignment=TA_CENTER
    )
    set_title_style = ParagraphStyle(
        'SetTitle', parent=styles['Heading1'],
        fontSize=13, textColor=colors.white,
        spaceAfter=6, spaceBefore=10,
        backColor=colors.HexColor('#1a237e'),
        alignment=TA_CENTER, fontName='Helvetica-Bold',
        leftIndent=-10, rightIndent=-10
    )
    topic_style = ParagraphStyle(
        'Topic', parent=styles['Normal'],
        fontSize=10, textColor=colors.HexColor('#5c6bc0'),
        fontName='Helvetica-BoldOblique', spaceBefore=10, spaceAfter=4
    )
    q_style = ParagraphStyle(
        'Question', parent=styles['Normal'],
        fontSize=10.5, fontName='Helvetica-Bold',
        textColor=colors.HexColor('#212121'),
        spaceBefore=6, spaceAfter=2, leading=14
    )
    opt_style = ParagraphStyle(
        'Option', parent=styles['Normal'],
        fontSize=10, leftIndent=18,
        textColor=colors.HexColor('#424242'),
        spaceAfter=1, leading=13
    )
    ans_style = ParagraphStyle(
        'Answer', parent=styles['Normal'],
        fontSize=9, fontName='Helvetica-Bold',
        textColor=colors.HexColor('#2e7d32'),
        leftIndent=18, spaceAfter=6
    )
    ak_title_style = ParagraphStyle(
        'AKTitle', parent=styles['Normal'],
        fontSize=12, fontName='Helvetica-Bold',
        textColor=colors.white,
        backColor=colors.HexColor('#37474f'),
        alignment=TA_CENTER, spaceBefore=10, spaceAfter=6,
        leftIndent=-10, rightIndent=-10
    )

    story = []

    # === COVER ===
    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph("Mathematics MCQ Practice Paper", title_style))
    story.append(Paragraph("100 Multiple Choice Questions — Two Sets of 50", subtitle_style))
    story.append(Paragraph(
        "Topics: Basic Algebra · Arithmetic Skills · Percentages · Ratios &amp; Proportion · "
        "Simple Linear Equations · Basic Geometry · Geometry Formulas",
        ParagraphStyle('info', parent=styles['Normal'], fontSize=9,
                       textColor=colors.grey, alignment=TA_CENTER, spaceAfter=2)
    ))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1a237e'), spaceAfter=14))

    def add_questions(qs, show_answers=True):
        for i, (num, q, opts, ans) in enumerate(qs):

            story.append(Paragraph(f"Q{num}  {q}", q_style))
            for opt in opts:
                story.append(Paragraph(opt, opt_style))
            if show_answers:
                story.append(Paragraph(f"✓ Answer: {ans}", ans_style))

    # === SET 1 ===
    story.append(Paragraph("SET 1 — Basic Algebra, Arithmetic, Percentages, Ratios &amp; Proportion", set_title_style))
    story.append(Spacer(1, 0.3*cm))
    add_questions(SET1, show_answers=False)

    # === SET 2 ===
    story.append(PageBreak())
    story.append(Paragraph("SET 2 — Linear Equations, Geometry &amp; Geometry Formulas", set_title_style))
    story.append(Spacer(1, 0.3*cm))
    add_questions(SET2, show_answers=False)

    doc.build(story)
    print(f"PDF saved: {filename}")


build_pdf("/Users/nadirali/math/Math_MCQ_100_Questions.pdf")
