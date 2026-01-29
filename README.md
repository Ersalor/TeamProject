# 🇹🇷 Türkiye Neighborhood Information Management System (NIMS)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## 📖 Project Overview
NIMS is a **CLI-based (Command Line Interface)** application designed to manage, query, and analyze hierarchical geographical data (Province -> District -> Neighborhood) specifically for Turkey.

Standard sorting algorithms often fail with Turkish characters (e.g., 'İ', 'ı', 'Ş', 'ğ'). This project features a **custom localization engine** built from scratch to handle Turkish character encoding, casing logic, and alphabetical sorting without relying on external libraries.

This project demonstrates proficiency in **File I/O operations**, **Algorithm Design**, and **CRUD implementation** in a collaborative environment.

## 🚀 Key Features

### 🛠 Core Functionality (CRUD)
* **Smart Search:** Supports both **Exact Match** and **Partial Match** queries to find neighborhoods across different provinces.
* **Hierarchical Listing:** Lists data efficiently by Province or District context.
* **Data Management:**
    * **Add:** Insert new neighborhood records with duplicate validation.
    * **Delete:** Remove specific records based on province/district hierarchy.
    * **Update & Move:** Rename neighborhoods or transfer them between districts.

### ⚙️ Technical Highlights
* **Custom Turkish Localization:** Implements bespoke `turkish_lower`, `turkish_upper`, and `sorting_rule` functions to ensure linguistically correct data processing.
* **Raw Data Parsing:** Includes custom parsing logic to handle non-standard text formatting within the database file.
* **Modular Architecture:** Logic (`functions.py`) is strictly separated from the interface (`main.py`), adhering to clean code principles.

## 📂 Project Structure

```bash
├── functions.py        # Core logic, CRUD operations, and string manipulation algorithms
├── main.py             # Entry point and CLI menu loop
├── neighborhoods.txt   # The flat-file database
└── README.md           # Documentation
