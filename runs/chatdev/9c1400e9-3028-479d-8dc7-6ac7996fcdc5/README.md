# Run Summary

**Run ID**: 9c1400e9-3028-479d-8dc7-6ac7996fcdc5
**Framework**: chatdev
**Started**: 2025-10-28T20:50:04.687356Z
**Completed**: 2025-10-28T21:09:06.940838Z
**Duration**: 1142.25s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 184.41 |
| 2 | 2 | completed | 0/0 | 0 | 154.26 |
| 3 | 3 | completed | 0/0 | 0 | 167.05 |
| 4 | 4 | completed | 0/0 | 0 | 206.27 |
| 5 | 5 | completed | 0/0 | 0 | 215.65 |
| 6 | 6 | completed | 0/0 | 0 | 214.61 |

## Directory Structure

```
9c1400e9-3028-479d-8dc7-6ac7996fcdc5/
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
