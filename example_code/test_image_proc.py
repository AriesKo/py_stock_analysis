import requests
from PIL import Image
import hashlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

if __name__ == "__main__":
    url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    r = requests.get(url,stream=True).raw
    img = Image.open(r)
    # img.show()
    img.save("googlelogo.png")
    print(img.get_format_mimetype)
    
    buf_size = 1024
    with open("googlelogo.png",'rb') as sf, open("dst.png", "wb") as df:
        while True:
            data = sf.read()
            if not data:
                break
            df.write(data)

    sha_src = hashlib.sha256()
    sha_dst = hashlib.sha256()

    with open("googlelogo.png",'rb') as sf, open("dst.png",'rb') as df:
        sha_src.update(sf.read())
        sha_dst.update(df.read())
    
    print("src hash: {}".format(sha_src.hexdigest()))  
    print("dst hash: {}".format(sha_dst.hexdigest()))
    
    plt.suptitle("image processing",fontsize=16)
    plt.subplot(1,2,1)
    plt.title("original")
    plt.imshow(mpimg.imread("googlelogo.png"))

    plt.subplot(1,2,2)
    plt.title("pesudocolor image")
    dst_img = mpimg.imread("dst.png")
    peudo_img = dst_img[:,:,0]
    plt.imshow(peudo_img, cmap="gray")
    plt.show()
            
