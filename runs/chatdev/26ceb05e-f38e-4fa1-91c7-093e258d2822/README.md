# Run Summary

**Run ID**: 26ceb05e-f38e-4fa1-91c7-093e258d2822
**Framework**: chatdev
**Started**: 2025-10-29T18:29:39.767356Z
**Completed**: 2025-10-29T18:50:26.945051Z
**Duration**: 1247.18s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 161.98 |
| 2 | 2 | completed | 0/0 | 0 | 134.28 |
| 3 | 3 | completed | 0/0 | 0 | 195.81 |
| 4 | 4 | completed | 0/0 | 0 | 271.57 |
| 5 | 5 | completed | 0/0 | 0 | 239.62 |
| 6 | 6 | completed | 0/0 | 0 | 243.91 |

## Directory Structure

```
26ceb05e-f38e-4fa1-91c7-093e258d2822/
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
