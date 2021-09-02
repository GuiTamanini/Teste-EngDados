-- Query 1 - Contagem total de linhas de SalesOrderDetail com mais de 3 linhas de detalhes
Select count(1) as number_rows from (
	Select SalesOrderID
	From `teste-roxpartner.bicyclesales_roxpartner.Sales_SalesOrderDetail` 
	Group By SalesOrderID
	having count(SalesOrderDetailID) > 3
) t

-- Query 2 - Join entre as tabelas [Sales.SalesOrderDetail], [Sales.SpecialOfferProduct] e [Production.Product] retornando os 3 produtos mais vendidos
Select PROD.Name
From `teste-roxpartner.bicyclesales_roxpartner.Sales_SalesOrderDetail` as SOD
Inner Join `teste-roxpartner.bicyclesales_roxpartner.Production_Product` as PROD on PROD.ProductID = SOD.ProductID
Inner Join `teste-roxpartner.bicyclesales_roxpartner.Sales_SpecialOfferProduct` as SOP on SOP.ProductID = SOD.ProductID
Group by PROD.DaysToManufacture, PROD.Name
Order by sum(cast(OrderQty as int)) desc
LIMIT 3

-- Query 3 - Join entre as tabelas [Person.Person], [Sales.Consumer] e [SalesOrderHeader] para obter nome de clientes e número de pedidos
BEGIN
    CREATE TEMP TABLE TotalOrdersTemp
    AS
    Select CustomerID, count(customerID) as num_orders, sum(totaldue) as tot_price
	From `teste-roxpartner.bicyclesales_roxpartner.Sales_SalesOrderHeader`
	Group by customerID
;
Select C.CustomerID
	   ,P.FirstName
	   ,P.MiddleName
	   ,P.LastName
	   ,T.num_orders
	   ,T.tot_price
From `teste-roxpartner.bicyclesales_roxpartner.Person_Person` as P
Inner Join `teste-roxpartner.bicyclesales_roxpartner.Sales_Customer` as C on C.PersonID = P.BusinessEntityID
Inner Join `teste-roxpartner.bicyclesales_roxpartner.Sales_SalesOrderHeader` as SOH on SOH.CustomerID = C.CustomerID
Inner Join TotalOrdersTemp as T on T.CustomerID = C.CustomerID
Order By T.num_orders, T.tot_price desc
;END

-- Query 4 - Join entre as tabelas [Sales.SalesOrderDetail], [SalesOrderHeader] e [Production.Product] para obter o total de produtos por ProductID e OrderDate
Select SOD.ProductID, sum(cast(OrderQty as int)) as Tot_Prod_byID_Date
From `teste-roxpartner.bicyclesales_roxpartner.Sales_SalesOrderDetail` as SOD
Inner Join `teste-roxpartner.bicyclesales_roxpartner.Sales_SalesOrderHeader` as SOH on SOH.SalesOrderID = SOD.SalesOrderID
Inner Join `teste-roxpartner.bicyclesales_roxpartner.Production_Product` as PROD on PROD.ProductID = SOD.ProductID
Group by SOD.ProductID, SOH.OrderDate

-- Query 5 - Retornar campos SalesOrderID, OrderDate e TotalDue com data de setembro/2011 e valor maior que 1000
Select SalesOrderID, OrderDate, TotalDue 
From `teste-roxpartner.bicyclesales_roxpartner.Sales_SalesOrderHeader`
Where OrderDate between '2011-09-01' and '2011-09-30' 
	And TotalDue > 1000
Order by TotalDue desc