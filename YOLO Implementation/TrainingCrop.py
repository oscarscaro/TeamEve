from PIL import Image
import csv, os

os.chdir("D:/Wastesorting/Model/dataset/")
print(os.getcwd())

with open("D:/Wastesorting/train_sorted.csv") as train:
    train_csv=list(csv.reader(train))
    train_csv.pop(0)

    for entry in train_csv:
        img=Image.open('train/'+entry[5]+'/'+entry[0]+'.jpg')
        #print(img.size)
        cropped=img.crop((float(entry[1]),
                          float(entry[2]),
                          float(entry[1])+float(entry[3]),
                          float(entry[2])+float(entry[4])))
        try:
            cropped.save('train_crop/'+entry[5]+'/'+entry[0]+'.jpg')
        except FileNotFoundError:
            os.mkdir('train_crop/'+entry[5])
            print('Cropping category '+entry[5])
            cropped.save('train_crop/'+entry[5]+'/'+entry[0]+'.jpg')

print('done')
