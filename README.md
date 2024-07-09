# Trustee Fund Holdings Extractor

This project extracts trustee fund holdings information from an HTML file and outputs the data to a CSV file.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Setup

1. Clone this repository or download the source code.
    ```sh
    git clone https://github.com/yogesh1801/web-scrape.git
    ```
2. Navigate to the project directory:
    ```sh
    cd web-scrape
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment
    ```sh
    source venv/Scripts/activate
    ```
5. Install Required packages
    ```sh
    pip install requirements.txt
    ```
6. Run the Script
    ```
    python script.py
    ``` 

7. The script will generate the following files:
- `extracted_content.html`: Extracted content from the original HTML
- `extracted_table1.html`: Extracted "Interested Trustees" table
- `extracted_table2.html`: Extracted "Independent Trustees" table
- `combined_trustee_fund_holdings.csv`: Final output CSV file containing the extracted data


