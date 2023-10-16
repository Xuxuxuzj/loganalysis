'''
import pandas as pd

def group_similar_errors(filtered_errors_df):
    grouped_errors = {}

    for _, row in filtered_errors_df.iterrows():
        error_text = row['Error']
        count = row['Count']

        prefix = error_text[:5]  # Extract the first 5 characters as the prefix

        if prefix in grouped_errors:
            # If the prefix is already in the dictionary, add up the counts
            grouped_errors[prefix]['Count'] += count
        else:
            # Otherwise, create a new entry for that prefix in the dictionary
            grouped_errors[prefix] = {'Texts': [error_text], 'Count': count}

    grouped_error_list = [{'Error Group': prefix, 'Texts': '\n'.join(data['Texts']), 'Count': data['Count']} for prefix, data in grouped_errors.items()]

    grouped_error_df = pd.DataFrame(grouped_error_list)

    return grouped_error_df

filtered_error_df = pd.read_csv('filtered_error_df.csv')

grouped_error_df = group_similar_errors(filtered_error_df)
grouped_error_df.to_csv('grouped_errors.csv', index=False)
'''
import pandas as pd

def group_similar_errors(filtered_errors_df):
    grouped_errors = {}

    for _, row in filtered_errors_df.iterrows():
        error_text = row['Error']
        count = row['Count']

        # Check if error_text is a string
        if isinstance(error_text, str):
            prefix = error_text[:5]  # Extract the first 5 characters as the prefix

            if prefix in grouped_errors:
                # If the prefix is already in the dictionary, append the error text and update the count
                grouped_errors[prefix]['Texts'].append(error_text)
                grouped_errors[prefix]['Count'] += count
            else:
                # Otherwise, create a new entry for that prefix in the dictionary
                grouped_errors[prefix] = {'Texts': [error_text], 'Count': count}

    grouped_error_list = [{'Error Group': prefix, 'Texts': '\n'.join(data['Texts']), 'Count': data['Count']} for prefix, data in grouped_errors.items()]

    grouped_error_df = pd.DataFrame(grouped_error_list)

    return grouped_error_df

filtered_error_df = pd.read_csv('filtered_error.csv')

grouped_error_df = group_similar_errors(filtered_error_df)

grouped_error_df.to_csv('grouped_errors.csv', index=False)
