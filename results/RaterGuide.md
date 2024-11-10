# Rater guide

## Glossary

- Seed Datasets: The datasets used for generation.
- High-Quality: The scenario meets the “scenario-level” criteria Essential, Singular, Complete and Integrous 
- Mixed-Quality: The scenario does not meet at least 1 criteria.

## Content

- [HG/](HG/): High-Quality Seeded Generated Dataset
- [MG/](MG/): Mixed-Quality Seeded Generated Dataset

## Criteria

For the manual analysis, we use the following criteria, taken from Oliveira, G., Marczak, S., & Moralles, C. (2019, September). [How to evaluate BDD scenarios' quality?](https://dl.acm.org/doi/pdf/10.1145/3350768.3351301?casa_token=R2gNvm46ooAAAAAA:3uOUe5Lxqklc5TL2kpbjBfNEYcRiJQcT7SOQv7bV88tn-6AXeyZInJty9Pa-BxLSSNeAjOpYEj7w). In *Proceedings of the XXXIII Brazilian Symposium on Software Engineering* (pp. 481-490):

### Essential

*Does removing any steps affect the understanding?*

### Singular

*Can the scenario's single action be identified by its title and match what the scenario is doing? Can the scenario outcome or verifications be identified on its title and match what the scenario is doing?*

### Complete

*Are all the details needed to follow and understand the steps present?*

### Integrous

*Does the scenario respect Gherkin's rules?*

With the sub questions:

- *Does the scenario respect the natural sequence of steps: “Given steps first, followed by When and Then steps”?*  
- *Does the scenario respect each keyword type: “Given describing pre-conditions, When describing actions and Then describing verifications”?*

## Ratting

Ratting is reported in [Annotation.xlsx](Annotation.xlsx).

- Raters 1 and 2 are (resp.) the first and second authors and Rater 3 is the consensus value decided by authors 3 and 4.

- Ill-formed indicates that the python code was not properly generated (not taken into account in the paper).

- Kappa provides the Kappa score between Raters 1 and 2. The closer the score is to 1, the more they agree. The closer the score is to 0, the more likely it is that they agree by chance. The closer the score is to \-1, the more they disagree.

## Kappa Analysis tab

Provides the Kappa analysis for the different criteria.

## Proportion tab

The proportions for each criterion.

## Yamane

The number of samples to analyse (here, 286) according to Yamane formula are available under the Yamane tab in [Annotation.xlsx](Annotation.xlsx).
