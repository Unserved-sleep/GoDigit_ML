import csv
with open("C:\\Users\\Admin\\miniconda3\\pkgs\\numpy-base-2.4.1-py313h1e017a8_0\\Lib\\site-packages\\numpy\\_core\\tests\data\\umath-validation-set-tan.csv") as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')