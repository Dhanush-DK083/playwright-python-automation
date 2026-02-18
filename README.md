# Playwright Automation Framework (Python + Pytest)

## Overview
This project demonstrates a scalable UI automation framework using Playwright with Python and Pytest.

## Features
- Page Object Model (POM)
- Data-driven testing using JSON
- Login (positive & negative)
- Add to cart & remove validation
- Sorting validation
- End-to-end checkout flow
- HTML reporting
- Headed & headless execution

## Project Structure
automation_framework/
  pages/
  tests/
  utils/
  test_data/
  conftest.py
  pytest.ini

## Installation
pip install -r requirements.txt
playwright install

## Run Tests
pytest

## Run Headed
pytest --headed

## Generate HTML Report
pytest --html=report.html --self-contained-html
