#encoding:UTF-8

filenames=["ad.txt","not_ad.txt"]
output=open("tgrocery_train.txt","w")

for filename in filenames:
    with open(filename, 'r') as f:
        for line in f:   
            if filename=="ad.txt":  
                output.write("0\t"+line)
            else:
                output.write("1\t"+line)
    f.close()

output.flush()
output.close()








