DATA SEGMENT
    PORTA EQU 280H
    PORTB EQU 281H
    PORTC EQU 282H
    PORTR EQU 283H
    
    CLK0 EQU 2B8H
    CLK1 EQU 2B9H
    CLK2 EQU 2BAH
    CLKR EQU 2BBH
DATA ENDS
CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
START:
    MOV DX,PORTR
    MOV AL,92H
    OUT DX,AL
    MOV AL,01H
    MOV AH,AL
RUN:
    MOV DX,CLKR
    MOV AL,00110101B
    OUT DX,AL
    MOV DX,CLK0
    MOV AL,00H
    OUT DX,AL
    MOV AL,50H
    OUT DX,AL
    
    MOV DX,CLKR
    MOV AL,01110111B
    OUT DX,AL
    MOV DX,CLK1
    MOV AL,00H
    OUT DX,AL
    MOV AL,04H
    OUT DX,AL
    
TEST1:
    MOV DX,PORTA
    IN AL,DX
    CMP AL,00000001B
    JNZ TEST1
    
    MOV AL,AH
    MOV DX,PORTC
    OUT DX,AL
    ROL AL,1
    MOV BL,AL
TEST2:
    MOV DX,PORTB
    IN AL,DX
    CMP AL,00000001B
    JNZ TEST2
    
    MOV AL,BL
    MOV AH,AL
    
    JMP RUN
CODE ENDS
END START