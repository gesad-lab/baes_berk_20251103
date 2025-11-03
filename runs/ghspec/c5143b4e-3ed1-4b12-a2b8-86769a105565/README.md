# Run Summary

**Run ID**: c5143b4e-3ed1-4b12-a2b8-86769a105565
**Framework**: ghspec
**Started**: 2025-10-29T13:29:33.219225Z
**Completed**: 2025-10-29T13:49:32.067770Z
**Duration**: 1198.85s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 164.42 |
| 2 | 2 | completed | 0/0 | 0 | 121.30 |
| 3 | 3 | completed | 0/0 | 0 | 407.03 |
| 4 | 4 | completed | 0/0 | 0 | 130.33 |
| 5 | 5 | completed | 0/0 | 0 | 172.62 |
| 6 | 6 | completed | 0/0 | 0 | 203.15 |

## Directory Structure

```
c5143b4e-3ed1-4b12-a2b8-86769a105565/
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
