# NGS Contamination Matrix Tool

This project provides a comprehensive analysis of contamination between multiple Next-Generation Sequencing (NGS) data files. It creates a 9x9 matrix showing the shared and unique mutations between every pair of files. The tool is ideal for identifying potential DNA cross-contamination or understanding similarities between datasets.

## Features

- **Dynamic Mutation Matrix**:
  - Each cell displays the number of shared mutations and unique mutations from the first file.
  - Format: `Shared (Unique)`.
- **File Input**:
  - Accepts multiple CSV files for batch analysis.
- **Excel Export**:
  - Saves the matrix as an Excel file (.xlsx).
- **User-Friendly Interface**:
  - Select files and save results via a graphical interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ngs-matrix-tool.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ngs-matrix-tool
    ```
3. Install required dependencies:
    ```bash
    pip install pandas numpy openpyxl
    ```

## Usage

1. Run the Python script:
    ```bash
    python ngs_matrix_tool.py
    ```
2. Select the CSV files for analysis.
3. Save the generated mutation matrix to your desired location.

## Input Requirements

- **File Format**: CSV files with the following assumed structure:
  - Chromosome column: 1st column
  - Position column: 2nd column
  - Allele Fraction column: 22nd column
- **Threshold**: Default allele fraction threshold is 0.1.

## Output

- The output Excel file contains a square matrix with the following format in each cell:
  - `Shared Mutations (Unique to File 1)`

Example:

|          | File1.csv       | File2.csv       | File3.csv       |
|----------|-----------------|-----------------|-----------------|
| File1.csv| -               | 272 (-67)       | 275 (-70)       |
| File2.csv| 272 (-2)        | -               | 322 (-52)       |
| File3.csv| 275 (-7)        | 322 (-54)       | -               |

## Notes

- **Interpretation**:
  - High shared mutations and low unique mutations may indicate potential contamination.
  - Unique mutations highlight dataset-specific variations.
- **Limitations**:
  - Results are representative and may include sequencing artifacts or errors.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with new features or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
