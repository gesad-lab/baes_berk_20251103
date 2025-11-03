# Run Summary

**Run ID**: fd303ab8-07c4-49f2-860e-0ba3ee7f9345
**Framework**: baes
**Started**: 2025-10-29T16:09:12.568616Z
**Completed**: 2025-10-29T16:12:43.690532Z
**Duration**: 211.12s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 35.03 |
| 2 | 2 | completed | 0/0 | 0 | 38.50 |
| 3 | 3 | completed | 0/0 | 0 | 42.83 |
| 4 | 4 | completed | 0/0 | 0 | 25.36 |
| 5 | 5 | completed | 0/0 | 0 | 34.02 |
| 6 | 6 | completed | 0/0 | 0 | 35.38 |

## Directory Structure

```
fd303ab8-07c4-49f2-860e-0ba3ee7f9345/
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
