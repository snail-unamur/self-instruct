import numpy as np
import pandas as pd
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix



QUALITY = "MQ"
NB = 286
FILE = f"Annotation - Resolved {QUALITY}({NB}).csv"
PATH = f'data/{FILE}'
REVIEWER1 = 2
REVIEWER2 = 3

print(FILE)

DATA = pd.read_csv(PATH)
DATA.replace({True: 1, False: 0}, inplace=True)
filtered_data = DATA[(DATA['Scenario ID'] <= NB) & (DATA['Reviewer ID'].isin([REVIEWER1, REVIEWER2]))]

def calculate_kappa(scenario_data):
    """Calculate Cohen's Kappa for a specific scenario."""
    assert len(scenario_data) == 2, "There must be two reviewers for the scenario"
    reviewer_1_ratings = scenario_data[scenario_data['Reviewer ID'] == REVIEWER1][['Essential', 'Singular', 'Complete', 'Integrous', 'High-quality']].values.flatten()
    reviewer_2_ratings = scenario_data[scenario_data['Reviewer ID'] == REVIEWER2][['Essential', 'Singular', 'Complete', 'Integrous', 'High-quality']].values.flatten()
    return cohen_kappa_score(reviewer_1_ratings, reviewer_2_ratings)


def calculate_each_kappa(data):
    """Calculate Cohen's Kappa for each scenario in the data."""
    kappa_scores = []
    scenarios = data['Scenario ID'].unique()
    for scenario in scenarios:
        scenario_data = data[data['Scenario ID'] == scenario]
        kappa = calculate_kappa(scenario_data)
        kappa_scores.append((scenario, kappa))
    return pd.DataFrame(kappa_scores, columns=['Scenario ID', 'Cohen Kappa'])


def test_calculate_cohens_kappa():
    test_data = pd.DataFrame({
        'Scenario ID': [1, 1, 2, 2],
        'Reviewer ID': [1, 2, 1, 2],
        'Essential': [1, 1, 0, 0],
        'Singular': [1, 1, 1, 1],
        'Complete': [0, 0, 1, 1],
        'Integrous': [1, 1, 1, 1],
        'High-quality': [0, 0, 1, 1],
        'Ill-formed': [1, 1, 0, 0]
    })
    expected_scores =  pd.DataFrame([{'Scenario ID': 1, 'Cohen Kappa': 1.0}, {'Scenario ID': 2, 'Cohen Kappa': 1.0}])
    actual_scores = calculate_each_kappa(test_data)
    pd.testing.assert_frame_equal(actual_scores, expected_scores)

# Run the test
test_calculate_cohens_kappa()


# Calculate Cohen's Kappa for each scenario and store in a DataFrame
kappa_df = calculate_each_kappa(filtered_data)

kappa_df.to_csv(f'data/Cohen_Kappa - {FILE}.csv', index=False)


def calculate_kappa_ci(ratings_reviewer1, ratings_reviewer2):
    cm = confusion_matrix(ratings_reviewer1, ratings_reviewer2)
    n = np.sum(cm)
    p_a = np.trace(cm) / n
    marginal_rater1 = np.sum(cm, axis=1)
    marginal_rater2 = np.sum(cm, axis=0)
    p_e = np.sum((marginal_rater1 / n) * (marginal_rater2 / n))
    kappa = (p_a - p_e) / (1 - p_e) if 1 - p_e != 0 else 0
    se_kappa = np.sqrt((p_a * (1 - p_a)) / (n * (1 - p_e)**2))
    z = 1.96  
    lower_bound = kappa - z * se_kappa
    upper_bound = kappa + z * se_kappa
    return lower_bound, kappa, upper_bound

def calculate_column_kappa_ci(data, column):
    """Calculate the confidence interval for Cohen's Kappa for a specific column."""
    reviewer_1_data = data[data['Reviewer ID'] == 1][column].values
    reviewer_2_data = data[data['Reviewer ID'] == 2][column].values
    return calculate_kappa_ci(reviewer_1_data, reviewer_2_data)


for column in ['Essential', 'Singular', 'Complete', 'Integrous', 'High-quality']:
    lower_bound, kappa, upper_bound = calculate_column_kappa_ci(filtered_data, column)
    print(f"\n95% Confidence Interval for Cohen's Kappa for {column}: ({lower_bound:.2f}, {upper_bound:.2f})")
    print(f"Cohen's Kappa for {column}: {kappa:.2f}")