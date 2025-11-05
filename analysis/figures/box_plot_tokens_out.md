# Visualization Documentation: box_plot_tokens_out.svg

**Visualization Type**: Boxplot  
**Metric**: tokens_out  
**Frameworks**: ghspec, baes, chatdev  
**Generated**: 2025-11-03T11:36:32.462834Z

---

## Rationale

This Boxplot visualization was generated to compare Output Tokens (count) performance across ghspec, baes, chatdev. The box plot shows median, quartiles, and outliers to enable robust comparison of distributions.

**Interpretation Guidance**: Box plots use median (50th percentile) as the central measure, making them robust to outliers. When comparing groups: (1) Check for box overlap—minimal overlap suggests different distributions. (2) Examine outliers (points beyond whiskers)—these may indicate data quality issues or extreme cases worth investigating. (3) Compare IQR widths—larger IQR indicates higher variability. For statistical testing: If boxes show non-normal patterns (asymmetric, heavy outliers), prefer non-parametric tests (Mann-Whitney U, Kruskal-Wallis) over t-tests/ANOVA.

---

## Data

| Framework | Mean | Median | Median 95% CI | Std Dev | Min | Max | Q1 | Q3 | Outliers | N |
|-----------|------|--------|---------------|---------|-----|-----|----|----|----------|---|
| ghspec | 52490.180 | 51643.000 | [50609.000, 53956.000] | 6351.669 | 38737.000 | 72642.000 | 47675.250 | 56534.250 | 2 | 100 |
| baes | 9372.010 | 9031.500 | [9023.000, 9046.500] | 576.600 | 8953.000 | 11281.000 | 9010.500 | 10138.500 | 0 | 100 |
| chatdev | 50550.520 | 48016.500 | [45467.000, 49658.000] | 10145.859 | 35241.000 | 83436.000 | 43469.250 | 54369.500 | 6 | 100 |

**Statistical Concepts**:
- **95% Confidence Interval (CI)**: A confidence interval shows the range where the true value likely falls. A 95% CI means if we repeated this experiment 100 times, about 95 would produce intervals containing the true value.
- **Outliers**: Interquartile Range (IQR) measures spread using middle 50% of data. Q1 is 25th percentile, Q3 is 75th percentile, IQR = Q3-Q1. Values >1.5×IQR beyond Q3 or <1.5×IQR below Q1 are outliers.
- **Q1/Q3**: Quartiles dividing data into quarters; Q1=25th percentile, Q3=75th percentile.


---

## Analysis

The boxplot reveals Output Tokens (count) patterns across frameworks. baes shows the lowest mean (9372.010), while ghspec exhibits the highest (52490.180), representing a 460.1% relative difference. **Statistical Assumptions**: Normality testing (Shapiro-Wilk) indicates non-normal distributions for 3/3 framework(s). Robust alternatives recommended: median-based comparisons and non-parametric tests (Mann-Whitney U, Kruskal-Wallis) for hypothesis testing. 

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

The boxplot compares Output Tokens across ghspec, baes, and chatdev with N=100 per framework. Visually, baes exhibited a much lower central tendency (~9–10k tokens) with a tight IQR, while ghspec and chatdev clustered around substantially higher medians (~51k and ~48k, respectively). The IQR of baes did not overlap with either ghspec or chatdev, indicating a large practical separation. ghspec showed the highest central tendency and a moderate IQR; chatdev displayed a wider spread and more extreme high-end outliers (≈70–85k), suggesting greater variability. Outliers were evident in ghspec and chatdev, consistent with long right tails. Programmatic checks reported non-normality for all frameworks (Shapiro–Wilk p<0.05 for 3/3) and high skewness in two, justifying median-based summaries and non-parametric inference. The mean contrast was large (baes 9,372 vs. ghspec 52,490; +460.1%), but means are less reliable under skew. Median bootstrap 95% CIs (reported methodology) would be informative; given the non-overlapping boxes, CI overlap between baes and the others is unlikely, whereas ghspec and chatdev likely show partial overlap. The distributional differences imply large effect sizes (e.g., Cliff’s delta) for baes vs. the other two, and a smaller, possibly moderate effect between ghspec and chatdev. Data quality concerns center on heavy-tailed behavior and multiple outliers, particularly for chatdev, warranting sensitivity analyses to assess their influence.

### Camera-Ready Paragraph

Figure: box_plot_tokens_out.svg contrasted the distributions of Output Tokens across three frameworks. The visualization showed that baes produced substantially fewer tokens, with a low median near 9–10k and a compact interquartile range, whereas ghspec and chatdev exhibited much higher medians (~51k and ~48k, respectively). Outliers were present for ghspec and chatdev, including several extreme high values, indicating heavy right tails. Shapiro–Wilk tests indicated non-normality for all groups (p<0.05), and two frameworks displayed high skewness (|skew|>1), supporting the use of median-based summaries and non-parametric tests. The practical separation was large: the mean for ghspec (52,490) exceeded that of baes (9,372) by 460.1%. Non-overlapping boxes for baes versus the other frameworks suggested large effects, while the partial overlap between ghspec and chatdev implied a smaller difference. These results supported the hypothesis that frameworks differ in token usage and indicate that baes is markedly more token-efficient, whereas ghspec and chatdev generate higher and more variable output volumes. This suggests researchers should adopt non-parametric comparisons (e.g., Kruskal–Wallis with post hoc Dunn tests and effect sizes such as Cliff’s delta) to quantify these differences and report bootstrap 95% confidence intervals for medians.

### Actionable Recommendations

Interpret the figure as strong evidence of differing token budgets: baes is token-efficient, while ghspec and chatdev are verbose, with chatdev showing higher variability and more extreme runs. For inference, run a Kruskal–Wallis test followed by Dunn–Bonferroni pairwise comparisons, and report effect sizes (Cliff’s delta or rank-biserial r) with bootstrap 95% CIs for medians. Conduct sensitivity checks by trimming or Winsorizing to assess outlier influence and by stratifying runs (e.g., task complexity) to rule out confounding. Avoid relying on means due to skew; emphasize medians, IQR, and robust dispersion (MAD). In publication, annotate medians and sample sizes on the plot, and note non-normality (Shapiro–Wilk p<0.05). Consider adding violin or ECDF overlays to convey tail behavior and reproducibility details (seeds, prompts, versions).

---

**Analysis Metadata**:
- Model: gpt-5
- Generation Time: 51.9s
- Token Usage: 4,519 tokens (1,740 prompt + 2,779 completion)
- Estimated Cost: $0.0000 USD
