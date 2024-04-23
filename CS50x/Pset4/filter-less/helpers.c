#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/ 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }

    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int Red = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int Green = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int Blue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            if (Red > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else {image[i][j].rgbtRed = Red;}

            if (Green > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else {image[i][j].rgbtGreen = Green;}

            if (Blue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else {image[i][j].rgbtBlue = Blue;}
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < (width / 2); j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][(width - 1) - j]; // last element in the row minus j
            image[i][width -1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum_B, sum_G, sum_R;
            sum_B = 0;
            sum_G = 0;
            sum_R = 0;
            int divisor = 0;

            for (int a = i - 1; a < i + 2; a++)
            {
                for(int b = j - 1; b < j + 2; b++)
                {
                    if (a >= 0 && a < height && b >= 0 && b < width)
                    {
                        sum_B += copy[a][b].rgbtBlue;
                        sum_G += copy[a][b].rgbtGreen;
                        sum_R += copy[a][b].rgbtRed;
                        divisor += 1;
                    }
                }
            }
            image[i][j].rgbtBlue = round((float)sum_B / divisor);
            image[i][j].rgbtGreen = round((float)sum_G / divisor);
            image[i][j].rgbtRed = round((float)sum_R / divisor);
        }
    }
    return;
}
