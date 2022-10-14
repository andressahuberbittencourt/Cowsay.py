userText = input("Digite uma fala para a joaninha: ")
words = userText.split()

if len(words) > 10:
   firstline = " ".join(words[:len(words)//2 + 1]) 
   secondline = " ".join(words[len(words)//2 + 1:])
   line = (len(firstline) + 4) * "-"
   padding = (len(firstline) - len(secondline)) * " "
   content = "| " + firstline + " |\n| " + secondline + padding + " |"

else:  
    line = (len(userText) + 4) * "-"
    content ="| " + userText + " |" 

container = [line, content, line]

for item in container:
    print(item)

ladybug = ["     \        ",    
"      \  .         .  ",
"       \  \ ----- /       ",
"         ( *  V  * )      ",
"     ^\  /    |    \  /^     ",
"       \|  .  | .   |/    ",
"    ____|  () | ()  |____     ",
"   <    |. . (|)   .|    >      ",
"        |() . |   ()|          ",
"       /|   ()| .   |\          ",
"     ^/  \____|____/  \^       "]
for item in ladybug:
    print(item)