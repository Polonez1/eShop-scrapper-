import pandas as pd
import json


def read_data(json_file: str):
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    processed_data = []

    for item in data:
        product_data = {
            "name": item["name"],
            "url": item["url"],
            "price_eur": item["price_eur"],
            "price_cnt": item["price_cnt"],
            "discount": item["discount"],
        }
        categories_data = item.get("categories", {})
        product_data.update(categories_data)

        processed_data.append(product_data)

    return pd.DataFrame(processed_data)


def data_to_xlsx():
    df = read_data(json_file="_output_discount.json")
    df.to_excel("_varle_discount.xlsx")


if "__main__" == __name__:
    data_to_xlsx()
