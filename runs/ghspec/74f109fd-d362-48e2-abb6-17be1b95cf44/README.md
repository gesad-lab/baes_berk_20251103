# Run Summary

**Run ID**: 74f109fd-d362-48e2-abb6-17be1b95cf44
**Framework**: ghspec
**Started**: 2025-10-30T18:52:50.541780Z
**Completed**: 2025-10-30T19:11:57.037407Z
**Duration**: 1146.50s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 158.71 |
| 2 | 2 | completed | 0/0 | 0 | 225.87 |
| 3 | 3 | completed | 0/0 | 0 | 216.81 |
| 4 | 4 | completed | 0/0 | 0 | 194.99 |
| 5 | 5 | completed | 0/0 | 0 | 165.06 |
| 6 | 6 | completed | 0/0 | 0 | 185.05 |

## Directory Structure

```
74f109fd-d362-48e2-abb6-17be1b95cf44/
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
