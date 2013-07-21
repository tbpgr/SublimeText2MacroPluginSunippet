# -*- coding: utf-8 -*-

class TableJustifier:
  def justify(self, value, separator):
    rows = value.split("\n")

    separated_rows = self._get_separated_rows(value, separator)
    max_lens = self._get_max_lens(value, separator)
    justyfid_rows = self._get_justyfid_rows(separated_rows, max_lens, separator)
    return justyfid_rows

  def _get_separated_rows(self, value, separator):
    rows = value.split("\n")
    separated_rows = []
    for row_index, row in enumerate(rows):
      columns = row.split(separator)
      separated_rows.append(columns)
    return separated_rows

  def _get_max_lens(self, value, separator):
    max_lens= []
    rows = value.split("\n")
    for row_index, row in enumerate(rows):
      columns = row.split(separator)
      for column_index,column in enumerate(columns):
        if (column_index == len(columns) -1):
          break
        if row_index == 0:
          max_lens.append(len(column))
          continue
        if max_lens[column_index] < len(column):
          max_lens[column_index] = len(column)
    return max_lens

  def _get_justyfid_rows(self, separated_rows, max_lens, separator):
    justyfid_rows = []
    for separated_row in separated_rows:
      justyfid_columns = ""
      for separated_column_index,separated_column in enumerate(separated_row):
        if (separated_column_index == len(separated_row) -1):
          break
        justyfid_columns += separated_column.ljust(max_lens[separated_column_index])
        justyfid_columns += separator
      justyfid_rows.append(justyfid_columns)
    return "\n".join(justyfid_rows)

# inputs="""    |column1|coln2|c3|
#     |v1|value2|val3|
#     |value1|v2|value3|"""

# justifier = TableJustifier()
# print justifier.justyfy(inputs, "|")
