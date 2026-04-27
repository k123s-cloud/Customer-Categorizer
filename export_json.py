import pandas as pd

# CSV read karo
df = pd.read_csv("notebooks/marketing_campaign.csv")

# JSON me convert karo
df.to_json("notebooks/marketing_campaign.json", orient="records", indent=4)

print("JSON file created successfully 🚀")

