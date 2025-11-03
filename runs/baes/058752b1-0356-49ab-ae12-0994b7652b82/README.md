# Run Summary

**Run ID**: 058752b1-0356-49ab-ae12-0994b7652b82
**Framework**: baes
**Started**: 2025-10-29T17:30:28.264308Z
**Completed**: 2025-10-29T17:33:29.580086Z
**Duration**: 181.32s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 21.73 |
| 2 | 2 | completed | 0/0 | 0 | 37.16 |
| 3 | 3 | completed | 0/0 | 0 | 28.52 |
| 4 | 4 | completed | 0/0 | 0 | 31.42 |
| 5 | 5 | completed | 0/0 | 0 | 31.80 |
| 6 | 6 | completed | 0/0 | 0 | 30.68 |

## Directory Structure

```
058752b1-0356-49ab-ae12-0994b7652b82/
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
