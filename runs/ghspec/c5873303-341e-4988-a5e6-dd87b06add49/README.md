# Run Summary

**Run ID**: c5873303-341e-4988-a5e6-dd87b06add49
**Framework**: ghspec
**Started**: 2025-10-30T16:59:27.003697Z
**Completed**: 2025-10-30T17:23:02.382098Z
**Duration**: 1415.38s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 254.98 |
| 2 | 2 | completed | 0/0 | 0 | 153.99 |
| 3 | 3 | completed | 0/0 | 0 | 211.64 |
| 4 | 4 | completed | 0/0 | 0 | 483.09 |
| 5 | 5 | completed | 0/0 | 0 | 150.64 |
| 6 | 6 | completed | 0/0 | 0 | 161.04 |

## Directory Structure

```
c5873303-341e-4988-a5e6-dd87b06add49/
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
