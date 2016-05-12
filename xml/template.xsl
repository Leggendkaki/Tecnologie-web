<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
			
<xsl:template match="/">
  <html>
  <body>
  <p>ciao</p>
	<style>
		td{
		border:black solid 1px;
		}
	</style>
	<table>
		<xsl:for-each select="//portal">
		<tr>
			<td>
				<xsl:value-of select="title"/>
			</td>
			
			<td>
				<xsl:value-of select="description"/>
			</td>
			
			<td>
				<xsl:value-of select="img"/>
			</td>
			
			<td>
				<xsl:value-of select="latitude"/>
			</td>
			
			<td>
				<xsl:value-of select="longitude"/>
			</td>
			
			<td>
				<xsl:value-of select="nickname"/>
			</td>
			
			
			
		</tr>
		</xsl:for-each>
	</table>

  
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>