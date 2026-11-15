# Dataset Card

## Identity and Provenance

- **Dataset name:** The National Longitudinal Survey of Youth 1997 (NLSY97)
- **Source owner:** U.S. Bureau of Labor Statistics (BLS), The National Longitudinal Surveys Program
- **Retrieval method and date:** A custom subset of the NLSY97 data was downloaded through the NLS Investigator tool on 11/14/2026
- **License or access agreement:** NLSY97 is public-use data and may be accessed through the NLS Investigator tool. Follow the official [NLS documentation](https://nlsinfo.org/) for citation, access, and redistribution guidance.
- **Immutable version, checksum, or query:**
The exact NLSY97 data extract used for this card (Local file name: `nlsy97_raw_physical_activity_chronic_pain.csv`) has the following SHA-256 checksum: 

  ```text
  f61d8de73be48569a987a6f52b32728045b4e3dca05713e450eb15632ed79314
  ```

## Observation and Sampling

- **What does one row represent?** One original NLSY97 cohort member
- **What population or process produced the rows?**

    NLSY97 is a longitudinal U.S. survey of people born between 1980–1984 and living in the United States at its initial sampling in 1997. It contains 6,748 cross-sectional participants and an additional 2,236 participants that oversamples Black and Hispanic/Latino youth for a total of 8,984 respondants. Interviews were conducted annually from 1997 to 2011 and biennially since then. 

- **Which units repeat, interact, or depend on one another?** 
    
    Each respondant in the dataset has a unique `respondent_id` across all survey rounds. No respondent ID repeats within the current file.

- **Which time, site, batch, subject, or spatial boundaries matter?**

    Baseline feature predictors come from the Round 17 (2015–2016) interview, while the chronic-pain outcome comes from the Round 19 (2019–2020) interview. Besides the scope of the United States, there is no detailed location boundary, and the findings should not be interpreted as location-specific.

## Schema and Measurement

The local CSV has a total of 23 integer-valued columns and 8,984 rows. 19 columns are predictor variables, two columns are the interview years, `respondant_id` serves as the identifier column, and `chronic_pain_30d_2019` is the classification target. The column names here refer to the renamed CSV, not the original NLSY97 reference numbers.

### 1. Respondent and Interview Information

These fields identify respondents or describe when the data were collected.

| Column | Role | What It Represents | Values/Units |
| --- | --- | --- | --- |
| `respondent_id` | Identifier | Unique person in the NLSY97 sample | ID number represented by an integer | 
| `interview_year_2015_round` | Metadata | Actual year of the Round 17 (baseline) interview | `2015` or `2016` | 
| `interview_year_2019_round` | Metadata | Actual year of the Round 19 (follow-up) interview | `2019` or `2020` |

### 2. Baseline Health Features (2015–2016)

| Column | Role | What it Measures | Values/Units |
| --- | --- | --- | --- |
| `age_at_interview_2015` | Predictor | Age at the baseline interview | Years |
| `self_rated_health_2015` | Predictor | Self-reported health status | Integer from `1` to `5`, where `1` = Excellent; `2` = Very good; `3` = Good; `4` = Fair; `5` = Poor  | 
| `health_limits_kind_of_work_2015` | Predictor | Health-related limitation on type of work | Binary category, where `0` does not limit the kind of work and `1` limits the kind of work | 
| `health_limits_amount_of_work_2015` | Predictor | Health-related limitation on amount of work | Binary category, where `0` does not limit the amount of work and `1` limits the amount of work | 

### 3. Physical activity features (2015–2016)

The dataset includes three types of physical activity responses: vigorous, light/moderate, and muscle-strengthening. Each has five fields: participation status, frequency, frequency unit, duration, and duration unit.

#### A. Vigorous activity

Activities lasting at least 10 minutes that cause heavy sweating or a large increase in breathing or heart rate.

| Variable | What it Records | Values/Units |
| --- | --- | --- |
| `vigorous_activity_status_2015` | Whether the person does vigorous activity | `0` = Never; `1` = Participates; `2` = Unable |
| `vigorous_activity_frequency_2015` | How often | Number of times (interpret with frequency unit) |
| `vigorous_activity_frequency_unit_2015` | Frequency time period | `1` = Per day; `2` = Per week; `3` = Per month; `4` = Per year |
| `vigorous_activity_duration_2015` | How long each time | Numeric amount (interpret with duration unit) |
| `vigorous_activity_duration_unit_2015` | Duration time unit | `1` = Minutes; `2` = Hours |

#### B. Light or moderate activity

Activities lasting at least 10 minutes that cause slight sweating or a slight-to-moderate increase in breathing or heart rate.

| Variable | What It Records | Values/Units |
| --- | --- | --- |
| `moderate_activity_status_2015` | Whether the person does light/moderate activity | `0` = Never; `1` = Participates; `2` = Unable |
| `moderate_activity_frequency_2015` | How often | Number of times (interpret with frequency unit) |
| `moderate_activity_frequency_unit_2015` | Frequency time period | `1` = Per day; `2` = Per week; `3` = Per month; `4` = Per year |
| `moderate_activity_duration_2015` | How long each time | Numeric amount (interpret with duration unit) |
| `moderate_activity_duration_unit_2015` | Duration time unit | `1` = Minutes; `2` = Hours |

#### C. Muscle-strengthening activity

Exercises intended to strengthen muscles, such as weightlifting or calisthenics.

| Variable | What It Records | Values/Units |
| --- | --- | --- |
| `strength_activity_status_2015` | Whether the person does strengthening activity | `0` = Never; `1` = Participates; `2` = Unable |
| `strength_activity_frequency_2015` | How often | Number of times (interpret with frequency unit) |
| `strength_activity_frequency_unit_2015` | Frequency time period | `1` = Per day; `2` = Per week; `3` = Per month; `4` = Per year |
| `strength_activity_duration_2015` | How long each time | Numeric amount (interpret with duration unit) |
| `strength_activity_duration_unit_2015` | Duration time unit | `1` = Minutes; `2` = Hours |

#### Example:
- Frequency: `3` + frequency unit `2` = **3 times per week**
- Duration `30` + duration unit `1` = **30 minutes per session**
- Note: If status is `0` (never) or `2` (unable), follow-up frequency/duration fields may contain `-4` (valid skip), which should not be mistaken for a numerical measurement.


### 4. Later outcome (2019–2020)

| Column | Role | What It Measures | Units/Values |
| --- | --- | --- | --- | 
| `chronic_pain_30d_2019` | **Classification Target** | Self-reported chronic pain in the preceding 30 days | Binary response, where `1` = Yes; `0` = No |

### Missing-Value Convention:

The NLSY97 dataset uses negative values to identify missing, refused, skipped, or noninterview responses. In this study, these codes are not considered valid measurements of age, health, physical activity, or chronic pain and will be removed during data selection. 

| Code | Meaning |
|---|---|
| `-1` | Refusal |
| `-2` | Don't know |
| `-3` | Invalid skip |
| `-4` | Valid skip |
| `-5` | Noninterview |

### Availability Time and Data Leakage

This study only uses variables collected during the 2015–2016 survey round to predict chronic pain in 2019–2020.

To prevent data leakage:
- Do not use `chronic_pain_30d_2019` or `interview_year_2019_round` as predictors.
- Handle missing values, scaling, and encoding using only the training data.
- Select model features without examining the test results.

**Note:** Health-related work limitations may reflect existing medical conditions, so their relationship with future chronic pain should be interpreted carefully.

## Data Access and Privacy

- **Files on GitHub:** Dataset documentation, configuration files, processing scripts, tests, and synthetic sample data may be committed.
- **Local data:** The NLSY97 CSV remains in `data/local/` and is excluded from Git. Respondent-level data and sensitive information should not be committed.
- **Credentials:** No credentials are needed to access the existing local CSV.
- **CI testing:** A synthetic, "test" dataset will be created in `data/fixtures/` to test data loading, validation, and preprocessing without accessing real respondent records.

## Representativeness and Limitations

- **Known exclusions:** The current dataset excludes demographic, socioeconomic, and occupational factors, limiting the scope of analysis.
- **Selection effects:** Not all respondents participated in both survey rounds. Missing responses and exclusions may introduce selection bias.
- **Label limitations:** Chronic pain is self-reported over the preceding 30 days. It does not represent a confirmed medical diagnosis or necessarily a new case of chronic pain.
- **Measurement limitations:** Physical activity and health measures rely on self-reported responses, which may contain errors. Survey codes and time units must be interpreted correctly, and any differences in measurement across rounds should be checked.
- **Generalizability:** The NLSY97 follows individuals born between 1980 and 1984. Findings may not apply to older or younger populations and should not be treated as nationally representative. 
- **Causation and intended use:** Associations between physical activity and chronic pain do not establish causation. The dataset is intended for educational research, not medical diagnosis or clinical decisions.