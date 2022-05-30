import pandas as pd
from pyarrow import feather

def main():
    chunk_iter = pd.read_csv("data/train_data.csv.zip", chunksize=100)
    for i, chunk in enumerate(chunk_iter):
        first_customer_id = "0000099d6bd597052cdcda90ffabf56573fe9d7c79be5fbac11a8ed792feb62a"
        customer = chunk[chunk["customer_ID"] == first_customer_id]
        print(customer)
        print(customer.columns)
        break
        #df = chunk.groupby("customer_ID").count()
        #print(df)
        #break
    return

if __name__ == "__main__":
    main()

