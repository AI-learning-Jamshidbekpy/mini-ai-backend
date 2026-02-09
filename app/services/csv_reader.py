import csv
import io
from fastapi import HTTPException


def reader_csv_bytes(file_bytes: bytes) -> tuple[list[str], list[dict]]:
    # bytes -> text stream
    text = file_bytes.decode("utf-8", errors="replace")
    f = io.StringIO(text)

    reader = csv.DictReader(f)

    # Header borligini tekshirish
    if not reader.fieldnames:
        raise HTTPException(status_code=400, detail="CSV header topilmadi (fieldnames yo'q).")

    columns = [c.strip() for c in reader.fieldnames if c is not None]

    rows = []
    for row in reader:
        # bo'sh qatordan qochish
        if row and any((v or "").strip() for v in row.values()):
            rows.append(row)

    if len(rows) < 1:
        raise HTTPException(status_code=400, detail="CSV ichida kamida 1 ta row bo‘lishi kerak.")

    return columns, rows