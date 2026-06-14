"""
<table>
    <thead>
        <tr>
            <th>Book</th>
            <th>Author</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Java</td>
            <td>Amit</td>
        </tr>
    </tbody>
</table>
"""

# rows = len(driver.find_elements(
#     By.XPATH,
#     "//table[@name='BookTable']//tr"
# ))   no. of rows
#     "//table[@name='BookTable']//th"
#      no. of cols
#      "//table[@name='BookTable']//tr[5]/td[1]"
#      specific cell


# for r in range(2, rows + 1):
#     for c in range(1, columns + 1):
#         data = driver.find_element(
#             By.XPATH,
#             "//table[@name='BookTable']//tr[" +
#             str(r) +
#             "]/td[" +
#             str(c) +
#             "]"
#         ).text
#
#         print(data, end="\t")
#     print()       to real all cells