file1 = open('data\\Python_Introduction',encoding="utf-8")
readme_txt = file1.read()
file1.close()
print( type(readme_txt), len(readme_txt), readme_txt[:21])

with open('data\\Python_Introduction',encoding="utf-8") as file2:
    readme_txt2 = file2.read()

print( type(readme_txt2), len(readme_txt2), readme_txt2[:21])

file3 = open('data\\clone1','w',encoding="utf-8")
file3.write(readme_txt)
file3.close()

with open('data\\clone2','w',encoding="utf-8") as file4:
    file4.write(readme_txt2)