import nbformat
import regex as re

# --- Notebook Manipulation Functions ---

def split_markdown_cells(notebook_path, output_path, start_header=None, stop_header=None):
    """
    Splits markdown cells in a Jupyter notebook based on headers.

    Args:
        notebook_path (str): Path to the input notebook.
        output_path (str): Path to save the modified notebook.
        start_header (str, optional): Header to start processing (inclusive). Defaults to None (start from the beginning).
        stop_header (str, optional): Header to stop processing (exclusive). Defaults to None (process until the end).
    """
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    new_cells = []
    start_index = None
    stop_index = None

    # Find start and stop indices based on headers
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown':
            if start_header is not None and start_index is None and start_header in cell.source:
                start_index = i
            if stop_header is not None and stop_index is None and stop_header in cell.source:
                stop_index = i
                #break  # Stop searching after finding stop_header

    # Process cells within the specified range
    for i, cell in enumerate(nb.cells):
        if start_index is not None and i < start_index:
            new_cells.append(cell)
            continue
        if stop_index is not None and i >= stop_index:
            new_cells.append(cell)
            continue

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

# #Template
notebook_path = 'Machine Learning/machine_learning.ipynb'
output_path = 'Machine Learning/machine_learning.ipynb'
start_header = '## Machine Learning Workflow'
stop_header = '# END'

split_markdown_cells(notebook_path, output_path, start_header=start_header, stop_header=stop_header)

##############################################################################################################################################################################

def modify_headers_in_section(notebook_path, output_path, add_or_subtract, start_heading=None, end_heading=None):
    """
    Modifies headers within a specific section of a Jupyter Notebook.
    Allows the user to specify a start and stop header, and whether to add or subtract '#' symbols.

    Args:
        notebook_path (str): Path to the input Jupyter Notebook.
        output_path (str): Path to save the modified notebook.
        add_or_subtract (str): '+' to add '#' symbols, '-' to subtract '#' symbols.
        start_heading (str, optional): The header text to start modifying from (inclusive). Defaults to None.
        end_heading (str, optional): The header text to stop modifying at (exclusive). Defaults to None.
    """

    if add_or_subtract not in ['+', '-']:
        print("Invalid input for add_or_subtract. Please use '+' to add or '-' to subtract.")
        return

    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
    except FileNotFoundError:
        print(f"Error: Notebook file not found at {notebook_path}")
        return
    except Exception as e:
        print(f"An error occurred while reading the notebook: {e}")
        return

    modify = False
    if start_heading is None:
        modify = True

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            lines = cell.source.split('\n')

            if start_heading is not None and any(start_heading in line for line in lines):
                modify = True
            if end_heading is not None and any(end_heading in line for line in lines):
                modify = False

            if modify:
                new_lines = []
                for line in lines:
                    if line.startswith('#'):
                        if add_or_subtract == '+':
                            line = '#' + line  # Add a '#'
                        elif add_or_subtract == '-':
                            if line.startswith('# '):
                                line = line[2:]  # Remove '# '
                            elif line.startswith('#'):
                                line = line[1:]
                    new_lines.append(line)
                cell.source = '\n'.join(new_lines)

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Notebook successfully modified and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while writing the notebook: {e}")

# Template:
# notebook_path = 'Machine Learning/machine_learning.ipynb'
# output_path = 'Machine Learning/machine_learning_2.ipynb'
# add_or_subtract = '+'
# start_heading = '# Recommender Systems'
# end_heading = None

# modify_headers_in_section(notebook_path, output_path, add_or_subtract, start_heading, end_heading)

##############################################################################################################################################################################

# --- Utility Functions ---

def math_format(x):
    return re.sub(r'\\\(\s*(.*?)\s*\\\)', r'$ \1 $', x)
##############################################################################################################################################################################
