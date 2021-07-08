#!/usr/bin/env python
#	
#	u	Dec   	Hex 	HTML    	Unicode character 
#	""	34  	0x22	&quot;  	quotation mark (2x)
#	“	8220	0x201C	&ldquo; 	left double quotation mark
#	”	8221	0x201D	&rdquo; 	right double quotation mark
#	„	8222	0x201E	&bdquo; 	double low-9 quotation mark
#	‟	8223	0x201F	&#8223; 	double high-reversed-9 quotation mark
#	❝	10077	0x275D	&#10077;	heavy double turned comma quotation mark ornament
#	❞	10078	0x275E	&#10078;	heavy double comma quotation mark ornament
#	⹂	11842	0x2E42	&#11842;	double low-reversed-9 quotation mark
#	〝	12317	0x301D	&#12317;	reversed double prime quotation mark
#	〞	12318	0x301E	&#12318;	double prime quotation mark
#	〟	12319	0x301F	&#12319;	low double prime quotation mark
#	
#	https://unicodelookup.com/#quo
#	
import re
def uni2dQuote(s):
  return re.sub(r'[\u201C\u201D\u201E\u201F\u275D\u275E\u2E42\u301D\u301E\u301F]',
                r'"',  s)   if type(s) is str else s

print(uni2dQuote(' Abc „Def” Ghi')) # Abc "Def" Ghi

#csvWr.writerow([uni2dQuote(s) for s in row])