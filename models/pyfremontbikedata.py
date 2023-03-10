import pandas as pd
from sodapy import Socrata

client = Socrata("data.seattle.gov",None)

# Results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("65db-xm6k")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

return results_df