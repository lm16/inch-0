import langid


s1 = "大佬天天见"
s2 = "fasfd"
s3 = 'Flüssigkeiten zum Nassbehandel'
print(langid.classify(s1))
print(langid.classify(s2))
print(langid.classify(s3))