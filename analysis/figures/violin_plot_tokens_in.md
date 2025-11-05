# Visualization Documentation: violin_plot_tokens_in.svg

**Visualization Type**: Violin  
**Metric**: tokens_in  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:33:04.266206Z

---

## Rationale

This Violin visualization was generated to compare Input Tokens (count) performance across ghspec, baes, chatdev. The violin plot combines box plot features with kernel density estimation to show full distribution shapes.

**Interpretation Guidance**: Violin plots reveal full distribution shapes through kernel density estimation. Look for: (1) Multiple peaks (multimodality) suggesting distinct performance regimes. (2) Skewness—fat tail on right/left indicates asymmetric behavior. (3) Width at different heights—wide sections have more data concentration. Test selection: Shapiro-Wilk p<0.05 indicates non-normality, requiring robust methods. For software metrics where higher variance often accompanies higher means, consider log-transformation or coefficient of variation for fair comparison.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 294720.580 | 288673.500 | [280733.500, 301019.000] | 32567.513 | 234785.000 | 394313.000 | 269970.750 | 315616.000 | 1 | 100 |
| baes | 35750.290 | 35167.000 | [35167.000, 35167.000] | 953.219 | 35167.000 | 38937.000 | 35167.000 | 37052.000 | 0 | 100 |
| chatdev | 154917.440 | 146999.500 | [141594.000, 153324.000] | 32749.365 | 102986.000 | 282095.000 | 135513.750 | 173201.750 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The violin reveals Input Tokens (count) patterns across frameworks. baes shows the lowest mean (35750.290), while ghspec exhibits the highest (294720.580), representing a 724.4% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

*Shapiro-Wilk tests if data follows a bell curve (normal distribution). p>0.05 suggests normality; p<0.05 indicates non-normal data requiring robust statistical methods.* 

*Mann-Whitney U is a non-parametric test comparing groups without assuming normality. Ranks all values and tests if one group tends to have higher ranks. More robust than t-test for skewed data.*

**Skewness Detected**: 2 framework(s) exhibit high skewness (|skew| > 1.0), indicating median is more representative than mean. 

*Skewness measures distribution asymmetry. Positive skew: long right tail (mean>median). Negative skew: long left tail (mean<median). |skew|>1 indicates high skewness affecting mean reliability.*

**Outliers**: Detected in 2 framework(s): ghspec, chatdev. 

*Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.*

**Statistical Methodology**: N=100 runs per framework, distributions characterized by median with bootstrap 95% CIs, IQR, and outlier detection (1.5×IQR criterion). 

*Bootstrapping estimates uncertainty by repeatedly resampling data with replacement. Creates thousands of simulated samples to calculate confidence intervals without assuming normal distributions.* 

*A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.*

---

## LLM-Enhanced Analysis

### Focused Insights

The violin plot contrasts Input Tokens (count) for ghspec, baes, and chatdev across N=100 runs each. The most salient pattern is a strong separation of scales: ghspec concentrates at the highest token counts, chatdev sits lower but still high, and baes is tightly clustered at the lowest range. Descriptively, baes had the lowest mean (35,750), while ghspec had the highest (294,721), a 724.4% relative difference. However, distributional diagnostics indicate that means are not reliable: Shapiro–Wilk tests were significant (p<0.05) for all three frameworks, and two frameworks showed high skewness (|skew|>1), making the median and IQR more representative. The violins for ghspec and chatdev are wide with extended right tails and flagged outliers (1.5×IQR rule), implying substantial heterogeneity and potential heavy-tailed behavior; baes appears narrow, with limited spread and fewer extreme values. Density overlap between baes and the other frameworks is minimal, suggesting large rank-based effect sizes; overlap between ghspec and chatdev occurs mainly in the lower tail of ghspec and the upper tail of chatdev. Bootstrap 95% CIs around medians (as used in the study) provide an appropriate uncertainty summary under non-normality. Data quality is generally strong given sample size, but the presence of outliers and heteroscedasticity warrants robust inference (Kruskal–Wallis or Mann–Whitney) and possibly log transformation to stabilize variance.

### Camera-Ready Paragraph

Figure: violin_plot_tokens_in.svg visualized the distribution of Input Tokens (count) across three frameworks (N=100 per framework) and revealed large between-group differences. ghspec exhibited the highest central tendency and the widest spread, chatdev showed intermediate but highly variable counts, and baes was tightly concentrated at a low level. Normality tests (Shapiro–Wilk) were significant for all frameworks (p<0.05), and two frameworks displayed high skewness (|skew| > 1), indicating that median- and rank-based summaries were more appropriate than means. Outliers were detected for ghspec and chatdev using the 1.5×IQR rule. Descriptively, the mean for ghspec exceeded baes by 724.4% (294,721 vs. 35,750 tokens), demonstrating a pronounced practical effect. These patterns supported the hypothesis that frameworks differ markedly in input token requirements and motivate nonparametric inference (e.g., Kruskal–Wallis with post hoc pairwise tests). The figure indicates that ghspec typically requires substantially more input tokens than chatdev and baes, while baes operates in a comparatively resource-efficient regime. This suggests meaningful operational cost and scalability implications tied to framework choice.

### Actionable Recommendations

Interpret differences using robust statistics: report medians, IQRs, and bootstrap 95% CIs, not just means. Conduct a Kruskal–Wallis test followed by Holm-adjusted Dunn pairwise comparisons, and quantify effects with rank-biserial or Cliff’s delta. Because variance scales with the mean, consider a log transformation or compare coefficients of variation to normalize heteroscedasticity. Inspect and report outliers transparently; perform sensitivity analyses with and without extremes. Investigate task- or dataset-level factors that may explain the heavy tails in ghspec and chatdev. For presentation, add median markers and CI notches inside the violins, overlay jittered points to show sample density, and use a log-scaled y-axis to improve readability across orders of magnitude. Clearly state N per framework and the non-normality diagnostics in the caption.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 54.7s
- Token Usage: 5,072 tokens (1,721 prompt + 3,351 completion)
- Estimated Cost: $0.0000 USD
