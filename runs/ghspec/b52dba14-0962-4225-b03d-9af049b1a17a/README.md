# Run Summary

**Run ID**: b52dba14-0962-4225-b03d-9af049b1a17a
**Framework**: ghspec
**Started**: 2025-10-29T09:59:34.937296Z
**Completed**: 2025-10-29T10:21:19.606694Z
**Duration**: 1304.67s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 223.61 |
| 2 | 2 | completed | 0/0 | 0 | 152.40 |
| 3 | 3 | completed | 0/0 | 0 | 235.92 |
| 4 | 4 | completed | 0/0 | 0 | 187.24 |
| 5 | 5 | completed | 0/0 | 0 | 216.45 |
| 6 | 6 | completed | 0/0 | 0 | 289.05 |

## Directory Structure

```
b52dba14-0962-4225-b03d-9af049b1a17a/
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
