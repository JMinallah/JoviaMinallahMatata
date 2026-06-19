# declare 2 variables(integer and string). concatenate the 2
num = 10
text = "The number is: "
result = text + str(num)
print(result)

# ouput string without spaces anywhere
txt = "  Hello,  Uganda  "
clean_txt = txt.replace(" ", "")
print(clean_txt)
# or
# clean_txt = txt.strip()
# print(clean_txt)

#convert the string to uppercase.
upper_txt = txt.upper()
print(upper_txt)

# replace U with V in upper_txt
v_txt = upper_txt.replace("U", "V")
print(v_txt)

# return range of characterss from 2nd, 3rd and 4th position
y = "I am proudly Ugandan"
substring = y[1:4]
print(substring)

# correct the string
# x = "All "Data Scientists" are cool!"
# corrected_x = x.replace('"', '')
# print(corrected_x)
