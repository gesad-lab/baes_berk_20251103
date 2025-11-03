# Run Summary

**Run ID**: ab987f1b-9363-4d33-b212-6fbcd93360ab
**Framework**: baes
**Started**: 2025-10-29T06:24:37.339903Z
**Completed**: 2025-10-29T06:27:52.552741Z
**Duration**: 195.21s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 28.70 |
| 2 | 2 | completed | 0/0 | 0 | 30.56 |
| 3 | 3 | completed | 0/0 | 0 | 35.52 |
| 4 | 4 | completed | 0/0 | 0 | 35.42 |
| 5 | 5 | completed | 0/0 | 0 | 31.98 |
| 6 | 6 | completed | 0/0 | 0 | 33.02 |

## Directory Structure

```
ab987f1b-9363-4d33-b212-6fbcd93360ab/
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
