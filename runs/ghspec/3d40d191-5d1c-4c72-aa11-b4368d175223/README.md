# Run Summary

**Run ID**: 3d40d191-5d1c-4c72-aa11-b4368d175223
**Framework**: ghspec
**Started**: 2025-10-31T19:39:33.689405Z
**Completed**: 2025-10-31T19:54:37.055138Z
**Duration**: 903.37s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 126.69 |
| 2 | 2 | completed | 0/0 | 0 | 92.19 |
| 3 | 3 | completed | 0/0 | 0 | 211.77 |
| 4 | 4 | completed | 0/0 | 0 | 174.88 |
| 5 | 5 | completed | 0/0 | 0 | 114.85 |
| 6 | 6 | completed | 0/0 | 0 | 182.97 |

## Directory Structure

```
3d40d191-5d1c-4c72-aa11-b4368d175223/
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
