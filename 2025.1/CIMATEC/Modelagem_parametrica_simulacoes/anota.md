To achieve this, you can use LibreOffice Calc's VLOOKUP function. Here's a step-by-step guide:

In the first sheet, add a new column where you want to display the grades.
In the first row of this new column, enter the header "Grade".
Select the cell below the header and enter the following formula:
text

Copiar
=VLOOKUP(B2, 'Groups Sheet'!A:B, 2, FALSE)
Assuming the group names are in column B in the first sheet and the grades are in column A in the "Groups Sheet".

B2 refers to the cell containing the group name of the student.
'Groups Sheet' refers to the name of the sheet containing the grades.
A:B refers to the range of cells containing the group names and grades.
2 refers to the column index of the grades (since the group names are in column A).
FALSE specifies an exact match.
Drag the fill handle (small square at the bottom-right corner of the cell) down to apply the formula to the rest of the cells in the column.
Alternatively, you can use the INDEX-MATCH function combination, which is more flexible and efficient:

text

Copiar
=INDEX('Groups Sheet'!B:B, MATCH(B2, 'Groups Sheet'!A:A, 0))
This formula looks up the group name in the "Groups Sheet" and returns the corresponding grade.

If you need more help or clarification, feel free to ask!
