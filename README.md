# NPV and IRR Calculator

A Python-based financial analysis tool that calculates Net Present Value (NPV) and Internal Rate of Return (IRR) for investment projects, along with risk assessment and cash flow visualization.

## Description

This project helps investors and financial analysts evaluate the viability of investment projects by calculating key financial metrics:
- **Net Present Value (NPV)** - The difference between the present value of cash inflows and outflows
- **Internal Rate of Return (IRR)** - The discount rate that makes the NPV equal to zero
- **Risk Level Assessment** - Based on the calculated IRR
- **Project Decision Recommendation** - Whether to accept or reject the project
- **Cash Flow Visualization** - Graphical representation of cash flows over time

## Features

- Interactive user input for project parameters
- NPV calculation using discounted cash flow analysis
- IRR calculation using binary search algorithm
- Automated project acceptance/rejection decision
- Risk level classification (Low, Medium, High)
- Cash flow trend visualization using matplotlib
- Input validation for financial calculations

## Requirements

- Python 3.x
- Required libraries:
  - `matplotlib` (for graph visualization)

## Installation

1. **Clone or download the project**
   ```bash
   git clone https://github.com/rohmashah21/npv-irr-calculator.git
   cd npv-irr-calculator
Install required dependencies

bash
pip install matplotlib
Usage
Run the script:

bash
python npv_irr_calculator.py
Input Parameters
You'll be prompted to enter:

Initial Investment - The upfront cost of the project (negative cash flow at year 0)

Discount Rate (%) - The required rate of return or cost of capital

Number of Years - The project's time horizon

Cash Flows - Net cash flow for each year of the project

Example
text
NPV AND IRR CALCULATOR
enter your initial investment: 100000
enter your rate(%): 10
no of years: 5
Cash flow year 1: 25000
Cash flow year 2: 30000
Cash flow year 3: 35000
Cash flow year 4: 40000
Cash flow year 5: 45000
Output
The program will display:

NPV value (rounded to 2 decimal places)
IRR percentage
Project acceptance/rejection decision
Risk level assessment
A line graph showing cash flow trends over the project years

Decision Criteria
NPV Decision Rule
NPV > 0 and IRR > Discount Rate → Project is acceptable

Otherwise → Project is not acceptable

Risk Assessment
IRR > 25% → High Return (High Risk)
IRR > 15% → Medium Risk
IRR ≤ 15% → Low Risk

How It Works
NPV Calculation

text
NPV = -Initial Investment + Σ(Cash Flow_t / (1 + r)^t)
Where:

t = year (1 to n)
r = discount rate
IRR Calculation
Uses binary search algorithm
Iterates 100 times to find the rate where NPV = 0
Searches between 0% and 100%

Visualization

Creates a line plot showing cash flow progression over the project lifecycle

Limitations
IRR search is limited to 100 iterations (0% to 100% range)
Assumes conventional cash flows (initial outflow followed by inflows)
Doesn't handle multiple IRRs for non-conventional cash flows
Requires matplotlib for graph visualization

Potential Improvements
Add support for multiple IRRs for unconventional cash flows
Implement sensitivity analysis
Add Excel export functionality
Include payback period calculation
Add profitability index calculation
Support for different compounding periods
Add GUI interface

License
This project is open-source and available for educational and professional use.

Contributing
Contributions, issues, and feature requests are welcome!

👤 Author
**Rohma Shah**
- GitHub: [@rohmashah21](https://github.com/rohmashah21)

Disclaimer: This tool is for educational purposes. Always consult with a financial professional before making investment decisions.
