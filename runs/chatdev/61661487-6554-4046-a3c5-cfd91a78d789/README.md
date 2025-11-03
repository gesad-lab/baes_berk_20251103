# Run Summary

**Run ID**: 61661487-6554-4046-a3c5-cfd91a78d789
**Framework**: chatdev
**Started**: 2025-10-29T04:59:14.778657Z
**Completed**: 2025-10-29T05:16:31.478344Z
**Duration**: 1036.70s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 184.68 |
| 2 | 2 | completed | 0/0 | 0 | 221.42 |
| 3 | 3 | completed | 0/0 | 0 | 157.51 |
| 4 | 4 | completed | 0/0 | 0 | 159.86 |
| 5 | 5 | completed | 0/0 | 0 | 143.39 |
| 6 | 6 | completed | 0/0 | 0 | 169.83 |

## Directory Structure

```
61661487-6554-4046-a3c5-cfd91a78d789/
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
