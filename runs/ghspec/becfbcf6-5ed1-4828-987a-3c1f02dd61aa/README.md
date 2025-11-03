# Run Summary

**Run ID**: becfbcf6-5ed1-4828-987a-3c1f02dd61aa
**Framework**: ghspec
**Started**: 2025-10-30T19:35:51.859067Z
**Completed**: 2025-10-30T19:50:48.140443Z
**Duration**: 896.28s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 205.48 |
| 2 | 2 | completed | 0/0 | 0 | 107.62 |
| 3 | 3 | completed | 0/0 | 0 | 120.53 |
| 4 | 4 | completed | 0/0 | 0 | 154.64 |
| 5 | 5 | completed | 0/0 | 0 | 127.55 |
| 6 | 6 | completed | 0/0 | 0 | 180.46 |

## Directory Structure

```
becfbcf6-5ed1-4828-987a-3c1f02dd61aa/
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
