import asyncio
from src.utils.table_formatters import convert_html_to_list_table

test_html_table = """
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>result</th>
      <th>score</th>
      <th>brazil scorers</th>
      <th>competition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>may 11 , 1919</td>
      <td>w</td>
      <td>6 - 0</td>
      <td>friedenreich (3) , neco (2) , haroldo</td>
      <td>south american championship</td>
    </tr>
    <tr>
      <th>1</th>
      <td>may 18 , 1919</td>
      <td>w</td>
      <td>3 - 1</td>
      <td>heitor , amílcar , millon</td>
      <td>south american championship</td>
    </tr>
    <tr>
      <th>2</th>
      <td>may 26 , 1919</td>
      <td>d</td>
      <td>2 - 2</td>
      <td>neco (2)</td>
      <td>south american championship</td>
    </tr>
    <tr>
      <th>3</th>
      <td>may 29 , 1919</td>
      <td>w</td>
      <td>1 - 0</td>
      <td>friedenreich</td>
      <td>south american championship</td>
    </tr>
    <tr>
      <th>4</th>
      <td>june 1 , 1919</td>
      <td>d</td>
      <td>3 - 3</td>
      <td>haroldo , arlindo (2)</td>
      <td>taça roberto cherry</td>
    </tr>
  </tbody>
</table>
"""

resulting_list_table = \
""".. list-table::
   :header-rows: 1

   * - 
     - date
     - result
     - score
     - brazil scorers
     - competition
   * - 0
     - may 11 , 1919
     - w
     - 6 - 0
     - friedenreich (3) , neco (2) , haroldo
     - south american championship
   * - 1
     - may 18 , 1919
     - w
     - 3 - 1
     - heitor , amílcar , millon
     - south american championship
   * - 2
     - may 26 , 1919
     - d
     - 2 - 2
     - neco (2)
     - south american championship
   * - 3
     - may 29 , 1919
     - w
     - 1 - 0
     - friedenreich
     - south american championship
   * - 4
     - june 1 , 1919
     - d
     - 3 - 3
     - haroldo , arlindo (2)
     - taça roberto cherry"""

result = asyncio.run(convert_html_to_list_table(test_html_table))
assert result == resulting_list_table
print("Test passed!")