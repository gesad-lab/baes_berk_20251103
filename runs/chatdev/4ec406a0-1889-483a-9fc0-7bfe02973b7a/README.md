# Run Summary

**Run ID**: 4ec406a0-1889-483a-9fc0-7bfe02973b7a
**Framework**: chatdev
**Started**: 2025-10-30T16:06:01.002074Z
**Completed**: 2025-10-30T16:27:50.534815Z
**Duration**: 1309.53s
**Total Sprints**: 6

## Sprint Results

| Sprint | Step ID | Status | Tokens (in/out) | API Calls | Time (s) |
|--------|---------|--------|-----------------|-----------|----------|
| 1 | 1 | completed | 0/0 | 0 | 287.86 |
| 2 | 2 | completed | 0/0 | 0 | 158.10 |
| 3 | 3 | completed | 0/0 | 0 | 194.15 |
| 4 | 4 | completed | 0/0 | 0 | 171.70 |
| 5 | 5 | completed | 0/0 | 0 | 286.87 |
| 6 | 6 | completed | 0/0 | 0 | 210.85 |

## Directory Structure

```
4ec406a0-1889-483a-9fc0-7bfe02973b7a/
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
