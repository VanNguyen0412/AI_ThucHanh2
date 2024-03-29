import pandas as pd

# Replace 'file_path.tsv' with the path to your TSV file
file_path = '04_gap-merged.tsv'

# Read the TSV file using pandas
df = pd.read_csv(file_path, sep='\t')


def cau1():
    print("Câu 1: ")
    print(df.head())


# Display the first 5 lines of the DataFrame


def cau2_3():
    num_rows, num_columns = df.shape
    print("Câu 2: ")
    print("Number of rows:", num_rows)
    print("Number of columns:", num_columns)
    # Câu 3
    column_names = df.columns
    print("Câu 3:")
    print("Column names:")
    for column_name in column_names:
        print(column_name)


def cau4_5():
    print("Câu 4: ")
    column_names_type = type(df.columns)

    print("Type of column names:", column_names_type)
    # Câu 5
    print("Câu 5: ")
    # Get the 'country' column and save it to its own variable
    country_column = df['country']

    # Show the first 5 observations of the 'country' column
    print(country_column.head())


def cau6_7():
    print("Câu 6: ")
    # Get the 'country' column
    country_column = df['country']

    # Show the last 5 observations of the 'country' column
    print(country_column.tail())
    # Câu 7
    print("Câu 7: ")
    # Select 'country', 'continent', and 'year' columns
    selected_columns = df[['country', 'continent', 'year']]

    # Show the first 5 observations of selected columns
    print("First 5 observations:")
    print(selected_columns.head())

    # Show the last 5 observations of selected columns
    print("\nLast 5 observations:")
    print(selected_columns.tail())


def cau8_9():
    print("Câu 8: ")
    # Get the first row
    first_row = df.iloc[0]

    # Get the 100th row
    hundredth_row = df.iloc[99]
    print("Dòng đầu tiên của file tsv: ")
    print(first_row)
    print("\nDòng thứ 100 của file tsv: ")
    print(hundredth_row)

    # Câu 9:
    print("Câu 9: ")
    # Get the first column
    first_column = df.iloc[:, 0]

    # Get the first and last column
    first_and_last_column = df.iloc[:, [0, -1]]
    print("Cột đầu tiên bằng cách sử dụng chỉ số nguyên: ")
    print(first_column)
    print("\nCột đầu tiên và cuối cùng bằng cách chuyển chỉ số nguyên.: ")
    print(first_and_last_column)


def cau10_11():
    print("Câu 10: ")
    print("Dòng cuối cùng với .loc")
    # Get the last row with .loc
    last_row = df.loc[df.index[-1]]
    print(last_row)
    print("Kết quả chính xác!!!!!!")

    #Câu 11
    print("Câu 11: ")

    print("Dòng đầu tiên, dòng thứ 100 và dòng thứ 1000 sử dụng với .iloc")
    # Select the first, 100th, and 1000th rows using .iloc
    rows_iloc = df.iloc[[0, 99, 999]]
    print(rows_iloc)

    print("\nDòng đầu tiên, dòng thứ 100 và dòng thứ 1000 sử dụng với .iloc")
    # Select the first, 100th, and 1000th rows using .loc
    rows_loc = df.loc[[df.index[0], df.index[99], df.index[999]]]
    print(rows_loc)


def cau12_13():
    print("Câu 12: ")
    print('Quốc gia thứ 43 bằng .iloc')
    # Get the 43rd country using .iloc
    country_iloc = df.iloc[42]['country']
    print(country_iloc)

    print('Quốc gia thứ 43 bằng .loc')
    # Get the 43rd country using .loc
    country_loc = df.loc[df.index[42], 'country']
    print(country_loc)
    #Câu 13
    print("\nCâu 13: ")
    print('Hàng thứ nhất, hàng thứ 100, hàng thứ 1000 của cột thứ nhất, thứ 4, thứ 6')
    # Get the first, 100th, and 1000th rows from the first, 4th, and 6th columns
    subset_data = df.iloc[[0, 99, 999], [0, 3, 5]]
    print(subset_data)


def cau14_15():
    print("Câu 14: ")
    print('10 dòng dữ liệu đầu tiên')
    first_10_rows = df.head(10)
    print(first_10_rows)
    print("\nCâu 15: ")
    print("Tuổi thọ trung bình của từng năm")
    average_life_expectation_per_year = df.groupby('year')['lifeExp'].mean()
    print(average_life_expectation_per_year)


def cau16_17():
    print("Câu 16: ")
    print("Sử dụng phương pháp tập con cho nghiệm cho câu 15")
    average_life_expectation_per_year_subsetting = df['lifeExp'].groupby(df['year']).mean()
    print(average_life_expectation_per_year_subsetting)

    print("Câu 17: ")
    print("Tạo một chuỗi có chỉ số 0 cho 'banana' và chỉ mục 1 cho '42'")
    series_17 = pd.Series(['banana', '42'], index=[0, 1])
    print(series_17)


def cau18_19():
    print("Câu 18: ")
    print("Thay đổi chỉ mục ‘Person’ thành ‘Wes MCKinney’ và chỉ mục ‘Ai’ cho ‘Creator of Pandas’")
    series_18 = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])
    print(series_18)

    print("Câu 19: ")
    data = {
        'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-04-16', '1937-10-16'],
        'Age': [37, 61]
    }
    index = ['Franklin', 'Gosset']

    pandas_dict = pd.DataFrame(data, index=index)
    print(pandas_dict)


if __name__ == "__main__":
    cau18_19()
