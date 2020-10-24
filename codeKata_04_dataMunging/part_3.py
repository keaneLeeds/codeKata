import requests
import os
import re
import pandas as pd


def set_pandas_options_shared():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)


def get_file_shared(url):
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


def clean_file_football(filename):
    new_filename = ''.join(['cleaned_', filename])
    with open(filename, 'r') as inp, open(new_filename, 'w') as output:
        for line in inp:
            new_line = re.sub('[-]', '', line)
            if len(new_line.strip()) > 0:
                output.write(new_line)

    return new_filename


def read_file_shared(filename):
    file = pd.read_csv(filename, delim_whitespace=True)
    return file


def remove_character_from_column(df, column_number, character):
    df[df.columns.values[column_number]] = df[df.columns.values[column_number]].str.strip(character)
    return df


def to_numeric_column(df, column_number):
    df[df.columns.values[column_number]] = pd.to_numeric(df[df.columns.values[column_number]])
    return df


def clean_data_weather(df, column_number):
    a = remove_character_from_column(df, column_number, '*')
    df = to_numeric_column(a, column_number)
    return df


def aggregate_data_weather(df):
    df['diff'] = df[df.columns.values[1]] - df[df.columns.values[2]]
    return df


def aggregate_data_football(df):
    # a = to_numeric_column(df, )
    df['diff'] = abs(pd.to_numeric(df['F']) - pd.to_numeric(df['A']))
    return df


def describe_data_shared(df, column1, column2):
    print('Length: ', len(df))
    print('Shape: ', df.shape)
    print('Head: ', list(df.columns.values))
    print()
    print('Describe')
    print(df.describe())
    print()
    print(df.columns.values[column1])
    print(df[df.columns.values[column1]])
    print()
    print(df.columns.values[column2])
    print(df[df.columns.values[column2]])
    print()
    print('diff_column')
    print(df['diff'])
    print()


def answer_question_shared(df, description):
    answer = df['diff'].min()
    print(description)
    print(df.loc[df['diff'] == answer])
    print()


def run_all():
    set_pandas_options_shared()

    weather = get_file_shared('http://codekata.com/data/04/weather.dat')
    weather_file = read_file_shared(weather)
    data_frame_weather = clean_data_weather(weather_file, 1)
    data_frame_weather = clean_data_weather(data_frame_weather, 2)
    data_frame_weather = aggregate_data_weather(data_frame_weather)
    describe_data_shared(data_frame_weather, 1, 2)
    answer_question_shared(data_frame_weather, 'Row with minimum difference in min and max temperature')

    football = get_file_shared('http://codekata.com/data/04/football.dat')
    football_cleaned = clean_file_football(football)
    football_file = read_file_shared(football_cleaned)
    data_frame_football = aggregate_data_football(football_file)
    describe_data_shared(data_frame_football, 5, 6)
    answer_question_shared(data_frame_football, 'Row with minimum difference between for and against goals')


if __name__ == '__main__':
    run_all()
