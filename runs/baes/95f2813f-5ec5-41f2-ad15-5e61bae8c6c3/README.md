# Run Summary

**Run ID**: 95f2813f-5ec5-41f2-ad15-5e61bae8c6c3
**Framework**: baes
**Started**: 2025-10-29T21:16:09.358562Z
**Completed**: 2025-10-29T21:19:03.057562Z
**Duration**: 173.70s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 21.17 |
| 2 | 2 | completed | 0/0 | 0 | 35.49 |
| 3 | 3 | completed | 0/0 | 0 | 32.69 |
| 4 | 4 | completed | 0/0 | 0 | 21.30 |
| 5 | 5 | completed | 0/0 | 0 | 27.71 |
| 6 | 6 | completed | 0/0 | 0 | 35.33 |

## Directory Structure

```
95f2813f-5ec5-41f2-ad15-5e61bae8c6c3/
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
