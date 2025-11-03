# Run Summary

**Run ID**: 6db3a3f7-dade-429f-93ca-c4d9118ab30e
**Framework**: baes
**Started**: 2025-10-28T11:17:50.019167Z
**Completed**: 2025-10-28T11:20:57.498486Z
**Duration**: 187.48s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 32.02 |
| 2 | 2 | completed | 0/0 | 0 | 44.78 |
| 3 | 3 | completed | 0/0 | 0 | 31.09 |
| 4 | 4 | completed | 0/0 | 0 | 18.25 |
| 5 | 5 | completed | 0/0 | 0 | 32.45 |
| 6 | 6 | completed | 0/0 | 0 | 28.89 |

## Directory Structure

```
6db3a3f7-dade-429f-93ca-c4d9118ab30e/
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
