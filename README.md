# IT Systems Security Review

This project simulates a security audit of a web application, identifying potential vulnerabilities and recommending improvements.

## How to Run the Project

1. Clone the repository.
2. Install dependencies:
    ```
    npm install
    ```
3. Run the app:
    ```
    node src/app.js
    ```
4. Access the app on `http://localhost:3000`.
5. Review identified vulnerabilities in `src/vulnerabilities.md`.
6. Review recommendations in `src/recommendations.md`.

## Running Security Tests
1. Install Python dependencies:
    ```
    pip install requests
    ```
2. Run the tests:
    ```
    python src/tests/test_vulnerabilities.py
    ```

## Audit Report
The audit findings are documented in `audit-report.md`.
