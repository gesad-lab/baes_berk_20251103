# AI Software Development Frameworks Benchmark

**Experiment ID:** baes_berk_20251103  
**Created:** November 3, 2025  
**Model:** GPT-4o-mini  
**Frameworks Evaluated:** BAES, ChatDev, GHSpec  
**Runs per Framework:** 100 (300 total)

## Overview

This experiment benchmarks three AI-powered software development frameworks to evaluate their performance, cost, and quality metrics. This repository contains everything needed to reproduce the experiment results.

**Time to Reproduce:** ~3 hours (30 min setup + 2.5 hours runtime)  
**System Requirements:** Linux/macOS, Python 3.11+, 8GB+ RAM, 10GB disk

## Quick Start

### 1. Setup (5 minutes)

```bash
# Run automated setup
./setup.sh

# Configure your OpenAI API keys
nano .env
```

Add your API keys to `.env`:
```
OPENAI_API_KEY_BAES=sk-...
OPENAI_API_KEY_CHATDEV=sk-...
OPENAI_API_KEY_GHSPEC=sk-...
OPENAI_API_KEY_ADM=sk-...  # For usage reconciliation
```

### 2. Run Experiment (~2.5 hours)

```bash
./run.sh
```

### 3. Analyze Results (after 1 hour delay)

```bash
# Wait 60 minutes for OpenAI Usage API data
./reconcile_usage.sh
```


## What Gets Installed

The `setup.sh` script:
- Creates Python virtual environment (`venv/`)
- Installs dependencies from `requirements.txt`
- Clones framework repositories to `frameworks/`
- Creates `.env` template for API keys

## Project Structure

```
├── config.yaml              # Experiment configuration
├── setup.sh                 # Automated setup script
├── run.sh                   # Execute experiment
├── reconcile_usage.sh       # Update token counts from OpenAI API
├── .env                     # API keys (you create this)
├── requirements.txt         # Python dependencies
├── src/                     # Source code
│   ├── adapters/           # Framework adapters
│   ├── orchestrator/       # Experiment orchestration
│   └── main.py             # Entry point
├── config/                  # Configurations
│   ├── prompts/            # Task prompts
│   └── hitl/               # Human-in-the-loop specs
├── frameworks/              # Framework repos (auto-created)
│   ├── baes/
│   ├── chatdev/
│   └── ghspec/
└── runs/                    # Experiment outputs (auto-created)
    ├── manifest.json
    ├── baes/
    ├── chatdev/
    └── ghspec/
```


## Configuration

Edit `config.yaml` to customize:
- **model**: OpenAI model (default: `gpt-4o-mini`)
- **frameworks**: Framework-specific settings
- **stopping_rule**: When to stop (default: 100 runs per framework)
- **metrics**: Data to collect (tokens, cost, time, quality)
- **timeouts**: Maximum execution times

## Advanced Usage

### Run Individual Components

```bash
source venv/bin/activate

# Setup frameworks only
python -m src.setup_frameworks

# Run experiment
python -m src.main

# Generate reports
python -m src.analysis.report_generator
```

### Usage Reconciliation

OpenAI's Usage API has a 30-60 minute delay. The experiment uses estimated token counts during execution. After waiting, reconcile with actual data:

```bash
# Check what needs reconciliation
./reconcile_usage.sh --list

# Reconcile all runs
./reconcile_usage.sh

# Reconcile specific framework
./reconcile_usage.sh baes

# Verify completion
./reconcile_usage.sh --list --verbose
```

**Note:** Requires `OPENAI_API_KEY_ADM` in `.env` with `api.usage.read` scope.


## Frameworks Evaluated

- **BAES** - Behavior-driven Agile Engineering System
- **ChatDev** - Communicative agents for software development
- **GHSpec** - GitHub Specification-driven development

## Output & Metrics

Results saved to `runs/<framework>/<run_id>/`:
- Token usage (prompt, completion, total)
- Cost (USD)
- Execution time

## Troubleshooting

### Setup Issues

```bash
# Recreate virtual environment
rm -rf venv
./setup.sh

# Reinstall frameworks
rm -rf frameworks/
python -m src.setup_frameworks
```

### API Key Issues

- Verify keys start with `sk-`
- Check permissions on OpenAI platform
- Ensure `OPENAI_API_KEY_ADM` has `api.usage.read` scope for reconciliation

### Reconciliation Issues

- **No runs listed:** Wait 30-60 minutes after experiment completion
- **Zero tokens returned:** API delay may exceed 60 minutes, retry later
- **Permission denied:** Run `chmod +x reconcile_usage.sh`

### Common Errors

```bash
# Import errors
source venv/bin/activate
pip install -r requirements.txt

# Path issues - use absolute paths
cd your_local_path/baes_berk_20251103
./run.sh
```


## Citation

If you use this experiment in your research, please cite the associated paper.

## License

See [LICENSE](LICENSE) file.

---

## Detailed Reproduction Guide

For researchers reproducing this experiment for publication.

### System Requirements

- **OS:** Linux or macOS
- **Python:** 3.11 or higher
- **RAM:** 8GB minimum, 16GB recommended
- **Disk:** 10GB free space
- **Network:** Internet connection required

### Prerequisites

```bash
# Verify Python version
python3 --version  # Must be 3.11+

# Required tools
git --version
pip --version
```

### Step-by-Step Reproduction

#### 1. Clone and Setup (10 minutes)

```bash
# Navigate to experiment directory
cd /home/amg/projects/uece/baes/baes_berk_20251103

# Run automated setup
./setup.sh

# Verify installation
source venv/bin/activate
python -c "import yaml; print('Setup successful')"
```

#### 2. Configure API Keys (5 minutes)

Edit `.env` with your OpenAI API keys:

```bash
OPENAI_API_KEY_BAES=sk-your-key-here
OPENAI_API_KEY_CHATDEV=sk-your-key-here
OPENAI_API_KEY_GHSPEC=sk-your-key-here
OPENAI_API_KEY_ADM=sk-admin-key-with-usage-scope
```

**Important:** 
- Use different keys for each framework (or the same if acceptable)
- Admin key requires `api.usage.read` permission

#### 3. Run Experiment (2.5 hours)

```bash
./run.sh
```

Monitor progress:
```bash
tail -f logs/experiment.log  # If logs/ exists
```

#### 4. Wait for API Data (60 minutes)

OpenAI Usage API has a propagation delay. Wait at least 60 minutes after experiment completion.

#### 5. Reconcile Usage Data (5 minutes)

```bash
# Check reconciliation status
./reconcile_usage.sh --list

# Reconcile all runs
./reconcile_usage.sh

# Verify completion
./reconcile_usage.sh --list --verbose
```

#### 6. Generate Analysis (5 minutes)

```bash
source venv/bin/activate
python -m src.analysis.report_generator
```

### Expected Results

After successful completion:

**Data files:**
- `runs/manifest.json` - Run metadata
- `runs/<framework>/<run_id>/` - Individual run data (300 total)
- `analysis/statistical_report.md` - Statistical analysis (if generated)

**Metrics per run:**
- Token counts (prompt, completion, total)
- Cost in USD
- Execution time
- Quality scores

**Verification:**
- 100 runs completed per framework (300 total)
- All runs have reconciled token counts
- Statistical analysis shows framework comparisons
- Results match paper within ±5% variance

### Advanced Troubleshooting

**Rate Limit Errors:**
- Reduce concurrent execution in `config.yaml`
- Add delays between framework runs

**Memory Issues:**
- Close other applications
- Reduce number of parallel runs
- Monitor with `htop`

**Framework Installation Failures:**
- Check framework documentation
- Verify Python version compatibility
- Manually install in `frameworks/` directory

**Statistical Variance:**
- Minor p-value differences (±0.05) are expected
- Rerun experiment for tighter confidence intervals
- Check random seed settings in `config.yaml`

### Validation Checklist

- [ ] Python 3.11+ installed
- [ ] All API keys configured in `.env`
- [ ] Virtual environment activated
- [ ] Experiment completed: 300 runs total
- [ ] Usage data reconciled after 60+ minute wait
- [ ] Analysis reports generated
- [ ] Results match paper benchmarks (±5%)

### Support

For issues during reproduction:
1. Check `logs/` directory for error details
2. Review `config.yaml` configuration
3. Verify all prerequisites installed
4. Consult troubleshooting section above

