# Run Summary

**Run ID**: 3af7a60f-9203-4c68-95c9-8bc27216fd03
**Framework**: chatdev
**Started**: 2025-10-29T07:14:43.887995Z
**Completed**: 2025-10-29T07:35:03.998760Z
**Duration**: 1220.11s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 186.40 |
| 2 | 2 | completed | 0/0 | 0 | 156.98 |
| 3 | 3 | completed | 0/0 | 0 | 181.22 |
| 4 | 4 | completed | 0/0 | 0 | 247.28 |
| 5 | 5 | completed | 0/0 | 0 | 256.48 |
| 6 | 6 | completed | 0/0 | 0 | 191.75 |

## Directory Structure

```
3af7a60f-9203-4c68-95c9-8bc27216fd03/
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
