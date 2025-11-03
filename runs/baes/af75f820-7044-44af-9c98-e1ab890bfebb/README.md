# Run Summary

**Run ID**: af75f820-7044-44af-9c98-e1ab890bfebb
**Framework**: baes
**Started**: 2025-10-31T16:29:15.961931Z
**Completed**: 2025-10-31T16:33:01.739562Z
**Duration**: 225.78s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 33.69 |
| 2 | 2 | completed | 0/0 | 0 | 39.89 |
| 3 | 3 | completed | 0/0 | 0 | 33.40 |
| 4 | 4 | completed | 0/0 | 0 | 46.01 |
| 5 | 5 | completed | 0/0 | 0 | 38.65 |
| 6 | 6 | completed | 0/0 | 0 | 34.13 |

## Directory Structure

```
af75f820-7044-44af-9c98-e1ab890bfebb/
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
