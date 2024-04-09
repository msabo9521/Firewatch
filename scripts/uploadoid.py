import pandas as pd
from core.models import ObjectID

input_file = "scripts/sysoid.csv"
df = pd.read_csv(input_file)

def run():
    try:
        for index, row in df.iterrows():
            if ObjectID.objects.filter(oid=str(row['oid'])):
                print(f"{str(row['oid'])} arlready exists")
            else:
                p = ObjectID(oid=str(row['oid']), vendor=row['vendor'], type=row['type'], model=row['model'])
                p.save()
    except Exception as e:
        print(e)
