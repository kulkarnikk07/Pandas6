# Pandas6

# 1 Problem 1 : Delete Duplicate Emails ( https://leetcode.com/problems/delete-duplicate-emails/)

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby(['email'])['id'].transform('min')
    remove_id = person[person['id'] != min_id]
    person.drop(remove_id.index, inplace = True)

# 2 Problem 2 : The Number of Rich Customers ( https://leetcode.com/problems/the-number-of-rich-customers/ )

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
	df = store[store['amount']>500]
	richCount = df['customer_id'].nunique()
	return pd.DataFrame([richCount], columns = ['rich_count'])