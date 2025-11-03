# Run Summary

**Run ID**: 6dc30c87-ca1f-4945-8c1d-8eecd58783c2
**Framework**: ghspec
**Started**: 2025-10-29T03:17:46.523664Z
**Completed**: 2025-10-29T03:30:19.331762Z
**Duration**: 752.81s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 86.82 |
| 2 | 2 | completed | 0/0 | 0 | 200.78 |
| 3 | 3 | completed | 0/0 | 0 | 90.12 |
| 4 | 4 | completed | 0/0 | 0 | 111.91 |
| 5 | 5 | completed | 0/0 | 0 | 158.10 |
| 6 | 6 | completed | 0/0 | 0 | 105.07 |

## Directory Structure

```
6dc30c87-ca1f-4945-8c1d-8eecd58783c2/
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
