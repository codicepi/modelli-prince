REM  *****  BASIC  *****

Sub InserisciTagPrince

 Dim oViewCursor As Object
 Dim oMasters 'All of the text field masters
 Dim oText 'Text object for the current document
 Dim oUField 'User field to insert
 Dim oMField 'The master field for the user field
 Dim oDoc 'oDoc is fewer characters than ThisComponent
 Dim sLead$ 'Leading field name
 Dim sName$ 'Name of the field to remove or insert
 Dim sTotName$ 'The entire name

 REM Set the names.
 sName = Trim(InputBox ("Tag:", "Crea tag lettera Prince", "$ADDETTO"))
 sLead = "com.sun.star.text.FieldMaster.Database"
 sTotName = sLead & "." & sName

 REM Check name
 If len(sName) = 0 Then
  MsgBox("Tag non valida")
  Stop
 End If

 REM Initialize some values.
 oDoc = ThisComponent
 oMasters = ThisComponent.getTextFieldMasters()

 REM Master field exists?
 If oMasters.hasByName(sTotName) Then
  REM Existing master field
  REM MsgBox "Master field exists"
  oMField = oMasters.getByName(sTotName)
 Else
  REM Create new master field
  oMField = oDoc.createInstance(sLead)
  oMField.Name = sName
  oMField.DataBaseName = "Prince"
  oMField.DataTableName = "Table"
  oMField.DataColumnName = sName
 End If

 REM Create field
 oUField = oDoc.createInstance("com.sun.star.text.TextField.Database")
 oUField.CurrentPresentation = "<" + sName + ">"
 oUField.attachTextFieldMaster(oMField)

 REM Get cursor position
 oViewCursor = oDoc.GetCurrentController.ViewCursor
 If IsEmpty(oViewCursor.Cell) Then
  oText = ThisComponent.text
 Else
  oText = oViewCursor.Cell.Text
 End If

 REM Insert the user field into the document.
 oText.insertTextContent(oViewCursor, oUField, False)

End Sub

