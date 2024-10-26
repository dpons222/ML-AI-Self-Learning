import nbformat

def split_markdown_cells(notebook_path, output_path):
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    new_cells = []
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            # Split the cell content by headers
            parts = cell.source.split('\n## ')
            for i, part in enumerate(parts):
                if i == 0:
                    new_cells.append(nbformat.v4.new_markdown_cell(part))
                else:
                    new_cells.append(nbformat.v4.new_markdown_cell('## ' + part))
        else:
            new_cells.append(cell)

    # Update the notebook cells
    nb.cells = new_cells

    # Write the updated notebook to a new file
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Example usage
split_markdown_cells('linear_algebra.ipynb', 'linear_algebra_split.ipynb')