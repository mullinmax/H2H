symbol | indent | C code
-------|------------------------------------------
`^`    | `+`    | `#include <cstdio>\nusing namespace std;\nchar array[30000] = {0};\nchar *ptr=array;\nint main(){`
`$`    | `-`    | `return(0);\n}`
`>`    | `=`    | `++ptr;`
`<`    | `=`    | `--ptr;`
`+`    | `=`    | `++*ptr;`
`-`    | `=`    | `--*ptr;`
`.`    | `=`    | `putchar(*ptr);`
`,`    | `=`    | `*ptr=getchar();`
`[`    | `+`    | `while (*ptr) {`
`]`    | `-`    | `}`