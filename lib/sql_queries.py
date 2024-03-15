select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex='F';
"""

select_all_bears_names_and_colors = """
    SELECT
        name,
        color
    FROM bears;
"""

select_all_bears_names_and_temperaments_where_alive = """
    SELECT
        name,
        temperament
    FROM bears
    WHERE alive=1;
"""

select_all_bears_order_by_id_desc = """
    SELECT
        *
    FROM bears
    ORDER BY id DESC;
"""

select_name_age_color_alive_from_bears_where_age_gt_6 = """
    SELECT
        name,
        age,
        color,
        alive
    FROM bears
    WHERE age > 6;
"""

select_name_and_count_of_bears_group_by_color = """
    SELECT
        color,
        COUNT(*) as count
    FROM bears
    GROUP BY color;
"""

select_name_and_age_of_oldest_bear = """
    SELECT
        name,
        age
    FROM bears
    WHERE age = (SELECT MAX(age) FROM bears);
"""
