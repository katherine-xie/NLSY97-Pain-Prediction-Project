"""
Maps original reference numbers to descriptive names (NLSY97 dataset)

"""

# Map original reference numbers to more descriptive names for readability
COLUMN_NAMES = {
    # Respondent information
    "R0000100": "respondent_id",
    "U0013202": "interview_year_2015_round",
    "U3450202": "interview_year_2019_round",
    # General health
    "U0001800": "age_at_interview_2015",
    "U1096500": "self_rated_health_2015",
    "U1100200": "health_limits_kind_of_work_2015",
    "U1100300": "health_limits_amount_of_work_2015",
    # Vigorous physical activity
    "U1098200": "vigorous_activity_status_2015",
    "U1098300": "vigorous_activity_frequency_2015",
    "U1098400": "vigorous_activity_frequency_unit_2015",
    "U1098500": "vigorous_activity_duration_2015",
    "U1098600": "vigorous_activity_duration_unit_2015",
    # Moderate physical activity
    "U1098700": "moderate_activity_status_2015",
    "U1098800": "moderate_activity_frequency_2015",
    "U1098900": "moderate_activity_frequency_unit_2015",
    "U1099000": "moderate_activity_duration_2015",
    "U1099100": "moderate_activity_duration_unit_2015",
    # Strength-building activity
    "U1099200": "strength_activity_status_2015",
    "U1099300": "strength_activity_frequency_2015",
    "U1099400": "strength_activity_frequency_unit_2015",
    "U1099500": "strength_activity_duration_2015",
    "U1099600": "strength_activity_duration_unit_2015",
    # Chronic pain target
    "U4368200": "chronic_pain_30d_2019",
}
