SELECT
    A.Id,
    A.Revenue_Metric_1,
    A.Revenue_Metric_2,
    A.Termination_Flag_1,
    A.Termination_Flag_2,
    B.Num_NPS_Surveys,
    B.Avg_NPS_Score,
    B.Num_Comment_Surveys,
    B.Avg_Overall_Score,
    B.Avg_Case_Duration
FROM
    schema_name.account_table AS A
INNER JOIN (
    SELECT
        account_id,
        COUNT(DISTINCT survey_id) AS Num_Comment_Surveys,
        AVG(CAST(score AS FLOAT)) AS Avg_Overall_Score,
        COUNT(DISTINCT CASE WHEN nps IS NOT NULL THEN nps END) AS Num_NPS_Surveys,
        AVG(CAST(nps AS FLOAT)) AS Avg_NPS_Score,
        AVG(DATEDIFF(MINUTE, created_date, closed_date)) AS Avg_Case_Duration
    FROM
        schema_name.survey_table
    WHERE
        survey_date >= '2022-01-01'
        AND survey_type <> 'Example Exclusion'
    GROUP BY
        account_id
) AS B ON A.Id = B.account_id;
