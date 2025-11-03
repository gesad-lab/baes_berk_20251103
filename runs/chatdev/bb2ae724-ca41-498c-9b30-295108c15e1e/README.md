# Run Summary

**Run ID**: bb2ae724-ca41-498c-9b30-295108c15e1e
**Framework**: chatdev
**Started**: 2025-10-28T18:34:26.239079Z
**Completed**: 2025-10-28T18:54:21.967745Z
**Duration**: 1195.73s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 169.39 |
| 2 | 2 | completed | 0/0 | 0 | 149.93 |
| 3 | 3 | completed | 0/0 | 0 | 167.39 |
| 4 | 4 | completed | 0/0 | 0 | 200.39 |
| 5 | 5 | completed | 0/0 | 0 | 227.40 |
| 6 | 6 | completed | 0/0 | 0 | 281.22 |

## Directory Structure

```
bb2ae724-ca41-498c-9b30-295108c15e1e/
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
