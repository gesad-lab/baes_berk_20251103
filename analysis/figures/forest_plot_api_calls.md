# Visualization Documentation: forest_plot_api_calls.svg

**Visualization Type**: Effect Forest  
**Metric**: api_calls  
**Frameworks**: baes, chatdev, ghspec  
**Generated**: 2025-11-03T08:20:41.160677Z

---

## Rationale

This Effect Forest visualization was generated to compare API Calls (count) performance across baes, chatdev, ghspec. The forest plot displays effect sizes with confidence intervals for rigorous statistical comparison.

**Interpretation Guidance**: Effect sizes measure practical significance independent of sample size. For Cliff's Delta: |δ|<0.15 (negligible), 0.15-0.33 (small), 0.33-0.47 (medium), ≥0.47 (large). Decision criteria: (1) CI excludes zero = statistically significant. (2) Effect magnitude ≥medium = practically significant. (3) Both conditions met = strong evidence of meaningful difference. Domain context: For software engineering metrics, even 'small' effects (0.15-0.33) can be valuable if they improve critical aspects like security or user experience.

---

## Data

### Data: Effect Sizes

#### Pairwise Comparisons

| Comparison | Effect Size (Cliff's δ) | 95% CI | Magnitude | Interpretation |
|------------|-------------------------|---------|-----------|----------------|
| ghspec vs baes | 1.000 | [1.000, 1.000] | large | Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes. |
| ghspec vs chatdev | -0.766 | [-0.848, -0.672] | large | Cliff's Delta = -0.766 [-0.848, -0.672]: large effect size. ghspec has systematically lower values compared to chatdev (probability: 11.7%). |
| baes vs chatdev | -1.000 | [-1.000, -1.000] | large | Cliff's Delta = -1.000 [-1.000, -1.000]: large effect size. all observed values in baes are less than those in chatdev. |

#### Aggregation Methodology

| Property | Value |
|----------|-------|
| Effect Size Measure | Cliff's Delta (δ) - non-parametric |
| Confidence Intervals | 95% bootstrap CIs (10,000 iterations) |
| Magnitude Thresholds | Negligible: |δ|<0.15, Small: 0.15-0.33, Medium: 0.33-0.47, Large: >0.47 |
| Interpretation | Probability superiority measure (-1 to +1) |


---

## Analysis

### Analysis

This forest plot displays pairwise effect size comparisons for API Calls (count), enabling identification of statistically and practically significant differences between frameworks. Each row shows one pairwise comparison with the effect size estimate and 95% confidence interval. 

**Effect Size Range**: The largest effect is observed in ghspec vs baes (cliffs_delta = 1.000, large), while the smallest is in ghspec vs chatdev (cliffs_delta = -0.766, large). 

**Practical Significance**: 3/3 comparisons (100.0%) show large effect sizes (cliffs_delta > 0.474), indicating substantial practical differences. 

**Complete Separation**: 2 comparison(s) show complete separation (|effect| = 1.0 with zero uncertainty), indicating no overlap in value distributions. This represents the strongest possible evidence of difference. Comparisons: ghspec vs baes, baes vs chatdev. 

**Effect Size Methodology**: All comparisons use cliffs_delta, a non-parametric effect size measure suitable for ordinal or non-normal data. Values range from -1 to +1, where 0 indicates no effect (distributions identical), positive values indicate the first framework has higher values, and negative values indicate the second framework has higher values (interpretation depends on whether higher is better). Confidence intervals are computed using bootstrapping with 10,000 iterations, providing robust uncertainty estimates without normality assumptions. 

Magnitude thresholds follow Romano et al. (2006): negligible (|Δ| < 0.147), small (0.147 ≤ |Δ| < 0.330), medium (0.330 ≤ |Δ| < 0.474), large (|Δ| ≥ 0.474). 

**Interpretation Guidance**: Focus on effect sizes with CIs that exclude zero (statistically significant) AND have large magnitude (practically significant). Narrow CIs indicate high precision and confidence in the estimate. Wide CIs suggest high variability or small sample size - consider increasing n_runs. The forest plot format enables quick visual assessment: points far from the zero line with non-overlapping CIs represent the strongest evidence of difference. 
