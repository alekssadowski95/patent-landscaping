SELECT 
  publication_number,
  title,
  url,
  `cpc`[SAFE_OFFSET(0)].code,
  ARRAY_LENGTH(cited_by) AS number_of_cited_by
FROM 
  `patents-public-data.google_patents_research.publications_202409` 
ORDER BY
  number_of_cited_by DESC   -- Sort patents by the number of citations (descending)
LIMIT 10000