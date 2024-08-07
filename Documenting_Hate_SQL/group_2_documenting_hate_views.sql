USE inst327_project;

CREATE OR REPLACE VIEW hate_crimes_committed_by_women AS
	SELECT 
        suspect_firstname,
        suspect_lastname,
        age,
        race,
        gender
	FROM suspects
    JOIN race USING (race_id)
    JOIN gender USING (gender_id)
    WHERE gender_id = 2
    ORDER BY suspect_firstname;
  
CREATE OR REPLACE VIEW hate_crimes_by_location AS
	SELECT 
        incident_summary,
		hate_crime_categories,
        city,
        state
	FROM incidents
    JOIN hate_crimes USING (hate_crime_id)
    JOIN locations USING (location_id)
    ORDER BY state;

CREATE OR REPLACE VIEW count_of_hate_crimes_by_category AS
	SELECT 
		incident_summary,
        suspect_firstname,
        suspect_lastname,
        victim_firstname,
        victim_lastname,
        COUNT(*) AS hate_crime_categories
	FROM incidents
    JOIN suspects USING (suspect_id)
    JOIN victims USING (victim_id)
    JOIN hate_crimes USING (hate_crime_id)
    WHERE hate_crime_categories = "Religion"
    GROUP BY 
		incident_summary,
		suspect_firstname,
        suspect_lastname,
        victim_firstname,
        victim_lastname
    ORDER BY hate_crime_categories;
    
CREATE OR REPLACE VIEW count_of_hate_crimes_committed_by_age_18_to_25 AS
	SELECT
		hate_crime_categories,
        suspect_firstname,
        suspect_lastname,
        COUNT(*) AS age,
        race,
        gender
	FROM suspects
    JOIN race USING (race_id)
    JOIN gender USING (gender_id)
    JOIN incidents USING (suspect_id)
    JOIN hate_crimes USING (hate_crime_id)
    WHERE age >= 18 AND age <= 25
    GROUP BY 
		hate_crime_categories,
        suspect_firstname,
        suspect_lastname,
        race,
        gender
    ORDER BY suspect_firstname;

CREATE OR REPLACE VIEW hate_crime_men_victims AS
	SELECT
        hate_crime_categories,
        victim_firstname,
        victim_lastname,
        age,
        race,
        gender
    FROM victims
    JOIN race USING (race_id)
    JOIN gender USING (gender_id)
    JOIN incidents USING (victim_id)
    JOIN hate_crimes USING (hate_crime_id)
    WHERE gender_id = 1
    ORDER BY victim_firstname;

CREATE OR REPLACE VIEW hate_crime_victims_by_white_race AS
	SELECT
		victim_firstname,
        victim_lastname,
		race,
        age,
        gender,
		hate_crime_categories
    FROM victims
    JOIN race USING (race_id)
    JOIN gender USING (gender_id)
    JOIN incidents USING (victim_id)
    JOIN hate_crimes USING (hate_crime_id)
    WHERE race_id = 15
    ORDER BY race;
	
CREATE OR REPLACE VIEW articles_by_date AS
SELECT
    subquery.article_title,
    subquery.article_link,
    subquery.source_name,
    subquery.date_published,
    subquery.time_published
FROM (
    SELECT
        articles.article_title,
        articles.article_link,
        sources.source_name,
        articles.date_published,
        articles.time_published
    FROM
        articles
    JOIN
        sources USING (source_id)
    ORDER BY
        articles.date_published, articles.time_published
) AS subquery;

CREATE OR REPLACE VIEW articles_by_authors AS
	SELECT
		article_title,
        article_link,
        author_firstname,
        author_lastname
	FROM articles
    JOIN article_authors USING (article_id)
    JOIN author USING (author_id)
    ORDER BY author_firstname;
    
    SELECT * FROM hate_crimes_committed_by_women;
    SELECT * FROM hate_crimes_by_location;
    SELECT * FROM count_of_hate_crimes_by_category;
    SELECT * FROM count_of_hate_crimes_committed_by_age_18_to_25;
    SELECT * FROM hate_crime_men_victims;
    SELECT * FROM hate_crime_victims_by_white_race;
    SELECT * FROM articles_by_date;
    SELECT * FROM articles_by_authors;
	
    