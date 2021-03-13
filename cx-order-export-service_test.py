import json

jsonobj = {
"s3_bucket_1010": "dev-sap-files-for-data-api",
"filename_prefix_1010":"LA_",
"pending_foldername_1010":"outcome_data/1010/Orders/Pending/"
"s3_bucket_2040":"monolit"
"filename_prefix_2040":"RU_",
"pending_foldername_2040":"outcome_data/2040/Orders/Pending/"
}

ordernumber = "1010"

print(jsonobj[ordernumber + '_filename_prefix'])