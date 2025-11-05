# 🚀 Quick Start: How to Read This Statistical Report
*Don't know statistics? No problem! This guide will help you navigate.*

## 📍 Where to Start
**If you just want the key findings:**
1. Jump to the "Executive Summary" section below
2. Look at the visualizations (pictures tell the story!)
3. Read the "Key Findings" bullets

**If you want to understand the statistics:**
1. Each statistical test has a 📚 "Understanding" section
2. Start with the "What is this test?" paragraph
3. Skip the technical details unless you're curious
4. Focus on the "How to interpret" section

## 🎨 Icon Guide
We use emojis to make the report easier to scan:

- 📚 **Understanding** = What/Why explanations
- 💡 **Why** = Rationale and reasoning
- 📊 **Results** = Numbers and findings
- 🎓 **Interpret** = What it means in plain English
- ✅ **Recommendation** = What to do next
- ⚠️ **Warning** = Important limitations or concerns
- 📏 **Effect Size** = How big is the difference?
- ⚡ **Power** = Can we trust these results?

## ⏭️ What You Can Skip (If You Want)
These sections are for statistical review - feel free to skip:

- Assumption validation details
- Q-Q plots (unless you're checking normality)
- Detailed test statistics
- Methodology section (unless needed for peer review)

## 📖 Key Terms in 10 Seconds
- **p-value**: Probability results are due to chance (lower = more confident)
- **Effect size**: How big is the difference? (more important than p-value!)
- **Confidence interval**: Range where true value likely falls (95% sure)
- **Power**: Ability to detect real effects (want 80%+)
- **Significant**: Unlikely to be random chance (p < 0.05)

## ❓ Common Questions

**Q: What's more important - p-value or effect size?**
A: Effect size! A tiny, meaningless difference can have p < 0.05 with enough data. Focus on whether the effect size is large enough to matter.

**Q: What if the test says 'not significant'?**
A: This means there's insufficient evidence to conclude a difference exists. This could indicate (1) truly similar distributions, (2) a difference too small to detect, or (3) inadequate sample size. **Always check the power analysis!** If power < 80%, the sample may be too small to detect real differences.

**Q: Which plot should I include in my paper?**
A: Box plots show distributions clearly. Forest plots show effect sizes with uncertainty. Pick what tells your story best.

**Q: What's the difference between t-test and Mann-Whitney?**
A: Both compare two groups. t-test assumes normal data. Mann-Whitney doesn't - use it when data is skewed or has outliers.

## 📋 Your Report at a Glance
- Experiment: experiment_baes_vs_chatdev_vs_ghspec
- Metrics analyzed: 7
- Statistical tests performed: 7
- Significant results: 7/7
- Large effect sizes: 20/21

---


---
## Table of Contents

1. [Descriptive Statistics](#descriptive-statistics)
2. [Normality Assessment](#normality-assessment)
3. [Assumption Validation](#assumption-validation)
4. [Statistical Comparisons](#statistical-comparisons)
5. [Statistical Methodology](#statistical-methodology)
6. [Glossary](#glossary)

---

## 1. Descriptive Statistics

### api_calls

| Framework | n | Mean | Median | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis | Outliers |
|-----------|---|------|--------|---------|-----|-----|----|----|-----|----------|----------|----------|
| ghspec | 100 | **89.91** | 89.00 | **10.09** | 70.00 | 116.00 | 82.00 | 97.25 | 15.25 | 0.47 | -0.52 | 0 |
| baes | 100 | 18.31 | **18.00** | 0.51 | 18.00 | 20.00 | 18.00 | 19.00 | **1.00** | 1.28 | 0.58 | 0 |
| chatdev | 100 | **116.01** | 111.00 | **20.05** | 85.00 | 172.00 | 103.00 | 129.25 | 26.25 | 0.46 | -0.46 | 1 |

**ghspec**: The mean value is 89.91 (SD: 10.09), with a median of 89.00 and IQR of 15.25. *Distribution is nearly symmetric; mean ± SD appropriate.*

**baes**: The median value is 18.00 with an IQR of 1.00, indicating typical performance and variability. (Mean: 18.31, SD: 0.51). *High skewness detected; median strongly preferred over mean.*

**chatdev**: The mean value is 116.01 (SD: 20.05), with a median of 111.00 and IQR of 26.25. *Distribution is nearly symmetric; mean ± SD appropriate.*

### cached_tokens

| Framework | n | Mean | Median | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis | Outliers |
|-----------|---|------|--------|---------|-----|-----|----|----|-----|----------|----------|----------|
| ghspec | 100 | **149184.00** | 147008.00 | **20169.20** | 113920.00 | 201600.00 | 133728.00 | 160992.00 | 27264.00 | 0.45 | -0.45 | 0 |
| baes | 100 | 69.12 | **0.00** | 402.89 | 0.00 | 2688.00 | 0.00 | 0.00 | **0.00** | 5.81 | 32.63 | 3 |
| chatdev | 100 | 10056.96 | **7872.00** | 7654.75 | 0.00 | 39424.00 | 5184.00 | 12288.00 | **7104.00** | 1.65 | 2.58 | 9 |

**⚠️ Note on Skewness**: This metric shows severe skewness (|skewness| > 2.0) for some frameworks. **Median and IQR are emphasized** (shown in bold) as they are more robust to outliers and extreme values than mean and standard deviation. The median represents the center of the distribution, while IQR captures the spread of the middle 50% of values.

**ghspec**: The mean value is 149184.00 (SD: 20169.20), with a median of 147008.00 and IQR of 27264.00. *Distribution is nearly symmetric; mean ± SD appropriate.*

**baes**: The median value is 0.00 with an IQR of 0.00, indicating typical performance and variability. (Mean: 69.12, SD: 402.89). *Severe skewness (5.81) detected; mean is substantially biased by extreme values. Median provides more accurate central tendency.*

**chatdev**: The median value is 7872.00 with an IQR of 7104.00, indicating typical performance and variability. (Mean: 10056.96, SD: 7654.75). *High skewness detected; median strongly preferred over mean.*

### execution_time

| Framework | n | Mean | Median | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis | Outliers |
|-----------|---|------|--------|---------|-----|-----|----|----|-----|----------|----------|----------|
| ghspec | 100 | **973.93** | 971.11 | **171.45** | 572.16 | 1440.58 | 885.39 | 1065.04 | 179.65 | 0.10 | 0.35 | 5 |
| baes | 100 | 206.31 | **210.02** | 37.93 | 128.54 | 409.45 | 186.65 | 225.77 | **39.11** | 1.32 | 6.85 | 1 |
| chatdev | 100 | 1238.11 | **1195.21** | 303.45 | 600.24 | 2057.13 | 1039.52 | 1313.35 | **273.84** | 0.95 | 0.48 | 11 |

**ghspec**: The mean value is 973.93 (SD: 171.45), with a median of 971.11 and IQR of 179.65. *Distribution is nearly symmetric; mean ± SD appropriate.*

**baes**: The median value is 210.02 with an IQR of 39.11, indicating typical performance and variability. (Mean: 206.31, SD: 37.93). *High skewness detected; median strongly preferred over mean.*

**chatdev**: The median value is 1195.21 with an IQR of 273.84, indicating typical performance and variability. (Mean: 1238.11, SD: 303.45). *Moderate skewness detected; median and IQR are more robust.*

### tokens_in

| Framework | n | Mean | Median | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis | Outliers |
|-----------|---|------|--------|---------|-----|-----|----|----|-----|----------|----------|----------|
| ghspec | 100 | 294720.58 | **288673.50** | 32567.51 | 234785.00 | 394313.00 | 269970.75 | 315616.00 | **45645.25** | 0.56 | -0.12 | 1 |
| baes | 100 | 35750.29 | **35167.00** | 953.22 | 35167.00 | 38937.00 | 35167.00 | 37052.00 | **1885.00** | 1.29 | 0.60 | 0 |
| chatdev | 100 | 154917.44 | **146999.50** | 32749.36 | 102986.00 | 282095.00 | 135513.75 | 173201.75 | **37688.00** | 1.08 | 1.50 | 3 |

**ghspec**: The median value is 288673.50 with an IQR of 45645.25, indicating typical performance and variability. (Mean: 294720.58, SD: 32567.51). *Moderate skewness detected; median and IQR are more robust.*

**baes**: The median value is 35167.00 with an IQR of 1885.00, indicating typical performance and variability. (Mean: 35750.29, SD: 953.22). *High skewness detected; median strongly preferred over mean.*

**chatdev**: The median value is 146999.50 with an IQR of 37688.00, indicating typical performance and variability. (Mean: 154917.44, SD: 32749.36). *High skewness detected; median strongly preferred over mean.*

### tokens_out

| Framework | n | Mean | Median | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis | Outliers |
|-----------|---|------|--------|---------|-----|-----|----|----|-----|----------|----------|----------|
| ghspec | 100 | 52490.18 | **51643.00** | 6351.67 | 38737.00 | 72642.00 | 47675.25 | 56534.25 | **8859.00** | 0.51 | 0.41 | 2 |
| baes | 100 | 9372.01 | **9031.50** | 576.60 | 8953.00 | 11281.00 | 9010.50 | 10138.50 | **1128.00** | 1.26 | 0.47 | 0 |
| chatdev | 100 | 50550.52 | **48016.50** | 10145.86 | 35241.00 | 83436.00 | 43469.25 | 54369.50 | **10900.25** | 1.25 | 1.04 | 6 |

**ghspec**: The median value is 51643.00 with an IQR of 8859.00, indicating typical performance and variability. (Mean: 52490.18, SD: 6351.67). *Moderate skewness detected; median and IQR are more robust.*

**baes**: The median value is 9031.50 with an IQR of 1128.00, indicating typical performance and variability. (Mean: 9372.01, SD: 576.60). *High skewness detected; median strongly preferred over mean.*

**chatdev**: The median value is 48016.50 with an IQR of 10900.25, indicating typical performance and variability. (Mean: 50550.52, SD: 10145.86). *High skewness detected; median strongly preferred over mean.*

### tokens_total

| Framework | n | Mean | Median | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis | Outliers |
|-----------|---|------|--------|---------|-----|-----|----|----|-----|----------|----------|----------|
| ghspec | 100 | 347210.76 | **338787.00** | 38116.26 | 274758.00 | 464365.00 | 319176.75 | 370940.50 | **51763.75** | 0.53 | -0.08 | 1 |
| baes | 100 | 45122.30 | **44198.50** | 1529.46 | 44120.00 | 50218.00 | 44177.50 | 47190.50 | **3013.00** | 1.28 | 0.55 | 0 |
| chatdev | 100 | 205467.96 | **193778.50** | 41986.35 | 139789.00 | 365531.00 | 181751.25 | 225626.50 | **43875.25** | 1.08 | 1.22 | 3 |

**ghspec**: The median value is 338787.00 with an IQR of 51763.75, indicating typical performance and variability. (Mean: 347210.76, SD: 38116.26). *Moderate skewness detected; median and IQR are more robust.*

**baes**: The median value is 44198.50 with an IQR of 3013.00, indicating typical performance and variability. (Mean: 45122.30, SD: 1529.46). *High skewness detected; median strongly preferred over mean.*

**chatdev**: The median value is 193778.50 with an IQR of 43875.25, indicating typical performance and variability. (Mean: 205467.96, SD: 41986.35). *High skewness detected; median strongly preferred over mean.*

### total_cost_usd

| Framework | n | Mean | Median | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis | Outliers |
|-----------|---|------|--------|---------|-----|-----|----|----|-----|----------|----------|----------|
| ghspec | 100 | 0.06451 | **0.06358** | 0.00711 | 0.05001 | 0.08718 | 0.05935 | 0.06852 | **0.00918** | 0.59 | 0.51 | 2 |
| baes | 100 | 0.01098 | **0.01069** | 0.00049 | 0.01049 | 0.01261 | 0.01068 | 0.01164 | **0.00096** | 1.25 | 0.47 | 0 |
| chatdev | 100 | 0.05281 | **0.04969** | 0.01027 | 0.03745 | 0.09001 | 0.04620 | 0.05825 | **0.01205** | 1.11 | 0.93 | 3 |

**ghspec**: The median value is 0.06 with an IQR of 0.01, indicating typical performance and variability. (Mean: 0.06, SD: 0.01). *Moderate skewness detected; median and IQR are more robust.*

**baes**: The median value is 0.01 with an IQR of 0.00, indicating typical performance and variability. (Mean: 0.01, SD: 0.00). *High skewness detected; median strongly preferred over mean.*

**chatdev**: The median value is 0.05 with an IQR of 0.01, indicating typical performance and variability. (Mean: 0.05, SD: 0.01). *High skewness detected; median strongly preferred over mean.*

## 2. Normality Assessment

### Shapiro-Wilk Test Results

| Metric | Framework | W-statistic | p-value | Result | Interpretation |
|--------|-----------|-------------|---------|--------|----------------|
| api_calls | ghspec | 0.9680 | p = 0.016 | ❌ Non-normal | Shapiro-Wilk test for ghspec: W=0.9680, p = 0.016. Data deviates from normality (α=0.05). |
| api_calls | baes | 0.6029 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for baes: W=0.6029, p < 0.001. Data deviates from normality (α=0.05). |
| api_calls | chatdev | 0.9613 | p = 0.005 | ❌ Non-normal | Shapiro-Wilk test for chatdev: W=0.9613, p = 0.005. Data deviates from normality (α=0.05). |
| cached_tokens | ghspec | 0.9700 | p = 0.022 | ❌ Non-normal | Shapiro-Wilk test for ghspec: W=0.9700, p = 0.022. Data deviates from normality (α=0.05). |
| cached_tokens | baes | 0.1621 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for baes: W=0.1621, p < 0.001. Data deviates from normality (α=0.05). |
| cached_tokens | chatdev | 0.8319 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for chatdev: W=0.8319, p < 0.001. Data deviates from normality (α=0.05). |
| execution_time | ghspec | 0.9841 | p = 0.275 | ✅ Normal | Shapiro-Wilk test for ghspec: W=0.9841, p = 0.275. Data appears normally distributed (α=0.05). |
| execution_time | baes | 0.9080 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for baes: W=0.9080, p < 0.001. Data deviates from normality (α=0.05). |
| execution_time | chatdev | 0.9156 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for chatdev: W=0.9156, p < 0.001. Data deviates from normality (α=0.05). |
| tokens_in | ghspec | 0.9720 | p = 0.032 | ❌ Non-normal | Shapiro-Wilk test for ghspec: W=0.9720, p = 0.032. Data deviates from normality (α=0.05). |
| tokens_in | baes | 0.6039 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for baes: W=0.6039, p < 0.001. Data deviates from normality (α=0.05). |
| tokens_in | chatdev | 0.9285 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for chatdev: W=0.9285, p < 0.001. Data deviates from normality (α=0.05). |
| tokens_out | ghspec | 0.9804 | p = 0.142 | ✅ Normal | Shapiro-Wilk test for ghspec: W=0.9804, p = 0.142. Data appears normally distributed (α=0.05). |
| tokens_out | baes | 0.6450 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for baes: W=0.6450, p < 0.001. Data deviates from normality (α=0.05). |
| tokens_out | chatdev | 0.8815 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for chatdev: W=0.8815, p < 0.001. Data deviates from normality (α=0.05). |
| tokens_total | ghspec | 0.9747 | p = 0.051 | ✅ Normal | Shapiro-Wilk test for ghspec: W=0.9747, p = 0.051. Data appears normally distributed (α=0.05). |
| tokens_total | baes | 0.6195 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for baes: W=0.6195, p < 0.001. Data deviates from normality (α=0.05). |
| tokens_total | chatdev | 0.9185 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for chatdev: W=0.9185, p < 0.001. Data deviates from normality (α=0.05). |
| total_cost_usd | ghspec | 0.9735 | p = 0.041 | ❌ Non-normal | Shapiro-Wilk test for ghspec: W=0.9735, p = 0.041. Data deviates from normality (α=0.05). |
| total_cost_usd | baes | 0.6579 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for baes: W=0.6579, p < 0.001. Data deviates from normality (α=0.05). |
| total_cost_usd | chatdev | 0.9054 | p < 0.001 | ❌ Non-normal | Shapiro-Wilk test for chatdev: W=0.9054, p < 0.001. Data deviates from normality (α=0.05). |

## 3. Assumption Validation

### Levene's Test (Variance Homogeneity)

| Metric | Frameworks | W-statistic | p-value | Result | Recommendation |
|--------|------------|-------------|---------|--------|----------------|
| api_calls | ghspec, baes, chatdev | 96.0689 | p < 0.001 | ❌ Unequal variances | Consider using Welch's ANOVA (does not assume equal variances) or non-parametric Kruskal-Wallis test. |
| cached_tokens | ghspec, baes, chatdev | 132.4420 | p < 0.001 | ❌ Unequal variances | Consider using Welch's ANOVA (does not assume equal variances) or non-parametric Kruskal-Wallis test. |
| execution_time | ghspec, baes, chatdev | 51.5664 | p < 0.001 | ❌ Unequal variances | Consider using Welch's ANOVA (does not assume equal variances) or non-parametric Kruskal-Wallis test. |
| tokens_in | ghspec, baes, chatdev | 64.9845 | p < 0.001 | ❌ Unequal variances | Consider using Welch's ANOVA (does not assume equal variances) or non-parametric Kruskal-Wallis test. |
| tokens_out | ghspec, baes, chatdev | 54.1874 | p < 0.001 | ❌ Unequal variances | Consider using Welch's ANOVA (does not assume equal variances) or non-parametric Kruskal-Wallis test. |
| tokens_total | ghspec, baes, chatdev | 60.6563 | p < 0.001 | ❌ Unequal variances | Consider using Welch's ANOVA (does not assume equal variances) or non-parametric Kruskal-Wallis test. |
| total_cost_usd | ghspec, baes, chatdev | 55.6738 | p < 0.001 | ❌ Unequal variances | Consider using Welch's ANOVA (does not assume equal variances) or non-parametric Kruskal-Wallis test. |

## 4. Statistical Comparisons

### api_calls

### 📚 Understanding the Kruskal Wallis

**What is this test?**

The Kruskal-Wallis test compares three or more groups without assuming normality

**💡 Why did we use it?**

It's a robust alternative to ANOVA when data is skewed or has outliers

*Specific reason:* Kruskal-Wallis test selected: at least one group non-normally distributed (Shapiro-Wilk p≤0.05). Non-parametric test appropriate.

**📊 What did we find?**

- Groups compared: ghspec, baes, chatdev

- Test statistic: 241.6996

- p < 0.001

- Result: Significant difference detected

**🎓 How to interpret this:**

At least one group shows a different distribution pattern from the others


*In plain English:* Comparing 3 groups (ghspec, baes, chatdev): Significant differences detected (p < 0.001, α=0.05). At least one group differs.


**ℹ️ Technical note:** Makes fewer assumptions than ANOVA - works with any distribution shape

#### Effect Sizes

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs baes

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in baes 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs chatdev

- Cliff's Delta = -0.766

- 95% Confidence Interval: [-0.848, -0.672]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -0.766 [-0.848, -0.672]: large effect size. ghspec has systematically lower values compared to chatdev (probability: 11.7%).


Bottom line: ghspec tended to show lower values than chatdev 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: baes vs chatdev

- Cliff's Delta = -1.000

- 95% Confidence Interval: [-1.000, -1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -1.000 [-1.000, -1.000]: large effect size. all observed values in baes are less than those in chatdev.


Bottom line: baes in this sample, all observed values in baes were less than those in chatdev 
with a **large** effect size.

### cached_tokens

### 📚 Understanding the Kruskal Wallis

**What is this test?**

The Kruskal-Wallis test compares three or more groups without assuming normality

**💡 Why did we use it?**

It's a robust alternative to ANOVA when data is skewed or has outliers

*Specific reason:* Kruskal-Wallis test selected: at least one group non-normally distributed (Shapiro-Wilk p≤0.05). Non-parametric test appropriate.

**📊 What did we find?**

- Groups compared: ghspec, baes, chatdev

- Test statistic: 273.5239

- p < 0.001

- Result: Significant difference detected

**🎓 How to interpret this:**

At least one group shows a different distribution pattern from the others


*In plain English:* Comparing 3 groups (ghspec, baes, chatdev): Significant differences detected (p < 0.001, α=0.05). At least one group differs.


**ℹ️ Technical note:** Makes fewer assumptions than ANOVA - works with any distribution shape

#### Effect Sizes

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs baes

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in baes 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs chatdev

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in chatdev.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in chatdev 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: baes vs chatdev

- Cliff's Delta = -0.986

- 95% Confidence Interval: [-1.000, -0.963]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -0.986 [-1.000, -0.963]: large effect size. baes has systematically lower values compared to chatdev (probability: 0.7%).


Bottom line: baes tended to show lower values than chatdev 
with a **large** effect size.

### execution_time

### 📚 Understanding the Kruskal Wallis

**What is this test?**

The Kruskal-Wallis test compares three or more groups without assuming normality

**💡 Why did we use it?**

It's a robust alternative to ANOVA when data is skewed or has outliers

*Specific reason:* Kruskal-Wallis test selected: at least one group non-normally distributed (Shapiro-Wilk p≤0.05). Non-parametric test appropriate.

**📊 What did we find?**

- Groups compared: ghspec, baes, chatdev

- Test statistic: 221.0146

- p < 0.001

- Result: Significant difference detected

**🎓 How to interpret this:**

At least one group shows a different distribution pattern from the others


*In plain English:* Comparing 3 groups (ghspec, baes, chatdev): Significant differences detected (p < 0.001, α=0.05). At least one group differs.


**ℹ️ Technical note:** Makes fewer assumptions than ANOVA - works with any distribution shape

#### Effect Sizes

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs baes

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in baes 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs chatdev

- Cliff's Delta = -0.571

- 95% Confidence Interval: [-0.689, -0.444]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing amateur athletes to semi-professionals - distinct groups


**✅ What this means for your research:**

Cliff's Delta = -0.571 [-0.689, -0.444]: large effect size. ghspec has systematically lower values compared to chatdev (probability: 21.4%).


Bottom line: ghspec tended to show lower values than chatdev 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: baes vs chatdev

- Cliff's Delta = -1.000

- 95% Confidence Interval: [-1.000, -1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -1.000 [-1.000, -1.000]: large effect size. all observed values in baes are less than those in chatdev.


Bottom line: baes in this sample, all observed values in baes were less than those in chatdev 
with a **large** effect size.

### tokens_in

### 📚 Understanding the Kruskal Wallis

**What is this test?**

The Kruskal-Wallis test compares three or more groups without assuming normality

**💡 Why did we use it?**

It's a robust alternative to ANOVA when data is skewed or has outliers

*Specific reason:* Kruskal-Wallis test selected: at least one group non-normally distributed (Shapiro-Wilk p≤0.05). Non-parametric test appropriate.

**📊 What did we find?**

- Groups compared: ghspec, baes, chatdev

- Test statistic: 268.2744

- p < 0.001

- Result: Significant difference detected

**🎓 How to interpret this:**

At least one group shows a different distribution pattern from the others


*In plain English:* Comparing 3 groups (ghspec, baes, chatdev): Significant differences detected (p < 0.001, α=0.05). At least one group differs.


**ℹ️ Technical note:** Makes fewer assumptions than ANOVA - works with any distribution shape

#### Effect Sizes

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs baes

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in baes 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs chatdev

- Cliff's Delta = 0.991

- 95% Confidence Interval: [0.971, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 0.991 [0.971, 1.000]: large effect size. ghspec has systematically higher values compared to chatdev (probability: 99.5%).


Bottom line: ghspec tended to show higher values than chatdev (99.5% estimated ) 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: baes vs chatdev

- Cliff's Delta = -1.000

- 95% Confidence Interval: [-1.000, -1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -1.000 [-1.000, -1.000]: large effect size. all observed values in baes are less than those in chatdev.


Bottom line: baes in this sample, all observed values in baes were less than those in chatdev 
with a **large** effect size.

### tokens_out

### 📚 Understanding the Kruskal Wallis

**What is this test?**

The Kruskal-Wallis test compares three or more groups without assuming normality

**💡 Why did we use it?**

It's a robust alternative to ANOVA when data is skewed or has outliers

*Specific reason:* Kruskal-Wallis test selected: at least one group non-normally distributed (Shapiro-Wilk p≤0.05). Non-parametric test appropriate.

**📊 What did we find?**

- Groups compared: ghspec, baes, chatdev

- Test statistic: 204.0254

- p < 0.001

- Result: Significant difference detected

**🎓 How to interpret this:**

At least one group shows a different distribution pattern from the others


*In plain English:* Comparing 3 groups (ghspec, baes, chatdev): Significant differences detected (p < 0.001, α=0.05). At least one group differs.


**ℹ️ Technical note:** Makes fewer assumptions than ANOVA - works with any distribution shape

#### Effect Sizes

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs baes

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in baes 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs chatdev

- Cliff's Delta = 0.266

- 95% Confidence Interval: [0.105, 0.425]

- Magnitude: **SMALL**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

👉 0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

   ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing test scores of B students vs A students - overlap but clearly different


**✅ What this means for your research:**

Cliff's Delta = 0.266 [0.105, 0.425]: small effect size. ghspec has systematically higher values compared to chatdev (probability: 63.3%).


Bottom line: ghspec tended to show higher values than chatdev (63.3% estimated ) 
with a **small** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: baes vs chatdev

- Cliff's Delta = -1.000

- 95% Confidence Interval: [-1.000, -1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -1.000 [-1.000, -1.000]: large effect size. all observed values in baes are less than those in chatdev.


Bottom line: baes in this sample, all observed values in baes were less than those in chatdev 
with a **large** effect size.

### tokens_total

### 📚 Understanding the Kruskal Wallis

**What is this test?**

The Kruskal-Wallis test compares three or more groups without assuming normality

**💡 Why did we use it?**

It's a robust alternative to ANOVA when data is skewed or has outliers

*Specific reason:* Kruskal-Wallis test selected: at least one group non-normally distributed (Shapiro-Wilk p≤0.05). Non-parametric test appropriate.

**📊 What did we find?**

- Groups compared: ghspec, baes, chatdev

- Test statistic: 262.9445

- p < 0.001

- Result: Significant difference detected

**🎓 How to interpret this:**

At least one group shows a different distribution pattern from the others


*In plain English:* Comparing 3 groups (ghspec, baes, chatdev): Significant differences detected (p < 0.001, α=0.05). At least one group differs.


**ℹ️ Technical note:** Makes fewer assumptions than ANOVA - works with any distribution shape

#### Effect Sizes

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs baes

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in baes 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs chatdev

- Cliff's Delta = 0.978

- 95% Confidence Interval: [0.943, 0.999]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 0.978 [0.943, 0.999]: large effect size. ghspec has systematically higher values compared to chatdev (probability: 98.9%).


Bottom line: ghspec tended to show higher values than chatdev (98.9% estimated ) 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: baes vs chatdev

- Cliff's Delta = -1.000

- 95% Confidence Interval: [-1.000, -1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -1.000 [-1.000, -1.000]: large effect size. all observed values in baes are less than those in chatdev.


Bottom line: baes in this sample, all observed values in baes were less than those in chatdev 
with a **large** effect size.

### total_cost_usd

### 📚 Understanding the Kruskal Wallis

**What is this test?**

The Kruskal-Wallis test compares three or more groups without assuming normality

**💡 Why did we use it?**

It's a robust alternative to ANOVA when data is skewed or has outliers

*Specific reason:* Kruskal-Wallis test selected: at least one group non-normally distributed (Shapiro-Wilk p≤0.05). Non-parametric test appropriate.

**📊 What did we find?**

- Groups compared: ghspec, baes, chatdev

- Test statistic: 228.6687

- p < 0.001

- Result: Significant difference detected

**🎓 How to interpret this:**

At least one group shows a different distribution pattern from the others


*In plain English:* Comparing 3 groups (ghspec, baes, chatdev): Significant differences detected (p < 0.001, α=0.05). At least one group differs.


**ℹ️ Technical note:** Makes fewer assumptions than ANOVA - works with any distribution shape

#### Effect Sizes

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs baes

- Cliff's Delta = 1.000

- 95% Confidence Interval: [1.000, 1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 1.000 [1.000, 1.000]: large effect size. all observed values in ghspec exceed those in baes.


Bottom line: ghspec in this sample, all observed values in ghspec exceeded those in baes 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: ghspec vs chatdev

- Cliff's Delta = 0.664

- 95% Confidence Interval: [0.537, 0.779]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = 0.664 [0.537, 0.779]: large effect size. ghspec has systematically higher values compared to chatdev (probability: 83.2%).


Bottom line: ghspec tended to show higher values than chatdev (83.2% estimated ) 
with a **large** effect size.

### 📏 Effect Size: Cliff's Delta

**What is Cliff's Delta?**

Cliff's Delta measures how often one group's values exceed the other group's values

**Why does it matter?**

It's a non-parametric effect size that works when data isn't normally distributed

**📊 Your results:**

- Comparing: baes vs chatdev

- Cliff's Delta = -1.000

- 95% Confidence Interval: [-1.000, -1.000]

- Magnitude: **LARGE**


**Interpretation scale:**

   < 0.147: Groups overlap almost completely

   0.147-0.33: Noticeable but modest separation

   0.33-0.474: Clear separation between groups

👉 ≥ 0.474: Groups are distinctly different


**💡 Real-world analogy:**

Like comparing high school players to Olympic athletes - almost no overlap


**✅ What this means for your research:**

Cliff's Delta = -1.000 [-1.000, -1.000]: large effect size. all observed values in baes are less than those in chatdev.


Bottom line: baes in this sample, all observed values in baes were less than those in chatdev 
with a **large** effect size.

## 5. Statistical Methodology

**Statistical Analysis**: Data normality was assessed using the Shapiro-Wilk test (α=0.05). Statistical test selection was based on distribution characteristics: parametric tests (Student's t-test for 2 groups, ANOVA for 3+ groups) were used when data met normality assumptions; non-parametric tests (Mann-Whitney U for 2 groups, Kruskal-Wallis for 3+ groups) were used otherwise. Variance homogeneity was assessed using Levene's test (median-centered). Effect sizes were quantified using Cliff's Delta. 95% confidence intervals for effect sizes were computed using bootstrap resampling (n=10,000 iterations, seed=42). Effect size calculations included data quality checks: groups with near-zero variance (coefficient of variation < 1% AND relative IQR < 1%) were flagged, as standardized effect sizes (e.g., Cohen's d) are inappropriate for such data. This relative approach works correctly across metrics of different scales (e.g., tokens vs. cost). In these cases, Cohen's d was skipped, and Cliff's Delta confidence intervals flagged as 'deterministic' to indicate categorical separation rather than continuous effect magnitude. Outliers were identified using Tukey's method (values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR) and reported in descriptive statistics. **Outliers were retained in all analyses** (no winsorization or trimming), as they may represent genuine variation in framework performance. Robust non-parametric methods (Mann-Whitney U, Kruskal-Wallis, Cliff's Delta) were preferentially used when outliers were present, as these methods are resistant to extreme values. Statistical significance was assessed at α=0.05. Statistical analyses were performed using SciPy 1.11.0 and statsmodels 0.14.0.

### Interpreting Statistical vs. Practical Significance

Statistical significance (p-value < 0.05) indicates that an observed difference is unlikely to be due to random chance alone. However, **statistical significance does not automatically imply practical importance**.

**Effect sizes** provide the magnitude of differences and should be considered alongside p-values when evaluating practical significance:

- **Cohen's d**: |d| < 0.2 negligible, 0.2-0.5 small, 0.5-0.8 medium, >0.8 large
- **Cliff's Delta**: |δ| < 0.147 negligible, 0.147-0.33 small, 0.33-0.474 medium, >0.474 large

For performance benchmarks, even small effect sizes may be practically meaningful if they translate to measurable improvements in real-world applications. Conversely, large effect sizes on metrics with zero or near-zero variance (e.g., cached tokens that are always identical) may reflect data characteristics rather than meaningful performance differences.

**Recommendation**: Consider both statistical significance, effect size magnitude, and domain-specific context when drawing conclusions about framework performance.

### Reproducibility Information

| Parameter | Value |
|-----------|-------|
| analysis_date | 2025-11-03T08:18:28.999765 |
| scipy_version | 1.11.0 |
| statsmodels_version | 0.14.0 |
| numpy_version | 1.24.3 |
| random_seed | 42 |
| alpha | 0.05 |
| bootstrap_iterations | 10000 |
| target_power | 0.8 |

## ⚠️ Notes and Warnings

The following conditions were detected during analysis and may affect interpretation:

1. **Assumption Violation**: Normality assumption violated for metric 'api_calls' in group 'ghspec' (p=0.0157); non-parametric test recommended
2. **Assumption Violation**: Normality assumption violated for metric 'api_calls' in group 'baes' (p=0.0000); non-parametric test recommended
3. **Assumption Violation**: Normality assumption violated for metric 'api_calls' in group 'chatdev' (p=0.0050); non-parametric test recommended
4. **Assumption Violation**: Variance homogeneity assumption violated for metric 'api_calls' (Levene's test p=0.0000); robust test recommended
5. **Assumption Violation**: Normality assumption violated for metric 'cached_tokens' in group 'ghspec' (p=0.0220); non-parametric test recommended
6. **Assumption Violation**: Normality assumption violated for metric 'cached_tokens' in group 'baes' (p=0.0000); non-parametric test recommended
7. **Assumption Violation**: Normality assumption violated for metric 'cached_tokens' in group 'chatdev' (p=0.0000); non-parametric test recommended
8. **Assumption Violation**: Variance homogeneity assumption violated for metric 'cached_tokens' (Levene's test p=0.0000); robust test recommended
9. **Assumption Violation**: Normality assumption violated for metric 'execution_time' in group 'baes' (p=0.0000); non-parametric test recommended
10. **Assumption Violation**: Normality assumption violated for metric 'execution_time' in group 'chatdev' (p=0.0000); non-parametric test recommended
11. **Assumption Violation**: Variance homogeneity assumption violated for metric 'execution_time' (Levene's test p=0.0000); robust test recommended
12. **Assumption Violation**: Normality assumption violated for metric 'tokens_in' in group 'ghspec' (p=0.0318); non-parametric test recommended
13. **Assumption Violation**: Normality assumption violated for metric 'tokens_in' in group 'baes' (p=0.0000); non-parametric test recommended
14. **Assumption Violation**: Normality assumption violated for metric 'tokens_in' in group 'chatdev' (p=0.0000); non-parametric test recommended
15. **Assumption Violation**: Variance homogeneity assumption violated for metric 'tokens_in' (Levene's test p=0.0000); robust test recommended
16. **Assumption Violation**: Normality assumption violated for metric 'tokens_out' in group 'baes' (p=0.0000); non-parametric test recommended
17. **Assumption Violation**: Normality assumption violated for metric 'tokens_out' in group 'chatdev' (p=0.0000); non-parametric test recommended
18. **Assumption Violation**: Variance homogeneity assumption violated for metric 'tokens_out' (Levene's test p=0.0000); robust test recommended
19. **Assumption Violation**: Normality assumption violated for metric 'tokens_total' in group 'baes' (p=0.0000); non-parametric test recommended
20. **Assumption Violation**: Normality assumption violated for metric 'tokens_total' in group 'chatdev' (p=0.0000); non-parametric test recommended
21. **Assumption Violation**: Variance homogeneity assumption violated for metric 'tokens_total' (Levene's test p=0.0000); robust test recommended
22. **Assumption Violation**: Normality assumption violated for metric 'total_cost_usd' in group 'ghspec' (p=0.0412); non-parametric test recommended
23. **Assumption Violation**: Normality assumption violated for metric 'total_cost_usd' in group 'baes' (p=0.0000); non-parametric test recommended
24. **Assumption Violation**: Normality assumption violated for metric 'total_cost_usd' in group 'chatdev' (p=0.0000); non-parametric test recommended
25. **Assumption Violation**: Variance homogeneity assumption violated for metric 'total_cost_usd' (Levene's test p=0.0000); robust test recommended

## 6. Glossary

# 📚 Statistical Terms Glossary
*Plain-language definitions for common statistical terms*

## Effect Size Interpretation Guide

### Cohen's d (Parametric)

| Range | Interpretation | Practical Meaning |
|-------|----------------|-------------------|
| \|d\| < 0.2 | Negligible | Minimal practical difference |
| 0.2 ≤ \|d\| < 0.5 | Small | Detectable but modest difference |
| 0.5 ≤ \|d\| < 0.8 | Medium | Moderate, meaningful difference |
| \|d\| ≥ 0.8 | Large | Substantial difference |

### Cliff's Delta (Non-Parametric)

| Range | Interpretation | Dominance Level |
|-------|----------------|-----------------|\ n| \|δ\| < 0.147 | Negligible | Groups largely overlap |
| 0.147 ≤ \|δ\| < 0.33 | Small | One group tends higher |
| 0.33 ≤ \|δ\| < 0.474 | Medium | Clear tendency difference |
| \|δ\| ≥ 0.474 | Large | Strong separation |
| \|δ\| = 1.0 | Complete | No overlap (all A > all B) |

**Note**: Effect size interpretation should consider domain context. Small effects may be practically important in performance benchmarking.

---

**ANOVA**
: Analysis of Variance - compares averages across 3+ groups to see if at least one is different from the others.

**Alpha (α)**
: The significance level, usually 0.05. It's the probability of saying there's a difference when there isn't one (false alarm rate).

**Assumption**
: A requirement for a statistical test to work correctly (e.g., normal distribution, equal variances).

**Bonferroni Correction**
: Adjustment made when doing multiple comparisons to avoid false positives. Makes the significance threshold stricter.

**Bootstrap**
: A resampling method where we repeatedly sample our data (with replacement) to estimate uncertainty. Like simulation using your own data.

**Box Plot**
: Visual showing the median (middle line), quartiles (box edges), range (whiskers), and outliers (dots) of data.

**Cliff's Delta (δ)**
: Non-parametric effect size. Measures how often one group's values are larger than another's. Range: -1 to +1.

**Cohen's d**
: Standardized effect size for comparing two groups. Measures difference in standard deviation units. |d| ≥ 0.8 is considered large.

**Confidence Interval (CI)**
: Range of values likely to contain the true value. A 95% CI means we're 95% confident the true value is in this range.

**Effect Size**
: Measure of how big a difference is, regardless of sample size. Answers: 'Is this difference meaningful?' Examples: Cohen's d, Cliff's Delta.

**Forest Plot**
: Visual showing effect sizes and their confidence intervals across multiple comparisons. Dots = effect size, lines = uncertainty.

**Homogeneity of Variance**
: The assumption that all groups have similar spread (variability). Tested with Levene's test.

**Kruskal-Wallis Test**
: Non-parametric test comparing 3+ groups. Like ANOVA but doesn't assume normal distribution.

**Levene's Test**
: Tests if groups have equal variance (similar spread). If it fails, use Welch's t-test or non-parametric tests.

**Mann-Whitney U Test**
: Non-parametric test comparing two groups. Like a t-test but doesn't assume normal distribution. Good for skewed data.

**Median**
: The middle value when data is sorted. Less affected by outliers than the mean (average).

**Non-parametric**
: Statistical methods that don't assume specific distribution shapes (like normal). More robust but slightly less powerful.

**Normal Distribution**
: Bell-shaped curve. Many statistical tests assume data follows this pattern. Tested with Shapiro-Wilk test.

**Null Hypothesis**
: The 'nothing special is happening' assumption. Tests try to reject this. Example: 'The groups are the same.'

**Outlier**
: Data point far from the others. Might be real or error. Can strongly affect some analyses.

**Parametric**
: Statistical methods assuming specific distribution (usually normal). More powerful but require assumptions.

**Power (1-β)**
: Probability of detecting a real effect if it exists. Want 80%+. Low power means you might miss real differences.

**Q-Q Plot**
: Quantile-Quantile plot. Checks if data follows normal distribution. Points on diagonal = normal. Curves away = non-normal.

**Quartile**
: Data split into four parts. Q1 = 25th percentile, Q2 = median (50th), Q3 = 75th percentile.

**Shapiro-Wilk Test**
: Tests if data is normally distributed. If p > 0.05, data appears normal and parametric tests are OK.

**Significance**
: When results are unlikely to be due to chance alone. Conventionally p < 0.05. But also check effect size!

**Standard Deviation (SD)**
: Measure of spread. About 68% of data falls within 1 SD of the mean in normal distributions.

**Type I Error**
: False positive - saying there's a difference when there isn't. Controlled by alpha (α).

**Type II Error**
: False negative - missing a real difference. Related to power (1-β). Low power = high Type II error risk.

**Variance**
: Measure of spread (squared standard deviation). Higher variance = more spread out data.

**Violin Plot**
: Like a box plot but shows full distribution shape. Wider = more data at that value.

**Welch's t-test**
: Modified t-test that doesn't assume equal variances. Use when Levene's test fails.

**p-value**
: Probability of seeing results this extreme if the null hypothesis (no effect) is true. p < 0.05 typically means 'significant'.

**t-test**
: Compares averages of two groups. Assumes normal distribution and equal variances. Common and powerful when assumptions met.

---

*For more detailed explanations, see the main sections of this report.*

