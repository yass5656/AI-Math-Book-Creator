# Cambridge Math Studio 1.0

## Scope

Curriculum:
- Cambridge Primary Mathematics

Stages:
- Stage 1
- Stage 2
- Stage 3
- Stage 4
- Stage 5
- Stage 6

Terms:
- Term 1
- Term 2

Output Books:
1. Practice Book
2. Progressive Assessment Book
3. Answer Book

Language:
- English

Output:
- PDF

---

## Knowledge Base Structure

knowledge_base/
    Cambridge/
        Primary/
            StageX/
                TermY/
                    curriculum.yaml
                    Unit1/
                        unit.yaml
                        skills.yaml
                        patterns/
                    Unit2/
                    ...

---

## Question Pipeline

Curriculum
→ Unit
→ Lesson
→ Skill
→ Pattern
→ Generator
→ Exercise
→ Page
→ Book
→ PDF

---

## Core Rules

- No question is stored in Python.
- All questions are generated.
- Python contains only logic.
- YAML contains only data.
- One Generator per mathematical skill.
- One Pattern per question style.
- Three books only.

---

## Book Types

Practice Book

Contains:
- Warm Up
- Examples
- Practice
- Workbook Style
- Progression Style
- Review

Assessment Book

Contains:
- Progressive Tests
- Workbook Style
- Progression Style

Answer Book

Contains:
- Answers
- Worked Solutions

---

## Development Rules

- Never rename folders.
- Never duplicate logic.
- Never hardcode Stage or Term.
- Never hardcode Curriculum.
