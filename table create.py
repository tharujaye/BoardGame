# Define the table data
table_data = [[i + 1 for i in range(20)], [(i + 1) * 10 for i in range(20)]]

# Define the table size
num_rows = len(table_data)
num_cols = len(table_data[0])

# Define the border characters
border_horiz = "─"
border_vert = "│"
border_corner = "┼"

# Print the table
for i in range(num_rows):
    if i == 0:
        # Print the top border
        print(border_corner + border_horiz * (num_cols * 5 - 1) + border_corner)
    for j in range(num_cols):
        # Print the cell value with borders
        cell = "{:^5}".format(table_data[i][j])
        if j == 0:
            print(border_vert + cell + border_vert, end="")
        elif j == num_cols - 1:
            print(cell + border_vert)
        else:
            print(cell + border_vert, end="")
    if i == num_rows - 1:
        # Print the bottom border
        print(border_corner + border_horiz * (num_cols * 5 - 1) + border_corner)
