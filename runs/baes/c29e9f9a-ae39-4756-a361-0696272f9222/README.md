# Run Summary

**Run ID**: c29e9f9a-ae39-4756-a361-0696272f9222
**Framework**: baes
**Started**: 2025-10-28T14:39:48.559609Z
**Completed**: 2025-10-28T14:43:51.181144Z
**Duration**: 242.62s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 41.86 |
| 2 | 2 | completed | 0/0 | 0 | 23.33 |
| 3 | 3 | completed | 0/0 | 0 | 47.36 |
| 4 | 4 | completed | 0/0 | 0 | 45.11 |
| 5 | 5 | completed | 0/0 | 0 | 41.78 |
| 6 | 6 | completed | 0/0 | 0 | 43.17 |

## Directory Structure

```
c29e9f9a-ae39-4756-a361-0696272f9222/
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
