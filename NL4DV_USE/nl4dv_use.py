from nl4dv import NL4DV

nl4dv_instance = NL4DV(data_url="housing.csv")
query = "create a barchart showing average lot area across foundation type."
resp = nl4dv_instance.analyze_query(query)

print(resp)

keyword_list = []

keyword_dict = {
    "relationship": [("correlation", None)],
}