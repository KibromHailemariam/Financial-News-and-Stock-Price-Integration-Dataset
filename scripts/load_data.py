# import pandas as pd
# import os

# def load_and_clean_data(data_folder):
#     all_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
#     df_list = [pd.read_csv(os.path.join(data_folder, file)) for file in all_files]
#     combined_df = pd.concat(df_list, ignore_index=True)
#     combined_df['date'] = pd.to_datetime(combined_df['date'], errors='coerce')
#     return combined_df.dropna()

# data = load_and_clean_data('week_1/data')
# data.to_csv('..data/processed_data.csv', index=False)