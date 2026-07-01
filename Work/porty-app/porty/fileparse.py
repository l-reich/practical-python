# fileparse.py
#
# Exercise 3.3

import csv
import logging

log = logging.getLogger(__name__)


def parse_csv(
    f,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
) -> list:
    """
    Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(f, delimiter=delimiter)

    if has_headers:
        # Read the file headers
        headers = next(rows)

        if select:
            indices = {idx: col for idx, col in enumerate(headers) if col in select}
            headers = [header for header in headers if header in select]
        else:
            indices = dict(enumerate(headers))

    records = []
    for row_idx, row in enumerate(rows):
        try:
            if not row:  # Skip rows with no data
                continue
            if has_headers:
                record = [
                    value for idx, value in enumerate(row) if idx in indices.keys()
                ]
                if types:
                    record = [func(val) for func, val in zip(types, record)]
                record = dict(zip(headers, record))
            else:
                if types:
                    record = tuple([func(val) for func, val in zip(types, row)])
                else:
                    record = tuple(row)

            records.append(record)

        except ValueError as e:
            if not silence_errors:
                log.warning("Row %d: Couldn't convert %s", row_idx, row)
                log.debug("Row %d: Reason %s", row_idx, e)

    return records
