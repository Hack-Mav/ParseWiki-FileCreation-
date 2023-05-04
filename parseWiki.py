import wikipediaapi
import wikipedia

wiki = wikipediaapi.Wikipedia('en')

title = input("Enter the title of the Wikipedia page: ")
page_for_file = wiki.page(title)
page_for_summary = wikipedia.page(title)

# Checking for page if exist
print(page_for_file)

# Checking for sections if exist
print(page_for_file.sections[0])

intro = wikipedia.summary(page_for_summary.title, sentences=5)

# Print the introduction text
print(intro)

# Creating introduction part
filename = title + ".txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(intro)

# Creating file and inserting content
for section in page_for_file.sections:
#     print(section.title)
    filename = section.title + ".txt"
    with open(filename, "w", encoding="utf-8") as file:
        if section.sections:
            file.write(str(section.section_by_title)) 
        else:
            file.write(section.text) 
