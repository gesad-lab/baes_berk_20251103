# Run Summary

**Run ID**: 347086b1-5437-471d-9987-f858d46cb7eb
**Framework**: ghspec
**Started**: 2025-10-31T09:34:53.545335Z
**Completed**: 2025-10-31T09:51:35.949088Z
**Duration**: 1002.40s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 199.94 |
| 2 | 2 | completed | 0/0 | 0 | 125.85 |
| 3 | 3 | completed | 0/0 | 0 | 127.05 |
| 4 | 4 | completed | 0/0 | 0 | 169.00 |
| 5 | 5 | completed | 0/0 | 0 | 241.08 |
| 6 | 6 | completed | 0/0 | 0 | 139.48 |

## Directory Structure

```
347086b1-5437-471d-9987-f858d46cb7eb/
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
