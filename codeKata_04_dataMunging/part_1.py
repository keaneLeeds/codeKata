import requests
import os
import pandas as pd


def set_pandas_options():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)


def get_file():
    url = 'http://codekata.com/data/04/weather.dat'
    filename = url.split('/')[-1]
    if os.path.isfile(filename):
        print('Already downloaded')
        return filename

    r = requests.get(url)
    r.raise_for_status()  # check that the request was successful

    with open(filename, 'wb') as output_file:
        output_file.write(r.content)

    print('Download complete')
    return filename


def read_file(filename):
    file = pd.read_csv(filename, delim_whitespace=True)
    return file


def clean_data(data_frame, column_number):
    data_frame[data_frame.columns.values[column_number]] = \
        pd.to_numeric(data_frame[data_frame.columns.values[column_number]].str.strip('*'))
    return data_frame


def aggregate_data(data_frame):
    data_frame['diff'] = data_frame[data_frame.columns.values[1]] - data_frame[data_frame.columns.values[2]]
    return data_frame


def describe_data(data_frame):
    print('Length: ', len(data_frame))
    print('Shape: ', data_frame.shape)
    print('Head: ', list(data_frame.columns.values))
    print()
    print('Describe')
    print(data_frame.describe())
    print()
    print('max_column')
    print(data_frame[data_frame.columns.values[1]])
    print()
    print('min_column')
    print(data_frame[data_frame.columns.values[2]])
    print()
    print('diff_column')
    print(data_frame['diff'])
    print()


def answer_question(data_frame):
    answer = data_frame['diff'].min()
    print('Row with minimum difference in min and max temperature:')
    print(data_frame.loc[data_frame['diff'] == answer])


def run_all():
    set_pandas_options()
    f = get_file()
    fi = read_file(f)
    df = clean_data(fi, 1)
    df = clean_data(df, 2)
    df = aggregate_data(df)
    describe_data(fi)
    answer_question(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_all()
