# Run Summary

**Run ID**: 7de498a2-958c-48b7-a73b-ebcdf6042a06
**Framework**: ghspec
**Started**: 2025-10-28T11:38:35.610295Z
**Completed**: 2025-10-28T12:09:05.111964Z
**Duration**: 1829.50s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 320.91 |
| 2 | 2 | completed | 0/0 | 0 | 431.21 |
| 3 | 3 | completed | 0/0 | 0 | 290.98 |
| 4 | 4 | completed | 0/0 | 0 | 301.98 |
| 5 | 5 | completed | 0/0 | 0 | 295.10 |
| 6 | 6 | completed | 0/0 | 0 | 189.31 |

## Directory Structure

```
7de498a2-958c-48b7-a73b-ebcdf6042a06/
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
