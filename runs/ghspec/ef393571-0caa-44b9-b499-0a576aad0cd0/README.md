# Run Summary

**Run ID**: ef393571-0caa-44b9-b499-0a576aad0cd0
**Framework**: ghspec
**Started**: 2025-10-31T14:23:33.697515Z
**Completed**: 2025-10-31T14:44:14.971283Z
**Duration**: 1241.27s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 132.01 |
| 2 | 2 | completed | 0/0 | 0 | 175.90 |
| 3 | 3 | completed | 0/0 | 0 | 143.62 |
| 4 | 4 | completed | 0/0 | 0 | 190.41 |
| 5 | 5 | completed | 0/0 | 0 | 203.40 |
| 6 | 6 | completed | 0/0 | 0 | 395.92 |

## Directory Structure

```
ef393571-0caa-44b9-b499-0a576aad0cd0/
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
