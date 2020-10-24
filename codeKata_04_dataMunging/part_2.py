import requests
import os
import re
import pandas as pd


def set_pandas_options():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)


def get_file(url):
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


def clean_file(filename):
    new_filename = ''.join(['cleaned_', filename])
    with open(filename, 'r') as inp, open(new_filename, 'w') as output:
        for line in inp:
            new_line = re.sub('[-]', '', line)
            if len(new_line.strip()) > 0:
                output.write(new_line)

    return new_filename


def read_file(filename):
    file = pd.read_csv(filename, delim_whitespace=True)
    return file


def aggregate_data(df):
    df['diff'] = abs(pd.to_numeric(df['F']) - pd.to_numeric(df['A']))
    return df


def describe_data(df):
    print('Length: ', len(df))
    print('Shape: ', df.shape)
    print('Head: ', list(df.columns.values))
    print()
    print('Describe')
    print(df.describe())
    print()
    print('For')
    print(df['F'])
    print()
    print('Against')
    print(df['A'])
    print()
    print('diff_column')
    print(df['diff'])
    print()


def answer_question(df):
    answer = df['diff'].min()
    print('Row with minimum difference in min and max temperature:')
    print(df.loc[df['diff'] == answer])


def run_all():
    set_pandas_options()
    f = get_file('http://codekata.com/data/04/football.dat')
    n_f = clean_file(f)
    fi = read_file(n_f)
    data_frame = aggregate_data(fi)
    describe_data(data_frame)
    answer_question(data_frame)


if __name__ == '__main__':
    run_all()
