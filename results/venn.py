from venny4py.venny4py import venny4py
import pandas as pd


QUALITY = "HQ"
NB = 286
FILE = f"Annotation - Resolved {QUALITY}({NB}).csv"
PATH = f'data/{FILE}'
REVIEWER = 3
OUT = f'data/venn/Resolved {QUALITY}({NB}) - Reviewer {REVIEWER}'

DATA = pd.read_csv(PATH)
DATA.replace({True: 1, False: 0}, inplace=True)
filtered_data = DATA[(DATA['Scenario ID'] <= NB) & (DATA['Reviewer ID'].isin([1, 2, 3]))]
REVIEWER_DATA = filtered_data[filtered_data['Reviewer ID'] == REVIEWER]

sets = {
    "Essential": set(REVIEWER_DATA[REVIEWER_DATA["Essential"] == 1]["Scenario ID"]),
    "Singular": set(REVIEWER_DATA[REVIEWER_DATA["Singular"] == 1]["Scenario ID"]),
    "Complete": set(REVIEWER_DATA[REVIEWER_DATA["Complete"] == 1]["Scenario ID"]),
    "Integrous": set(REVIEWER_DATA[REVIEWER_DATA["Integrous"] == 1]["Scenario ID"]),
}

    
venny4py(sets=sets, out=OUT, ext='pdf', dpi=1000)
