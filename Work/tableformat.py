class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """

    def headings(self, headers):
        print("<tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr>")

    def row(self, rowdata):
        print("<tr>" + "".join(f"<td>{d}</td>" for d in rowdata) + "</tr>")


class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == "html":
        return HTMLTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "txt":
        return TextTableFormatter()
    else:
        raise FormatError()


def print_table(object_list: list, col_list: list, formatter: TableFormatter):
    formatter.headings(col_list)
    for obj in object_list:
        rowdata = [str(getattr(obj, col)) for col in col_list]
        formatter.row(rowdata)
