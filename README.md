## Core
exit
clear
echo <message>

## help
help
help [command_name]

## history
history
history [!n]
history [clear]
history export <file>

## flux / config / plugins
flux
flux setup
flux show
flux reset

flux set <key> <value>      
flux get <key>               
flux import <file>          
flux export <file>           
flux run <file>             

flux install <plugin_name>
flux remove <plugin_name>
flux enable <plugin_name>
flux disable <plugin_name>
flux list                   

## user stuff
user create <username>       
user login <username>      
user logout                  
user whoami                  
user delete <username>      
user rename <new_username> 

## ui modification
ui show                      
ui set theme <theme_name>   
ui set prompt <prompt_style> 
ui set username <username>   
ui set servername <servername> 
ui reset                     
ui list themes              
ui preview <theme_name>  