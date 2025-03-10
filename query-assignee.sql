SELECT
  patents_publications_202111.publication_number,
  assignee,
  title,
  url,
  ARRAY_LENGTH(cited_by) AS number_of_cited_by
FROM
  patents-public-data.patents.publications_202111 patents_publications_202111
LEFT JOIN
  patents-public-data.google_patents_research.publications_202111 patents_research_publications_202111
ON
  patents_publications_202111.publication_number = patents_research_publications_202111.publication_number
WHERE
  EXISTS(
  SELECT
    *
  FROM
    UNNEST(patents_publications_202111.assignee) AS x
  WHERE
    x LIKE 'Vibracoustic%')
  AND ARRAY_LENGTH(cited_by) > 0
ORDER BY
  number_of_cited_by DESC
LIMIT 50