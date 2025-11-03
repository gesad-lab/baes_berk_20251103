# Run Summary

**Run ID**: 7272759e-402a-49fd-aa39-bd26df1da978
**Framework**: baes
**Started**: 2025-10-31T01:34:53.005220Z
**Completed**: 2025-10-31T01:38:44.426351Z
**Duration**: 231.42s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 50.21 |
| 2 | 2 | completed | 0/0 | 0 | 39.59 |
| 3 | 3 | completed | 0/0 | 0 | 33.14 |
| 4 | 4 | completed | 0/0 | 0 | 33.20 |
| 5 | 5 | completed | 0/0 | 0 | 36.02 |
| 6 | 6 | completed | 0/0 | 0 | 39.25 |

## Directory Structure

```
7272759e-402a-49fd-aa39-bd26df1da978/
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
