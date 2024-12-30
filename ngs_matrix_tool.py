import pandas as pd
from tkinter import Tk, filedialog
from tkinter import messagebox
import os
import numpy as np

def ensure_numeric_and_string(df, chromosome_column, position_column):
    """Ensure chromosome is string and position is numeric."""
    df.iloc[:, chromosome_column - 1] = df.iloc[:, chromosome_column - 1].astype(str)
    df.iloc[:, position_column - 1] = pd.to_numeric(df.iloc[:, position_column - 1], errors="coerce")
    return df

def create_mutation_matrix(file_paths, allele_fraction_column=22, chromosome_column=1, position_column=2, threshold=0.1):
    """Create a 9x9 mutation matrix with shared and unique mutations."""
    dataframes = {os.path.basename(path): pd.read_csv(path) for path in file_paths}

    # Ensure data consistency
    for file_name, df in dataframes.items():
        dataframes[file_name] = ensure_numeric_and_string(df, chromosome_column, position_column)

    file_names = list(dataframes.keys())
    matrix = np.empty((len(file_names), len(file_names)), dtype=object)

    for i in range(len(file_names)):
        for j in range(len(file_names)):
            if i == j:
                matrix[i, j] = "-"
                continue

            df1 = dataframes[file_names[i]]
            df2 = dataframes[file_names[j]]

            df1_high_quality = df1[df1.iloc[:, allele_fraction_column - 1] >= threshold]
            df2_high_quality = df2[df2.iloc[:, allele_fraction_column - 1] >= threshold]

            shared_mutations = pd.merge(
                df1_high_quality.iloc[:, [chromosome_column - 1, position_column - 1, allele_fraction_column - 1]],
                df2_high_quality.iloc[:, [chromosome_column - 1, position_column - 1, allele_fraction_column - 1]],
                on=[df1.columns[chromosome_column - 1], df1.columns[position_column - 1]],
                suffixes=('_File1', '_File2')
            )

            unique_to_file1 = len(df1_high_quality) - len(shared_mutations)
            matrix[i, j] = f"{len(shared_mutations)} ({unique_to_file1})"

    return pd.DataFrame(matrix, index=file_names, columns=file_names)

def main():
    root = Tk()
    root.withdraw()
    
    messagebox.showinfo("File Selection", "Please select the CSV files for analysis.")
    file_paths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])

    if not file_paths:
        messagebox.showerror("Error", "No files selected. Exiting.")
        return

    try:
        matrix = create_mutation_matrix(file_paths)
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")], title="Save Matrix")

        if output_file:
            matrix.to_excel(output_file, index=True)
            messagebox.showinfo("Success", f"Matrix saved to {output_file}")
        else:
            messagebox.showinfo("Cancelled", "Matrix not saved.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
