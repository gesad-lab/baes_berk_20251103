# Run Summary

**Run ID**: da372b4b-4c7b-448f-ba95-069e4a4bb298
**Framework**: baes
**Started**: 2025-10-30T19:50:52.265689Z
**Completed**: 2025-10-30T19:53:57.875128Z
**Duration**: 185.61s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 28.68 |
| 2 | 2 | completed | 0/0 | 0 | 49.24 |
| 3 | 3 | completed | 0/0 | 0 | 31.27 |
| 4 | 4 | completed | 0/0 | 0 | 24.47 |
| 5 | 5 | completed | 0/0 | 0 | 23.64 |
| 6 | 6 | completed | 0/0 | 0 | 28.29 |

## Directory Structure

```
da372b4b-4c7b-448f-ba95-069e4a4bb298/
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
