# Scene: Create budgets to your company
# Objetivo: Automatically generate PDFs with PYTHON

# Step 1 - Collecting data
project = input("Type the description of the project: ")
estimated_hours = input("Type the estimated total hours: ")
value_hour = input("Type the value of the hour: ")
estimated_deadline = input("Type the estimated deadline: ")

## Analyzing the values
print(project)
print(estimated_hours)
print(value_hour)
print(estimated_deadline)


# Step 2 - Calculating the estimated total value
total_estimated_value = int(estimated_hours) * int(value_hour)

## Analyzing the values
print (total_estimated_value)


# Step 3 - Generating the PDF with the budget
## Instaling the library - pip install fpdf in cmd

from fpdf import FPDF # Importing the library 


# Step 4 - Creating a PDF file

pdf = FPDF() # Creating a PDF file
pdf.add_page() # Adding a page to the file
pdf.set_font("Arial") # Setting the font to the file


# Step 5 - Inserting data to the PDF file
## Using a template
pdf.image("template.png", x=0, y=0 )

## Inserting data
pdf.text(115, 145, project) # 115,145 are the coordinates of the file. x,y
pdf.text(115, 160, estimated_hours)
pdf.text(115, 175, value_hour)
pdf.text(115, 190, estimated_deadline)
pdf.text(115, 205, str(total_estimated_value))


# Step 6 - Saving the file 
pdf.output("budget.pdf")
print("Budget generated successfully!")







