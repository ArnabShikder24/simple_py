import pypandoc

output = pypandoc.convert_file('Payback_Period_Assignment.docx', 'pdf', outputfile='Payback_Period_Assignment.pdf')

# assert output == ""
