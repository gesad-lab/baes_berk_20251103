# Run Summary

**Run ID**: e5598cef-f5b6-48b1-a655-9fefc4f9b236
**Framework**: chatdev
**Started**: 2025-10-30T13:41:06.611193Z
**Completed**: 2025-10-30T14:02:42.311197Z
**Duration**: 1295.70s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 195.23 |
| 2 | 2 | completed | 0/0 | 0 | 150.44 |
| 3 | 3 | completed | 0/0 | 0 | 203.58 |
| 4 | 4 | completed | 0/0 | 0 | 223.08 |
| 5 | 5 | completed | 0/0 | 0 | 213.52 |
| 6 | 6 | completed | 0/0 | 0 | 309.85 |

## Directory Structure

```
e5598cef-f5b6-48b1-a655-9fefc4f9b236/
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
