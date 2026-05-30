#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// BBCode renderer with dots - renders a black chicken
#define CHICKEN_WIDTH 40
#define CHICKEN_HEIGHT 10

void render_chicken_with_dots() {
    const char* chicken[] = {
        ".................[black.chicken].............",
        ".................*....*...*..................",
        ".................*..*...*..*..............",
        ".................*.....*.....*.............",
        ".................*..........*.............",
        ".................*....*...*..................",
        ".................*..*...*..*..............",
        ".................*.....*.....*.............",
        ".................[end.chicken].............",
        ".................................................."
    };
    
    for (int i = 0; i < CHICKEN_HEIGHT; i++) {
        printf("%s\n", chicken[i]);
    }
}

// Parse and render BBCode tags with dots
void render_bbcode(const char* text) {
    if (strstr(text, "[black.chicken]") != NULL) {
        render_chicken_with_dots();
    } else {
        printf("%s\n", text);
    }
}

int main(int argc, char* argv[]) {
    printf("BBCode Renderer - Rendering with dots\n");
    printf("=====================================\n\n");
    
    // Render black chicken ASCII art with dots
    render_bbcode("[black.chicken]");
    
    printf("\n\nBBCode rendering complete!\n");
    
    return 0;
}
