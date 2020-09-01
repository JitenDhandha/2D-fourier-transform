####################################################################################
# Jiten Dhandha, 26/04/2019                                                        #
# A program to compute the fourier transform of a 2D image or of individual        #
# letters in a string.                                                             #
####################################################################################

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt


#Main function that computes fourier transform
def compute_fourier(image):
    
    #Converting image to an array
    image_arr = np.array(image)
    #Finding its fourier transform
    fourier_transform = np.fft.fft2(image_arr)
    #Shifting it to center of image
    fshift = np.fft.fftshift(fourier_transform)
    #Converting complex fourier transform to its magnitude
    magnitude_spectrum = np.log(1+np.abs(fshift))
    
    return magnitude_spectrum
    
    
#Function to convert string to fourier transform
def string_to_fourier(string):
    
    #FONT PARAMETERS (need not be changed)
    fontsize = 1000
    font = ImageFont.truetype("arial.ttf", fontsize)
    
    #Opening matplotlib figure
    fig=plt.figure()
    
    #Iterating through each letter in string
    for i in range(len(string)):
        
        #Converting letter to an image
        letter_img = Image.new(mode = "L", size =(fontsize,fontsize), color = "white")
        draw = ImageDraw.Draw(letter_img)
        draw.text((0,0), string[i], font=font, fill="black")
        #Computing the fourier transform
        letter_img_FT = compute_fourier(letter_img)
        #Adding it to matplotlib figure
        fig.add_subplot(1,len(string),i+1,title=string[i])
        plt.axis('off')
        plt.imshow(letter_img_FT, cmap="gray")
    
    #Showing the plots
    plt.show()
        
    
#Function to convert image to fourier transform
def image_to_fourier(file):
        
    #Opening image file
    image = Image.open(file).convert("L") 
    #Computing the fourier transform
    image_FT = compute_fourier(image)
    #Showing the plot
    plt.axis('off')
    plt.imshow(image_FT, cmap="gray")
  
    
#Main function
def main():
    #Taking input
    inp = input("Enter image path or string: ")
    #Check whether it's a file or a string
    if(inp.endswith(('.png', '.jpeg', '.jpg'))):
        image_to_fourier(inp)
    else:
        string_to_fourier(inp)

if __name__ == '__main__':
    main()