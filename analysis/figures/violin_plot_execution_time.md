# Visualization Documentation: violin_plot_execution_time.svg

**Visualization Type**: Violin  
**Metric**: execution_time  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:28:03.581899Z

---

## Rationale

This Violin visualization was generated to compare Execution Time (seconds) performance across ghspec, baes, chatdev. The violin plot combines box plot features with kernel density estimation to show full distribution shapes.

**Interpretation Guidance**: Violin plots reveal full distribution shapes through kernel density estimation. Look for: (1) Multiple peaks (multimodality) suggesting distinct performance regimes. (2) Skewness—fat tail on right/left indicates asymmetric behavior. (3) Width at different heights—wide sections have more data concentration. Test selection: Shapiro-Wilk p<0.05 indicates non-normality, requiring robust methods. For software metrics where higher variance often accompanies higher means, consider log-transformation or coefficient of variation for fair comparison.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 973.927 | 971.109 | [947.341, 1013.552] | 171.452 | 572.157 | 1440.584 | 885.385 | 1065.036 | 5 | 100 |
| baes | 206.312 | 210.017 | [199.557, 213.785] | 37.926 | 128.538 | 409.449 | 186.652 | 225.766 | 1 | 100 |
| chatdev | 1238.107 | 1195.212 | [1101.955, 1247.122] | 303.450 | 600.241 | 2057.135 | 1039.516 | 1313.354 | 11 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The violin reveals Execution Time (seconds) patterns across frameworks. baes shows the lowest mean (206.312), while chatdev exhibits the highest (1238.107), representing a 500.1% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 1 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 3 framework(s): ghspec, baes, chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The violin plot compares execution-time distributions for ghspec, baes, and chatdev. baes concentrates tightly around ~200 s with a modest right tail, indicating consistently faster runs and low dispersion. ghspec centers near ~950–1,050 s with moderate spread and a few high-end outliers. chatdev exhibits the largest central tendency (~1,200 s) and the broadest distribution, with a long right tail extending beyond 1,800–2,000 s, signaling high variability and occasional very slow runs. Descriptively, baes had the lowest mean (206.312 s), while chatdev had the highest (1,238.107 s), a 500.1% relative difference; ghspec fell in between. The observed ordering by medians mirrors the means, but distribution asymmetry—skewness exceeded |1| for one framework—suggests medians are more reliable than means. Normality assumptions were violated for all three frameworks (Shapiro–Wilk p<0.05), justifying non-parametric inference. Interquartile widths visibly separate baes from the others, implying meaningful effect sizes; ghspec and chatdev show partial overlap in their middle ranges but differ in scale and tails. Outliers were detected in all frameworks (1.5×IQR rule), particularly pronounced for chatdev, which could inflate mean-based comparisons. With N=100 per framework and bootstrap 95% CIs (for medians), the performance separation—especially baes versus the others—appears robust. No missingness is evident, but heteroscedasticity and skewness recommend robust statistical tests and possibly log transformation for fairer cross-framework comparisons.

### Camera-Ready Paragraph

Figure: violin_plot_execution_time.svg visualized execution-time distributions for three frameworks. The analysis revealed that baes had the lowest central tendency and variability, concentrating around 200 s, whereas ghspec centered near 1,000 s and chatdev exhibited the highest and most dispersed times around 1,200 s with a pronounced right tail. Descriptive means corroborated the visual patterns (baes = 206.312 s; chatdev = 1,238.107 s), indicating a 500.1% relative difference; ghspec lay between these extremes. Normality was rejected for all frameworks (Shapiro–Wilk p<0.05), and one framework showed high skewness (|skew|>1), motivating median-focused summaries and non-parametric inference. Outliers were present across groups (1.5×IQR rule), particularly for chatdev, consistent with the heavy-tailed shape. These findings support the hypothesis that execution time differs substantially across frameworks and position baes as the most time-efficient option. The distributional contrasts—narrow, low-centered density for baes versus wide, high-centered densities for ghspec and chatdev—imply practical gains in both speed and stability when using baes. This suggests that methodological choices should account for heteroscedastic, non-normal performance profiles when comparing software frameworks.

### Actionable Recommendations

Interpret the results using robust summaries (median, IQR) and report non-parametric tests: a Kruskal–Wallis omnibus comparison followed by Dunn’s post hoc tests with Holm adjustment. Quantify effects with median differences and bootstrap 95% CIs and include rank-based effect sizes (e.g., Cliff’s delta). Given skew and heteroscedasticity, consider a log-time analysis or modeling with quantile regression to assess differences across the distribution. Investigate outliers to separate true extremes from measurement artifacts; if legitimate, report their frequency and operational conditions. For presentation, annotate medians and 95% CIs on the violins, optionally overlay jittered observations, and state N=100 per framework in the caption. If reproducibility is a goal, accompany the figure with a table of summary statistics and share scripts used for bootstrapping and outlier detection.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 78.9s
- Token Usage: 4,793 tokens (1,722 prompt + 3,071 completion)
- Estimated Cost: $0.0000 USD
