#All functions should be here


def main():
    pass

# ↓↓↓ Ersalor's work space ↓↓↓ 



# ↓↓↓ Mehmetcan's work space ↓↓↓

def AllNeighboodsList():
    with open("neighborhoods.txt","r",encoding="utf-8") as rows:
        list = []
        for line in rows:
            list.append(line.strip())
        return list

for line in AllNeighboodsList():    
    print(line)

# ↓↓↓ Hasan's work space ↓↓↓



if __name__=="main":
    main()