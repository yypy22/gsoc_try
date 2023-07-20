import pandas as pd
pd.set_option('display.max_rows', 170000)
pd.set_option('display.max_columns', 170000)
df = pd.read_csv("Suffix.csv", header=None)
fam = df[0]
gob = df[8]
tag = " NounTag ;"
co = ":"
# print("%+"+fam+ "%<mod%>:%>"+gob+ " # ;")
print(fam+ "%<suff%>:"+gob+ " # ;")
# print(fam+ ":"+gob+ " NounTag ;")
# print(fam+"%<det%>%<dem%>:"+gob+" # ;")
# print("%<com%>:%>"+gob+ " # ;")
# print(f"col")
# with open(col) as f:
#     a = f.read(col)
#     print(a)
