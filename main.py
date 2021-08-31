from google.cloud import bigquery

def csv_to_bigquery(event, context):

    client = bigquery.Client()
    file_name = event['name']
    table_name = file_name[:file_name.index('.csv')].replace('.','_')
    table_id = 'teste-roxpartner.bicyclesales_roxpartner.' + table_name

    job_config = []
    
    #Verifys table name for setting the correct table schema
    if(table_name=='Person_Person'):        
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("BusinessEntityID", "INT64"),
                bigquery.SchemaField("PersonType", "STRING"),
                bigquery.SchemaField("NameStyle", "INT64"),
                bigquery.SchemaField("Title", "STRING"),
                bigquery.SchemaField("FirstName", "STRING"),
                bigquery.SchemaField("MiddleName", "STRING"),
                bigquery.SchemaField("LastName", "STRING"),
                bigquery.SchemaField("Suffix", "STRING"),
                bigquery.SchemaField("EmailPromotion", "INT64"),
                bigquery.SchemaField("AdditionalContatctInfo", "STRING"),
                bigquery.SchemaField("Demographics", "STRING"),
                bigquery.SchemaField("rowguid", "STRING"),
                bigquery.SchemaField("ModifiedDate", "DATETIME"),
            ],
            field_delimiter=";",
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            skip_leading_rows=1)
    elif(table_name=="Production_Product"):
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("ProductID", "INT64"),
                bigquery.SchemaField("Name", "STRING"),
                bigquery.SchemaField("ProductNumber", "STRING"),
                bigquery.SchemaField("MakeFlag", "INT64"),
                bigquery.SchemaField("FinishedGoodsFlag", "INT64"),
                bigquery.SchemaField("Color", "STRING"),
                bigquery.SchemaField("SafetyStockLevel", "INT64"),
                bigquery.SchemaField("ReorderPoint", "INT64"),
                bigquery.SchemaField("StandardCost", "FLOAT64"),
                bigquery.SchemaField("ListPrice", "FLOAT64"),
                bigquery.SchemaField("Size", "STRING"),
                bigquery.SchemaField("SizeUnitMeasureCode", "STRING"),
                bigquery.SchemaField("WeightUnitMeasureCode", "STRING"),
                bigquery.SchemaField("Weight", "FLOAT64"),
                bigquery.SchemaField("DaysToManufacture", "INT64"),
                bigquery.SchemaField("ProductLine", "STRING"),
                bigquery.SchemaField("Class", "STRING"),
                bigquery.SchemaField("Style", "STRING"),
                bigquery.SchemaField("ProductSubCategoryID", "INT64"),
                bigquery.SchemaField("ProductModelID", "INT64"),
                bigquery.SchemaField("SellStartDate", "DATETIME"),
                bigquery.SchemaField("SellEndDate", "DATETIME"),
                bigquery.SchemaField("DiscontinuedDate", "DATETIME"),
                bigquery.SchemaField("rowguid", "STRING"),
                bigquery.SchemaField("ModifiedDate", "DATETIME"),
            ],
            field_delimiter=";",
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            skip_leading_rows=1)
    elif(table_name=="Sales_Customer"):
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("CustomerID", "INT64"),
                bigquery.SchemaField("PersonID", "INT64"),
                bigquery.SchemaField("StoreID", "INT64"),
                bigquery.SchemaField("TerritoryID", "INT64"),
                bigquery.SchemaField("AccountNumber", "STRING"),
                bigquery.SchemaField("rowguid", "STRING"),
                bigquery.SchemaField("ModifiedDate", "DATETIME"),
            ],
            field_delimiter=";",
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            skip_leading_rows=1)
    elif(table_name=="Sales_SalesOrderDetail"):
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("SalesOrderID", "INT64"),
                bigquery.SchemaField("SalesOrderDetailID", "INT64"),
                bigquery.SchemaField("CarrierTrackingNumber", "STRING"),
                bigquery.SchemaField("OrderQty", "INT64"),
                bigquery.SchemaField("ProductID", "INT64"),
                bigquery.SchemaField("SpecialOfferID", "INT64"),
                bigquery.SchemaField("UnitPrice", "FLOAT64"),
                bigquery.SchemaField("UnitPriceDiscount", "FLOAT64"),
                bigquery.SchemaField("LineTotal", "FLOAT64"),
                bigquery.SchemaField("rowguid", "STRING"),
                bigquery.SchemaField("ModifiedDate", "DATETIME"),
            ],
            field_delimiter=";",
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            skip_leading_rows=1)
    elif(table_name=="Sales_SalesOrderHeader"):
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("SalesOrderID", "INT64"),
                bigquery.SchemaField("RevisionNumber", "INT64"),
                bigquery.SchemaField("OrderDate", "DATETIME"),
                bigquery.SchemaField("DueDate", "DATETIME"),
                bigquery.SchemaField("ShipDate", "DATETIME"),
                bigquery.SchemaField("Status", "INT64"),
                bigquery.SchemaField("OnlineOrderFlag", "INT64"),
                bigquery.SchemaField("SalesOrderNumber", "STRING"),
                bigquery.SchemaField("PurchaseOrderNumber", "STRING"),
                bigquery.SchemaField("AccountNumber", "STRING"),
                bigquery.SchemaField("CustomerID", "INT64"),
                bigquery.SchemaField("SalesPersonID", "INT64"),
                bigquery.SchemaField("TerritoryID", "INT64"),
                bigquery.SchemaField("BillToAddressID", "INT64"),
                bigquery.SchemaField("ShipToAddressID", "INT64"),
                bigquery.SchemaField("ShipMethodID", "INT64"),
                bigquery.SchemaField("CreditCardID", "INT64"),
                bigquery.SchemaField("CreditCardApprovalCode", "STRING"),
                bigquery.SchemaField("CurrencyRateID", "INT64"),
                bigquery.SchemaField("SubTotal", "FLOAT64"),
                bigquery.SchemaField("TaxAmt", "FLOAT64"),
                bigquery.SchemaField("Freight", "FLOAT64"),
                bigquery.SchemaField("TotalDue", "FLOAT64"),
                bigquery.SchemaField("Comment", "STRING"),
                bigquery.SchemaField("rowguid", "STRING"),
                bigquery.SchemaField("ModifiedDate", "DATETIME"),
            ],
            field_delimiter=";",
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            skip_leading_rows=1)
    elif(table_name=="Sales_SpecialOfferProduct"):
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("SpecialOfferID", "INT64"),
                bigquery.SchemaField("ProductID", "INT64"),
                bigquery.SchemaField("rowguid", "STRING"),
                bigquery.SchemaField("ModifiedDate", "DATETIME"),
            ],
            field_delimiter=";",
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            skip_leading_rows=1)       
    job_config.null_marker = 'NULL'
    
    uri = 'gs://byciclesales-roxpartner/' + event['name']

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )

    load_job.result()

    destination_table = client.get_table(table_id)
    print("Uploaded {} rows to {}.".format(destination_table.num_rows, table_name))