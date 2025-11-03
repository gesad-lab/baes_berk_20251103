# Run Summary

**Run ID**: 35d1a3b9-4d59-4b9c-9e90-f5917ed7cda9
**Framework**: ghspec
**Started**: 2025-10-28T17:55:20.406417Z
**Completed**: 2025-10-28T18:31:14.858608Z
**Duration**: 2154.45s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 191.77 |
| 2 | 2 | completed | 0/0 | 0 | 246.97 |
| 3 | 3 | completed | 0/0 | 0 | 324.30 |
| 4 | 4 | completed | 0/0 | 0 | 876.17 |
| 5 | 5 | completed | 0/0 | 0 | 260.98 |
| 6 | 6 | completed | 0/0 | 0 | 254.25 |

## Directory Structure

```
35d1a3b9-4d59-4b9c-9e90-f5917ed7cda9/
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
