import yaml

# with open("../data/lx.yaml", "r",encoding="utf-8") as f:
#     r = yaml.safe_load(f)
#     print(r)
#     print(type(r))

data = {"name":"张鹏博1456","age":25}

with open("../data/lx.yaml","a",encoding="utf-8") as f:
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)







