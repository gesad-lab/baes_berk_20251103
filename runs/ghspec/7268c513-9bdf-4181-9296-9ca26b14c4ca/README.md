# Run Summary

**Run ID**: 7268c513-9bdf-4181-9296-9ca26b14c4ca
**Framework**: ghspec
**Started**: 2025-10-28T15:05:04.225662Z
**Completed**: 2025-10-28T15:34:06.617431Z
**Duration**: 1742.39s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 223.69 |
| 2 | 2 | completed | 0/0 | 0 | 300.88 |
| 3 | 3 | completed | 0/0 | 0 | 285.33 |
| 4 | 4 | completed | 0/0 | 0 | 285.74 |
| 5 | 5 | completed | 0/0 | 0 | 196.77 |
| 6 | 6 | completed | 0/0 | 0 | 449.97 |

## Directory Structure

```
7268c513-9bdf-4181-9296-9ca26b14c4ca/
├── sprint_001/          # First sprint artifacts
│   ├── generated_artifacts/
│   ├── logs/
│   ├── metadata.json
│   └── validation.json
├── sprint_002/          # Second sprint artifacts
│   └── ...
├── final/               # Symlink to last successful sprint
└── metrics.json         # Run-level metrics (single source of truth)
```

## Accessing Results

### View final artifacts
```bash
cd final/generated_artifacts/managed_system/
```

### Compare sprints
```bash
diff -r sprint_001/generated_artifacts sprint_002/generated_artifacts
```

### View metrics (single source of truth)
```bash
cat metrics.json | jq
```

### Check specific sprint
```bash
cat sprint_001/metadata.json
```
