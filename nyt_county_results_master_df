df_all_states_final = pd.DataFrame()

for index, c in enumerate(csvs_list):
    df = pd.read_csv(csvs_list[index])
    df_all_states_final = df_all_states_final.append(df)

df_all_states_final.to_csv('df_all_states_final.csv')