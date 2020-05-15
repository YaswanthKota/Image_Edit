from PIL import Image
im1 = Image.open("20180601133717_IMG_8071.jpg")
print(' The editing options we are having are:')
print(' 1.Rotating the image')
print(' 2.converting the image into black and white')
print(' 3.Crop the pic')
print(' choose one option from above displayed in  numbers')
option=int(input())

def rotate(x):
    print(' Enter degrees to rotate')
    k=int(input())
    print(' Do you want to save the pic')
    print(' Enter "Y" if yes or "N" if no')
    requirement=input()
    if requirement.lower()=='n':
        l=x.rotate(k)
        print(' Your pic is editing.........:)')
        l.show()
    elif requirement.lower()=='y':
        l=x.rotate(k)
        s=l.save("newpic.jpg")
        print(' your pic is saved in the name of new pic')
    else:
        print(' please enter the valid option')
def bw(y):
    z=y.rotate(90)
    #print(z.size)
    f=z.convert('L')
    print(' Your pic is editing..........:)')
    f.show()
def crop(pic):
    y=pic.rotate(90)
    w=y.crop((860,100,3000,2500))
    print(' Your pic is editing..........:)')
    #print(pic.size)
    z=w.show()
    x=w.save('croped.jpg')
def main():
    if option==1:
        rotate(im1)
    elif option==2:
        bw(im1)
    elif option==3:
        crop(im1)
if __name__ == "__main__":
    main()

