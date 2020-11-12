version: *0.4.0*

symbol | description      | C code
-------|------------------|---------------------
 `!`   | print            | `putchar($);`       
 `?`   | read             | `$=getchar();`      
 `[`   | loop while > 0   | `while ($) {`       
 `]`   | end loop         | `}`                 
 `;`   | end expression   | `;`                 
 `(`   | left paren       | `(`                 
 `)`   | right paren      | `)`                 
 `=`   | set value        | ` = $`              
 `&`   | bitwise and      | ` & $`              
 `\|`  | bitwise or       | ` \| $`             
 `^`   | bitwise xor      | ` ^ $`              
 `~`   | bitwise not      | ` ~$`               
 `{`   | left shift       | ` << $`             
 `}`   | right shift      | ` >> $`             
 `%`   | modulous         | ` % $`              
 `*`   | multiply         | ` * $`              
 `/`   | divide           | ` / $`              
 `+`   | add              | ` + $`              
 `-`   | subtract         | ` - $`              
 `>`   | increment        | `++$;`              
 `<`   | decrement        | `--$;`              
 `@`   | Value at address | `a[$]`              
 `0`   | literal 0        | `0$`                
 `1`   | literal 1        | `1$`                
 `2`   | literal 2        | `2$`                
 `3`   | literal 3        | `3$`                
 `4`   | literal 4        | `4$`                
 `5`   | literal 5        | `5$`                
 `6`   | literal 6        | `6$`                
 `7`   | literal 7        | `7$`                
 `8`   | literal 8        | `8$`                
 `9`   | literal 9        | `9$`                
 `\n`  | new line         | `\n`                
 `\t`  | tab              | `\t`                
 ` `   | space            | ` `                 