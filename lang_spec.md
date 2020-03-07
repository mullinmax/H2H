language version: *0.1.0*

symbol | indent | description      | C code
-------|--------|------------------|---------------------
`BOF`  | `+`    | beginning of code | `#include <cstdio>\nchar a[30000] = {0};\nchar *ptr[10]={a, a, a, a, a, a, a, a, a, a};\nint main(){`
`EOF`  | `-`    | end of code      | `    return(0);\n}`
`"`    | `=`    | print            | `putchar(*$);`
`?`    | `=`    | read             | `*$=getchar();`
`[`    | `+`    | loop while > 0   | `while ($) {`
`]`    | `-`    | end loop         | `}`
`;`    | `=`    | end expression   | `;` 
`(`    | `=`    | left paren       | `(` 
`)`    | `=`    | right paren      | `)` 
`=`    | `=`    | set value        | ` = $`
`&`    | `=`    | bitwise and      | ` & $` 
`|`    | `=`    | bitwise or       | ` | $` 
`^`    | `=`    | XOR              | ` ^ $`
`!`    | `=`    | bitwise not      | ` ~$`
`%`    | `=`    | modulous         | ` % $` 
`*`    | `=`    | multiply         | ` * $` 
`/`    | `=`    | divide           | ` / $` 
`+`    | `=`    | add              | ` + $` 
`-`    | `=`    | subtract         | ` - $`  
`>`    | `=`    | increment        | ` ++$;` 
`<`    | `=`    | decrement        | ` --$;`
`@`    | `=`    | Value at head    | ` *$` 
`0`    | `=`    | head 0           | `ptr[0]` 
`1`    | `=`    | head 1           | `ptr[1]`
`2`    | `=`    | head 2           | `ptr[2]`
`3`    | `=`    | head 3           | `ptr[3]`
`4`    | `=`    | head 4           | `ptr[4]`
`5`    | `=`    | head 5           | `ptr[5]`
`6`    | `=`    | head 6           | `ptr[6]`
`7`    | `=`    | head 7           | `ptr[7]`
`8`    | `=`    | head 8           | `ptr[8]`
`9`    | `=`    | head 9           | `ptr[9]`
`.`    | `=`    | origin           | `a`
