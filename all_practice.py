import numpy as np
import pandas as pd

# Create the DataFrame
# columns are title, author, genre 
library = pd.DataFrame([
    ['To Kill a Mockingbird', 'Harper Lee', 'Fiction'],
    ['1984', 'George Orwell', 'Dystopian'],
    ['Moby Dick', 'Herman Melville', 'Adventure'],
    ['Pride and Prejudice', 'Jane Austen', 'Romance'],
    ['The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction'],
    ['Brave New World', 'Aldous Huxley', 'Dystopian']
    ],
    columns=['title', 'author', 'genre']
)

print(library)
subset = library.iloc[:3, :2]
print(f'this is subset {subset}')