CREATE INDEX "idx_HGNC_Gene_Symbol" ON "HGNC_gene_info" (
	"Gene_symbol"
)


CREATE VIEW vw_Diseases AS
SELECT HGNC_ID, gene_symbol, condition, GROUP_CONCAT(Concept_ID) AS Concept_ID, GROUP_CONCAT(Disease_id, ', ') AS Disease_Id, GROUP_CONCAT(Source, ', ') AS Source
FROM
(
	SELECT HGNC_ID, gene_symbol, Condition, Concept_ID, CASE WHEN OMIM_ID <> '#N/A' THEN '<a href="https://www.omim.org/entry/' || OMIM_ID || '" target="_blank">OMIM:' || OMIM_ID || '</a>' ELSE NULL END AS Disease_ID, Source 
	FROM NCBI_genes_to_phenotypes
	
	UNION ALL
	
	SELECT HGNC_ID, gene_symbol, disease_name, NULL
		, CASE 
			WHEN disease_id LIKE 'OMIM%' THEN '<a href="https://www.omim.org/entry/' || SUBSTRING(Disease_id, 6) || '" target="_blank">' || Disease_id || '</a>' 
			WHEN Disease_id LIKE 'ORPHA%' THEN '<a href="https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=' || SUBSTRING(Disease_id, 7) || '" target="_blank">' || Disease_id || '</a>'  ELSE disease_id END, 'HPO' 
	FROM HPO_diseases
)
GROUP BY HGNC_ID, gene_symbol, UPPER(condition)