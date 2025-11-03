# Run Summary

**Run ID**: 7f44730e-b57f-4f86-8779-e3aef43204cc
**Framework**: ghspec
**Started**: 2025-10-30T08:22:43.349257Z
**Completed**: 2025-10-30T08:40:44.463903Z
**Duration**: 1081.11s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 189.01 |
| 2 | 2 | completed | 0/0 | 0 | 123.42 |
| 3 | 3 | completed | 0/0 | 0 | 299.97 |
| 4 | 4 | completed | 0/0 | 0 | 176.50 |
| 5 | 5 | completed | 0/0 | 0 | 131.55 |
| 6 | 6 | completed | 0/0 | 0 | 160.66 |

## Directory Structure

```
7f44730e-b57f-4f86-8779-e3aef43204cc/
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
