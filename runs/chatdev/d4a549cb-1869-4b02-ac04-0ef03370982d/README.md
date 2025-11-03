# Run Summary

**Run ID**: d4a549cb-1869-4b02-ac04-0ef03370982d
**Framework**: chatdev
**Started**: 2025-10-30T22:07:56.359616Z
**Completed**: 2025-10-30T22:25:49.612553Z
**Duration**: 1073.25s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 206.47 |
| 2 | 2 | completed | 0/0 | 0 | 153.10 |
| 3 | 3 | completed | 0/0 | 0 | 159.64 |
| 4 | 4 | completed | 0/0 | 0 | 179.70 |
| 5 | 5 | completed | 0/0 | 0 | 168.91 |
| 6 | 6 | completed | 0/0 | 0 | 205.44 |

## Directory Structure

```
d4a549cb-1869-4b02-ac04-0ef03370982d/
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
