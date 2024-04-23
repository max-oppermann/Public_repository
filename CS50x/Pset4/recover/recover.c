#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int BLOCK = 512;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover [image]\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    uint8_t buffer[BLOCK];
    char* name = malloc(8 * sizeof(char));
    if (name == NULL)
    {
        return 1;
    }

    int image_counter = 0;

    FILE *file = NULL; // AI-Duck idea

    while (fread(&buffer, 1, BLOCK, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (file != NULL)
            {
                fclose(file);
            }
            sprintf(name, "%03i.jpg", image_counter);
            file = fopen(name, "wb");
            image_counter +=1;
            fwrite(&buffer, 1, BLOCK, file);
        }
        else
        {
            if(file != NULL)
            {
                fwrite(&buffer, 1, BLOCK, file);
            }
        }
    }
    fclose(file);
    fclose(card);
    free(name);
}
mv directory1 directory2 ~/CS50x/Pset4/
