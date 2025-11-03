# Run Summary

**Run ID**: 1e35d4fe-76a6-4737-93e8-d414a3002fca
**Framework**: baes
**Started**: 2025-10-30T01:49:23.045838Z
**Completed**: 2025-10-30T01:53:05.427842Z
**Duration**: 222.38s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 22.55 |
| 2 | 2 | completed | 0/0 | 0 | 42.10 |
| 3 | 3 | completed | 0/0 | 0 | 37.37 |
| 4 | 4 | completed | 0/0 | 0 | 38.47 |
| 5 | 5 | completed | 0/0 | 0 | 45.85 |
| 6 | 6 | completed | 0/0 | 0 | 36.04 |

## Directory Structure

```
1e35d4fe-76a6-4737-93e8-d414a3002fca/
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
