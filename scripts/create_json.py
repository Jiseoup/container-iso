"""Create ISO Container JSON file.

This script preprocesses CSV files to generate a JSON-formatted ISO Container file.
The generated JSON file is utilized in package functions to load and use its values.
"""
import json
from pathlib import Path

import pandas as pd

# Configure path.
base_dir = Path(__file__).resolve().parent
json_path = base_dir / '../iso_container/datasets.json'
code_path = base_dir / '../datasets/data/iso-container-codes.csv'
group_path = base_dir / '../datasets/data/iso-container-groups.csv'

# Read CSV files.
code_data = pd.read_csv(code_path)
group_data = pd.read_csv(group_path)

# Merging code data and group data.
merged_data = pd.merge(
    code_data,
    group_data.rename(
        columns={
            'code': 'group',
            'description': 'group_description'
        }
    ),
    on='group',
    how='left'
)

# Converting as dictionary type.
data_dict = {
    row['code']: {
        'class': row['group_description'].upper(),
        'type': row['description'].upper(),
        'length': row['length'],
        'height': row['height'],
    }
    for _, row in merged_data.iterrows()
}

# Save as JSON file.
with open(json_path, 'w') as file:
    json.dump(data_dict, file, indent=4)

print('Successfully create JSON file.')
