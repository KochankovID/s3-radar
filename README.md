# :package:  S3 radar

Simple cli tool for measurement s3 network bandwidth

---

## :arrow_down: Installation

### :snake: PIP

```bash
pip install s3_radar
```

### :honey_pot: Poetry

```bash
poetry add s3_radar
```

## :cake: How to use it

### Measure upload speed

```bash
s3r up <bucket> <ak> <ask> -s <size-in-bytes>
```

### Measure upload and download speed

```bash
s3r down <bucket> <ak> <ask> -s <size-in-bytes>
```

### Show command list

```bash
smithy --help
```
