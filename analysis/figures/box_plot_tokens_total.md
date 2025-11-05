# Visualization Documentation: box_plot_tokens_total.svg

**Visualization Type**: Boxplot  
**Metric**: tokens_total  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:40:26.729854Z

---

## Rationale

This Boxplot visualization was generated to compare Total Tokens (count) performance across ghspec, baes, chatdev. The box plot shows median, quartiles, and outliers to enable robust comparison of distributions.

**Interpretation Guidance**: Box plots use median (50th percentile) as the central measure, making them robust to outliers. When comparing groups: (1) Check for box overlap—minimal overlap suggests different distributions. (2) Examine outliers (points beyond whiskers)—these may indicate data quality issues or extreme cases worth investigating. (3) Compare IQR widths—larger IQR indicates higher variability. For statistical testing: If boxes show non-normal patterns (asymmetric, heavy outliers), prefer non-parametric tests (Mann-Whitney U, Kruskal-Wallis) over t-tests/ANOVA.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 347210.760 | 338787.000 | [332269.000, 356658.000] | 38116.260 | 274758.000 | 464365.000 | 319176.750 | 370940.500 | 1 | 100 |
| baes | 45122.300 | 44198.500 | [44190.000, 44213.500] | 1529.463 | 44120.000 | 50218.000 | 44177.500 | 47190.500 | 0 | 100 |
| chatdev | 205467.960 | 193778.500 | [186545.000, 201611.000] | 41986.351 | 139789.000 | 365531.000 | 181751.250 | 225626.500 | 3 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The boxplot reveals Total Tokens (count) patterns across frameworks. baes shows the lowest mean (45122.300), while ghspec exhibits the highest (347210.760), representing a 669.5% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The boxplot compares Total Tokens across ghspec, baes, and chatdev. Visibly, ghspec shows the highest central tendency with a median near the mid-300k range and the widest IQR, indicating substantial variability. chatdev is intermediate with a median around 190–200k and moderate spread. baes exhibits the lowest token usage with a compact IQR centered near 45–50k, implying stable, low consumption. Boxes for all three groups show minimal overlap; baes is clearly separated from the others, and ghspec and chatdev have non-overlapping boxes with whiskers that nearly touch. Outliers are present for ghspec and chatdev (red points above the upper whiskers), suggesting rare, high-cost runs that warrant inspection. Shapiro–Wilk normality checks indicated non-normality for 3/3 groups (p<0.05), justifying emphasis on medians, IQRs, and bootstrap 95% confidence intervals. The mean difference between the extremes is large (ghspec mean ≈347,211 vs. baes mean ≈45,122; +669.5%), and median ratios appear similarly large, providing a strong practical effect size. Skewness is evident for at least two frameworks (|skew|>1), reinforcing that the mean is less reliable than the median. Given the visual CI separation and distributional differences, a non-parametric omnibus test (Kruskal–Wallis) is appropriate; subsequent pairwise comparisons (e.g., Dunn tests with Holm correction) would likely confirm significant differences. No missing data are apparent; the main data-quality concern is the influence of high-end outliers on interpretation.

### Camera-Ready Paragraph

Figure: box_plot_tokens_total.svg visualized Total Tokens (count) across three frameworks. The analysis revealed that ghspec had the highest token consumption with a broad interquartile range, chatdev was intermediate with moderate spread, and baes had the lowest and most compact distribution. Shapiro–Wilk tests indicated non-normality for all groups (p<0.05), so medians, interquartile ranges, and bootstrap 95% confidence intervals were emphasized. Boxes showed minimal overlap across frameworks; baes was fully separated from the others, and ghspec and chatdev exhibited non-overlapping boxes with whiskers in close proximity. Outliers were detected for ghspec and chatdev, reflecting occasional high-cost runs. The effect sizes were substantial in practical terms: the mean for ghspec exceeded baes by approximately 669.5%, and the medians suggested similarly large ratios. This suggests pronounced framework-dependent differences in token usage. In relation to the research questions, the figure supports the hypothesis that frameworks differ materially in token demand, with baes being the most efficient and ghspec the most expensive. Because distributions were skewed, a Kruskal–Wallis test with post hoc Dunn comparisons is appropriate to confirm group differences; the visual separation and CI behavior imply statistically meaningful contrasts.

### Actionable Recommendations

Interpretation: Treat medians and IQRs as primary metrics; the large separation indicates that baes is consistently more token-efficient, chatdev is moderate, and ghspec is costly with higher variability. Follow-up analyses: Run a Kruskal–Wallis test followed by Dunn tests (Holm-adjusted) and report effect sizes (Cliff’s delta or rank-biserial) for each pair. Provide bootstrap 95% CIs for medians and, optionally, analyze log-transformed tokens to assess multiplicative differences. Investigate outlier runs in ghspec and chatdev to determine whether they arise from specific prompts or failure modes. Limitations: Non-normal, skewed distributions and potential heterogeneity across tasks may influence generalizability. Presentation tips: Include sample sizes (N=100/group), annotate medians and CIs on the plot, consider a log-scale y-axis for readability, and describe the outlier definition (1.5×IQR) in the caption.

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 48.8s
- Token Usage: 4,122 tokens (1,740 prompt + 2,382 completion)
- Estimated Cost: $0.0000 USD
