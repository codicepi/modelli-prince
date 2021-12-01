import csv

inizio = """<?xml version="1.0" encoding="UTF-8"?>

<office:document-content xmlns:officeooo="http://openoffice.org/2009/office" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:rpt="http://openoffice.org/2005/report" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" office:version="1.3">
 <office:scripts/>
 <office:font-face-decls>
  <style:font-face style:name="Droid Sans Devanagari" svg:font-family="&apos;Droid Sans Devanagari&apos;" style:font-family-generic="system" style:font-pitch="variable"/>
  <style:font-face style:name="Droid Sans Devanagari1" svg:font-family="&apos;Droid Sans Devanagari&apos;" style:font-family-generic="swiss"/>
  <style:font-face style:name="Liberation Sans" svg:font-family="&apos;Liberation Sans&apos;" style:font-family-generic="swiss" style:font-pitch="variable"/>
  <style:font-face style:name="Liberation Serif" svg:font-family="&apos;Liberation Serif&apos;" style:font-family-generic="roman" style:font-pitch="variable"/>
  <style:font-face style:name="Noto Sans CJK SC" svg:font-family="&apos;Noto Sans CJK SC&apos;" style:font-family-generic="system" style:font-pitch="variable"/>
 </office:font-face-decls>
 <office:automatic-styles>
  <style:style style:name="Table" style:family="table">
   <style:table-properties style:width="17cm" table:align="margins"/>
  </style:style>
  <style:style style:name="Table.A" style:family="table-column">
   <style:table-column-properties style:column-width="4.251cm" style:rel-column-width="16383*"/>
  </style:style>
  <style:style style:name="Table.A1" style:family="table-cell">
   <style:table-cell-properties fo:background-color="transparent" fo:padding="0.097cm" fo:border-left="0.5pt solid #000000" fo:border-right="none" fo:border-top="0.5pt solid #000000" fo:border-bottom="0.5pt solid #000000" style:writing-mode="page">
    <style:background-image/>
   </style:table-cell-properties>
  </style:style>
  <style:style style:name="Table.D1" style:family="table-cell">
   <style:table-cell-properties fo:background-color="transparent" fo:padding="0.097cm" fo:border="0.5pt solid #000000" style:writing-mode="page">
    <style:background-image/>
   </style:table-cell-properties>
  </style:style>
  <style:style style:name="Table.A2" style:family="table-cell">
   <style:table-cell-properties fo:background-color="transparent" fo:padding="0.097cm" fo:border-left="0.5pt solid #000000" fo:border-right="none" fo:border-top="none" fo:border-bottom="0.5pt solid #000000" style:writing-mode="page">
    <style:background-image/>
   </style:table-cell-properties>
  </style:style>
  <style:style style:name="Table.D2" style:family="table-cell">
   <style:table-cell-properties fo:background-color="transparent" fo:padding="0.097cm" fo:border-left="0.5pt solid #000000" fo:border-right="0.5pt solid #000000" fo:border-top="none" fo:border-bottom="0.5pt solid #000000" style:writing-mode="page">
    <style:background-image/>
   </style:table-cell-properties>
  </style:style>
 </office:automatic-styles>
 <office:body>
  <office:text>
   <text:sequence-decls>
    <text:sequence-decl text:display-outline-level="0" text:name="Illustration"/>
    <text:sequence-decl text:display-outline-level="0" text:name="Table"/>
    <text:sequence-decl text:display-outline-level="0" text:name="Text"/>
    <text:sequence-decl text:display-outline-level="0" text:name="Drawing"/>
    <text:sequence-decl text:display-outline-level="0" text:name="Figure"/>
   </text:sequence-decls>
"""

print(inizio)

with open('campiprince.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = True
    for row in csv_reader:
        if header:
            header = False
        else:
            etichetta = row[0][1:]
            campo = row[0]
            print(f"""   <text:p text:style-name="Standard">{etichetta}: <text:database-display text:table-name="table" text:table-type="table" text:column-name="{campo}" text:database-name="db_prince">&lt;{campo}&gt;</text:database-display></text:p>""")
            if not row[0][1:7] == "ELENCO":
                continue
            codice = row[0] + ".Codice"
            desc1 = row[0] + ".Descrizione" 
            desc2 = row[0] + ".Descrizione2"
            desc3 = row[0] + ".Descrizione3"
            print(f"""       <table:table table:name="Table" table:style-name="Table" table:template-name="Default Style">
        <table:table-column table:style-name="Table.A" table:number-columns-repeated="4"/>
        <table:table-header-rows>
         <table:table-row table:style-name="TableLine94407609426208">
          <table:table-cell table:style-name="Table.A1" office:value-type="string">
           <text:p text:style-name="Table_20_Heading">Codice</text:p>
          </table:table-cell>
          <table:table-cell table:style-name="Table.A1" office:value-type="string">
           <text:p text:style-name="Table_20_Heading">Descrizione</text:p>
          </table:table-cell>
          <table:table-cell table:style-name="Table.A1" office:value-type="string">
           <text:p text:style-name="Table_20_Heading">Descrizione2</text:p>
          </table:table-cell>
          <table:table-cell table:style-name="Table.D1" office:value-type="string">
           <text:p text:style-name="Table_20_Heading">Descrizione3</text:p>
          </table:table-cell>
         </table:table-row>
        </table:table-header-rows>
        <table:table-row table:style-name="TableLine94407609426208">
         <table:table-cell table:style-name="Table.A2" office:value-type="string">
          <text:p text:style-name="Standard"><text:database-display text:table-name="table" text:table-type="table" text:column-name="{codice}" text:database-name="db_prince">&lt;{codice}&gt;</text:database-display></text:p>
         </table:table-cell>
         <table:table-cell table:style-name="Table.A2" office:value-type="string">
          <text:p text:style-name="Standard"><text:database-display text:table-name="table" text:table-type="table" text:column-name="{desc1}" text:database-name="db_prince">&lt;{desc1}&gt;</text:database-display></text:p>
         </table:table-cell>
         <table:table-cell table:style-name="Table.A2" office:value-type="string">
          <text:p text:style-name="Standard"><text:database-display text:table-name="table" text:table-type="table" text:column-name="{desc2}" text:database-name="db_prince">&lt;{desc2}&gt;</text:database-display></text:p>
         </table:table-cell>
         <table:table-cell table:style-name="Table.D2" office:value-type="string">
          <text:p text:style-name="Standard"><text:database-display text:table-name="table" text:table-type="table" text:column-name="{desc3}" text:database-name="db_prince">&lt;{desc3}&gt;</text:database-display></text:p>
         </table:table-cell>
        </table:table-row>
       </table:table>
       <text:p text:style-name="Standard"/>
""")

fine = """  </office:text>
 </office:body>
</office:document-content>"""

print(fine)
    

