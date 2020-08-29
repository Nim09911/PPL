Study use of files created by option save-temps 

1. use command save-temps options while comiplation of all program 
    gcc -save -temps filename.c
2. use objdump tool to read object file (explore option of objdump namely l,d,r, prefix-addresses)
    objdump -l -d -r filename.o


