# Run Summary

**Run ID**: 89e16766-d82c-4c4d-84d9-91c72f616564
**Framework**: ghspec
**Started**: 2025-10-29T01:20:02.461715Z
**Completed**: 2025-10-29T01:35:06.297080Z
**Duration**: 903.84s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 189.95 |
| 2 | 2 | completed | 0/0 | 0 | 98.52 |
| 3 | 3 | completed | 0/0 | 0 | 134.33 |
| 4 | 4 | completed | 0/0 | 0 | 213.36 |
| 5 | 5 | completed | 0/0 | 0 | 97.60 |
| 6 | 6 | completed | 0/0 | 0 | 170.07 |

## Directory Structure

```
89e16766-d82c-4c4d-84d9-91c72f616564/
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
