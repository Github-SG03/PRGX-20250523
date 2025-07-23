/* =============================================
Script to evaluate a databases compression and free space!
Returns 3 sections:
1) Compression %
	The Compression % should be very high, ideally 100%.  Anything above 90% is acceptable.
2) Free Space %
	The Free Space % should be very low, ideally 0%.  Anything below 10% is ok, as long as it is below 50GB total.
3) Uncompressed tables/indexes
============================================= */
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

--Calculate database compression %
	SELECT @@serverName as [ServerName], DB_NAME() as [DatabaseName], T.name as TableName, P.data_compression, P.data_compression_desc, T.object_id, T.schema_id, S.name as SchemaName, P.rows, T.create_date, T.modify_date, P.index_id, I.name as IndexName, I.type_desc, I.is_unique, I.is_unique_constraint, I.is_primary_key, I.fill_factor, I.is_padded, I.is_disabled, (SUM(A.used_pages) * 8) / 1024 AS UsedSpaceMB, (SUM(A.data_pages) * 8) / 1024 AS DataSpaceMB, getdate() as [RecordDate]
	INTO #DimTable 
	FROM sys.partitions P INNER JOIN sys.tables T ON T.object_id = P.object_id INNER JOIN sys.schemas S on S.schema_id = T.schema_id LEFT OUTER JOIN sys.indexes I on I.object_id = P.object_id and I.index_id = P.index_id	INNER JOIN sys.allocation_units A ON P.partition_id = A.container_id
	WHERE P.index_id in (0,1) 
	GROUP BY T.name, P.data_compression, P.data_compression_desc, T.object_id, T.schema_id, S.name, P.rows, T.create_date, T.modify_date, P.index_id, I.name, I.type_desc, I.is_unique, I.is_unique_constraint, I.is_primary_key, I.fill_factor, I.is_padded, I.is_disabled

	INSERT INTO #DimTable ([ServerName],[DatabaseName],[TableName],[data_compression],[data_compression_desc],[object_id],[schema_id],[SchemaName],[rows],[create_date],[modify_date],[index_id],[IndexName],[type_desc],[is_unique],[is_unique_constraint],[is_primary_key],[fill_factor],[is_padded],[is_disabled],UsedSpaceMB,DataSpaceMB,[RecordDate])
	SELECT @@serverName as [ServerName], DB_NAME() as [DatabaseName], T.name as TableName, P.data_compression, P.data_compression_desc, T.object_id, T.schema_id, S.name as SchemaName, P.rows, T.create_date, T.modify_date, P.index_id, I.name as IndexName, I.type_desc, I.is_unique, I.is_unique_constraint, I.is_primary_key, I.fill_factor, I.is_padded, I.is_disabled, (SUM(A.used_pages) * 8) / 1024 AS UsedSpaceMB, (SUM(A.data_pages) * 8) / 1024 AS DataSpaceMB, getdate() as [RecordDate]
	FROM sys.partitions P INNER JOIN sys.tables T ON T.object_id = P.object_id INNER JOIN sys.schemas S on S.schema_id = T.schema_id INNER JOIN sys.indexes I on I.object_id = P.object_id and I.index_id = P.index_id INNER JOIN sys.allocation_units A ON P.partition_id = A.container_id
	WHERE P.index_id > 1 
	GROUP BY T.name, P.data_compression, P.data_compression_desc, T.object_id, T.schema_id, S.name, P.rows, T.create_date, T.modify_date, P.index_id, I.name, I.type_desc, I.is_unique, I.is_unique_constraint, I.is_primary_key, I.fill_factor, I.is_padded, I.is_disabled

	Select [ServerName],[DatabaseName],[data_compression_desc],sum(UsedSpaceMB) as SpaceUsed
	into #Comp
	from #DimTable
	where [data_compression_desc] <> 'NONE'
	group by [ServerName],[DatabaseName],[data_compression_desc]
	order by [ServerName],[DatabaseName],[data_compression_desc]

	select A.[ServerName], A.[DatabaseName], C.[data_compression_desc] as CompressionType, C.[SpaceUsed] as CompressedSpace, cast(sum(A.UsedSpaceMB) as decimal(9,2)) as TotalSpace, cast((case when sum(A.UsedSpaceMB) = 0 then 0 else (C.[SpaceUsed] / cast(sum(A.UsedSpaceMB) as decimal(9,2)) * 100) end) as decimal(5,2)) as [Compression%]
	into #Total
	from #DimTable A left outer join #Comp C on A.ServerName = C.ServerName and A.[DatabaseName] = C.[DatabaseName]
	group by A.[ServerName],A.[DatabaseName],C.[data_compression_desc], C.[SpaceUsed]
	order by A.[ServerName],A.[DatabaseName],C.[data_compression_desc]

	select * from #Total  
	Drop table #DimTable
	Drop table #Comp
	Drop table #Total


--Free Space Info
	SELECT DatabaseName, ' * Total * ' as FileName, cast(Sum(CurrentSizeMB) AS Decimal(18,2)) AS CurrentSizeMB, cast(Sum(FreeSpaceMB)  AS Decimal(18,2)) AS FreeSpaceMB, cast(Sum(FreeSpaceMB) / Sum(CurrentSizeMB) * 100 AS Decimal(18,2)) AS FreeSpacePercent 
	FROM (SELECT DB_NAME() AS DatabaseName, name AS FileName, size/128.0 AS CurrentSizeMB, size/128.0 - CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS FreeSpaceMB, cast((size - CAST(FILEPROPERTY(name, 'SpaceUsed') AS Decimal(18,4))) / size * 100 AS Decimal(6,2)) AS FreeSpacePercent FROM sys.database_files) i
	group by DatabaseName
	UNION ALL 
	SELECT DB_NAME() AS DatabaseName, name AS FileName, cast(size/128.0 AS Decimal(18,2)) AS CurrentSizeMB, cast(size/128.0 - CAST(FILEPROPERTY(name, 'SpaceUsed') AS INT)/128.0 AS Decimal(18,2)) AS FreeSpaceMB, cast((size - CAST(FILEPROPERTY(name, 'SpaceUsed') AS Decimal(18,2))) / size * 100 AS Decimal(6,2)) AS FreeSpacePercent FROM sys.database_files



--What tables and indexes are not compressed
	SELECT DB_NAME() as DatabaseName, st.name as TableName, sp.index_id, Coalesce(I.name, ' * Table * ') as IndexName, sp.rows as Records
	FROM sys.partitions SP INNER JOIN sys.tables ST ON st.object_id = sp.object_id INNER JOIN sys.indexes I on SP.object_id = I.object_id and SP.index_id = I.index_id
	where sp.data_compression = 0
	order by sp.data_compression, st.name
