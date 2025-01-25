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

# Example usage
# split_markdown_cells('practice.ipynb', 'practice_split.ipynb')
##########################################################################################################

def modify_headers(notebook_path, output_path):
    """
    Iterates through the headers in a Jupyter Notebook and modifies them. 
    Changes '#' to '##' and '##' to '###'.

    Args:
        notebook_path (str): The path to the input Jupyter Notebook file.
        output_path (str): The path where the modified notebook should be saved.
    """
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            lines = cell.source.split('\n')
            new_lines = []
            for line in lines:
                if line.startswith('# '):  # Change '#' to '##'
                    line = '#' + line 
                elif line.startswith('## '):  # Change '##' to '###'
                    line = '#' + line
                new_lines.append(line)
            cell.source = '\n'.join(new_lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Example usage
# notebook_path = 'my_notebook.ipynb'
# output_path = 'modified_notebook.ipynb'
# modify_headers(notebook_path, output_path)
##########################################################################################################

def modify_headers_in_section(notebook_path, output_path, start_heading, end_heading):
    """
    Modifies headers within a specific section of a Jupyter Notebook. 
    Changes '#' to '##' and '##' to '###'.

    Args:
        notebook_path (str): Path to the input Jupyter Notebook.
        output_path (str): Path to save the modified notebook.
        start_heading (str): The header text that marks the beginning of the section.
        end_heading (str): The header text that marks the end of the section.
    """

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    modify = False
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            lines = cell.source.split('\n')
            if any(start_heading in line for line in lines):  # Start modifying
                modify = True
            if any(end_heading in line for line in lines):  # Stop modifying
                modify = False

            if modify:
                new_lines = []
                for line in lines:
                    if line.startswith('# '):
                        line = '#' + line
                    elif line.startswith('## '):
                        line = '#' + line
                    new_lines.append(line)
                cell.source = '\n'.join(new_lines)

    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

# Example usage:
# notebook_path = 'my_notebook.ipynb'
# output_path = 'modified_notebook.ipynb'
# start_heading = '## Data Preprocessing'  
# end_heading = '## Model Evaluation'
# modify_headers_in_section(notebook_path, output_path, start_heading, end_heading)
##########################################################################################################

def math_format(x):
    return re.sub(r'\\\(\s*(.*?)\s*\\\)', r'$ \1 $', x)

