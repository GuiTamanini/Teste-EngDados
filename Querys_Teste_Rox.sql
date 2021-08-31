-- Query 1 - Contagem total de linhas de SalesOrderDetail com mais de 3 linhas de detalhes
Select count(1) as number_rows from (
	Select SalesOrderID
	From [Sales.SalesOrderDetail] 
	Group By SalesOrderID
	having count(SalesOrderDetailID) > 3
) t


-- Query 2 - Join entre as tabelas [Sales.SalesOrderDetail], [Sales.SpecialOfferProduct] e [Production.Product] retornando os 3 produtos mais vendidos
Select Top (3) PROD.Name
From [Sales.SalesOrderDetail] as SOD
Inner Join [Production.Product] as PROD on PROD.ProductID = SOD.ProductID
Inner Join [Sales.SpecialOfferProduct] as SOP on SOP.ProductID = SOD.ProductID
Group by PROD.DaysToManufacture, PROD.Name
Order by sum(cast(OrderQty as int)) desc

-- Query 3 - Join entre as tabelas [Person.Person], [Sales.Consumer] e [SalesOrderHeader] para obter nome de clientes e número de pedidos
Select C.CustomerID 
      ,(Select count(CustomerID) from [Sales.SalesOrderHeader] as H where H.CustomerID = C.CustomerID group by CustomerID) as num_orders
	  ,(Select sum(Cast(H.TotalDue as Numeric(10,2))) from [Sales.SalesOrderHeader] as H where H.CustomerID = C.CustomerID group by CustomerID) as tot_price
into #TotalOrdersTemp 
From [Sales.Customer] as C

Select C.CustomerID
	   ,P.FirstName
	   ,P.MiddleName
	   ,P.LastName
	   ,T.num_orders
	   ,T.tot_price
From [Person.Person] as P
Inner Join [Sales.Customer] as C on C.PersonID = P.BusinessEntityID
Inner Join [Sales.SalesOrderHeader] as SOH on SOH.CustomerID = C.CustomerID
Inner Join #TotalOrdersTemp as T on T.CustomerID = C.CustomerID
Order By T.num_orders, T.tot_price desc

Drop Table #TotalOrdersTemp

-- Query 4 - Join entre as tabelas [Sales.SalesOrderDetail], [SalesOrderHeader] e [Production.Product] para obter o total de produtos por ProductID e OrderDate

Select SOD.ProductID, sum(cast(OrderQty as int)) as Tot_Prod_byID_Date
From [Sales.SalesOrderDetail] as SOD
Inner Join [Sales.SalesOrderHeader] as SOH on SOH.SalesOrderID = SOD.SalesOrderID
Inner Join [Production.Product] as PROD on PROD.ProductID = SOD.ProductID
Group by SOD.ProductID, SOH.OrderDate

-- Query 5 - Retornar campos SalesOrderID, OrderDate e TotalDue com data de setembro/2011 e valor maior que 1000

Select SalesOrderID, OrderDate, TotalDue 
From [Sales.SalesOrderHeader]
Where Convert(DATETIME,OrderDate,103) between '01/09/2011' and '30/09/2011' 
	And TotalDue > 1000
Order by TotalDue desc