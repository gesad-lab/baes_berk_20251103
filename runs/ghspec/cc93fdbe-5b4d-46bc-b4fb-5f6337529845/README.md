# Run Summary

**Run ID**: cc93fdbe-5b4d-46bc-b4fb-5f6337529845
**Framework**: ghspec
**Started**: 2025-10-30T20:12:33.018961Z
**Completed**: 2025-10-30T20:27:28.950899Z
**Duration**: 895.93s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 137.26 |
| 2 | 2 | completed | 0/0 | 0 | 128.56 |
| 3 | 3 | completed | 0/0 | 0 | 122.14 |
| 4 | 4 | completed | 0/0 | 0 | 155.46 |
| 5 | 5 | completed | 0/0 | 0 | 210.10 |
| 6 | 6 | completed | 0/0 | 0 | 142.41 |

## Directory Structure

```
cc93fdbe-5b4d-46bc-b4fb-5f6337529845/
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
