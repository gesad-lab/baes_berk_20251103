# Run Summary

**Run ID**: d383a702-26ee-4245-88b4-421dbae82945
**Framework**: chatdev
**Started**: 2025-10-31T20:15:34.341507Z
**Completed**: 2025-10-31T20:35:26.441234Z
**Duration**: 1192.10s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 133.21 |
| 2 | 2 | completed | 0/0 | 0 | 121.41 |
| 3 | 3 | completed | 0/0 | 0 | 152.88 |
| 4 | 4 | completed | 0/0 | 0 | 183.87 |
| 5 | 5 | completed | 0/0 | 0 | 600.02 |
| 6 | 6 | completed | 0/0 | 0 | 0.70 |

## Directory Structure

```
d383a702-26ee-4245-88b4-421dbae82945/
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
