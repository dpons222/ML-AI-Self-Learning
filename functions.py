import nbformat
import regex as re

def split_markdown_cells(notebook_path, output_path):
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    new_cells = []
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            # Split the cell content by headers
            parts = re.split(r'(?=\n#)', cell.source)
            for part in parts:
                new_cells.append(nbformat.v4.new_markdown_cell(part.strip()))
        else:
            new_cells.append(cell)

    # Update the notebook cells
    nb.cells = new_cells

    # Write the updated notebook to a new file
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

def math_format(x):
    return re.sub(r'\\\(\s*(.*?)\s*\\\)', r'$ \1 $', x)

# Example usage
#split_markdown_cells('/Users/diegopons/Documents/Coding/Chat-GPT-Learning/Machine Learning/machine_learning.ipynb', '/Users/diegopons/Documents/Coding/Chat-GPT-Learning/Machine Learning/NEW_machine_learning.ipynb')