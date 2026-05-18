text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
spos = text.find('5',pos)
res = text[pos:spos+1]
print(res)