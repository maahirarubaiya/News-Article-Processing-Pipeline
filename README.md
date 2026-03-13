# News-Article-Processing-Pipeline

A Python-based news article processing pipeline built as part of CS 2100 at Northeastern University Oakland. The project demonstrates object-oriented programming, data processing, and software engineering best practices including type annotations, unit testing, and clean API design.

---

## 🔍 Overview

This pipeline processes and searches news articles using three core components:

- **`Article`** — A data class representing a single news article with attributes like title, source, date, and content
- **`SearchNews`** — Handles querying and filtering articles based on keywords and metadata
- **`NewsProcessor`** — Orchestrates the full pipeline, processing batches of articles and producing structured output

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `unittest`, `unittest.mock`
- **Type Checking:** `mypy`
- **Testing:** pytest

---

## 📁 Project Structure

```
sp26-hw4/
├── article.py          # Article data class
├── search_news.py      # Search and filtering logic
├── news_processor.py   # Pipeline orchestration
├── test_pipeline.py    # Unit tests with mocking
└── README.md
```

---

## ▶️ How to Run

**1. Clone the repo:**
```bash
git clone https://github.com/your-username/sp26-hw4.git
cd sp26-hw4
```

**2. Install dependencies:**
```bash
pip install pytest mypy
```

**3. Run the pipeline:**
```bash
python news_processor.py
```

**4. Run tests:**
```bash
pytest test_pipeline.py
```

**5. Type check:**
```bash
mypy article.py search_news.py news_processor.py
```

---

## Key Concepts Demonstrated

- Object-oriented design with clearly separated responsibilities
- Type annotations throughout for readability and static analysis
- Unit testing with `unittest.mock` to isolate and test components independently
- Clean `__repr__` formatting for readable object output

---

## Author

**Maahira Rubaiya**
BS Computer Science & Business Administration, Northeastern University Oakland
[LinkedIn](https://www.linkedin.com/in/maahira-rubaiya-62811a2b4/)
