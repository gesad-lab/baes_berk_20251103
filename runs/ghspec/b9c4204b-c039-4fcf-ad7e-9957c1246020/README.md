# Run Summary

**Run ID**: b9c4204b-c039-4fcf-ad7e-9957c1246020
**Framework**: ghspec
**Started**: 2025-10-28T13:29:51.988649Z
**Completed**: 2025-10-28T13:51:26.045348Z
**Duration**: 1294.06s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 266.24 |
| 2 | 2 | completed | 0/0 | 0 | 154.85 |
| 3 | 3 | completed | 0/0 | 0 | 149.68 |
| 4 | 4 | completed | 0/0 | 0 | 279.36 |
| 5 | 5 | completed | 0/0 | 0 | 276.93 |
| 6 | 6 | completed | 0/0 | 0 | 166.98 |

## Directory Structure

```
b9c4204b-c039-4fcf-ad7e-9957c1246020/
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
