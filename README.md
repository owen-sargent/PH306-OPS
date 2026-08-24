# PH 306 Mechanics Warm-Up

This repository is a script-first starter for a simple introductory Physics assignment in PH 306. The goal is to practice getting set up in GitHub Codespaces, editing a Python file, and reading CodeGrade feedback without adding a lot of overhead.

## Primary File

- `assignment.py`: the student work file for this assignment

## Supporting Files

- `test_public.py`: visible checks that match the CodeGrade auto-grader.

## What Students Implement

Complete the function stubs in `assignment.py`:

- `distance_traveled`
- `kinetic_energy`
- `free_fall_height`
- `projectile_range`
- `quadratic_solver`

Each function uses a standard introductory mechanics/mathematical equation.

## Workflow

1. Open `assignment.py` in Codespaces or your local editor.
1. Fill in the function bodies.
1. Run `python assignment.py` or `pytest` to check your work.
1. Commit and push your changes.
1. Review the autograding results in CodeGrade.

## Grading and Checks

CodeGrade evaluates submissions with four categories of checks:

1. Syntax validity: parsed with `ast` to confirm your file is valid Python.
1. Structure and quality: checked with `semgrep`, `flake8`, `mypy`, and `numpydoc`.
1. Functionality: checked with `pytest` against the public tests (and private tests on CodeGrade).
  - Note: public test files in this repo mirror the public tests on CodeGrade.

## Environment

The repository includes `requirements.txt` for pip-based setup and `environment.yml` for Codespaces or conda-style workflows.
