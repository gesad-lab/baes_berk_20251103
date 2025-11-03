# Run Summary

**Run ID**: 4543b001-42fe-4cd7-9c7b-0b1749868c64
**Framework**: baes
**Started**: 2025-10-29T21:55:45.526195Z
**Completed**: 2025-10-29T21:58:26.688577Z
**Duration**: 161.16s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 19.83 |
| 2 | 2 | completed | 0/0 | 0 | 21.54 |
| 3 | 3 | completed | 0/0 | 0 | 35.32 |
| 4 | 4 | completed | 0/0 | 0 | 27.36 |
| 5 | 5 | completed | 0/0 | 0 | 26.65 |
| 6 | 6 | completed | 0/0 | 0 | 30.44 |

## Directory Structure

```
4543b001-42fe-4cd7-9c7b-0b1749868c64/
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
