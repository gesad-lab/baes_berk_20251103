# Run Summary

**Run ID**: 76b443d5-e8ce-4294-95a1-997fe1e7afa3
**Framework**: ghspec
**Started**: 2025-10-31T01:55:18.734441Z
**Completed**: 2025-10-31T02:10:54.556880Z
**Duration**: 935.82s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 179.06 |
| 2 | 2 | completed | 0/0 | 0 | 123.36 |
| 3 | 3 | completed | 0/0 | 0 | 148.01 |
| 4 | 4 | completed | 0/0 | 0 | 149.58 |
| 5 | 5 | completed | 0/0 | 0 | 137.39 |
| 6 | 6 | completed | 0/0 | 0 | 198.41 |

## Directory Structure

```
76b443d5-e8ce-4294-95a1-997fe1e7afa3/
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
