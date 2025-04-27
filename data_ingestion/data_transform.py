import pandas as pd
from langchain_core.documents import Document



class data_converter:

    def __init__(self):
        print("data convert has been init...")
        self.product_data = pd.read_csv("/Users/pandhari/Customer_Support_System/data/amazon_product_review.csv")
        # print(self.product_data.head())

    def data_transformation(self):
        required_cols = self.product_data.columns[1:]
        # print(required_cols)

        product_list = []

        for index , row in self.product_data.iterrows():
            object = {
                "product_name": row['product_title'] , 
                "product_rating": row['rating'] , 
                "product_summary": row['summary'] , 
                "product_review": row['review']
            }

            product_list.append(object)
        
        # print("************ Below is my product list ***********")
        # print(product_list[:5])

        docs = []


        for entry in product_list:
            metadata = {"product_name":entry["product_name"] , "product_rating": entry["product_rating"] , "product_summary": entry["product_summary"]}
            doc = Document(page_content = entry["product_review"] , metadata = metadata)
            docs.append(doc)
        
        return docs
    




if __name__ == "__main__":
    data_conv = data_converter()
    data_conv.data_transformation()
