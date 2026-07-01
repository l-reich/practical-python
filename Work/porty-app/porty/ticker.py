import csv

from . import follow
from .follow import follow
from . import tableformat


from . import report


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, symbols):
    for row in rows:
        if row["name"] in symbols:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    """
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    """
    # using generator expressions instead of the functions
    rows = ([row[index] for index in [0, 1, 4]] for row in rows)
    rows = ([func(val) for func, val in zip([str, float, float], row)] for row in rows)
    rows = (dict(zip(["name", "price", "change"], row)) for row in rows)
    return rows


def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])

    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)

    for row in rows:
        formatter.row(str(val) for val in list(row.values()))


if __name__ == "__main__":
    import report

    portfolio = report.read_portfolio("Data/portfolio.csv")
    lines = follow("Data/stocklog.csv")
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
