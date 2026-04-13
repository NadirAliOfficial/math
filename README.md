# Math Notes — BS-IV Mathematics

Personal notes, assignments, and midterm papers for BS-IV Mathematics at the Department of Mathematics.

**Teacher:** Dr. Hisam Uddin Shaikh, Chairman — Department of Mathematics  
**Student:** Nadir Ali Khan

---

## Folder Structure

### Numerical_Analysis
Notes and midterms for Numerical Analysis I.

| File | Description |
|------|-------------|
| `Numerical_Analysis.tex / .pdf` | Chapter 1 — Full theoretical treatment of 5 root-finding methods (37 pages) |
| `Numerical_Analysis_I_MidTerm_2026.tex / .pdf` | Midterm paper 2026 |
| `midterm.tex / .pdf` | Midterm solutions |
| `questions.tex` | Root-finding practice questions |
| `Numerical Methods f(x)...pdf` | Reference: $f(x) = x^3 - 2x - 5 = 0$ worked example |

**Topics covered in Chapter 1:**
1. Bisection Method
2. Regula Falsi Method (+ Illinois, Pegasus, Anderson-Björck variants)
3. Newton-Raphson Method (+ Halley's, systems via Jacobian)
4. Secant Method (+ Muller's, IQI, Brent's)
5. Fixed Point Iteration (+ Steffensen's, Banach theorem, connections to ODEs/eigenvalues)

---

### Operations_Research
| File | Description |
|------|-------------|
| `Operations_Research_MidTerm_2026.tex / .pdf` | Midterm paper 2026 |

---

### Statistical_Inference
| File | Description |
|------|-------------|
| `Statistical_Inference_MidTerm_2025.tex / .pdf` | Midterm paper 2025 |

---

### Laplace_Transform
| File | Description |
|------|-------------|
| `Assignment_Laplace_Transform.tex / .pdf` | Assignment on Laplace Transforms |

---

### Practice
| File | Description |
|------|-------------|
| `Math_MCQ_100_Questions.pdf` | 100 MCQ practice questions |

---

## Compiling

All `.tex` files require **XeLaTeX** (for Unicode support):

```bash
xelatex Numerical_Analysis.tex
```

Required LaTeX packages: `amsmath`, `amssymb`, `tcolorbox`, `tikz`, `booktabs`, `multicol`, `enumitem`, `titlesec`, `fancyhdr`, `geometry`, `xcolor`, `multirow`.
