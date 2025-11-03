# Run Summary

**Run ID**: b85fe942-a726-47ed-8e99-28f83a3c967d
**Framework**: chatdev
**Started**: 2025-10-30T20:30:18.532987Z
**Completed**: 2025-10-30T20:51:30.445598Z
**Duration**: 1271.91s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 196.20 |
| 2 | 2 | completed | 0/0 | 0 | 155.35 |
| 3 | 3 | completed | 0/0 | 0 | 198.33 |
| 4 | 4 | completed | 0/0 | 0 | 201.53 |
| 5 | 5 | completed | 0/0 | 0 | 258.40 |
| 6 | 6 | completed | 0/0 | 0 | 262.09 |

## Directory Structure

```
b85fe942-a726-47ed-8e99-28f83a3c967d/
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
