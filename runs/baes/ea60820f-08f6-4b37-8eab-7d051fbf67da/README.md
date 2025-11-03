# Run Summary

**Run ID**: ea60820f-08f6-4b37-8eab-7d051fbf67da
**Framework**: baes
**Started**: 2025-10-31T18:50:54.468190Z
**Completed**: 2025-10-31T18:54:07.316368Z
**Duration**: 192.85s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 32.75 |
| 2 | 2 | completed | 0/0 | 0 | 30.22 |
| 3 | 3 | completed | 0/0 | 0 | 31.26 |
| 4 | 4 | completed | 0/0 | 0 | 33.55 |
| 5 | 5 | completed | 0/0 | 0 | 28.92 |
| 6 | 6 | completed | 0/0 | 0 | 36.13 |

## Directory Structure

```
ea60820f-08f6-4b37-8eab-7d051fbf67da/
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
