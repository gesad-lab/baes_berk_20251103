# Run Summary

**Run ID**: 16338765-f8aa-4e05-9495-ad6a6b168934
**Framework**: ghspec
**Started**: 2025-10-31T10:53:16.569347Z
**Completed**: 2025-10-31T11:12:14.242313Z
**Duration**: 1137.67s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 205.81 |
| 2 | 2 | completed | 0/0 | 0 | 175.33 |
| 3 | 3 | completed | 0/0 | 0 | 275.90 |
| 4 | 4 | completed | 0/0 | 0 | 195.87 |
| 5 | 5 | completed | 0/0 | 0 | 148.56 |
| 6 | 6 | completed | 0/0 | 0 | 136.19 |

## Directory Structure

```
16338765-f8aa-4e05-9495-ad6a6b168934/
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
